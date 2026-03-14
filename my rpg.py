import random
from random import randint
boss_level = 0
boss_name = ['슬라임', '오크', '']
print("게임에 오신것을 환영합니다!")

upgrade_matrix = [
    [70, 30,  0,  0],
    [60, 25, 10,  5],
    [50, 30, 15,  5],
    [45, 30, 20,  5],
    [40, 30, 20, 10],
    [35, 30, 25, 10],
    [30, 30, 30, 10],
    [25, 30, 30, 15],
    [20, 30, 30, 20],
    [15, 30, 30, 25],
    [ 0, 100,  0,  0]
]

weapon_level = 0
outcomes = ["up", "keep", "down", "break"]
current_weights = upgrade_matrix[weapon_level]
result = random.choices(outcomes,weights = current_weights)[0]
while True:
    choice = input("숫자를 입력 하세요:   0.종료     1.무기강화       2.보스도전")
    if choice == "0" :
        break

    elif choice == "1" :
        reinforcing = input("무기를 강화 하시겠습니까? Y or N")
        if reinforcing == "Y":
            print("강화를 시작합니다")
            if result == "up":
                print("강화성공")
                weapon_level = weapon_level + 1

            elif result == "keep":
                print("강화실패:레벨유지")

            elif result == "down":
                print("강화실패:레벨하락")
                weapon_level = weapon_level -1

            elif result == "break":
                print("강화실패:무기파괴")
                weapon_level = 0


    elif choice == "2":
        print("보스도전")





