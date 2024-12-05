# Unclosed File Bug in Python

This repository demonstrates a common but easily missed error in Python: failing to close a file after opening it.  Unclosed files can lead to resource leaks, especially in larger programs or when dealing with many files.

## The Bug

The `bug.py` file contains a function that opens a file, performs some operations, and *fails to close the file*.  In a real-world scenario, this could lead to issues such as:

* **Resource exhaustion:** If many files are opened without closing, the system might run out of file handles.
* **Data loss:** In some cases, data written to the file might not be properly flushed to disk if the file isn't closed.
* **Unexpected behavior:**  Other parts of the program or the operating system might interfere with the unclosed file.

## The Solution

The `bugSolution.py` demonstrates the correct way to handle file I/O: using a `with` statement to ensure the file is always closed, even if errors occur.