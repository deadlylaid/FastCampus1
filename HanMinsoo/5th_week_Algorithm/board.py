import json
import os

board = []

if os.path.exists('board.json'):
    with open('board.json','r') as fp:
        board = json.loads(fp.read())

def show_list():
    for i in range(len(board)):
        print(board[i]['text'])

while True:
    cmd = input('글 쓰기(w), 종료(q), 목록(l): ')
    if cmd == 'q':
        break
    if cmd == 'w':
        text = input('글 내용: ')
        cnt = len(board)
        board.append({
            'id' : cnt+1,
            'text': text
        })
    elif cmd == 'l':
        show_list()

with open('board.json','w') as fp:
    fp.write(json.dumps(board))
