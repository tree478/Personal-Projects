#A program that uses public key cryptography algorithms to encrypt and decrypt user input.

from math import sqrt
import random
import string
import secrets

def remove(strs):
    ns=""

    for i in strs:
        if(not i.isspace()):
            ns+=i

    return ns

def encrypt(strs, shared_secret_number):           
    output = ""   

    for letter in strs:                        
        value = ord(letter) + shared_secret_number
        letter = chr(value)              
        output += letter
       
    final_message = str(output)
    return final_message

def decrypt(strs, shared_secret_number):            
    output = ""
    final_message = ""
    strs = remove(strs)                        
    for letter in strs:                         
        value = ord(letter) - shared_secret_number  
        letter = chr(value)              
        output += letter       
    final_message = output
    final_message = str(final_message)
    return final_message

def check_if_prime(number):
    if number == 0:
        return False
    
    if number == 1:
        return False
    
    for i in range(2, int(sqrt(number))+1):
        if number%i == 0:
            return False
        
    return True

def find_primitive_root(number):

    while True:
        list_of_numbers = []
        root = random.randrange(1, number)

        for i in range(1, number):
            list_of_numbers.append(root**i%number)
            
        if len(set(list_of_numbers)) != len(list_of_numbers):
                continue
        
        if len(set(list_of_numbers)) == len(list_of_numbers):
                return root
        
status = True
while status != False:
    number = random.randint(0, 100)
    if check_if_prime(number) == True:
        root = find_primitive_root(number)
        status = False
    elif check_if_prime(number) == False:
         continue

generator = f"{root} % {number}"

class User:
    def __init__(self, generator, private_key, root, number):
        self.generator = generator
        self.private_key = private_key
        self.public_key = root**private_key % number

    def generate_key(self, key):
        note = '2659'
        return ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for i in range(20)) + note + str(key) + ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for i in range(20))

    def store_key(self, file_name, key):
        with open(file_name, 'w') as f:
            f.write(key)

    def get_key_value(self, file_name):
        with open(file_name, 'r') as f:
            string = f.read()
            Node = '2659'
            return string[string.index(Node)+5:string.index(Node)+6]

        


user1 = User(generator, random.randint(1,100), root, number)
user2 = User(generator, random.randint(1,100), root, number)

# user1.store_key('user1publickey.txt', user1.generate_key(user1.public_key))
# user1.store_key('user1privatekey.txt', user1.generate_key(user1.private_key))
# user2.store_key('user2publickey.txt', user2.generate_key(user2.public_key))
# user2.store_key('user2privatekey.txt', user2.generate_key(user2.private_key))

shared_secret_number = int(user2.get_key_value('user2publickey.txt')) ** int(user1.get_key_value('user1privatekey.txt')) % number

if shared_secret_number == 0:
    shared_secret_number = shared_secret_number * random.randint(1,9)

action = 'start'
while action != 'quit':
    action = input("Do you want to encrypt or decrypt a message?(encrypt/decrypt/quit)")
    if action == "encrypt":
        text = input("What would you like to encrypt?")
        print("Your encrypted text is:", encrypt(text, shared_secret_number))
    if action == "decrypt":
        text = input("What would you like to decrypt?")
        print("Your decrypted text is:", decrypt(text, shared_secret_number))
    
