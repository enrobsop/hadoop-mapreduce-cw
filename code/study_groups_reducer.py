#!/usr/bin/python

import sys
import csv

# ------------------ Helper ------------------

def has_id_changed(id, previous_id):
    return previous_id != None and id != previous_id

def write(key, value):
    print "{0}\t{1}".format(key, value)

# ------------------ Reducer ------------------

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    previousId  = None
    students    = []

    for line in reader:

        try:
            id, authorId = line

            if has_id_changed(id, previousId):
                write(previousId, students)
                students = []

            students.append(int(authorId))
            previousId = id

        except ValueError as e:
            print "Error: ", e, " Line: ", line

    # Write final ID
    write(id, students)

reducer()
