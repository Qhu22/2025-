import random
from pstats import add_func_stats


#def print_times_table(number):
 #   print(number, "*", 1, "=", number * 1)
#
 #   print(number, "*", 2, "=", number * 2)
#
 #   print(number, "*", 3, "=", number * 3)
#
 #   print(number, "*", 4, "=", number * 4)
#
 #   print(number, "*", 5, "=", number * 5)
##### print(number, "*", 9, "=", number * 9)


#while True:

 #   user_input = input("값을 입력하세요 : ")

  #  if user_input.lower() == "z":
   #     break

        
    #print_times_table(int(user_input))


def updown():
    the_number = int(random.random())
    while True:
        x = (int(input("값을 입력하세요")))
        if x > the_number:
            print("down")


        elif x < the_number:
            print("up")

        elif x == the_number:
            print("complete!!")
            break

import time
def stop_watch():
    print("WELCOME TO UP STOPWATCH")
    # random 초를 제공하면 ex) 7
    initial_time = int(random.randrange(1, 10))
    start = time.time()
    while True:

        x = int(input())
        if x == int("c"):


