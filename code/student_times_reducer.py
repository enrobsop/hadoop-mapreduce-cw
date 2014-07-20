#!/usr/bin/python

import sys
import csv
import operator

# ------------------ Helper functions ------------------

def has_id_changed(id, previous_id):
    return previous_id != None and id != previous_id

# Increments the frequency count in a dictionary for a given key
def increment_frequency_count(key, frequencies):
    if key in frequencies:
        frequencies[key] = frequencies[key] + 1
    else:
        frequencies[key] = 1

# Returns a list of the most frequent hours. E.g. [12, 5]
def find_most_frequent(frequencies):
    freqs_descending = sorted(frequencies.iteritems(), key=operator.itemgetter(1), reverse=True)
    max_freq = freqs_descending[0][1]
    result = []
    for key, frequency in freqs_descending:
        if frequency == max_freq:
            result.append(key)
        else:
            break
    return sorted(result)

def write(key, value):
    print "{0}\t{1}".format(key, value)

# Writes the reducer output using multiple lines when 'equal' max hour frequencies
def write_lines(id, frequencies):
    mostFrequent = find_most_frequent(frequencies)
    for hour in mostFrequent:
        write(id, hour)

# ------------------ Reducer ------------------

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    frequencies = {}        # Dictionary of frequency of hours for an ID {'hour':freq}. E.g {'23':2, '13':5, '18',9}
    previousId = None

    for line in reader:

        try:
            id, hour = line

            if has_id_changed(id, previousId):
                write_lines(previousId, frequencies)
                frequencies = {}

            increment_frequency_count(hour, frequencies)
            previousId = id

        except ValueError as e:
            print "Error: ", e, " Line: ", line

    # Write hours for final ID
    write_lines(id, frequencies)

reducer()
