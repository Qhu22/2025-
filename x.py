x=1
print(x+3)

x=3.5
print(x)


x=3+5
print(x)


x=3==5
print(x)


x=True
print(x)


x = [1,2,3,4,5]#list
print(x[1])
print(type(x))
print(x[3])

x = [1,2,3,4,5]
x= x * 2
print("x * 2", x)
#slicing
print(x[2:5]) # [start_index : end_index+1]
print("append======")
x.append(7)
print(x)
print("insert======")
x.insert(1,9)
print(x)
print("remove======")#인덱스가 아닌 값을 지우는 함수
x.remove(1) # 인덱스가 아닌 값을 지우는 함수
print(x)
print("9->6=========")
x[0] = 6
print(x)

#참조 할 수 없는 위치를 참조했을때 (배열길이 이상)
#IndexError: list assignment index  out of range
#x[7] = 1
print("배열의 길이=========")
print(len(x))

print("마지막 배열의 인덱스")
print(len(x)-1)






x = {'a': 100, 'b': 200}
print(x['a'])
print(type(x))

example = {

    'python': [True, False, True, True, True, True, True, False, False, True],

    'java': [True, False, False, True, True, True, False, False, False, True],

    'git': [False, False, True, True, False, True, True, True, True, True],

}
print(example['python'][0])
print(example['python'])
print(example)
python_description = [

    {

        'answer': 1,

        'description': 'python에 대한 설명은 1번이 맞습니다.'

    },

    {

        'answer': "list",

        'description': 'python의 열거형 데이터 타입은 list입니다.'

    },

    {

        'answer': True,

        'description': 'python의 LIST 안에 Dictionary를 사용할 수 있습니다.'

    },

]
print(python_description[0])
list_example = [1, "+", 2, "="]

dict_example = {
    1:'asdf'#key에 변수,함수는 사용불가하지만 상수, 문자는 가능하다 ,
    ,'a':'asdf'
}
















