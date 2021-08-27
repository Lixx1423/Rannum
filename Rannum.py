import random as r
random_num = r.randint(0,100)
print(random_num, "is the number")
bl = []

def number_gussed():
    computer_num = r.randint(0,100)

    if computer_num == random_num:
        print("It did it", computer_num)
        print("List of miss guessed", bl)
    elif computer_num in bl:
        number_gussed()
    else:
        bl.append(computer_num)
        number_gussed()
number_gussed()