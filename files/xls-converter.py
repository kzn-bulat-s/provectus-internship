#!/usr/bin/python2

from argparse import ArgumentParser
import xlrd

import sys

parser = ArgumentParser(description='Converts xls/xlsx file to xml ' \
                                    '(data-centric) or json file.')

parser.add_argument('-t', '--type', choices=['xml', 'json'],
                    help='destination format', required=True)

group = parser.add_mutually_exclusive_group()
group.add_argument('-i', '--index', type=int, default=0,
                    help='sheet index')
group.add_argument('-n', '--name', type=unicode,
                    help='sheet name')

parser.add_argument('src', help='workbook containing sheet to convert')

parser.add_argument('dst', nargs='?',
                    help='destination file (stdout by default)')

args = parser.parse_args()

def build_xml(sheet, dst):
    from lxml import etree

    dst.write('<data>\n')

    header = sheet.row_values(0)

    for row_idx in xrange(1, sheet.nrows):
        row = sheet.row_values(row_idx)
        item = etree.Element('item')
        for key, value in zip(header, row):
            attr = etree.SubElement(item, key)
            attr.text = value
        dst.write(etree.tostring(item, encoding='utf-8') + '\n')

    dst.write('</data>\n')

def build_json(sheet, dst):
    from json import dump

    dst.write('{"data":[\n')

    header = sheet.row_values(0)

    first_row = True

    for row_idx in xrange(1, sheet.nrows):
        if not first_row:
            dst.write(',\n')
        else:
            first_row = False
        
        row = sheet.row_values(row_idx)
        record = dict(zip(header, row))
        dump(record, dst, ensure_ascii=False, encoding='utf-8')

    dst.write('\n]}\n')

with xlrd.open_workbook(args.src) as wb:
    if args.name:
        sheet = wb.sheet_by_name(args.name)
    else:
        sheet = wb.sheet_by_index(args.index)

    dst = sys.stdout if not args.dst else open(args.dst, 'w')

    try:
        if args.type == 'xml':
            build_xml(sheet, dst)
        
        elif args.type == 'json':
            build_json(sheet, dst)

    finally:
        dst.close()
