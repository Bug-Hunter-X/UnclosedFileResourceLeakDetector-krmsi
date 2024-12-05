def function_with_unclosed_file(filename):
    f = open(filename, 'w')
    # ... some code that might raise an exception ...
    # forgot to close file here
    return

function_with_unclosed_file("my_file.txt")