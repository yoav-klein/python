
import shutil

class MyException(Exception):
    pass

def foo():
    try:
        # this will raise a FileNotFoundError
        shutil.copy("non_existing_file", "new_file")
    except FileNotFoundError as err:
        raise MyException(err.args[-1]) from err

def bar():
    try:
        # this will raise a PermissionError
        shutil.copy("error-handling.py", "C:\\Windows\\System\\script.py")
    except:
        raise


try:
    foo()
    bar()
except (OSError, FileNotFoundError, PermissionError, MyException) as err:
    print(type(err), err)
    print(dir(err))