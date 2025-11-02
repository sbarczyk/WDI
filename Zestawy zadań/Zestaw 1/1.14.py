def calculate_factorial(num):
    factorial = 1
    for i in range (1, num+1):
        factorial *= i
    return factorial

def cos_Maclaurin(x, n):
    result = 0
    for i in range(n):
        pom = ((-1) ** i) * (x ** (2 * i)) / calculate_factorial(2 * i)
        result += pom
    return result

x = float(input("Wprowadź wartość x (w radianach): "))
n = int(input("Podaj liczbę wyrazów szeregu do uwzględnienia (dokładność obliczeń): "))

print(cos_Maclaurin(x, n))