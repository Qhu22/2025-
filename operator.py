x = 10 #대입연산자
y = 15

#조건연산자
z = x == y
print("x == y :", z)

z = x != y
print("x != y :", z)
z = x > y
print("x > y :", z)
z = x >= y
print("x >= y :", z)
z = x < y
print("x < y :", z)
z = x <= y
print("x <= y :", z)

z = x + y
print("x + y :", z)
z = x - y
print("x - y :", z)
z = x * y
print("x * y :", z)
z = x / y
print("x / y :", z)

z = x % y
print("x % y :", z)
#나머지 출력

z = x // y
print("x // y :", z)
#몫 출력

z = x ** y
print("x ** y", z) # 제곱


z = x + 5 * 3 # 곱셈이 덧셈보다 우선순위가 높음
print("x + 5 * 3:" , z)

z = (x + 5) * 3 # 괄호로 우선 순위 높이기
print("(x + 5) * 3:" , z)

str_x = "hello"
str_y = "python"

str_z = str_x + str_y
print("str_x + str_y :", str_z )
#unsupported operand type(s) for - 'str' and 'str'
#str_z = str_x - str-y
#print("str_x - str-y" , str_z)
str_z = str_x * 2
print("str_x * 2 :", str_z)

#delayed_effect_skill_a_ = "" # snake_case
#delayedeffectskilla ='' #camel case

array_x = [3, 6]
array_y = [4, 5]

array_z = array_x + array_y
print("array_x + array_y", array_z)

array_z = array_x * 2
print("array_x * 2", array_z)

array_z = array_x * array_y[0]
print("array_x + array_y[0] :", array_z)

#논리 연산자
report_card = {
    "국어": 3,
    "수학": 2,
    "영어": 6,
    "물리": 1,
    "화학": 2,
    "생명과학": 1
}

can_apply = report_card["국어"] < 3 and report_card["수학"] < 3 and report_card["영어"] < 3

print("지원가능여부:", can_apply)

# 3합 6
tatal_score = report_card["국어"]+report_card["수학"]+report_card["영어"] <=6
print("3합 6:", tatal_score)

#과학 영재반
can_apply_class_for_the_gifted = report_card["물리"] == 1 or report_card["화학"] ==1 or report_card["생명과학"]
print("영재반 지원가능여부", can_apply_class_for_the_gifted)

