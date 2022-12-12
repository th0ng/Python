#coding: utf-8

#import module
import random


#In[1]
def takePlayerInput():
    player = "blank"
    while not (player.lower() == "r" or player.lower() == "p" or player.lower() == "s"):
        player = input("Please Enter your input out of R - P - S : ")
    return player.lower()

#In[2]
takePlayerInput()

#In[3]
def takeBotInput():
    lst = ["r", "p", "s"]
    return random.choice(lst)

#In[4]
takeBotInput()

# In[5]
def checkWinner(player, bot):
    if player == "r" and bot == "r":
        return "Draw"
    elif player == "r" and bot == "p":
        return "Bot"
    elif player == "r" and bot == "s":
        return "Player"
    elif player == "p" and bot == "p":
        return "Draw"
    elif player == "p" and bot == "r":
        return "Player"
    elif player == "p" and bot == "s":
        return "Bot"
    elif player == "s" and bot == "s":
        return "Draw"
    elif player == "s" and bot == "p":
        return "Player"
    elif player == "s" and bot == "r":
        return "Bot"
    else:
        return "DRAW"
    
# In[6]:


checkWinner("s", "p")


# In[7]:
def rockPaperScissor():
    endTheGame = "n"
    player_score = 0
    bot_score = 0
    while endTheGame.lower() != "y":
        ply = takePlayerInput()
        bt = takeBotInput()
        print("Bot Entered -", bt)
        winner = checkWinner(player=ply, bot=bt)
        print("Winner is - ", winner)
        if winner == "Player":
            player_score += 2
        elif winner == "Bot":
            bot_score += 2
        else:
            player_score += 1
            bot_score += 1

        print("-----Score Board-----")
        print("-----Player-----", player_score)
        print("-----Bot-----", bot_score)
        print(" ")
        endTheGame = input("You want to end Y/N - ")

# In[8]:
rockPaperScissor()