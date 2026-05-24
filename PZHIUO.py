from abc import ABC
from datetime import datetime


#Absztakt osztály

class Auto(ABC):

    def __init__(self, rendszam, tipus, berleti_dij):
        self.__rendszam = rendszam
        self.__tipus = tipus
        self.__berleti_dij = berleti_dij

    def get_rendszam(self):
        return self.__rendszam

    def get_tipus(self):
        return self.__tipus

    def get_berleti_dij(self):
        return self.__berleti_dij

    def __str__(self):
        return f"{self.__tipus} - {self.__rendszam} - {self.__berleti_dij} Ft/nap"


#Személyautó

class Szemelyauto(Auto):

    def __init__(self, rendszam, tipus, berleti_dij, ferohely):
        super().__init__(rendszam, tipus, berleti_dij)
        self.__ferohely = ferohely

    def get_ferohely(self):
        return self.__ferohely

    def __str__(self):
        return f"Személyautó: {super().__str__()} - Férőhely: {self.__ferohely}"


#Teherautó

class Teherauto(Auto):

    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        self.__teherbiras = teherbiras

    def get_teherbiras(self):
        return self.__teherbiras

    def __str__(self):
        return f"Teherautó: {super().__str__()} - Teherbírás: {self.__teherbiras} kg"


#Bérlés

class Berles:

    def __init__(self, auto, datum):
        self.__auto = auto
        self.__datum = datum

    def get_auto(self):
        return self.__auto

    def get_datum(self):
        return self.__datum

    def __str__(self):
        return f"{self.__auto.get_rendszam()} - {self.__datum}"


#Autókölcsönző

class Autokolcsonzo:

    def __init__(self, nev):
        self.__nev = nev
        self.__autok = []
        self.__berlesek = []

    def auto_hozzaadas(self, auto):
        self.__autok.append(auto)

    def berles_hozzaadas(self, berles):
        self.__berlesek.append(berles)

    def autok_listazasa(self):

        print("\n--- Autók ---")

        for auto in self.__autok:
            print(auto)

    def berlesek_listazasa(self):

        print("\n--- Aktuális bérlések ---")

        if len(self.__berlesek) == 0:
            print("Nincs aktív bérlés.")
            return

        for berles in self.__berlesek:
            print(berles)

    def auto_berles(self, rendszam, datum):

        #Dátum ellenőrzése
        try:
            datum_obj = datetime.strptime(datum, "%Y-%m-%d")

            if datum_obj.date() < datetime.now().date():
                raise ValueError("Múltbeli dátum nem adható meg!")

        except ValueError as hiba:
            print(f"Hibás dátum: {hiba}")
            return

        #Autó keresése
        auto = None

        for a in self.__autok:
            if a.get_rendszam() == rendszam:
                auto = a
                break

        if auto is None:
            print("Nincs ilyen rendszámú autó!")
            return

        #Fogalalt-e
        for berles in self.__berlesek:

            if (berles.get_auto().get_rendszam() == rendszam and
                    berles.get_datum() == datum):

                print("Az autó már foglalt erre a napra!")
                return

        #Új bérlés
        uj_berles = Berles(auto, datum)
        self.__berlesek.append(uj_berles)

        print("\nSikeres bérlés!")
        print(f"Fizetendő összeg: {auto.get_berleti_dij()} Ft")

    def berles_lemondas(self, rendszam, datum):

        for berles in self.__berlesek:

            if (berles.get_auto().get_rendszam() == rendszam and
                    berles.get_datum() == datum):

                self.__berlesek.remove(berles)

                print("Bérlés sikeresen lemondva.")
                return

        print("Nincs ilyen bérlés!")


#Alap adatok

kolcsonzo = Autokolcsonzo("SpeedCar")

auto1 = Szemelyauto("ABC-123", "Toyota Corolla", 12000, 5)
auto2 = Szemelyauto("DEF-456", "Honda Civic", 14000, 5)
auto3 = Teherauto("GHI-789", "Ford Transit", 20000, 1500)

kolcsonzo.auto_hozzaadas(auto1)
kolcsonzo.auto_hozzaadas(auto2)
kolcsonzo.auto_hozzaadas(auto3)

# Alap bérlések
kolcsonzo.berles_hozzaadas(Berles(auto1, "2026-05-25"))
kolcsonzo.berles_hozzaadas(Berles(auto2, "2026-05-26"))
kolcsonzo.berles_hozzaadas(Berles(auto3, "2026-05-27"))
kolcsonzo.berles_hozzaadas(Berles(auto1, "2026-05-28"))


#Menüpont

while True:

    print("\n---- Autókölcsönző rendszer ----")
    print("1 - Autók listázása")
    print("2 - Autó bérlése")
    print("3 - Bérlés lemondása")
    print("4 - Bérlések listázása")
    print("0 - Kilépés")

    valasztas = input("Válassz egy menüpontot: ")

    if valasztas == "1":

        kolcsonzo.autok_listazasa()

    elif valasztas == "2":

        rendszam = input("Add meg a rendszámot: ")
        datum = input("Add meg a dátumot (ÉÉÉÉ-HH-NN): ")

        kolcsonzo.auto_berles(rendszam, datum)

    elif valasztas == "3":

        rendszam = input("Add meg a rendszámot: ")
        datum = input("Add meg a dátumot (ÉÉÉÉ-HH-NN): ")

        kolcsonzo.berles_lemondas(rendszam, datum)

    elif valasztas == "4":

        kolcsonzo.berlesek_listazasa()

    elif valasztas == "0":

        print("Kilépés...")
        break

    else:

        print("Érvénytelen menüpont!")