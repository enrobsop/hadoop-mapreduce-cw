# Common functions used for multiple mappers and/or reducers

def has_id_changed(id, previous_id):
    return previous_id != None and id != previous_id

def write(key, value):
    print "{0}\t{1}".format(key, value)

def is_header(line):
    return line[0] == "id"


