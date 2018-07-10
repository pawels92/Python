a=input("Wpisz kwotę \n")
p=input("Jaka jest stopa procentowa? \n")
n=input("Na ile lat? \n")
a=float(a)
p=float(p)
n=float(n)
k=round((a*(1+(p/100))**n),2)

print("Stan konta na koniec lokaty wyniesie "+str(k))