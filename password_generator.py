import random,string
import pyperclip

#variable to store password length
pass_len=25

#function to generate password
def passGenerator():
    
    #password string
    password = ''
    
    #logic for creating the password
    for y in range(pass_len):
        password = password + random.choice(
            string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase  )
        
    #copies created password to clipboard
    pyperclip.copy(password)


passGenerator()
