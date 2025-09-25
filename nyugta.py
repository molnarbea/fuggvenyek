def fejlec(kar:str="*"):
    print(f"{kar*24}\n{kar}{"NYUGTA":^22}{kar}\n{kar*24}")

def nyugta(egyenlo:str="=",vonal:str="_"):

    tetel1=input("Kérek egy tételt: ")
    ar1=int(input("Mennyibe került: "))
    tetel2=input("Kérek egy másik tételt: ")
    ar2=int(input("Mennyibe került: "))
    tetel3=input("Kérek egy harmadik tételt: ")
    ar3=int(input("Mennyibe került: "))
    osszesen=ar1+ar2+ar3
    szervizdij=osszesen/10

    fejlec()
    print(f"{tetel1}{ar1:>{21-len(tetel1)}} Ft")
    print(f"{tetel2}{ar2:>{21-len(tetel2)}} Ft")
    print(f"{tetel3}{ar3:>{21-len(tetel3)}} Ft")
    print(f"{egyenlo*24}")
    print(f"Összesen:{osszesen:>{21-len("Összesen:")}} Ft")
    print(f"Szervizdíj:{szervizdij:>{21-len("Szervízdíj:")}} Ft")
    print(f"{egyenlo*24}")
    print(f"Fizetendő:{osszesen+szervizdij:>{21-len("Fizetendő:")}} Ft")
    print(f"{vonal*9}{vonal*9:>{24-len(vonal*9)}}")
    print(f"{"Dátum":>7}{"Név":>14}")
    lablec()
    

def lablec(kar:str="*"):
    print(f"{kar*24}\n{kar}{"CÉG":^22}{kar}\n{kar*24}")