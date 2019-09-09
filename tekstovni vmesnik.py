from model import Igralec, Igra, Preveri_simbol

ime1 = input("Vnesi ime prvega igralca: ")
ime1 = ime1.upper()
ime2 = input("Vnesi ime drugega igralca: ")
ime2 = ime2.upper()

while(True) :
    simbol1 = input("{}, izberi si simbol: ".format(ime1))
    simbol2 = input("{}, izberi si simbol: ".format(ime2))
    if Preveri_simbol(simbol1, simbol2) :
        break
    else :
        print("Beseda ni simbol! Izbirajta ponovno.")
        continue

print("Živjo, {} in {}, dobrodošla v igri TIC-TAC-TOE!".format(ime1,ime2))

igralec1 = Igralec(ime1, simbol1)
igralec2 = Igralec(ime2, simbol2)
Tic = Igra(ime1, ime2, simbol1, simbol2)

while(True) :
    Prvi, Drugi = Tic.Kdo_zacne()
    print("\nIgra se bo začela... Na skrajni desni četrtini tipkovnice so tipke s števili od 1 do 9, ki predstavljajo vajino igralno površino. Števila od 1 do 9 torej predstavljajo polja, kamor vnašata simbole.")
    print("Začne {}.".format(Prvi))

    while(True) :
        #PRVI
        if Prvi == ime1 :
            while(True) :
                i = input("Kam želiš vstaviti svoj simbol? ")
                if Tic.Preveri(int(i)) :
                    print("Na tem mestu je že simbol, izbiraj ponovno!\n")
                    continue
                else :
                    Tic.Vstavi_simbol(simbol1, i)
                    break
        else :
            while(True) :
                i = input('Kam želiš vstaviti svoj simbol? ')
                if Tic.Preveri(int(i)) :
                    print("Na tem mestu je že simbol, izberi ponovno!\n")
                    continue
                else :
                    Tic.Vstavi_simbol(simbol2, i) 
                    break
        Tic.Igralna_povrsina()

        if Tic.Preveri_zmago() : 
            Tic.Zmaga()
            break
        if Tic.Preveri_rezultat() :
            print("Nihče ni zmagal.")
            break

        #DRUGI
        if Drugi == ime1 :
            print("\nNa vrsti je {}.".format(ime1))
            while(True) : 
                i = input('Izberi polje. ')
                if Tic.Preveri(int(i)) :
                    print("Na tem mestu je že simbol, izbiraj ponovno!\n")
                    continue
                else :
                    Tic.Vstavi_simbol(simbol1, i)
                    break 
        else :
            print("\nNa vrsti je {}.".format(ime2))
            while(True) :
                i = input('Izberi polje. ')
                if Tic.Preveri(int(i)) :
                    print("Na tem mestu je že simbol, izbiraj ponovno!\n")
                    continue
                else :
                    Tic.Vstavi_simbol(simbol2, i) 
                    break
        Tic.Igralna_povrsina()
        
        if Tic.Preveri_zmago(): 
            Tic.Zmaga()
            break
        if Tic.Preveri_rezultat() :
            print("Nihče ni zmagal")
            break
        
        #zato ker prvemu ne sprinta da je na vrsti
        if Prvi == ime1 :
            print("\nNa vrsti je {}.".format(ime1)) 
        else :
            print("\nNa vrsti je {}.".format(ime2))
    

    Tic.Boljsi()
    Tic.Rezultat()
    Tic.Sprazni()
       
    odg = input("\nAli želiš nadaljevati z igro? JA/NE \n")
    if Tic.Igraj_ponovno(odg) :
        continue
    else :
        break 


print("\n{} in {}, hvala za igro. Igra je končana.".format(ime1,ime2))

