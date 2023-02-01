# Rekvalifikace-konzultace-dotazy
## 1) https://www.itnetwork.cz/python/zaklady/resene-ulohy-k-7-lekci-pythonu
- proč neprošel median validací?
- Výstup ukázkového řešení odpovídá výstupu mého řešení. Tak ne tak docela..

## 2) https://www.itnetwork.cz/python/oop/python-tutorial-referencni-a-hodnotove-tyoy-garbage-collector
- pamet.py to už se "u" vždycky rovná "v"? Je to potřeba více vysvětlit.
- "u" a "v" jsou objekty a "u = v" stále platí, pouze se změnil parametr uvnitř "v", samotné "v" stále existuje
- "s" a "t" jsou proměnné (ikdyž taky objekty?) a tím, že se udělá "t = t.capitalize()" se vytvoří nový objekt

## 3) https://www.itnetwork.cz/python/oop/c-sharp-net-resene-priklady-oop-programovani-reference-a-none
- Ulohy4/stredni-priklad: proč neprojde validací?

## 4) https://www.itnetwork.cz/python/oop/python-tutorial-vlastnosti-gettery-settery
- Jaký je rozdím mezi tímto:
  ```
    @property # Vytvoří vlastnost, takže by to mělo být definováno před setterem a getterem?
    def nazev_vlastnosti(self):
        return soukromy_atribut_vlastnosti  
  ```
  a tímto:
  ```
    @nazev_vlastnosti.getter
    def nazev_vlastnosti(self):
        return soukromy_atribut_vlastnosti  
  ```
## 5) Na co se nyní soustředit?
## 6) Jak je to s otevíráním dalších cvičení? Django, SOLID, ..
