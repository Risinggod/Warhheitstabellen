fileWriter = open("tabellen.txt", "wt")
#Funktionnen

def warheitswert(a, b, x ):
    fileWriter.write(str(a) + "|" + str(b) + "|" + str(x) + "\n")

a=bytes
b=bytes
x=bytes

def tabelle(warhetswert):
    fileWriter.write( warhetswert )
    fileWriter.write("================\n")
    fileWriter.write("|A:  |B:   |C:  \n")
    fileWriter.write("+----+-----+----\n")

#nand
fileWriter = open("tabellen.txt", "at")
tabelle("======NAND=====")

warheitswert(False, False, not(a and b))
warheitswert(False, True, not(a and b))
warheitswert(True, False, not(a and b))
warheitswert(True, True, not(a and b))

fileWriter.close()

#AND
fileWriter = open("tabellen.txt", "at")
tabelle("======AND=======")

warheitswert(False, False, a and b)
warheitswert(False, True, a and b)
warheitswert(True, False, a and b)
warheitswert(True, True, a and b)

fileWriter.close()
#OR
fileWriter = open("tabellen.txt", "at")
tabelle("======or=======")

warheitswert(False, False, a or b)
warheitswert(False, True, a or b)
warheitswert(True, False, a or b)
warheitswert(True, True, a or b)

fileWriter.close()
#NOT
fileWriter = open("tabellen.txt", "at")
tabelle("======NOT=======")

warheitswert(False, not a, not x)
warheitswert(True, not a,  not x)

fileWriter.close()
#NOR
fileWriter = open("tabellen.txt", "at")
tabelle("======NOR=======")

warheitswert(False, False, not(a or b))
warheitswert(False, True, not(a or b))
warheitswert(True, False, not(a or b))
warheitswert(True, True, not(a or b))

fileWriter.close()

