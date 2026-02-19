import tempfile
import os
from contextlib import contextmanager

@contextmanager
def create_temporary_file(suffix=".txt", mode="r"):
    """
    Create a temporary file, yield its path, and remove it automatically.
    """
    fd, path = tempfile.mkstemp(suffix=suffix)
    os.close(fd)
    try:
        with open(path, mode) as f:
            yield f
    finally:
        # cleanup: remove the file
        if os.path.exists(path):
            os.remove(path)
            print(f"Temporary file {path} deleted")


with create_temporary_file(mode="w+") as f:
    f.write("Hello world!!!")
    f.seek(0)
    print(f.read())
