# Takes an input of a file path and returns a list with the file split by new lines

def split_file_into_lines(path):
    file = open(path).read()
    return file.split("\n")