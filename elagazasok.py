def relacio(szam1:int,szam2:int):
    relacio=""
    if szam1>szam2:
        relacio=">"
    elif szam1<szam2:
        relacio="<"
    else:
        relacio="="
    return relacio

def kiiras():
    szam1=int(input("Kérek egy számot: "))
    szam2=int(input("Kérek egy számot: "))
    ertek=relacio(szam1,szam2)
    print(szam1,ertek,szam2)

def kor():
    szam=int(input("Kérek egy számot: "))
    kerulet=kor_kerulet(szam)
    terulet=kor_terulet(szam)
    if szam < 0:
        print("Hiba: a kör sugara nem pozitív!")
    else:
        print(f"A kör kerülete {kerulet} és a területe {terulet}.")


def kor_kerulet(szam:int):
    kerulet=2*szam*3.14
    return kerulet

def kor_terulet(szam:int):
    terulet=szam**2*3.14
    return terulet