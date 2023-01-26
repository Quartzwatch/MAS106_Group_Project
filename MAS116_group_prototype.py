import numpy as np

#this part should be self explanitory. It rolls the dice. If the binomial distrobution seems out of place I am only getting a 1 or 0 with the odds given as the second variable.

def die_c(rolls):
    return 3*np.ones(rolls)
    
def die_d(rolls):
    return 4*np.random.binomial(1,2/3,rolls)

def die_e(rolls):
    return 4*np.random.binomial(1,1/2,rolls)+1

def die_f(rolls):
    return 4*np.random.binomial(1,1/3,rolls)+2

#numbers the dice.
def die_to_number(die):
    if die=="c":
        return 0
    if die=="d":
        return 1
    if die=="e":
        return 2
    if die=="f":
        return 3
    #Techincally the last if statement is not needed but its clearer if I leave it in.

def wins(rolls,die_rolled):
    #Creates a grid all the results.
    result_grid=np.concatenate(([die_c(rolls)],[die_d(rolls)],[die_e(rolls)],[die_f(rolls)]))

    return np.sum(result_grid[die_rolled]<np.delete(result_grid,die_rolled,axis=0),axis=1)

#Keeps them trapped until they do a vaild input
while True:
    die=str(input("Please enter c, d, e or f."))
    if die=="c" or die=="d" or die=="e" or die=="f":
        break
    print("Error: Please try again.")

while True:
    try:
        rolls=int(input("How many rolls?"))
        break
    except:
        print("Error: Please try again.")

results=wins(rolls,die_to_number(die))

dice_not_chosen=np.delete(["c","d","e","f"],die_to_number(die))

print("""Out of """,rolls,""" rolls: die""",die,"""beat
die""",dice_not_chosen[0],"""""",results[0],"""times for a win rate of""",results[0]/rolls,"""
die""",dice_not_chosen[1],"""""",results[1],"""times for a win rate of""",results[1]/rolls,"""
die""",dice_not_chosen[2],"""""",results[2],"""times for a win rate of""",results[2]/rolls,"""""")
