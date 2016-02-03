"""
스택수열문제
어디까지 넣었는가?
처음 4를 뽑고 싶다면
stack에 4까지 집어 넣어야한다.

"""
how_many = int(input())

stack1 = []
stack2 = []#부호저장
first_num = 0

for i in range(how_many):
    num_in = int(input())

    if num_in <= how_many:
        check_bigger = num_in - first_num
        first_num = num_in
        if check_bigger > 0:
            for a in range(check_bigger):
                stack2.append('+')

        elif check_bigger < 0:
            for a in range(-(check_bigger)+1):
                stack2.append('-')

for j in stack2:
    print(j)



