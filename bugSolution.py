def function_with_closed_file(filename):
    try:
        with open(filename, 'w') as f:
            # ... some code that might raise an exception ...
            f.write("This is a test")
    except Exception as e:
        print(f"An error occurred: {e}")

function_with_closed_file("my_file.txt")