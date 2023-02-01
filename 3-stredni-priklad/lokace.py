class Lokace:
    def __init__(self, nazev_lokace, popis_lokace) -> None:
        self.__nazev_lokace = nazev_lokace
        self.__popis_lokace = popis_lokace
        self.vychod = 0
        self.zapad = 0
        self.sever = 0
        self.jih = 0


    def mozne_pohyby(self):
        kam_muzu_jit = ""
        if (self.jih != 0):
            kam_muzu_jit += "jih "
        if (self.sever != 0):
            kam_muzu_jit += "sever "
        if (self.zapad != 0):
            kam_muzu_jit += "západ "
        if (self.vychod != 0):
            kam_muzu_jit += "východ"
        return kam_muzu_jit.split()

    def __str__(self) -> str:
        return str(f"{self.__nazev_lokace}\n{self.__popis_lokace}\n\nMůžeš jít na {' '.join(self.mozne_pohyby())}\n")

