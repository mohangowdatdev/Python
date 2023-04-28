#mohans part.............................................................................
import time
# main python proghram

response = ['Welcome to APEX smart bot', '\n Cheif engineer: Manjunath G \n Design engineers: Mohan Gowda and Sanketh B\n Bot name: Rocky',
            'Thanks for using apex we hope we satisfied you', 'Sorry ,this is beyond my ability','This is the the place where we meet the new world']


# fetching tokens from the text command
def extract_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l


# calculating LCM
def lcm(a, b):
    L = a if a > b else b
    while L <= a * b:
        if L % a == 0 and L % b == 0:
            return L
        L += 1


# calculating HCF
def hcf(a, b):
    H = a if a < b else b
    while H >= 1:
        if a % H == 0 and b % H == 0:
            return H
        H -= 1


# Addition
def add(a, b):
    return a + b 


# Subtraction
def sub(a, b):
    return a - b


# Multiplication
def mul(a, b):
    return a * b


# Division
def div(a, b):
    return a / b


# Remainder
def mod(a, b):
    return a % b


# Response to command
# printing - "Thanks for enjoy with me" on exit
def end():
    print(response[2])
    input('press enter key to exit')
    exit()

def age():
    return print("I was Born on 15th December 2019 just 9 days ago, You can wish me next year")
def whosename():
    return print("Whose name do you want?" )
def botname():
    return print("My name is Rocky Thank you for asking ",nm)
def engname():
    return print("My pleasured engineer is Mohan Gowda \n I even have a senior chief engineer do you want to know?")
def hero():
    return print("I am a hero to myself, lol")
def yes():
    return print("Senior Chief Engineer: Manjunath G")
def thank():
    return print("You are Welcome ",nm)
def sorry():
    print(response[3])
def appreciation():
    return print("Thank you ",nm," this means a lot for me. I will get better everyday and rule the artificial intelligence \n taking over alexa google and siri. \n Please keep helping me learn things.")

# Operations - performed on the basis of text tokens
operations = {'ADD': add, 'PLUS': add, 'SUM': add, 'ADDITION': add,
              'SUB': sub, 'SUBTRACT': sub, 'MINUS': sub, 'SUBTRACTION': sub,
              'DIFFERENCE': sub, 'LCM': lcm, 'HCF': hcf,
              'PRODUCT': mul, 'MULTIPLY': mul, 'MULTIPLICATION': mul,'INTO': mul,
              'DIVISION': div,'DIVIDE': div,'BY': div,'DIVIDED': div, 'MOD': mod, 'REMAINDER'
              : mod, 'MODULAS': mod, 'MODULUS': mod}

# commands
commands = {'NAMES' : whosename,'ENGINEER': engname,'ENGINEERS': engname, 'BOT' : botname,
            'NAME' : botname ,'OLD' : age ,'AGE': age,'BORN': age, 'EXIT': end, 'END': end, 'CLOSE': end,
            'HERO' : hero, "YES": yes, "WELL DONE" : appreciation , "GOOD": appreciation , "PERFECT": appreciation,
            "KEEP_IT_UP" : appreciation, "THANK": thank }

print('---------------------------' + response[0] + '------------------------------')
print('--------------' + response[4] + '--------------------')

nm=input("\n Enter your name: ")
time.sleep(2)
print("\n Hello ",nm, "Welcome to APEX Smart Bot")
time.sleep(2)
print("\n My Name is Rocky")
time.sleep(2)
print("\n I am an AI bot who is designed by my engineer Mohan Gowda")
time.sleep(3)
print("\n Please Enter your queries down but make sure that you don't use any symbols like (+)(-)(/)(*) \n")
time.sleep(4)
print("\n Loading please wait..... \n")
time.sleep(5)

#sankeths part..........................................................................................
while True:
    print()
    text = input('Enter your queries: ')
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extract_from_text(text)
                r = operations[word.upper()](l[0], l[1])
                print(r)
            except:
                print('something went wrong please try again !!')
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()
