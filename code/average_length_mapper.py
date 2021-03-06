#!/usr/bin/python

import sys
import csv

# ------------------ Helper ------------------

def is_header(line):
    return line[0] == "id"

# ------------------ Mapper ------------------

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    questionId = None

    for line in reader:

        if not is_header(line):
            try:
                id, title, tagnames, authorId, body, nodeType, parentId, absParentId, addedAt, score, stateAtring, lastEditedId, lastActivityById, lastActivityAt, activeRevisionId, extra, extraRefId, extraCount, marked = line

                questionId = id if nodeType == 'question' else absParentId

                print "{0}\t{1}\t{2}".format(questionId, nodeType, len(body))

            except ValueError as e:
                print "Error: ", e, " Line: ", line

mapper()