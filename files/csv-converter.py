#!/usr/bin/python2

from argparse import ArgumentParser
from csv import DictReader

import sys

parser = ArgumentParser(description='Converts csv file to xml (data-centric) '\
                                    'or json file.')

parser.add_argument('-t', '--type', choices=['xml', 'json'],
                    help='destination format', required=True)

parser.add_argument('src', help='csv-file to convert')

parser.add_argument('dst', nargs='?',
                    help='destination file (stdout by default)')

args = parser.parse_args()

def build_xml(csv_reader, dst):
    from lxml import etree

    header = csv_reader.fieldnames

    dst.write('<data>\n')

    for row in csv_reader:
        item = etree.Element('item')
        for key, value in row.iteritems():
            attr = etree.SubElement(item, key)
            attr.text = value
        dst.write(etree.tostring(item, encoding='utf-8') + '\n')

    dst.write('</data>\n')

def build_json(csv_reader, dst):
    from json import dump

    dst.write('{"data":[\n')

    first_row = True

    for row in csv_reader:
        if not first_row:
            dst.write(',\n')
        else:
            first_row = False

        dump(row, dst, ensure_ascii=False, encoding='utf-8')

    dst.write('\n]}\n')

with open(args.src) as src:
    csv_reader = DictReader(src)

    dst = sys.stdout if not args.dst else open(args.dst, 'w')

    try:
        if args.type == 'xml':
            build_xml(csv_reader, dst)
        elif args.type == 'json':
            build_json(csv_reader, dst)

    finally:
        dst.close()
