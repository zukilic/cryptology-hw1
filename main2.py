#Zeynep Ülkü Kılıç
#Homework1
#Question2

'''
Ben bu program için 5 basamaklı iki adet asal sayı tercih ettim. 9 basamaklı sayılar
denediğimde program sonuçlanmıyordu.
Programı çalıştırdığımda çarpma işleminin ne kadar kolay,
aksine bir sayıyı asal çarpanlarına ayırmanın ise oldukca zahmetli bir iş
olduğunu öğredim.
Bir denememde asal çarpanlara ayırırken ki geçen süre 84.47 saniye olmuştur.
Çarpma işlemi için gerekli süre ise her zaman 0 saniye çıkmaktadır.
'''

from time import time

def multiplication(num1, num2):
    time1 = time()
    product = (num1 * num2)
    time2 = time()

    elapsedTime = time2 - time1
    print("carpma islemi icin harcanan zaman", elapsedTime)

    return product

def primeFactorization(number):
    time1 = time()
    for i in range(1, number):
        if number % i == 0:
            prime1 = i
            prime2 = number//i
    time2 = time()

    elapsedTime = time2 - time1
    print("asal carpanlari bulmak icin harcanan zaman", elapsedTime)

    return prime1, prime2

num1 = 28051
num2 = 21773
product = multiplication(num1, num2)
prime1, prime2 = primeFactorization(product)

print("Carpim icin kullanilan asal sayilar: " + str(num1) + " " + str(num2))
print("Bulunan asal sayilar: " + str(prime1) + " " + str(prime2))