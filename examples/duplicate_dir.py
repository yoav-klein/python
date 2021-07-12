
import shutil

def create_directory(name):
    while True:
        try:
            shutil.copytree('structure', name)
            break
        except FileExistsError:
            raise

try:
    create_directory("new")
except Exception as e:
    print(dir(e.__traceback__))
    print(e.__traceback__.tb_frame)