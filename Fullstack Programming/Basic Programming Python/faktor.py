# Program Faktor
def faktor(angka):
    faktor_angka = []
    for i in range(1, 101):
        if angka % i == 0:
            faktor_angka.append(i)

    return faktor_angka


# Program Faktorial
def faktorial(angka):
    faktorial_angka = 1
    for i in range(1, angka+1):
        faktorial_angka *= i

    return faktorial_angka


faktor_10 = faktor(10)
faktorial_5 = faktorial(5)
print(faktor_10)
print(faktorial_5)
