#!/usr/bin/python

import sys
import csv
import myutil

# ------------------ Mapper ------------------

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:

        if not myutil.is_header(line):
            try:
                id, title, tagnames, authorId, body, nodeType, parentId, absParentId, addedAt, score, stateAtring, lastEditedId, lastActivityById, lastActivityAt, activeRevisionId, extra, extraRefId, extraCount, marked = line

                if nodeType == 'question':
                    for tagname in tagnames.split():
                        myutil.write(tagname, 1)

            except ValueError as e:
                print "Error: ", e, " Line: ", line

mapper()