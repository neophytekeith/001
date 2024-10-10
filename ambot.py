from random import *
from base64 import *
from time import *

rand_num = randint(1,50)

buhay = 5

print("Hulaa an number para makuha mo an text")

while buhay != 0:
    try:
        guess = int(input("Guess Number(1-50):"))
        buhay-=1
        if guess not in range(1,51):
            print("Enter only 1-50")
            continue
        if buhay == 0:
            print("Pls try again haha")
            print(f"Random number is: {rand_num}")
        else:
            if guess < rand_num:
                print("Higher!")
                print(f"May {buhay} ka nala na buhay.")
            elif guess > rand_num:
                print("Lower!")
                print(f"May {buhay} ka nala na buhay.")
            elif guess == rand_num:
                string0 = "VjFST1MwNVhUa2xWYlhCYVYwWkZPUT09"
                string1 = string0
                string2 = string1
                string3 = string2
                string4 = string3
                print("decoding.")
                sleep(2)
                print("decoding....")
                sleep(5)
                decoded = b64decode(string4).decode()
                print(decoded)
                break
    except ValueError:
        print("Please enter only a number.")