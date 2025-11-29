import random
def print_times_table(number):
    print(number, "*", 1, "=", number * 1)

    print(number, "*", 2, "=", number * 2)

    print(number, "*", 3, "=", number * 3)

    print(number, "*", 4, "=", number * 4)

    print(number, "*", 5, "=", number * 5)

    print(number, "*", 6, "=", number * 6)

    print(number, "*", 7, "=", number * 7)

    print(number, "*", 9, "=", number * 9)


while True:

    user_input = input("값을 입력하세요 : ")

    if user_input.lower() == "z":
        break
        
        
    print_times_table(int(user_input))


def updown ():
    the_number = int(random.random())
    while
        x= int(input())
        if x > the_number:
            print("down")

        if x < the_number:
            print("up")

        if x == the_number:
            print("complete!!")

