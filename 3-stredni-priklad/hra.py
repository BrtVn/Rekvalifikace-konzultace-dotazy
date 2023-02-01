from lokace import Lokace as _Lokace
class Hra:

    def __init__(self) -> None:
        
        self.dum = _Lokace("Dům",
                           "Stojíš před svým rodným domem, cítíš vůni čerstvě nasekaného dřeva, která se line z hromady vedle vstupních dveří.")
        self.les0 = _Lokace("Les",
                            "Jsi na lesní cestě, která se klikatí až za obzor, kde mizí v siluetě zapadajícího slunce. Ticho podvečerního lesa občas přeruší zpěv posledních ptáků.")
        self.rybnik = _Lokace("Rybník",
                              "Došel jsi ke břehu malého rybníka. Hladina je v bezvětří jako zrcadlo. Kousek od tebe je dřevěná plošina se stavidlem.")
        self.les1 = _Lokace("Les",
                            "Jsi na lesní cestě, která se klikatí až za obzor, kde mizí v siluetě zapadajícího slunce. Ticho podvečerního lesa občas přeruší zpěv posledních ptáků.")
        self.les2 = _Lokace("Les",
                            "Jsi na lesní cestě, která se klikatí až za obzor, kde mizí v siluetě zapadajícího slunce. Ticho podvečerního lesa občas přeruší zpěv posledních ptáků.")
        self.lesni_rozcesti = _Lokace("Lesní rozcestí",
                                      "Nacházíš se na lesním rozcestí.")
        self.hrad = _Lokace("Hrad",
                            "Stojíš před okovanou branou gotického hradu, která je zřejmě jediným vchodem do pevnosti. Klíčová dírka je pokryta pavučinami, což vzbuzuje dojem, že je budova opuštěná.")
       
        self.aktualni_lokace = self.dum
        self.dum.zapad = self.les0
        self.les0.vychod = self.dum
        self.les0.sever = self.lesni_rozcesti
        self.rybnik.zapad = self.les2
        self.les1.vychod = self.lesni_rozcesti
        self.les1.zapad = self.hrad
        self.les2.vychod = self.rybnik
        self.les2.zapad = self.lesni_rozcesti
        self.lesni_rozcesti.jih = self.les0
        self.lesni_rozcesti.zapad = self.les1
        self.lesni_rozcesti.vychod = self.les2
        self.hrad.vychod = self.les1

    def __input_pole(self, text_inputu, text_chyby):

        try:
            vstup = input(text_inputu)
        except ValueError:
            print(text_chyby)
        else:
            return vstup

    def pohyb(self):
        platne_prikazy = ["jdi na sever", "jdi na jih",
                          "jdi na západ", "jdi na východ", "konec"]
        cekej = False
        while (not cekej):
            if (not cekej):
                print(self.aktualni_lokace)
                cekej = True
            while (cekej):
                kam_jit = self.__input_pole(
                    "Zadej příkaz: ", "Chyba")
                if (len(kam_jit) >= 0):
                    ok = False
                    prikaz = ""
                    for prikaz in platne_prikazy:
                        if (prikaz == kam_jit):
                            ok = True
                            break
                        else:
                            ok = False
                    if (kam_jit == "konec"):
                        cekej = True
                        break
                    if (ok):
                        for cesta in self.aktualni_lokace.mozne_pohyby():
                            if (prikaz.find(cesta) != -1):
                                muzu_jit = True
                                break
                            else:
                                muzu_jit = False

                        if (muzu_jit):
                            if (cesta == "východ"):
                                self.aktualni_lokace = self.aktualni_lokace.vychod
                                
                            elif (cesta == "západ"):
                                self.aktualni_lokace = self.aktualni_lokace.zapad
                                
                            elif (cesta == "sever"):
                                self.aktualni_lokace = self.aktualni_lokace.sever
                                
                            elif (cesta == "jih"):
                                self.aktualni_lokace = self.aktualni_lokace.jih
                                
                        else:
                            print("Tímto směrem nelze jít.")
                        cekej = False
                    else:
                        print("Můj vstupní slovník neobsahuje tento příkaz.\n")
