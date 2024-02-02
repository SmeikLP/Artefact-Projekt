import random
import time
#case 1 UwU Translation, dont ask why this exists
def translate(phrase):
    translation = ""
    for char in phrase:
        if char in "RrLlVv":
            translation = translation + "w"
        elif char in "Tt":
            translation = translation + "d"
        else:
            translation = translation + char
    return translation
#case 2 Dice Roles, nothing else to say
def roll_dice(sides, roles):
    value = []
    for i in range(roles):
        outcome = random.randint(1, sides) 
        value.append(outcome)
    return value
#case 3 Gives current Time, only works with CET (I think)
def time_current():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time
#case 4 Caeser Incrition
def incription1(message, key):
    encrypted_sentence = ""
    for char in message:
            if char.isalpha():
                if char.isupper():
                    encrypted_char = chr((ord(char) - 65 + key) % 26 + 65)
                else:
                    encrypted_char = chr((ord(char) - 97 + key) % 26 + 97)
                encrypted_sentence += encrypted_char
            else:
                encrypted_sentence += char

    return encrypted_sentence
#case 5 Primfaktor Zerlegung: Divides a number into prime nunmbers
def pfz(n):
    value = []
    if n>1:
        i=2
    while n % i !=0:
        i=i+1
    value.append(i)
    print(value)
    #function calling itself
    pfz(n/i)
#case 6 Greatest common divident
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
#case 7 Checks if a nubmer is a prime number
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
#case 8 Generates a prime number
def generate_prime_number():
    while True:
        num = random.randint(2**10, 2**11)  # Adjust the range as per your requirements
        if is_prime(num):
            return num
#case 9 Generates somewhat useless overly complex passwords
def random_password(length, weirdness):
    password = []
    for index in range(length):
        password.append(chr(random.randint(1, weirdness)))
    text = ''.join(password)
    return text
#case 10 Converts Hex Numbers to normal decimal numbers
def hex_to_decimal(hex_number):
    decimal_number = int(hex_number, 16)
    return decimal_number
#case 11 Converts binary numbers to normal decimal numbers
def binary_to_decimal(binary_number):
    decimal_number = int(binary_number, 2)
    return decimal_number

print("uwu_translator 1\nDice Roll 2\nCurrent Time 3\nCaeser Incripton 4\nPrime Number Division 5\nGreatest Common Divident 6\nIs Primenumber? 7\n Generate Prime Number 8\nGenerate Password 9\nHex to Decimal 10\nBinary to Decimal 11")

what = int(input("Choose a Tool to use "))

match what:
    case 1:
        phrase = input("Type a word to be translated")
        print(translate(phrase))
    case 2:
        sides = int(input("How many Sides?"))
        roles = int(input("How many roles?"))
        print(roll_dice(sides, roles))
    case 3:
        print(time_current())
    case 4:
        message = input("Type your Message:")
        key = int(input("Key please"))
        print(incription1(message, key))
    case 5:
        n = int(input("Input your integer(Number)"))
        print(pfz(n))
    case 6:
        a = int(input("Input the first number"))
        b = int(input("Input the second number"))
        print(gcd(a, b))
    case 7:
        n = int(input("Input a potential prime number"))
        print(is_prime(n))
    case 8:
        print(generate_prime_number)
    case 9:
        length = int(input("How long should the password be?"))
        print("The weirder the password the more useless it becomes...")
        weirdness = input("How weird should the password be?")
        print(random_password(length, weirdness))
    case 10:
        hex_number = int(input("Input your Hexadezimal number"))
        print(hex_to_decimal(hex_number))
    case 11: 
        binary_number = int(input("Input your Binary nunmber number"))
        print(binary_to_decimal(binary_number))




### https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf



