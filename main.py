import math

print("Witaj w kalkulatorze !!")
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Wybierz rodzaj działani: 1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie, 5 - potęgowanie,\
 6 - pierwiastkowanie: "))
if (b==6):
    wynik = math.sqrt(a)
    print(" Pierwiastek z ",a, "to", wynik)
elif (b > 6):
    print("Muisz wybrać liczby od 1 do 6!")
else:
    c = int(input("Podaj drugą liczbę: "))

    if (b == 1):
        wynik = a + c
    elif (b == 2):
        wynik = a - c
    elif (b == 3):
        wynik = a * c
    elif (b == 4):
         wynik = a / c
    elif (b == 5):
        wynik = a ** c
    else:
        print("Dokonałeś złego wyobru!")

    print("Wynik działania to: ", wynik)