from cryptography.fernet import Fernet

KEY = Fernet.generate_key()
FERNET = Fernet(KEY)

def encode_text_file(txt_file):
        '''Writes changes made to the contacts in 
        self.contact_list to a .txt file.'''
               
        with open(txt_file, "rb") as file:
            
            file_data = file.read()
                        
            encrypted_file = FERNET.encrypt(file_data)
        
        with open(txt_file, "wb") as file:
            file.write(encrypted_file)
            
encode_text_file("hello.txt")  # Replace quoted text with any text file.

# I selected this algorithim because it is simple but effective - data is read 
# in binary, encrypted then written in binary. It allows for the txt file to 
# be inputted, not binding the function to one text file.

# This algorithim would meet GDPR regulations as it stores data in a way that
# masks its content. Fernet uses SHA256 which is a trusted, secure encoding 
# method.

