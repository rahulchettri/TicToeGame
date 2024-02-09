#tictactoe Game
from random import randint, randrange
mat=[
  ["*","*","*"],
  ["*","*","*"],
  ["*","*","*"]]

#player1="X" player2="O"
game=0  
winner=None
count,curPlayer=0,None
while game==0:  
  count+=1
  if count%2==0:
     curPlayer="P2"
  else:
     curPlayer="P1"
  choices=[]
  for i in range(0,len(mat)):
    for j in range(0,len(mat[i])):
      if mat[i][j]=="*":
        choices.append((i,j))
  if choices:      
     choice=randint(0, len(choices)-1)
     row,col=choices[choice]
     if curPlayer=="P1":
       mat[row][col]="O"
     else:
       mat[row][col]="X"
  else:
    game=1
    print(mat)
    winner="GAME TIED"
  
  if curPlayer=="P1":
    #check row
    for i in range(0,len(mat)):
      flag=0
      g=0
      for j in range(0,len(mat[i])):
        if mat[i][j]=="O":
          flag+=1
      if flag==3:
        game=1
        winner="P1"
        g=1
      if g==1:
        break
        
      

    #check col
    for i in range(0,len(mat)):
      flag=0
      g=0
      for j in range(0,len(mat[i])):
        if mat[j][i]=="O":
          flag+=1
      if flag==3:
        game=1
        winner="P1"
        g=1
      if g==1:
        break
    
    
    #check diagnol
    if mat[0][0]=="O" and mat[1][1]=="O" and mat[2][2]=="O":
      winner="P1"
      game=1
    elif mat[0][2]=="O" and mat[1][1]=="O" and mat[2][0]=="O":
      winner="P1"
      game=1
    print(mat)
    
  elif curPlayer=="P2":
    #check row
    for i in range(0,len(mat)):
      flag=0
      g=0
      for j in range(0,len(mat[i])):
        if mat[i][j]=="X":
          flag+=1
      if flag==3:
        game=1
        winner="P2"
        g=1
      if g==1:
        break
        
      

    #check col
    for i in range(0,len(mat)):
      flag=0
      g=0
      for j in range(0,len(mat[i])):
        if mat[j][i]=="X":
          flag+=1
      if flag==3:
        game=1
        winner="P2"
        g=1
      if g==1:
        break
    
    
    #check diagnol
    if mat[0][0]=="X" and mat[1][1]=="X" and mat[2][2]=="X":
      winner="P2"
      game=1
    elif mat[0][2]=="X" and mat[1][1]=="X" and mat[2][0]=="X":
      winner="P2"
      game=1
    print(mat)  
print(winner)    
    