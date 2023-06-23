cell=[[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]]
cell1=[[0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]]
#part 1
def a1(num):
    for a in range (0,4):
        num[0][a]=sym
def a2(num):
    for a in range (0,4):
        num[3][a]=sym
def a3(num):
    for a in range (0,4):
        num[6][a]=sym
def a4(num):
    a1(num)
    a2(num)
def b1(num):
    for a in range (0,4):
        num[a][0]=sym
def b2(num):
    for a in range (0,4):
        num[a][3]=sym
def b3(num):
    for a in range (3,7):
        num[a][0]=sym
def b4(num):
    for a in range (3,7):
        num[a][3]=sym
def b5(num):
    b1(num)
    b3(num)
def b6(num):
    b2(num)
    b4(num)
def c1(num):
    for a in range (0,4):
        for b in range (0,4):
            if(a==b):
                num[a][b]=sym
def c2(num):
    b=0
    for a in range (3,-1,-1):
        num[b][a]=sym
        b=b+1
def c3(num):
    b=3
    for a in range (0,4):
        num[b][a]=sym
        b=b+1
def c4(num):
    b=3
    for a in range (3,-1,-1):
        num[b][a]=sym
        b=b+1
#part 2
def check(word):
    if((word=='A')):
        a1(cell)
        a2(cell)
        b5(cell)
        b6(cell)
    elif ((word=='B')):
        b5(cell)
        a1(cell)
        a2(cell)
        a3(cell)
        b6(cell)
        cell[0][3] = 0;cell[3][3] = 0;cell[6][3] = 0

    elif ((word == 'C')):
        a1(cell)
        a3(cell)
        b5(cell)
        cell[0][0]=0;cell[0][1] = 0;cell[1][0] = 0;cell[5][0] = 0;cell[6][0] = 0;cell[6][1] = 0;cell[1][1] = sym;cell[5][1] = sym
    elif ((word == 'D')):
        b5(cell)
        a1(cell)
        a3(cell)
        b6(cell)
        cell[0][3] = 0;cell[0][2] = 0;cell[1][3] = 0;cell[5][3] = 0;cell[6][2] = 0;cell[6][3] = 0;cell[1][2] = sym;cell[5][2] = sym
    elif ((word == 'E')):
        b5(cell)
        a1(cell);a2(cell);a3(cell)
    elif ((word == 'f') or (word == 'F')):
        b5(cell)
        a1(cell);a2(cell)
    elif ((word == 'G')):
        b5(cell1);a1(cell1);a2(cell1);a3(cell1)
        cell1[0][0]=0;cell1[0][3]=0;cell1[6][0]=0;cell1[6][3]=0;cell1[3][1]=0;cell1[4][3]='*';cell1[5][3]=sym
    elif ((word == 'H')):
        b5(cell);b6(cell);a2(cell)
    elif ((word == 'I')):
        a1(cell1);a3(cell1);cell1[0][4]=sym;cell1[6][4]=sym;
        for a in range (0,7):
            cell1[a][2]=sym
    elif ((word == 'J')):
        a1(cell);a3(cell);cell[0][0]=0;cell[6][0]=0;b6(cell);cell[6][3]=0;cell[5][0]=sym
    elif ((word == 'K')):
        b5(cell1)
        b = 0
        for a in range(4, -1, -1):
            cell1[b][a] = sym
            b = b + 1
        b = 3
        for a in range(0, 4):
            cell1[b][a+1] = sym
            b = b + 1
    elif (word == 'L'):
        b5(cell1);a3(cell1);cell1[6][4]=sym
    elif (word == 'M'):
        b5(cell1);cell1[1][1]=sym;cell1[2][2]=sym;cell1[1][3]=sym
        for a in range (0,7):
            cell1[a][4]=sym
    elif (word == 'N'):
        b5(cell1);cell1[0][0]=0
        for a in range(1,4):
            cell1[a+1][a]=sym
            cell1[a+2][a]=sym
        for a in range (0,7):
            cell1[a][4]=sym
        cell1[0][4]=0;
    elif (word == 'O'):
        a1(cell1);a3(cell1);b5(cell1)
        for a in range (0,7):
            cell1[a][4]=sym
        cell1[0][0]=0;cell1[0][4]=0;cell1[6][0]=0;cell1[6][4]=0
    elif(word == 'P'):
        b5(cell);a1(cell);a2(cell);b2(cell)
    elif (word == 'Q'):
        a1(cell1);b5(cell1)
        for a in range (0,7):
            cell1[a][4]=sym
        cell1[0][0]=0;cell1[0][4]=0;cell1[5][0]=0;cell1[5][4]=0;cell1[6][0]=0;cell1[4][2]=sym;cell1[3][1]=sym;
        for a in range (1,4):
            cell1[5][a]=sym
    elif (word == 'R'):
        b5(cell);a1(cell);a2(cell);b2(cell);c3(cell)
    elif (word == 'S'):
        b5(cell1);a1(cell1);a2(cell1);a3(cell1)
        for a in range (0,7):
            cell1[a][4]=sym
        cell1[0][0]=0;cell1[0][4]=0;cell1[1][4]=0;cell1[2][4]=0;cell1[6][4]=0;cell1[3][0]=0;cell1[4][0]=0;cell1[5][0]=0;cell1[3][4]=0;cell1[6][0]=0
    elif (word == 'T'):
        a1(cell1);cell1[0][4]=sym
        for a in range (0,7):
            cell1[a][2]=sym
    elif (word == 'U'):
        b5(cell1);a3(cell1);cell1[6][0]=0
        for a in range(0,6):
            cell1[a][4]=sym
    elif (word == 'V'):
        for a in range(0,5):
            cell1[a][0]=sym
            cell1[a][4] = sym
        cell1[5][1] = sym;cell1[5][3]=sym;cell1[6][2]=sym
    elif (word == 'W'):
        b5(cell1);a3(cell1);cell1[6][0]=0;cell1[6][2]=0;cell1[4][2]=sym;cell1[5][2]=sym;cell1[3][2]=sym
        for a in range(0,6):
            cell1[a][4]=sym
    elif(word == 'X'):
        cell1[0][0]=sym;cell1[1][0]=sym;cell1[0][4]=sym;cell1[1][4]=sym;cell1[5][0]=sym
        cell1[6][0]=sym;cell1[5][4]=sym;cell1[6][4]=sym;cell1[2][3]=sym;cell1[4][1]=sym
        b=1
        for a in range (2,6):
            cell1[a][b]=sym
            b=b+1
    elif (word == 'Y'):
        cell1[0][0] = sym;cell1[1][0] = sym;cell1[0][4] = sym;cell1[1][4] = sym;cell1[2][0] = sym;cell1[2][4] = sym
        cell1[3][1]=sym;cell1[3][3]=sym
        for a in range(4,7):
            cell1[a][2]=sym
    elif (word == 'Z'):
        a1(cell1);a3(cell1);cell1[0][4]=sym;cell1[6][4]=sym
        for a in range (1,6):
            cell1[a][5-a]=sym

#part 3
stringg=input("ENTER STRING: ")
sym_num=int(input("ENTER SYMBOL NUMBER: "))
sym=chr(sym_num)
leng=len(stringg)
l0=[];l1=[];l2=[];l4=[];l5=[];l6=[];l3=[]

for h in stringg:
    h=h.upper()
    check(h)
    if((h=='G')or(h=='I')or(h=='K')or(h=='L')or(h=='M')or(h=='N')or(h=='O')or(h=='Q')or(h=='S')or(h=='T')or(h=='U')or(h=='V')or(h=='W')or(h=='X')or(h=='Y')or(h=='Z')):
        for a in range(0,7):
            for b in range(0,5):
                if (cell1[a][b]==0):
                    cell1[a][b]=' '
        n=0
        for each in cell1:
            if(n==0):
                l0.append("\t".join(each))
            elif(n==1):
                l1.append("\t".join(each))
            elif (n == 2):
                l2.append("\t".join(each))
            elif (n == 3):
                l3.append("\t".join(each))
            elif (n == 4):
                l4.append("\t".join(each))
            elif (n == 5):
                l5.append("\t".join(each))
            else:
                l6.append("\t".join(each))
            n=n+1
        for a in range(0,7):
            for b in range(0,5):
                cell1[a][b]=0
    else:
        for a in range(0, 7):
            for b in range(0, 4):
                if (cell[a][b] == 0):
                    cell[a][b] = ' '
        n = 0
        for each in cell:
            if (n == 0):
                l0.append("\t".join(each))
            elif (n == 1):
                l1.append("\t".join(each))
            elif (n == 2):
                l2.append("\t".join(each))
            elif (n == 3):
                l3.append("\t".join(each))
            elif (n == 4):
                l4.append("\t".join(each))
            elif (n == 5):
                l5.append("\t".join(each))
            else:
                l6.append("\t".join(each))
            n = n + 1
        for a in range(0, 7):
            for b in range(0, 4):
                cell[a][b] = 0
#part4
for each in l0:
    print(" ".join(each),end="\t\t")
print("\n")
for each in l1:
    print(" ".join(each),end="\t\t")
print("\n")
for each in l2:
    print(" ".join(each),end="\t\t")
print("\n")
for each in l3:
    print(" ".join(each),end="\t\t")
print("\n")
for each in l4:
    print(" ".join(each),end="\t\t")
print("\n")
for each in l5:
    print(" ".join(each),end="\t\t")
print("\n")
for each in l6:
    print(" ".join(each),end="\t\t")
print("\n")
