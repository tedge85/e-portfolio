from cmd import Cmd
import os

class MyPrompt(Cmd):
    prompt = "Type> "
    intro = "Hey! Type '?' to list commands!"

    def do_EXIT(self, inp):
        '''Exit the application.'''
        print("Bye")
        return True
    
    def default(self, inp):
        '''Ensure 'x' or 'q' input exits the shell.'''
        if inp == "x" or inp == "q":
            return self.do_exit(inp)
        
        print(f"Default: {inp}")
    
    def do_ADD(self, inp):
        '''Add 2 numbers together.'''
        
        num_1 = input("Enter a number: ")
        num_2 = input("Enter number to add to the first: ")
        
        try:
            result = int(num_1) + num_2
            
            return print(f"{num_1} + {num_2} = {result}")
        
        except TypeError:
            
            print("Inputs must be numbers!")
        
        
    
    def do_LIST(self, inp):
        '''Lists the contents of the current directory.'''
        current_directory = os.getcwd() # Get current directory.
        
        # List contents of directory.
        contents_of_directory = os.listdir(current_directory)
        
        # Iterate through each item in current directory and print.
        for item in contents_of_directory:
            print(item)
        

    do_EOF = do_EXIT 
    
MyPrompt().cmdloop()
print("after")
    
# Q1) What are the two main security vulnerabilities with your shell?
# A) (i) Handling input() variables - processing raw inupt can pose security 
#        problems, such as DOS attacks.
#    (ii) The do_LIST method lists the current directory of the system that 
#         the shell is running on; this will expose all files to the user and
#         could entice hackers to obtain certain files of interest. 