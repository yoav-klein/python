
import subprocess
import os.path

# Running a process with check=true
# if the process terminates with a non-zero exit code
# exception is raised

try:
    subprocess.run(["Powershell.exea", f"{os.path.dirname(__file__)}\\Script.ps1"], check=True, capture_output=True)
except subprocess.CalledProcessError as err:
    print("This process failed !")
    print(dir(err))
    print(err)
    print(err.args)
    print(err.stderr.decode('ascii'))
    print("---- cmd -----")
    print(err.cmd)
except subprocess.SubprocessError:
    print("Something went wrong with running this executable")
# except OSError as err:
#     print(err)
#     print(dir(err))
except FileNotFoundError as err:
    err_string = ''
    if err.filename:
        err_string += err.filename
    
    err_string = f"{err} {err_string}" 

    print(err_string)