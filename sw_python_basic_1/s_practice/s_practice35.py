player1 = str(input())
player2 = str(input())

player1 = str(input())
player2 = str(input())

def play():
    global player1
    global player2
    if(player1==player2):
        print("비겼습니다!")
    elif(player1=="바위" and player2 =="가위"):
        print("바위가 이겼습니다!")
    elif(player1=="바위" and player2 =="보"):
        print("보가 이겼습니다!")
    elif(player1=="가위" and player2 =="바위"):
        print("바위가 이겼습니다!")
    elif(player1=="가위" and player2 =="보"):
        print("가위가 이겼습니다!")
    elif(player1=="보" and player2 =="가위"):
        print("가위가 이겼습니다!")
    elif(player1=="보" and player2 =="바위"):
        print("보가 이겼습니다!")    

play()