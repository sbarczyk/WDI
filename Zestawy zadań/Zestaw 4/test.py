import math

def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Nie można dzielić przez zero!")

def potegowanie(x, y):
    return x ** y

def pierwiastek_kwadratowy(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        raise ValueError("Nie można obliczyć pierwiastka kwadratowego z liczby ujemnej.")

def kalkulator():
    while True:
        print("Wybierz operację:")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Potęgowanie")
        print("6. Pierwiastek kwadratowy")
        print("7. Wyjście")

        wybor = input("Podaj numer operacji (1/2/3/4/5/6/7): ")

        if wybor == '7':
            print("Do widzenia!")
            break

        if wybor in ('1', '2', '3', '4', '5', '6'):
            try:
                liczba1 = float(input("Podaj pierwszą liczbę: "))

                if wybor != '6':
                    liczba2 = float(input("Podaj drugą liczbę: "))

                if wybor == '1':
                    wynik = dodawanie(liczba1, liczba2)
                elif wybor == '2':
                    wynik = odejmowanie(liczba1, liczba2)
                elif wybor == '3':
                    wynik = mnozenie(liczba1, liczba2)
                elif wybor == '4':
                    wynik = dzielenie(liczba1, liczba2)
                elif wybor == '5':
                    wynik = potegowanie(liczba1, liczba2)
                elif wybor == '6':
                    wynik = pierwiastek_kwadratowy(liczba1)

                print("Wynik: {}".format(wynik))

            except ValueError as e:
                print("Błąd: {}".format(e))
        else:
            print("Nieprawidłowy wybór operacji.")

if __name__ == "__main__":
    kalkulator()
