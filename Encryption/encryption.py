from math import sqrt
import random
import string
import secrets

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
        print(value) 
        letter = chr(value)
        print(letter)              
        output += letter
       
    final_message = str(output)
    return final_message

def decrypt(strs, shared_secret_number):            
    output = ""
    final_message = ""
    strs = remove(strs)                        
    for letter in strs:
        print(shared_secret_number)                         
        value = ord(letter) - shared_secret_number  
        letter = chr(value)              
        output += letter       
    final_message = output
    final_message = str(final_message)
    print(final_message)

def generate_key(key):
    note = '2659'
    return ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for i in range(20)) + note + key + ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for i in range(20))

def store_key(file_name, key):
    with open(file_name, 'w') as f:
        f.write(key)

def get_key_value(file_name):
    with open(file_name, 'r') as f:
        string = f.read()
        Node = '2659'
        return string[string.index(Node)+5:string.index(Node)+6]

        
        

identity = input("Who am I talking to?(Person1/Person2)")

status = True
while status != False:
    number = random.randint(0, 100)
    if check_if_prime(number) == True:
        root = find_primitive_root(number)
        status = False
    elif check_if_prime(number) == False:
         continue

generator = f"{root} % {number}"

print(generator)

private_key_1_number = random.randint(0, 100)
print(private_key_1_number, 'PV1')
private_key_1 = generate_key(str(private_key_1_number))
public_key_1_number = root**private_key_1_number % number
print(public_key_1_number, 'PU1')
public_key_1 = generate_key(str(public_key_1_number))

private_key_2_number = random.randint(0, 100)
print(private_key_2_number, 'PV2')
private_key_2 = generate_key(str(private_key_2_number))
public_key_2_number = root**private_key_2_number % number
print(public_key_2_number, 'PU2')
public_key_2 = generate_key(str(public_key_2_number))



store_key('public_key_person_1.txt', str(public_key_1))
store_key('private_key_person_1.txt', str(private_key_1))
store_key('public_key_person_2.txt', str(public_key_2))
store_key('private_key_person_2.txt', str(private_key_2))

public_key_2_number = get_key_value('public_key_person_2.txt')
print(public_key_2_number, 'PU2')
private_key_1_number = get_key_value('private_key_person_1.txt')

shared_secret_number = int(public_key_2_number)**int(private_key_1_number) % int(number)
print(shared_secret_number, 'SSN')

if identity == "Person1":
    action = input("Do you want to encrypt or decrypt a message?(encrypt/decrypt)")
    if action == "encrypt":
        text = input("What would you like to encrypt?")
        print("Your encrypted text is:", encrypt(text, shared_secret_number))
    if action == "decrypt":
        text = input("What would you like to decrypt?")
        print("Your decrypted text is:", decrypt(text, shared_secret_number))

if identity == "Person2":
    action = input("Do you want to encrypt or decrypt a message?(encrypt/decrypt)")
    if action == "encrypt":
        text = input("What would you like to encrypt?")
        print("Your encrypted text is:", encrypt(text, shared_secret_number))
    if action == "decrypt":
        text = input("What would you like to decrypt?")
        print("Your decrypted text is:", decrypt(text, shared_secret_number))

