
class Math_Class():
    # Metoden herunder virker på et objekt af klassen Math_Class. Dette
    # kan vi se ved at den har parameteren self med i parameter listen
    def subtractNumbers(self, number1, number2):
        return (number1 - number2)

    # Metoden herunder virker på selve klassen Math_Class. Dette
    # kan vi se ved at den ikke har parameteren self med i parameter listen
    def subtractNumbersClass(number1, number2):
        return (number1 - number2)

    def multiplyNumbers(self, number1, number2):
        return (number1 * number2)



