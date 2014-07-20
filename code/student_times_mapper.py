#!/usr/bin/python

import sys
import csv
from datetime import datetime

# ------------------ Helper functions ------------------

def hour_of_day(dateStr):
    return int(datetime.strptime(dateStr[:13], '%Y-%m-%d %H').strftime('%H'))

def is_header(line):
    return line[0] == "id"

def write(key, value):
    print "{0}\t{1}".format(key, value)

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