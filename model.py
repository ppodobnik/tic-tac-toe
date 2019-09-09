import random

class Igralec :
    def __init__(self, ime, simbol) :
        self.ime = ime
        self.simbol = simbol
            
def Preveri_simbol(simbol1, simbol2) :
    if len(simbol1) == 1 and len(simbol2) == 1 :
        return True
    else :
        return False

class Igra : 
    def __init__(self, name1, name2, simbol1, simbol2) :
        self.name1 = name1
        self.name2 = name2
        self.simbol1 = simbol1
        self.simbol2 = simbol2
        self.score1 = 0 
        self.score2 = 0
        self.stevec = 0
        self.TTT = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] #10 jih je
        

    def Kdo_zacne(self) : 
        if random.randint(0,1) == 0 :
            return self.name1, self.name2
        else :
            return self.name2, self.name1

    def Vstavi_simbol(self, simbol, indeks) : 
        self.simbol = simbol
        self.indeks = int(indeks)
        self.stevec += 1
        self.TTT[self.indeks] = simbol
    
    
    def Preveri_zmago(self) :
        #check row
        for k in range(1, 8, 3) :
            if (self.TTT[k] == self.TTT[k+1] == self.TTT[k+2] == self.simbol1) :
                self.score1 += 1
                self.stevec = 0
                return True
            if (self.TTT[k] == self.TTT[k+1] == self.TTT[k+2] == self.simbol2) :
                self.score2 += 1
                self.stevec = 0
                return True

        #check col
        for l in range(1, 4) :
            if (self.TTT[l] == self.TTT[l+3] == self.TTT[l+6] == self.simbol1) :
                self.score1 += 1
                self.stevec = 0
                return True
            if (self.TTT[l] == self.TTT[l+3] == self.TTT[l+6] == self.simbol2) :
                self.score2 += 1
                self.stevec = 0
                return True
        
        #check diag
        d = 1
        if (self.TTT[d] == self.TTT[d+4] == self.TTT[d+8] == self.simbol1) or (self.TTT[d+2] == self.TTT[d+4] == self.TTT[d+6] == self.simbol1) :
            self.score1 += 1
            self.stevec = 0
            return True
        if (self.TTT[d] == self.TTT[d+4] == self.TTT[d+8] == self.simbol2) or (self.TTT[d+2] == self.TTT[d+4] == self.TTT[d+6] == self.simbol2) :
            self.score2 += 1
            self.stevec = 0
            return True

    def Preveri(self, x) :
        self.x = x
        if self.TTT[self.x] != ' ' and self.x <= 9:
            return True
        else :
            return False


    def Preveri_rezultat(self) :
        if self.stevec == 9 :
            return True
        else :
            return False


    def Igralna_povrsina(self) : 
        print('---------------\n',
        '| ' + str(self.TTT[7]) + ' | ' + str(self.TTT[8]) + ' | ' + str(self.TTT[9]) + ' | \n',
        '--------------\n',
        '| ' + str(self.TTT[4]) + ' | ' + str(self.TTT[5]) + ' | ' + str(self.TTT[6]) + ' | \n',
            '--------------\n',
        '| ' + str(self.TTT[1]) + ' | ' + str(self.TTT[2]) + ' | ' + str(self.TTT[3]) + ' | \n',
        '--------------')

    def Boljsi(self) :
        if self.score1 == self.score2 :
            return print("Rezultat je izenačen.")
        if self.score1 > self.score2 :
            return print("{} vodi".format(self.name1), end=" ")
        else:
            return print("{} vodi".format(self.name2), end=" ")


    def Rezultat(self) :
        return print(" {} : {}".format(str(self.score1),str(self.score2)))  


    def Ponovi(self) :
        for i in range(10) :
            self.TTT[i] = ' '


    def Zmaga(self) :
        #check rows
        for k in range(1, 8, 3) :
            if (self.TTT[k] == self.TTT[k+1] == self.TTT[k+2] == self.simbol1) :
                return print("{} je zmagal/a. HURA HURA HURA".format(self.name1))
            if (self.TTT[k] == self.TTT[k+1] == self.TTT[k+2] == self.simbol2) :
                return print("{} je zmagal/a. HURA HURA HURA".format(self.name2))

        #check cols
        for l in range(1, 4, 1) :
            if (self.TTT[l] == self.TTT[l+3] == self.TTT[l+6] == self.simbol1) :
                return print("{} je zmagal/a. HURA HURA HURA".format(self.name1))
            if (self.TTT[l] == self.TTT[l+3] == self.TTT[l+6] == self.simbol2) :
                return print("{} je zmagal/a. HURA HURA HURA".format(self.name2))

        #check diag
        d = 1
        if (self.TTT[d] == self.TTT[d+4] == self.TTT[d+8] == self.simbol1) :
            return print("{} je zmagal/a. HURA HURA HURA".format(self.name1))
        if (self.TTT[d+2] == self.TTT[d+4] == self.TTT[d+6] == self.simbol1) :
            return print("{} je zmagal/a. HURA HURA HURA".format(self.name1))
        if (self.TTT[d] == self.TTT[d+4] == self.TTT[d+8] == self.simbol2) :
            return print("{} je zmagal/a. HURA HURA HURA".format(self.name2))
        if (self.TTT[d+2] == self.TTT[d+4] == self.TTT[d+6] == self.simbol2) :
            return print("{} je zmagal/a. HURA HURA HURA".format(self.name2)) 

    def Igraj_ponovno(self, odgovor) :
        self.odgovor = odgovor
        if odgovor in ['JA', 'ja', 'Ja']:
            return True
        else:
            return False


