# Rekvalifikace-konzultace-dotazy
[Vyřešeno] ## 1) https://www.itnetwork.cz/python/zaklady/resene-ulohy-k-7-lekci-pythonu
- Proč neprošel median validací?
- Včera jsem přišel na to, že můj kód na některé vstupy odpovídá stejně jako řešení od ITnetwork a na některé trochu jinak. Chyba je tedy na mé straně.

[Vyřešeno] ## 2) https://www.itnetwork.cz/python/oop/python-tutorial-referencni-a-hodnotove-tyoy-garbage-collector
- pamet.py to už se "u" vždycky rovná "v"?
- "u" a "v" jsou objekty a "u = v" stále platí, pouze se změnil parametr uvnitř "v", samotné "v" stále existuje
- "s" a "t" jsou proměnné (ikdyž taky objekty?) a tím, že se udělá "t = t.capitalize()" se vytvoří nový objekt

[Vyřešeno] # 3) https://www.itnetwork.cz/python/oop/c-sharp-net-resene-priklady-oop-programovani-reference-a-none
- Ulohy4/stredni-priklad: proč neprojde validací?

[Vyřešeno] ## 4) https://www.itnetwork.cz/python/oop/python-tutorial-vlastnosti-gettery-settery
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
- Jak využít getter k logování, případně jak správně logovat.
[Vyřešeno] ## 5) Na co se nyní soustředit?
[Vyřešeno] ## 6) Jak je to s otevíráním dalších cvičení? Django, SOLID, ..
