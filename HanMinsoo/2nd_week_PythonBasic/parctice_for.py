check_Palindrom = input("단어를 입력하세요")

def Is_is_Palingdrom(a):
    t = len(a)
    word_list = []
    split_word=""
    revers_word=""
    how_many=0
    count = 1
    for i in a:
        if count == t:#만약에 문자열의 길이가 count와 일치한다면
            split_word+=i#i를 split_word에 넣음
            word_list.append(split_word)#워드리스트 에 추가함
            split_word=''#split_word초기화

        elif i is not " ":
            split_word+=i
            #print(i)
        elif i in " " or count == t:
            word_list.append(split_word)
            split_word=''
        elif count == t:
            continue

        count+=1
    #print(word_list)

    for word in word_list:
        re_word = word[::-1]
        if word == re_word:

            how_many+=1
        else :
            continue


    # while i != 0:
    #     revers_word += a[i-1]
    #     i-=1

    # if revers_word == a:
    #     return "This word is Palindrom"
    # else:
    #
    #     return "This word is not Palindrom"

    if how_many == 0:
        print("해당 문장에서는 palindrom은 존재하지 않습니다.")
    else :
        print(how_many,'개의 단어가 palindrom에 속 합니다.')

Is_is_Palingdrom(check_Palindrom)
