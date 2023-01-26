import numpy as np

def coinflip():
    try:
        coinflips=np.random.binomial(1, 0.5, size=512)
        for i in range(509):
            if coinflips[i]==0 and coinflips[i+1]==0 and coinflips[i+2]==0:
                ttt=i
                break
        for i in range(509):
            if coinflips[i]==0 and coinflips[i+1]==0 and coinflips[i+2]==1:     
                tth=i
                break
        for i in range(509):
            if coinflips[i]==0 and coinflips[i+1]==1 and coinflips[i+2]==0:     
                tht=i
                break
        for i in range(509):
            if coinflips[i]==0 and coinflips[i+1]==1 and coinflips[i+2]==1:    
                thh=i
                break
        for i in range(509):
            if coinflips[i]==1 and coinflips[i+1]==0 and coinflips[i+2]==0:
                htt=i
                break
        for i in range(509):
            if coinflips[i]==1 and coinflips[i+1]==0 and coinflips[i+2]==1:
                hth=i
                break
        for i in range(509):
            if coinflips[i]==1 and coinflips[i+1]==1 and coinflips[i+2]==0:
                hht=i
                break
        for i in range(509):
            if coinflips[i]==1 and coinflips[i+1]==1 and coinflips[i+2]==1:
                hhh=i
                break
        return np.array([ttt,tth,tht,thh,htt,hth,hht,hhh])
    #This except tries again if one of the patterns is not found within the 512 numbers. This is very unlikely to occur so I am not worried about any bias this has. This could technically cause a recursion error in Python. If you experiance a recursion error, please go play the lottery.
    except:
        print("Error encountered: You can probably ignore this message. It shouldn't affect your results.")
        return coinflip()

def wins(tests):
    victories=np.zeros((8,8))
    for i in range(tests):
        coinflip_results=np.array([coinflip()]*8)
        victories=victories+(coinflip_results<coinflip_results.T).astype(int)
    return victories

tests=1000000

results=wins(tests)/tests
print(wins(tests)/tests)
print("From left to right and up to down: ttt tth tht thh htt hth hht hhh")
print("Read the winrate of each pattern should be read from the row and the loss rate from the column.")
