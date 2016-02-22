money, how_much = map(int,input().split())
money_type = []
for i in range(1,money+1):
    money_type.append(int(input()))
count_coin = 0

for i in money_type[money::-1]:
    if how_much<10:
        count_coin+=int(how_much/i)
        how_much = how_much - i*int((how_much/i))

    elif int(how_much/i)>0:
        count_coin+=int(how_much/i)
        how_much = how_much - i*int((how_much/i))


print(int(count_coin))