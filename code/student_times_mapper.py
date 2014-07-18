#!/usr/bin/python

import sys
import csv
from dateutil import parser

# ------------------ Helper functions ------------------

def hour_of_day(dateStr):
    return parser.parse(dateStr).hour

def write(key, value):
    print "{0}\t{1}".format(key, value)

def is_header(line):
    return line[0] == "id"

# ------------------ Mapper ------------------

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:

        if not is_header(line):
            try:
                id, title, tagnames, authorId, body, nodeType, parentId, absParentId, addedAt, score, stateAtring, lastEditedId, lastActivityById, lastActivityAt, activeRevisionId, extra, extraRefId, extraCount, marked = line
                write(authorId, hour_of_day(addedAt))

            except ValueError as e:
                print "Error: ", e, " Line: ", line

mapper()