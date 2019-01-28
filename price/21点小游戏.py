# import random
# import numpy as np
# from sys import exit
#
# poker_name = ['♦10', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦A', '♦J', '♦K', '♦Q',
#  '♣10', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣A', '♣J', '♣K', '♣Q',
#  '♥10', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥A', '♥J', '♥K', '♥Q',
#  '♠10', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠A', '♠J', '♠K', '♠Q']
# #牌堆用一个列表来表示
#
# poker_value = {'♣A':1,'♥A':1,'♠A':1,'♦A':1,'♦10': 10, '♦2': 2, '♦3': 3, '♦4': 4, '♦5': 5, '♦6': 6, '♦7': 7, '♦8': 8, '♦9': 9,  '♦J': 10, '♦K': 10, '♦Q': 10,
#  '♣10': 10, '♣2': 2, '♣3': 3, '♣4': 4, '♣5': 5, '♣6': 6, '♣7': 7, '♣8': 8, '♣9': 9,  '♣J': 10, '♣K': 10, '♣Q': 10,
#  '♥10': 10, '♥2': 2, '♥3': 3, '♥4': 4, '♥5': 5, '♥6': 6, '♥7': 7, '♥8': 8, '♥9': 9,  '♥J': 10, '♥K': 10, '♥Q': 10,
#  '♠10': 10, '♠2': 2, '♠3': 3, '♠4': 4, '♠5': 5, '♠6': 6, '♠7': 7, '♠8': 8, '♠9': 9,  '♠J': 10, '♠K': 10, '♠Q': 10}
#  #根据牌堆里面的名称，设置每张牌对应的分值
#
#
# def Dealing_Poker(poker_database):
#     #发一张牌，并在牌堆中删除这张牌
#     return poker_database.pop(random.randint(0,len(poker_database)-1))
#
# def Score_Count(hand_poker):
#     #计算牌的点数
#     Score = 0
#     Have_Ace = False
#     for k in hand_poker:
#         Score += poker_value[k]
#     for i in hand_poker:
#         if i in Ace:
#             Have_Ace = True
#             break
#         else: continue
#     if Have_Ace == True:
#         if Score + 10 <= 21:
#             Score = Score + 10
#     return Score
#
# def Judgement(your_score,pc_score):
#     #结束要牌的时候，计算双方的点数，判断输赢
#     if your_score > 21 and pc_score > 21:
#         print('PUSH')
#         return np.array([0,0])
#     elif your_score > 21 and pc_score <= 21:
#         print('YOU LOSE')
#         return np.array([0,1])
#     elif your_score <= 21 and pc_score > 21:
#         print('YOU WIN')
#         return np.array([1,0])
#     elif your_score <= 21 and pc_score <= 21:
#         if your_score < pc_score:
#             print('YOU LOSE')
#             return np.array([0,1])
#         elif your_score > pc_score:
#             print('YOU WIN')
#             return np.array([1,0])
#         else:
#             print('PUSH')
#             return np.array([0,0])
#
#
# def Hit_or_Stand():
# #玩家需要判断是否继续叫牌
#     AskPoker = input('Would You Hit?(Y/N)>>:')
#     if AskPoker.upper() == 'Y':
#         return Dealing_Poker(poker_database)
#     elif AskPoker.upper() == 'N':
#         print('You stand')
#         return False
#     else:
#         print('Wrong input, please input Y/y or N/n!>>')
#         return Hit_or_Stand()
#
# def Continue_Or_Quit():
# #在每一轮结束后，判断是否继续下一轮的游戏。当牌堆里面牌的数目不足的时候，自动停止游戏
#     NextRound = input('Would you like start next round?(Y/N)>>')
#     if NextRound.upper() == 'Y':
#         if len(poker_database) <10:
#             print('The left pokers is not enough')
#             input('Game Over')
#             exit(1)
#         else:
#             return True
#     elif NextRound.upper() == 'N':
#         input('Game Over')
#         exit(1)
#     else:
#         print('Wrong Input, Please Try One More Time!')
#         Continue_Or_Quit()
#
# def Start_Dealing(poker_database):
# #开局的时候，自动给玩家和电脑发两张牌
#     return [poker_database.pop(random.randint(0,len(poker_database)-1)),poker_database.pop(random.randint(0,len(poker_database)-1))]
#
# def One_Round(poker_database):
# #一个回合的游戏
#     you_get = Start_Dealing(poker_database)
#     pc_get = Start_Dealing(poker_database)
#     print(f'Your hand poker:{you_get[0]} , {you_get[1]}')
#     print(f'PC\'s hand poker:{pc_get[0]} , ?\n')
#     your_hand_poker.extend(you_get)
#     pc_hand_poker.extend(pc_get)
#     score = np.array([Score_Count(your_hand_poker),Score_Count(pc_hand_poker)])
#     if score[0] == 21 or score[1] == 21:
#         print('BlackJack')
#         return Judgement(score[0],score[1])
#     else:
#         while score[0] <= 21:
#             Get_New_Poker = Hit_or_Stand()
#             if Get_New_Poker != False:
#                 your_hand_poker.append(Get_New_Poker)
#                 print(f'You Hand Poker:{your_hand_poker}')
#                 score[0] = Score_Count(your_hand_poker)
#                 if score[0] > 21:
#                     print('You Bust')
#                     print(f'PC\'s Hand Poker:{pc_hand_poker}')
#                     return Judgement(score[0],score[1])
#                 else:continue
#             elif Get_New_Poker == False:
#                 while score[1] < score[0]:
#                     PC_Ask_Poker = Dealing_Poker(poker_database)
#                     pc_hand_poker.append(PC_Ask_Poker)
#                     pc_score = Score_Count(pc_hand_poker)
#                     score[1] = pc_score
#                 print(f'PC final hand poker:{pc_hand_poker}')
#                 return Judgement(score[0],score[1])
#                 break
#             else:continue
#
#
#
# Ace = {'♣A','♥A','♠A','♦A'} #用于判断手牌中是否有A，根据分数来选择A牌的分值是0还是1
# poker_deck = 1 #一共是使用几副牌
# poker_database = poker_name * poker_deck #最终生成的牌堆
# total_score = np.array([0,0])    #总分的计分器
#
# Round = 1
# while len(poker_database) > 10:
#     your_hand_poker = []
#     pc_hand_poker = []
#     input('Start Dealing, good luck...<<Enter>>\n')
#     print(f'Round {Round}:')
#     print('.' * 60)
#     score = One_Round(poker_database)
#     total_score += score
#     print(f'Total score is:{total_score[0]}:{total_score[1]}')
#     Round += 1
#     Continue_Or_Quit()

import random
from functools import reduce


# 游戏
def game():
    print('------------------------------------------')
    print('欢迎光临21点！游戏开始！')
    user = [randcard(), randcard()]
    ai = [randcard(), randcard()]
    ai_hide = [ai[0], '暗牌']
    print('您的牌组：', user)
    print('庄家牌组：', ai_hide)
    if sum(user) > 21:
        print('游戏结束！您的牌组是', user, '，点数是', sum(user), '，超过了21点。')
        return game()
    elif sum(user) == 21:
        print('哇哦！刚好21点！')
        return game()
    elif sum(ai) > 21:
        print('恭喜！您获得了胜利！庄家的点数为', sum(ai), '，超过了21点。')
        return game()
    elif sum(user) > 21 and sum(ai) > 21:
        print('平局！您的点数是', sum(user), '，庄家的点数是', sum(ai), '。')
        return game()
    else:
        decide(user, ai, ai_hide)
        compare(user, ai)


# 抉择
def decide(user, ai, ai_hide):
    decision = str(input('请输入您的决定，“h”是继续发牌，“s”是停止发牌（h/s）：')).lower()
    if decision == 'h':
        user.append(randcard())
        ai.append(randcard())
        ai_hide.append('暗牌')
        if sum(user) > 21:
            print('游戏结束！您的牌组是', user, '，点数是', sum(user), '，超过了21点。')
            return game()
        elif sum(ai) > 21:
            print('恭喜！您获得了胜利！庄家的点数为', sum(ai), '，超过了21点。')
            return game()
        elif sum(user) > 21 and sum(ai) > 21:
            print('平局！您的点数是', sum(user), '，庄家的点数是', sum(ai), '，你们的点数都超过了21点。')
            return game()
        else:
            print('您的牌组：', user)
            print('庄家牌组：', ai_hide)
            return decide(user, ai, ai_hide)
    elif decision == 's':
        return


# 牌组
cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10,
         10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]


# 发牌
def randcard():
    index = random.randint(0, len(cards) - 1)
    randcard = cards[index]
    del cards[index]
    if len(cards) == 0:
        print('游戏结束！没牌发啦！')
        return game()
    else:
        return randcard


# 求和
def sum(user):
    return reduce(lambda x, y: x + y, user)


# 判断
def compare(user, ai):
    minus_user = 21 - sum(user)
    minus_ai = 21 - sum(ai)
    if minus_user < minus_ai:
        print('恭喜！您获得了胜利！您的点数是', sum(user), '，庄家的点数是', sum(ai), '。')
        return game()
    elif minus_user > minus_ai:
        print('非常遗憾！您输掉了本场对局，您的点数是', sum(user), '，庄家的点数是', sum(ai))
        return game()
    elif minus_user == minus_ai:
        print('平局！您的点数是', sum(user), '，庄家的点数是', sum(ai), '。')
        return game()


# 执行
game()