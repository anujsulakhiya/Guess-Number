def deco(func):
    def wrap():
        print("================")
        func()
        print("================")
    return wrap

def welcome():
    print("Welcome to Game")

decoration=deco(welcome)
decoration()

import random

b = random.randint(1, 9)

def condition():
    c=int(input("Enter a Number Again:"))
    if c==b:
        print("You are Winner of this game")
        print(b)

    else:
        print("You Lose")
        print(b)

f = random.randint(1, 9)

def condition2():
    e=int(input("Enter a Number Again:"))
    if e==f:
        print("You are Winner of this game")
        print(f)

    else:
        print("You Lose")
        print(f)



def game():
    a = int(input("Guess the Number between 1 to 9:"))

    def error():
        if a > 9:
            print("!!!...Enter a Single Digit Number...!!!")

    error()

    if a==b:
        print("You are Winner of this game")
        print(b)

    elif a==b+1:
        print("You are Just Near to Ur Answer,Try Again")
        condition()

    elif a==b-1:
        print("You are Just Near to Ur Answer,Try Again")
        condition()

    else:
        print("You Lose")
        print(b)

def game2():

    d = int(input("Try Again:"))

    def error():
        if d > 9:
            print("!!!...Enter a Single Digit Number...!!!")
    error()


    if d==f:
        print("You are Winner of this game")
        print(f)

    elif d==f+1:
        print("You are Just Near to Ur Answer,Try Again")
        condition2()

    elif d==f-1:
        print("You are Just Near to Ur Answer,Try Again")
        condition2()

    else:
        print("You Lose")
        print(f)


import random

b = random.randint(1, 9)

def condition():
    c=int(input("Enter a Number Again:"))
    if c==b:
        print("You are Winner of this game")
        print(b)

    else:
        print("You Lose")
        print(b)

f = random.randint(1, 9)

def condition2():
    e=int(input("Enter a Number Again:"))
    if e==f:
        print("You are Winner of this game")
        print(f)

    else:
        print("You Lose")
        print(f)



def game():
    a = int(input("Guess the Number between 1 to 9:"))

    def error():
        if a > 9:
            print("!!!...Enter a Single Digit Number...!!!")

    error()

    if a==b:
        print("You are Winner of this game")
        print(b)

    elif a==b+1:
        print("You are Just Near to Ur Answer,Try Again")
        condition()

    elif a==b-1:
        print("You are Just Near to Ur Answer,Try Again")
        condition()

    else:
        print("You Lose")
        print(b)

def game2():

    d = int(input("Try Again:"))

    def error():
        if d > 9:
            print("!!!...Enter a Single Digit Number...!!!")
    error()


    if d==f:
        print("You are Winner of this game")
        print(f)

    elif d==f+1:
        print("You are Just Near to Ur Answer,Try Again")
        condition2()

    elif d==f-1:
        print("You are Just Near to Ur Answer,Try Again")
        condition2()

    else:
        print("You Lose")
        print(f)

def again():
    s=input("Want To Continue y/n :")
    if (s=='y'):
        game()
        game2()
        again()
game()
game2()
again()
