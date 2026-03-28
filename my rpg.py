import random


boss_level = 0
win_rate_a = 0


boss_name = ['길 잃은 그림자', '굶주린 들개 우두머리', '이끼 덮인 바위 골렘',
             '늪의 약탈자 크로커', '저주받은 광산 감독관',
             '혹한의 서리 날개', '심연의 강철 기사', '폭풍을 부르는 그리핀',
             '지옥 불꽃의 수호자', '차원의 균열자 바르카스',
             '세계의 종말자 조준상']
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
boss_matrix = [[0,100]

,[20,80]

,[30,70]

,[50,50]

,[70,30]

,[90,10]

,[100,0]
]
weapon_level = 0
level_diff = weapon_level - boss_level







while True:
    outcomes = ["up", "keep", "down", "break"]


    win_rate = ["win", "lose"]


    choice = input("숫자를 입력 하세요:   0.종료     1.무기강화       2.보스도전")
    if choice == "0" :
        break

    elif choice == "1" :
        reinforcing = input("무기를 강화 하시겠습니까? Y or N")
        if reinforcing == "Y":
            print("강화를 시작합니다")

            current_weights = upgrade_matrix[weapon_level]
            result = random.choices(outcomes, weights=current_weights)[0]
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
        print("보스와 무기의 레벨차이: ", level_diff)
        print("현재보스: ", boss_name[boss_level])


        if level_diff <= -3:
            win_rate_a = 0

        elif level_diff == -2:
            win_rate_a = 1

        elif level_diff == -1:
            win_rate_a = 2


        elif level_diff == 0:
            win_rate_a = 3

        elif level_diff == 1:
            win_rate_a = 4


        elif level_diff == 2:
            win_rate_a = 5


        elif level_diff >= 3:
            win_rate_a = 6

        boss_weights = boss_matrix[win_rate_a]
        fight_result = random.choices(win_rate, weights=boss_weights)[0]

        if fight_result == "win":
            print("승리")
            boss_level = boss_level + 1
        elif fight_result == "lose":
            print("패배")
















