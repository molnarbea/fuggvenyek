hossz=24

def disz_sor(kar:str="*"):
    print(f"{kar*hossz}")

def nyugta(egyenlo:str="=",vonal:str="_"):

    tetel1=tetel()
    ar1=ar()
    tetel2=tetel()
    ar2=ar()
    tetel3=tetel()
    ar3=ar()
    disz_sor("*")
    szoveg("NYUGTA")
    disz_sor("*")
    er=osszeg(ar1,ar2,ar3)
    szer=er/10
    fiz=er+szer
    kiiras(tetel1,ar1)
    kiiras(tetel2,ar2)
    kiiras(tetel3,ar3)
    disz_sor("=")
    kiiras("Összesen",er)
    kiiras("Szervízdíj",szer)
    disz_sor("=")
    kiiras("Fizetendő",fiz)
    alairas("_")
    disz_sor("*")
    szoveg("CÉG")
    disz_sor("*")

def szoveg(felirat:str):
    print(f"*{felirat:^{hossz-2}}*")

def tetel():
    tetel=input("Kérek egy tételt: ")
    return tetel

def ar():
    ar=int(input("Mennyibe került: "))
    return ar

def osszeg(ar1:int,ar2:int,ar3:int):
    eredmeny=ar1+ar2+ar3
    return eredmeny

def kiiras(tetel, ar):
    print(f"{tetel}{ar:>{21-len(tetel)}} Ft")

def alairas(kar:str="_"):
    print(f"{kar*9}{kar*9:>{24-len(kar*9)}}")
    print(f"{"Dátum":>7}{"Név":>14}")
    