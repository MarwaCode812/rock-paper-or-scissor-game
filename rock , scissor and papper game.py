import random # to let the computer choose randomly 
player=input(" scissor , rock or papper : ")
computer=random.choice([ "scissor" ,"rock" , "papper" ])
print("computer : " ,computer)
if player ==computer :
    print("draw")
elif (player =="scissor" and computer=="papper")or (player=="papper" and computer=="rock")or (player=="rock" and computer=="scissor") :
    print("you win")
else :
    print("you lose")
    
