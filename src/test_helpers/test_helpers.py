import sys
from io import StringIO

def printToIO(node):
    original_stdout = sys.stdout 
    captured_output = StringIO()
    try:
        sys.stdout = captured_output
        print(node)
        printed_output = captured_output.getvalue().strip()
    finally:
        sys.stdout = original_stdout
    return printed_output