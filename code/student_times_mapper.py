#!/usr/bin/python

import sys
import csv
from datetime import datetime

import myutil

# ------------------ Helper functions ------------------

def hour_of_day(dateStr):
    return int(datetime.strptime(dateStr[:13], '%Y-%m-%d %H').strftime('%H'))

# ------------------ Mapper ------------------

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:

        if not myutil.is_header(line):
            try:
                id, title, tagnames, authorId, body, nodeType, parentId, absParentId, addedAt, score, stateAtring, lastEditedId, lastActivityById, lastActivityAt, activeRevisionId, extra, extraRefId, extraCount, marked = line
                myutil.write(authorId, hour_of_day(addedAt))

            except ValueError as e:
                print "Error: ", e, " Line: ", line

mapper()