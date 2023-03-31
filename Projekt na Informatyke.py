from random import randint


print('-'*64)
print("\t\t\tSymulator sklepu")
print('-'*64)

Imie = input("Wpisz imie i nazwisko swojej postaci: ")
Saldo = 1000

def Sprzedarz():
    global Saldo
    CIphone = randint(300, 1000)
    CTablteu = randint(1000, 3000)
    CKompa = randint(5000, 10000)
    IIphone = 0
    ITabletu = 0
    IKompa = 0
        
    while Saldo < 100000:
        print('-'*64)


        Menu = (input(f'''Rzeczy które możesz zrobić:

1. Kup Elekronike
2. Sprzedawaj Elektronike
3. Zacznij nowy dzień 

Twoje saldo jest równe {Saldo} $

Oraz posiadasz: 
Iphone - {IIphone}
Tablet - {ITabletu}
Komputer - {IKompa}

Wybierz liczbe: '''))
        print('-'*64)

        if Menu == "1":
            Wybór1 = (input(f'''Przedmioty które możesz kupić (Aby wyjść wpisz 0):
            
1. Iphone - {CIphone} $
2. Tablet - {CTablteu} $
3. Komputer - {CKompa} $

Wybierz liczbe: '''))
            print('-'*64)
            if Wybór1 == "1":
                Ilość = int(input(f"Wpisz ile chcesz kupić Iphonów, ich koszt to {CIphone} $ (Aby wyjść wpisz 0): "))
                print('-'*64)
                
                if Ilość == 0:
                    input("Kliknij przycisk aby wrócić do menu: ")
                elif CIphone*Ilość <= Saldo:
                    IIphone += Ilość
                    Saldo -= CIphone*Ilość
                    print(f"Udało ci sie kupić {Ilość} Iphonów, Obecnie posiadasz {IIphone} Iphonów")
                else:
                    input("Nie posiadasz wystarczająco $, Kliknij przycisk aby wrócić do menu: ")
            elif Wybór1 == "2":
                Ilość = int(input(f"Wpisz ile chcesz kupić Tabletówich koszt to {CTablteu} $ (Aby wyjść wpisz 0): "))
                print('-'*64)
                
                if Ilość == 0:
                    input("Kliknij przycisk aby wrócić do menu: ")
                elif CTablteu*Ilość <= Saldo:
                    ITabletu += Ilość
                    Saldo -= CTablteu*Ilość
                    print(f"Udało ci sie kupić {Ilość} tabletów, Obecnie posiadasz {ITabletu} tabletów")
                    
                else:
                    input("Nie posiadasz wystarczająco $, Kliknij przycisk aby wrócić do menu: ")
            elif Wybór1 == "3":
                Ilość = int(input(f"Wpisz ile chcesz kupić Komputerow, ich koszt to {CKompa} $ (Aby wyjść wpisz 0): "))
                print('-'*64)
                
                if Ilość == 0:
                    input("Kliknij przycisk aby wrócić do menu: ")
                elif CKompa*Ilość <= Saldo:
                    IKompa += Ilość
                    Saldo -= CKompa*Ilość
                    print(f"Udało ci sie kupić {Ilość} Kompuerów, Obecnie posiadasz {IKompa} Komputerów")
                    
                else:
                    input("Nie posiadasz wystarczająco $, Kliknij przycisk aby wrócićdo menu")
            elif Wybór1 == "0":
                    input("Kliknij przycisk aby wrócić do menu: ")
            else:
                input("Wpisana liczba jest nieprawidłowa, kilkinik przycisk aby wórcić do menu ")  
                
        elif Menu == "2":
            Wybór1 = (input(f'''Przedmioty które możesz sprzedać (Aby wyjść wpisz 0):
            
1. Iphone - {IIphone} - Cena {CIphone} $ 
2. Tablet - {ITabletu} - Cena {CTablteu} $
3. Komputer - {IKompa} - Cena {CKompa} $

Wybierz liczbe: '''))
            print('-'*64)   
            if Wybór1 == "1":
                Ilość = int(input(f"Wpisz ile chcesz sprzedać Iphonów, ich Cena to {CIphone} (Aktualnie posiadasz {IIphone} Iphonów, Aby wyjść wpisz 0): "))
                print('-'*64)

                if Ilość <= IIphone and Ilość > 0:
                    Cena = Ilość*CIphone
                    Saldo += Cena
                    IIphone -= Ilość
                    print(f"Udało ci sie Sprzedać {Ilość} Iphonów przez co zarobiłeś {Cena} $")
                    
                elif Ilość == 0:
                    input("Kliknij przycisk aby wrócić do menu: ")
                else:
                    input("Wpisana liczba jest nieprawidłowa, kilkinik przycisk aby wórcić do menu ")  
                    print('-'*64)
            elif Wybór1 == "2":
                Ilość = int(input(f"Wpisz ile chcesz sprzedać abletów, ich Cena to {CTablteu} (Aktualnie posiadasz {ITabletu} Tabletów, Aby wyjść wpisz 0): "))
                print('-'*64)

                if Ilość <= ITabletu and Ilość > 0:
                    Cena = Ilość*CTablteu
                    Saldo += Cena
                    ITabletu -= Ilość
                    print(f"Udało ci sie Sprzedać {ITabletu} Tabletów przez co zarobiłeś {Cena} $")
                    
                elif Ilość == 0:
                    input("Kliknij przycisk aby wrócić do menu: ")
                else:
                    input("Wpisana liczba jest nieprawidłowa, kilkinik przycisk aby wórcić do menu ")  
                    print('-'*64)
            elif Wybór1 == "3":
                Ilość = int(input(f"Wpisz ile chcesz sprzedać Komputerów, ich Cena to {CKompa} (Aktualnie posiadasz {IKompa} Komputerów, Aby wyjść wpisz 0): "))
                print('-'*64)

                if Ilość <= IKompa and Ilość > 0:
                    Cena = Ilość*CKompa
                    Saldo += Cena
                    IKompa -= Ilość
                    print(f"Udało ci sie Sprzedać {IKompa} komputerów przez co zarobiłeś {Cena} $")
                    
                elif Ilość == 0:
                    input("Kliknij przycisk aby wrócić do menu: ")
                else:
                    input("Wpisana liczba jest nieprawidłowa, kilkinik przycisk aby wórcić do menu ")  
                    print('-'*64)
            elif Wybór1 == "0":
                input("Kliknij przycisk aby wrócić do menu: ")
            else:
                input("Wpisana liczba jest nieprawidłowa, kilkinik przycisk aby wórcić do menu ")  
                    
        elif Menu == "3":
            print("Udało ci się Zacząć nowy dzień, cena Elektroniki się zmieniła oraz dostałeś dniówke 500$")
            CIphone = randint(300, 1000)
            CTablteu = randint(1000, 3000)
            CKompa = randint(5000, 10000)
            Saldo += 500
            
        else: 
            print("Wpisana liczba jest nieprawidłowa")
            
                

             
print('-'*64)

print(f"{Imie} witaj twoim zadaniem bedzie uzbieranie 100000 $")
Sprzedarz()
print('-'*64)
print("\t\t\tGratulacje przeszedłeś gre")
print('-'*64)


https://1drv.ms/p/s!AihusNxsNXXjfwWqAaK2P6RGcZ8?e=AZLUGl