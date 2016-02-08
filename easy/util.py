class TokenReader(object):
    """
    Python standard library doesn't provide tools to deal with very long
    input strings.
    TokenReader reads file by fixed size blocks to avoid this problem.
    It doesn't close the file by itself.
    """
    import re
    __expr = re.compile(r'\S+', flags=re.UNICODE)
    def __init__(self, istream, blocksz=4096):
        self.__istream = istream
        self.__blocksz = blocksz
        self.__prev = None
        self.__iter = iter([])
        self.__stop = False

    def __iter__(self):
        return self

    def next(self):
        if self.__stop:
            raise StopIteration

        while True:
            try:
                token = next(self.__iter).group(0)
                if self.__prev is None:
                    self.__prev = token
                    continue
                else:
                    ret = self.__prev
                    self.__prev = token
                    break
            except StopIteration:
                chunk = self.__istream.read(self.__blocksz)
                if not chunk:
                    if self.__prev is None:
                        raise StopIteration
                    else:
                        ret = self.__prev
                        self.__stop = True
                        break
                else:
                    if self.__prev == None:
                        self.__prev = ''
                    self.__iter = TokenReader.__expr.finditer(
                                    self.__prev + chunk)
                    self.__prev = None
 
        return ret
