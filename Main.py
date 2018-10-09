import Math

# Her er der defineret en funktion med navnet addNumbers. Funktionen tager
# imod 2 parametre number1 og number2. Og funktionen returnerer en
# værdi.
def addNumbers(number1, number2):
    return (number1 + number2)

def addNumbersAndPrintResult(number1, number2):
    tal3 = addNumbers(tal1, tal2)
    print(str(tal1) + " + " + str(tal2) + " = " + str(tal3))

def getRemainder(number1, number2):
    return(number1 % number2)


if __name__ == '__main__':
    tal1 = 10
    tal2 = 20
    addNumbersAndPrintResult(tal1, tal2)

    tal1 = 40
    tal2 = 60
    addNumbersAndPrintResult(tal1, tal2)

    print(getRemainder(9,4))

    # I syntaksen herunder er Math navnet på vores python fil: Math.py
    # og Math_Class er navnet på vores klasse inden i filen Math.py
    lommeregner = Math.Math_Class()
    # lommeregner er nu et objekt af vores klasse Math_Class


    # Da subtractNumbers er defineret ovre i vores Math_Class som en metode,
    # der skal virke på et objekt af vores Math_Class, kan vi bruge
    # subtractNumbers på vores objekt lommeregner.
    # Herunder kalder vi vi metoden subtractNumbers.
    tal3 = lommeregner.subtractNumbers(34, 12)
    print(tal3)

    # Da subtractNumbersClass er defineret ovre i vores Math_Class som en metode,
    # der skal virke på selve vores Math_Class, skal vi bruge selve klassen her
    # og ikke et objekt af vorers klasse.
    # Herunder kalder vi vi metoden subtractNumbers.
    tal4 = Math.Math_Class.subtractNumbersClass(47, 11)
    print(tal4)

    tal5 = lommeregner.multiplyNumbers(10, 100)
    print(tal5)
