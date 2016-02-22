"""
90~100 - A
80~89 - B
70 ~ 79 -C
60 ~69 - D
나머지 F
"""
score = int(input())

if score>=90:
    print('A')
elif score>=80:
    print('B')
elif score>=70:
    print('C')
elif score>=60:
    print('D')
else:
    print('F')


