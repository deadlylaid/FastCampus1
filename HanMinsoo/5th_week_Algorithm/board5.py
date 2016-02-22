"""
대댓글 기능
"""
import json
import os

info = {
    'board': 0,
    'comment': 0
}
board = []
comments = []

if os.path.exists('info.json'):
    with open('info.json','r') as fp:
        info = json.loads(fp.read())


if os.path.exists('board.json'):
    with open('board.json','r') as fp:
        board = json.loads(fp.read())

if os.path.exists('comments.json'):
    with open('comments.json','r') as fp:
        comments = json.loads(fp.read())

def show_list():
    for article in board:
        print('%d. %s'%(article['id'],article['text']))

def delete_article():
    board_id = int(input('글 번호: '))
    for i in range(len(board)):
        if board[i]['id'] == board_id:
            del board[i]
            break

def write_comment():
    board_id = int(input('글 번호: '))
    for article in board:
        if article['id'] == board_id:
            break
    else:
        print('글 없음')
        return
    comment = input('댓글 내용: ')
    info['comment'] += 1
    comments.append({
        'id': info['comment'],
        'text': comment,
        'board': board_id,
        'parent': 0
    })

def write_comment2(board_id):#대 댓글 달기
    comment_id = int(input('댓글 번호: '))#대 댓글을 달게 될 댓글의 아이디
    for comment in comments:#for문 돌림
        if comment['board'] == comment_id:#입력한 아이디의 댓글이 달려있을 경우
            text = input('댓글: ')
            info['comment'] += 1
            comments.append({
            'id': info['comment'],
            'text': text,
            'board': board_id,#보드의 아이디(만약 여러개의 게시글에 같은 댓글이 달려있을때 어떤 게시글의 댓글
                #인지 맞추기 위해서 보드아이디 저장
            'parent': comment_id
        })

        else:
            print('답 댓글을 달 수 없다')
            return
        break
    else:
        print('글 없음')
        return
def preorder(comment,depth):
   print(" "*depth*2, end = "")
   #print("댓글 번호:%d 내용:%s" %(comment['id'], comment['text']))
   depth += 1
   for son in comments:
       if(son['parent'] == comment['id']):
           preorder(son, depth)

def show_article():
    board_id = int(input('글 번호: '))
    for article in board:
        if article['id'] == board_id:
            print('%d. %s'%(article['id'],article['text']))
            break
    else:
        print('글 없음')
        return
    depth=0
    for comment in comments:
        if comment['board'] == board_id:
            depth+=1
            print('  %d. %s'%(comment['id'],comment['text']))
            preorder(comment,depth)

    cmd = input('닫기(q), 댓글의 댓글 달기(c): ')
    if cmd == 'c':
        write_comment2(board_id)

while True:
    cmd = input('글 쓰기(w), 종료(q), 목록(l), 삭제(d), 댓글(c), 읽기(r): ')
    if cmd == 'q':
        break
    if cmd == 'w':
        text = input('글 내용: ')
        info['board']  += 1
        board.append({
            'id' : info['board'],
            'text': text
        })
    elif cmd == 'l':
        show_list()
    elif cmd == 'd':
        delete_article()
    elif cmd == 'c':
        write_comment()
    elif cmd == 'r':
        show_article()

with open('board.json','w') as fp:
    fp.write(json.dumps(board))
with open('comments.json','w') as fp:
    fp.write(json.dumps(comments))
with open('info.json','w') as fp:
    fp.write(json.dumps(info))
