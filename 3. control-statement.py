def print_score_applied_or_not():
    score = int(input("점수를 입력하세요"))

    if score > 100 or score <0:
              print("정상적인 점수 범위가 아닙니다")


    else:
        if score >= 80:
            print("합격입니다")


        elif score >=60:
            print("재시험 응시가 필요합니다")

        else:
            print("불합격입니다")
def print_what_was_that():
    while True:
        user_input = input("값을 입력하세요 : ")

        if user_input.lower() == "z" :
            break

    input_number =int(input("숫자를 입력하세요."))
    index = 2

    while index <= input_number:
        if index % 2 == 0:
            print(index)
        index = index + 2


print("피보나치 수열 withlist")
def print_fibonacci_with_list():
    input_number = int(input("숫자를 입력하세요."))
    list = [1, 1]
    while list[-1] <= input_number:
        print(list[-1])
        list.append(list[-1] + list[-2])

print("피보나치 수열 withoutlist")
def print_fibonacci_type2():
    input_number = int(input("숫자를 입력하세요"))
    a=1
    b=1
    c=1

    while c <=input_number:
        print(c)
        c = a + b
        a = b
        b = c


#함수호출방법
#repeated_finction()

#arr = ['aa','bb','cc', 'dd']

#for i in arr:
#    print(i)


#수학
tset = [{'answer': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4]},
{'answer': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4]},
{'answer': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4]},
{'answer': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4]},
{'answer': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4]},
{'answer': [1, 5, 2, 4, 5, 3, 1, 2, 3, 4]}]

a =[1, 5, 2, 4, 5, 3, 1, 2, 3, 4]
correct_answer = [1, 3, 2, 4, 5, 3, 1, 2, 3, 4]
final_score = 0
#힉생의 점수 구하기 한 문항당 10점이라 가정
for (student, correct) in zip(a,correct_answer):
    print(student , '/', correct)
    if student == correct:
        final_score =final_score+10

print(final_score)

