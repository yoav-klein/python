
###
# Simple example of class-based context manager. 
####

class HelloContextManager:
    def __enter__(self):
        print("Enter context manager!")
        return "Hello world !"
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Exiting !")
        print(exc_type)
        print(exc_value)
        print(exc_tb)

###
#   Another way to use this, we can define the HelloContextManager()
#   and assign it to a variable, and then call 'with' with that variable. 
#
# hcm = HelloContextManager()
# with hcm as cm:
##

with HelloContextManager() as cm:
    print(cm)

    # Note that when raising an exception, the __exit__ funciton will receive the type, value, and traceback. 
    # if returns True explicitly, execution will continue, otherwise - the exception will be raised outside the context
    raise Exception("What an error !")

print("Going on")

