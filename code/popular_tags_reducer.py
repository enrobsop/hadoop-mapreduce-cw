#!/usr/bin/python

import sys
import csv
import myutil
import operator

# ------------------ Helper functions ------------------

def write_top_10(tags):
    tagsSorted = sorted(tags.iteritems(), key=operator.itemgetter(1), reverse=True)

    for tag, frequencey in tagsSorted[:10]:
        print tag, frequencey

    return None

# ------------------ Reducer ------------------

def reducer():
    reader              = csv.reader(sys.stdin, delimiter='\t')
    previous_tag_name   = None
    tags                = {}    # Dictionary of tags and frequencies {'tag':count}. E.g {'hello':2, 'world':5}
    count               = 0

    for line in reader:

        try:
            tagname, n = line  # n = 1 without a combiner, n >= 1 with a combiner

            if myutil.has_id_changed(tagname, previous_tag_name):
                tags[previous_tag_name] = count
                count = 0

            count += int(n)
            previous_tag_name = tagname


        except ValueError as e:
            print "Error: ", e, " Line: ", line

    tags[tagname] = count

    write_top_10(tags)

reducer()
