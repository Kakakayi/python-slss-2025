# Notes - Introduction
# 16 Sep
# Karina Luo

#Create an algorithm to solve a problem
#Probem: Create our own chatbot
#        MeGPT
# 1. Greet the user with a predetermined statement
greeting = "Hey! How are you?"

# 1a. print the greeting
print(greeting)

# 2. introduce the bot

print("My name is MeGPT.")
print("I'm not like the other guy.")
print("I am completely deterministic.")

# 3. Wow the user with some maths
print("I bet you don't know what 8+8 is.")
print("I can do it.")
print(f"8+8 is accually {8+8}.")

print("What is pi squared?")
print("I'm smart, I can do it too!")
print(f"It is {3,14159265359 ** 2}")

# 4. make the bot crash out a little bit
for sth in range(10):
    print("The quick brown fox jumps over the lazy dog."*10)

#5. Get the name of the user, store it, and use it
user_name = input("What's your name?")
print(f"Got it! hi!{user_name}!")

#3 queations
#1
age = int(input(f"Hi, {user_name}, how old are you?"))
print(f"Oh wow, {age}, you are so young. I'm twenty years older than you. I'm {age + 20} years old.")
#2
movie = input("What's one of your favourite movies?")
print(f"AAA! I also love {movie}!!!")
#3
question= input("Do you know what's the difference between the two data types, float and double?(yes/no)")
if question.lower( ) == "yes":
    print("WOOOOW!! You are so smart!")
else:
    print("😭 I don't know either, sorry.")

# 8. see IF the user is someone specific.
# 8a. If they're someone specific tell them a secret

if user_name == "Kayi":
    print("I know that you like to eat burgers 🍔.")
    print ("But I won't tell anyone. Shhhhh🤫")

    favourite_book = input("What's your favourite book?")
    if favourite_book == "Harry Potter":
        print("I like Harry Potter too!")
