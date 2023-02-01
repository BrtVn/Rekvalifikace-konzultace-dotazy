print("Zadávej čísla a nakonec zadej pouze ENTER pro ukončení zadavání")
pokracovat = True
seznam = []
while pokracovat:
    polozka = input("Zadej číslo: ")
    if (polozka == ""):
        pokracovat = False
    else:
        seznam.append(int(polozka))
#del seznam[:]
#seznam = [-1, -2, -3, -5, -2, -3, -1, -2, -4]
seznam_sorted = sorted(seznam)
pocet_polozek_seznamu = len(seznam_sorted)

if (pocet_polozek_seznamu % 2 > 0):
    median_index = (pocet_polozek_seznamu+1)/2
else:
    median_index = pocet_polozek_seznamu/2

median = seznam_sorted[int(median_index-1)]
#print(median)
for i in seznam:
    print(f"{i} se od mediánu odlišuje o {int(i-median)}")
