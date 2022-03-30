#Zeynep Ülkü Kılıç
#Homework1
#Question3

import math
import sys

#Girilen sayinin basamak sayisini döndürür
def basamakSayisi(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count

#Girilen sayının asal sayı olup olmadığını kontrol eden fonksiyon
def asal(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

#Mesajı verilen değerlere göre şifreleyen fonksiyon
def encryption(phi, e, n):
    message = 3
    c = pow(message, e)
    c = math.fmod(c, n)
    return c

#Şifrelenmiş mesajı kıran fonksiyon
def decryption(c, d, n):
    m = pow(c, d)
    m = math.fmod(m, n)
    return m

p = 0
q = 0
e = 0


while (not(basamakSayisi(p) == 2 and asal(p))):
    print("p giriniz:")
    p = int(input())


while (not(basamakSayisi(q) == 2 and asal(q))) or (p == q):
    print("q giriniz:")
    q = int(input())

n = p * q
phi = (p - 1) * (q - 1)

while (basamakSayisi(e) != 2 or e >= phi):
    print("e giriniz:")
    e = int(input())

print("p:" + str(p))
print("q:" + str(q))
print("e:" + str(e))
print("phi:" + str(phi))
print("n:" + str(n))

k = 3
d = (1 + (k * phi))/e

c = encryption(phi, e, n)
mesaj = decryption(c, d, n)

print("d:" + str(d))
print("sifrelenmis olan mesaj(c): " + str(c))
print("sifresi cozulen yani asil mesaj:" + str(decryption(c, d, n)))