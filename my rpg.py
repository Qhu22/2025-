from random import randint

print("게임에 오신것을 환영합니다!")
weapon_level = 0
level0_rate = {"up": 70, "keep": 30, "down":0, "break":0}
level1_rate = {"up": 60, "keep": 25, "down":10, "break": 5}
level2_rate = {"up": 50, "keep": 25, "down":10, "break": 5}
level3_rate = {"up": 45, "keep": 25, "down":10, "break": 5}
level4_rate = {"up": 40, "keep": 25, "down":10, "break": 5}
level5_rate = {"up": 35, "keep": 25, "down":10, "break": 5}
level6_rate = {"up": 30, "keep": 25, "down":10, "break": 5}
level7_rate = {"up": 25, "keep": 25, "down":10, "break": 5}
level8_rate = {"up": 20, "keep": 25, "down":10, "break": 5}
level9_rate = {"up": 10, "keep": 25, "down":10, "break": 5}
level10_rate = {"up": 0, "keep": 100, "down":0, "break": 0}
upgrade_rates =[level0_rate, level1_rate, level2_rate, level3_rate, level4_rate, level5_rate, level6_rate, level7_rate,
                level8_rate, level9_rate, level10_rate]

while True:
    choice = input("숫자를 입력 하세요:   0.종료     1.무기강화")
    if choice == "0" :
        break

    elif choice == "1" :
        reinforcing = input("무기를 강화 하시겠습니까? Y or N")
        if reinforcing == "Y":
            print("무기강화를 시작합니다")
            ran_num = randint(range(1, 99))
            if ran_num <= 59:





