#!/usr/bin/python

import sys
import csv
import myutil

# ------------------ Reducer ------------------

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    previousId  = None
    students    = []

    for line in reader:

        try:
            id, authorId = line

            if myutil.has_id_changed(id, previousId):
                myutil.write(previousId, students)
                students = []

            students.append(int(authorId))
            previousId = id

        except ValueError as e:
            print "Error: ", e, " Line: ", line

    # Write final ID
    myutil.write(id, students)

reducer()
