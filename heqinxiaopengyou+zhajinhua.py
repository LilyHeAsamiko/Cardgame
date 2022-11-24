import numpy as np 
#card_number =[1,2,3,4,5,6,7,8,9,10,11,12,13] stands for ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
card_pattern = ['D','C','H','S'] stands for ['diamond', 
'clover', 'heart', 'spade'] Card =[card_number, card_pattern]*/
#判斷牌型 P=4,3,2,1,0 分別代表豹子，同花順，一般順，同花，一對，單
def Pattern(Card):
    assert(len(Card) == 3)
    if(Card[0][0] == Card[1][0] && Card[1][0]== Card[2][0]):
        P = 4
        if(((Card[0][0] - Card[1][0])*(Card[1][0] - Card[2][0])==1):
            if(Card[0][1] == Card[1][1] && Card[1][1]== Card[2][1]):
                P = 3
            else:
                P = 2
        if(Card[0][0] == Card[1][0] or Card[1][0] == Card[2][0] or Card[0][0] == Card[2][0]) :
        P = 1
    return P
       
card = [('1','D'),('2','D'),('3','D'),('4','D'),('5','D'),('6','D'),('7','D'),('8','D'),('9','D'),('10','D'),('11','D'),('12','D'),('13','D')
,('1','C'),('2','C'),('3','C'),('4','C'),('5','C'),('6','C'),('7','C'),('8','C'),('9','C'),('10','C'),('11','C'),('12','C'),('13','C'),
,('1','H'),('2','H'),('3','H'),('4','H'),('5','H'),('6','H'),('7','H'),('8','H'),('9','H'),('10','H'),('11','H'),('12','H'),('13','H'),
('1','S'),('2','S'),('3','S'),('4','S'),('5','S'),('6','S'),('7','S'),('8','S'),('9','S'),('10','S'),('11','S'),('12','S'),('13','S')]
print(card)
try:
    input("请输入玩家人数 N(2-6):")
except:
    print(“輸入錯誤，非2-6整數”)
    input(“请重新输入玩家人数 N(2-6)：")
turns = 0
cardcp = card
Card = []
Score = []
Final_Score = np.zeros(N)
for turns < int(13*4/N):
    for N > 1:
        Card.append(random(cardcp, 3))
        Score.append(Pattern(Card[N]))
        cardcp.delete(Card)
        N -= 1
    Final_Score[np.max(Score[turns], 1)] += 1
print('總比分: '+Final_Score)
print('最後勝者: '+np max(Final_Score,1))
