# Karina Luo
# Oct 6
# #McDoBot

# Write a McDonald's bot that asks if you want fries with your meal.
# Call it  work-mcdobot.py .
# It should accept  Yes/yes  or  No/no  as inputs, and reply
# appropriately depending on the answer.
# If the user inputs anything else, it should repeat back their answer
# and say that it does not understand.


n = input("Would you like fries with your meal?")
if n.lower().strip("!. ,") == "yes":
    print("Here's your meal with fries.")
elif n.lower() == "no":
    print("Here's your mean without fries!")
else:
    print(f"I don't understand {n}")
