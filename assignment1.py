print("<----RULES---->")
print("1. BRUSH DOWN")
print("2. BRUSH UP")
print("3. VEHICLE ROTATES RIGHT")
print("4. VEHICLE ROTATES LEFT")
print("5. MOVE UP TO X")
print("6. JUMP")
print("7. REVERSE DIRECTION")
print("8. VIEW THE MATRIX")
print("0. EXIT")
print("Please enter the commands with a plus sign (+) between them.")




girdi = input("Write your input: ")
veriler = girdi.split("+")
n = int(veriler[0])
matrix = [[" "] * (n + 2) for i in range(n + 2)]

for i in range(n + 2):
    matrix[i][0] = "+"
    matrix[i][-1] = "+"
    matrix[-1][i] = "+"
    matrix[0][i] = "+"

move = []
movesayi = []
for i, hareket in enumerate(veriler):  # 5_ bulma !
    if '5_' in hareket:
        movesayi.append(int(hareket[2:]))
        move.append(hareket)
flag = 0
sub_list = ["8","0"]
if(all(x in veriler for x in sub_list)):
    flag = 1


pozx = 1
pozy = 1
next_pozx = 2
next_pozy = 1
brush = 2
if flag == 1:
    for x in veriler[1:]:

        if x == "1":
            brush = 1  # brush down (boya)
            matrix[pozy][pozx] = "*"
        elif x == "2":
            brush = 2  # brush up (boyama)

        elif x == "3":  # sağa dön
            if next_pozx > pozx:
                next_pozx = pozx
                next_pozy = pozy + 1
            elif pozx > next_pozx:
                next_pozx = pozx
                next_pozy = pozy - 1
            elif next_pozy > pozy:
                next_pozy = pozy
                next_pozx = pozx - 1
            elif pozy > next_pozy:
                next_pozy = pozy
                next_pozx = pozx + 1

        elif x == "4":  # sola dön
            if next_pozx > pozx:
                next_pozx = pozx
                next_pozy = pozy - 1
            elif pozx > next_pozx:
                next_pozx = pozx
                next_pozy = pozy + 1
            elif next_pozy > pozy:
                next_pozy = pozy
                next_pozx = pozx + 1
            elif pozy > next_pozy:
                next_pozy = pozy
                next_pozx = pozx - 1

        elif x == "7":  # 180 derece dön
            if next_pozx == pozx + 1:
                next_pozx = pozx - 1
            elif next_pozx == pozx - 1:
                next_pozx = pozx + 1
            elif next_pozy == pozy + 1:
                next_pozy = pozy - 1
            elif next_pozy == pozy - 1:
                next_pozy = pozy + 1

        elif x == "6":  # jump
            brush = 2
            for i in range(3):
                if next_pozx != pozx:
                    if next_pozx > n:
                        next_pozx = 1
                        pozx = 1
                        next_pozx = 2

                    elif next_pozx == 0:
                        next_pozx = n
                        pozx = next_pozx
                        next_pozx = n - 1

                    else:
                        pozx2 = pozx
                        pozx = next_pozx
                        next_pozx = next_pozx + next_pozx - pozx2


                else:
                    if next_pozy > n:
                        next_pozy = 1
                        pozy = 1
                        next_pozy = 2

                    elif next_pozy == 0:
                        next_pozy = n
                        pozy = next_pozy
                        next_pozy = n - 1

                    else:
                        pozy2 = pozy
                        pozy = next_pozy
                        next_pozy = next_pozy + next_pozy - pozy2

        elif x == "8":
            for i in matrix:
                print(*i, sep="")

        elif x == "0":
            break

        elif x in move:
            yuru = movesayi[move.index(x)]
            if brush == 1:
                for i in range(int(yuru)):
                    if next_pozx != pozx:
                        if next_pozx > n:
                            next_pozx =1
                            matrix[pozy][next_pozx] = "*"
                            pozx= 1
                            next_pozx = 2

                        elif next_pozx == 0:
                            next_pozx = n
                            matrix[pozy][next_pozx] = "*"
                            pozx= next_pozx
                            next_pozx = n-1

                        else:
                            matrix[pozy][next_pozx] = "*"
                            pozx2 = pozx
                            pozx = next_pozx
                            next_pozx = next_pozx + next_pozx - pozx2


                    else:
                        if next_pozy > n:
                            next_pozy = 1
                            matrix[next_pozy][pozx] = "*"
                            pozy = 1
                            next_pozy = 2

                        elif next_pozy == 0:
                            next_pozy = n
                            matrix[next_pozy][pozx] = "*"
                            pozy = next_pozy
                            next_pozy = n - 1

                        else:
                            matrix[next_pozy][pozx] = "*"
                            pozy2 = pozy
                            pozy = next_pozy
                            next_pozy = next_pozy + next_pozy - pozy2

            if brush == 2:
                for i in range(int(yuru)):
                    if next_pozx != pozx:
                        if next_pozx > n:
                            next_pozx =1
                            pozx= 1
                            next_pozx = 2

                        elif next_pozx == 0:
                            next_pozx = n
                            pozx= next_pozx
                            next_pozx = n-1

                        else:
                            pozx2 = pozx
                            pozx = next_pozx
                            next_pozx = next_pozx + next_pozx - pozx2


                    else:
                        if next_pozy > n:
                            next_pozy = 1
                            pozy = 1
                            next_pozy = 2

                        elif next_pozy == 0:
                            next_pozy = n
                            pozy = next_pozy
                            next_pozy = n - 1

                        else:
                            pozy2 = pozy
                            pozy = next_pozy
                            next_pozy = next_pozy + next_pozy - pozy2


        else:
            print("ERROR!.", "You entered wrong input!", "Therefore, output may incorrect!", sep="\n")
            break
else:
    print("ERROR!.", "You entered wrong input!", "Therefore, output may incorrect!", sep="\n")
