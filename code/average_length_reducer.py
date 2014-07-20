#!/usr/bin/python

import sys
import csv

# ------------------ Helper functions ------------------

def write(key, value):
    print "{0}\t{1}".format(key, value)

def write_lengths(key, questionLength, answerLengthTotal, answerCount):
    value = None
    if answerCount > 0:
        average_answer_length = float(answerLengthTotal) / answerCount
        value = "{0}\t{1:.1f}".format(questionLength, average_answer_length)
    else:
        value = str(questionLength) + "\t0"
    write(key, value)

def has_id_changed(id, previous_id):
    return previous_id != None and id != previous_id

# ------------------ Reducer ------------------

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')

    previousId          = None
    questionLength      = 0
    answerLengthTotal   = 0
    answerCount         = 0

    for line in reader:

        try:
            id, nodeType, length = line

            if has_id_changed(id, previousId):
                write_lengths(previousId, questionLength, answerLengthTotal, answerCount)
                questionLength = answerLengthTotal = answerCount = 0

            if nodeType == 'question':
                questionLength = length

            elif nodeType == 'answer':
                answerCount         += 1
                answerLengthTotal   += int(length)

            previousId = id

        except ValueError as e:
            print "Error: ", e, " Line: ", line

    # Write lengths for final ID
    write_lengths(previousId, questionLength, answerLengthTotal, answerCount)

reducer()

