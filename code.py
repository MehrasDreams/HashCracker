# import module
from hashlib import md5, sha1, sha256, sha384
from os import system as terminal
from colorama import Fore
from time import sleep
from sys import exit
from platform import system as getos


# This function get your message and say hashs of your message to you 
def get_any_input():
        empty_input = input(Fore.GREEN+"Enter Your String to hash: ")
        hashed_empty = md5(bytes(empty_input, encoding="utf-8"))
        clear_terminal()
        result = hashed_empty.hexdigest()
        print(f"The hash is {result}")
        


# The other function 
def clear_terminal():
    if get_os == "Windows": # Windows is fucking shit you know ? but anyway 
        terminal('cls')
    else:
        terminal('clear')


def read_Password_List():
    with open('pass.txt', 'r') as your_password_file:
        password = [x.strip() for x in your_password_file.readlines()]#1  passwrord=[1234,123456,1234567]  #2   Strip something you do not want done in the crack stages like # or something else
    return password



def hashed_Function(password, hashedstring):
    global found
    if md5(password.encode()).hexdigest() == hashedstring:
        found = True
        print("Hashed {0} cracked: {1}".format(hashedstring, password))




welcome = print(Fore.RED+"Welcome to Mehras Hasher :)) \n")
dec_enc_input = input(Fore.RED+"[1]Encrypt \n[2]Decrypt\n\n:>>>")
get_os = getos()



if dec_enc_input == '1':
    get_any_input()
elif dec_enc_input == '2':
    hash_input = input(Fore.BLUE+"Enter Your Valid Hash: ")






List = read_Password_List()
# Set default found to false 
found = False


while True:
    command_line = str(input(Fore.YELLOW+"#>>>: "))
    if (command_line == "hash"):

        for password in List:
            hashed_Function(password, hash_input) 
            if (found == True):
                    break
        
    else:
        print(Fore.RED+"Unknow Command Contact Us to add or resolve ths command")
        print(Fore.RED+"Wait for it to exit the app :(")
        sleep(13)
        exit()
        