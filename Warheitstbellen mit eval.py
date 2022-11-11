def warheitswert(a, b, x):
    fileWriter.write(str(a) + "|" + str(b) + "|" + str(x) + "\n")


def tabelle(name):
    fileWriter.write(name)
    fileWriter.write("\n")
    fileWriter.write("|A:  |B:   |C:  \n")
    fileWriter.write("+----+-----+----\n")

def print_body(function_name):
    a = False
    b = False
    warheitswert(a, b, eval(function_name))

    b = True
    warheitswert(a, b, eval(function_name))

    a = True
    b = False
    warheitswert(a, b, eval(function_name))

    b = True
    warheitswert(a, b, eval(function_name))


fileWriter = open("tabellen.txt", "wt")
#Funktionnen
#x=bytes



#nand
fileWriter = open("tabellen.txt", "at")
tabelle("======NAND=======")
print_body('not (a and b)')
print_body('a and b')
print_body('not (a or b)')
print_body('a or b')



fileWriter.close()
