def warheitswert(a, b, x ):
    fileWriter.write(str(a) + "|" + str(b) + "|" + str(x) + "\n")

def tabelle(warhetswert):
    fileWriter.write( warhetswert )
    fileWriter.write("\n")
    fileWriter.write("|A:  |B:   |C:  \n")
    fileWriter.write("+----+-----+----\n")

def print_nand():
    a = False
    b = False
    warheitswert(a, b, not (a and b))

    b = True
    warheitswert(a, b, not (a and b))

    a = True
    b = False
    warheitswert(a, b, not (a and b))

    b = True
    warheitswert(a, b, not (a and b))


fileWriter = open("tabellen.txt", "wt")
#Funktionnen
#x=bytes



#nand
fileWriter = open("tabellen.txt", "at")
tabelle("======NAND=======")
print_nand()

a=bytes
b=bytes

a = False
b = False



fileWriter.close()

#AND
fileWriter = open("tabellen.txt", "at")
tabelle("======AND")

warheitswert(False, False, (a and b))
warheitswert(False, True, a and b)
warheitswert(True, False, a and b)
warheitswert(True, True, a and b)

fileWriter.close()
#OR
fileWriter = open("tabellen.txt", "at")
tabelle("======or")

warheitswert(False, False, a or b)
warheitswert(False, True, a or b)
warheitswert(True, False, a or b)
warheitswert(True, True, a or b)

fileWriter.close()
#NOT
fileWriter = open("tabellen.txt", "at")
tabelle("======NOT")

warheitswert(False, not a, not a)
warheitswert(True, not a,not a)

fileWriter.close()
#NOR
fileWriter = open("tabellen.txt", "at")
tabelle("======NOR")

warheitswert(False, False, not(a or b))
warheitswert(False, True, not(a or b))
warheitswert(True, False, not(a or b))
warheitswert(True, True, not(a or b))

fileWriter.close()

