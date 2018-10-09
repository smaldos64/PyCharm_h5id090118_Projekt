# Her er der defineret en funktion med navnet addNumbers. Funktionen tager
# imod 2 parametre number1 og number2. Og funktionen returnerer en
# værdi.
def addNumbers(number1, number2):
    return (number1 + number2)

def addNumbersAndPrintResult(number1, number2):
    tal3 = addNumbers(tal1, tal2)
    print(str(tal1) + " + " + str(tal2) + " = " + str(tal3 + 2))


if __name__ == '__main__':
    tal1 = 10
    tal2 = 20
    addNumbersAndPrintResult(tal1, tal2)

    tal1 = 40
    tal2 = 60
    addNumbersAndPrintResult(tal1, tal2)
