import os

class ChangeDirectoryContext:
    def __init__(self, target_directory):
        self.target_directory = target_directory
        self.current_directory = os.getcwd()

    def __enter__(self):
        os.chdir(self.target_directory)

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.current_directory)

# Example usage:
with ChangeDirectoryContext('/path/to/directory'):
    # Code inside this block will be executed in the target directory
    print("Current directory:", os.getcwd())

# Code outside the context block will be executed in the original directory
print("Current directory:", os.getcwd())
