insert_word = input("")
count_num = int(input(""))
left_curser = list(insert_word)
right_curser=[]

i=0

while count_num>0:
    word = input()

    if word.upper()=='L':
        if len(left_curser)!=0:
            right_curser.append(left_curser.pop())

    elif word.upper()=='D':
        if len(right_curser)!=0:
            left_curser.append(right_curser.pop())

    elif word.upper()=='B':
        if len(left_curser)!=0:
            left_curser.pop()

    else:
        a = word.split(' ')
        if a[0].upper()=='P':
            left_curser.append(a[1])

    count_num-=1


result = left_curser+right_curser[::-1]
print(''.join(result))