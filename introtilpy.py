import numpy as np
import matplotlib.pyplot as plt

#betegner punkter med små bokstav, vektorer med stor bokstav

x = int(input("Hva er x-koordinaten? "))
y = int(input("Hva er y-koordinaten? "))

a = (x,y)           #Lager punkter som "tuple" i python, kan også lage punkter på andre måter
b = (8,9)

def make_vector(a,b):

    """Funksjon som tar inn to punkter og 
        returnerer vektoren som går igjennom dem"""

    AB = []

    x = b[0] - a[0]
    y = b[1] - a[1]

    AB.append(x)
    AB.append(y)

    return AB


AB = make_vector(a,b)
print("Vektoren som går bra punktet a = ", a, " til b = ", b, "blir: ", AB)

def skalar_produkt(A,B):

    """Funksjon som tar inn to vektorer, og returnerer
        skalarproduktet mellom dem."""
     
    skalar = 0
    for i in range(0, len(A)):
        prod = A[i]*B[i]
        skalar += prod
    return skalar

DC = [6,8]

skalarprodukt = skalar_produkt(AB,DC)

print("Skalarproduktet mellom AB = ", AB, " og DC = ", DC, " blir: ", skalarprodukt)

x_verdier = np.linspace(0, 2*np.pi, 100)    #Liste over 100 punkter mellom 0 og 2pi

def f(x):

    """Funksjon som returnerer et andregrads-  
        polynom"""

    return x**2+2*x+2

plt.plot(x_verdier, f(x_verdier))   #Vi ploter funksjonen på intervallet (0,2pi)
plt.show()