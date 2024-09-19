
pocet_knih = 0


knihy = [
    {"nazev": "Kde mají nejlepší kebab?", "autor": " Patrik Vypáčil", "ISBN": "1234567890", "dostupny": True},
    {'nazev': 'Proč se jmenuji dinousauří koťátko?', 'autor': 'Marek Ejchyrt', 'ISBN': '0987654321', 'dostupny': False},
    {'nazev': 'Fortnite mýma očima', 'autor': 'Lucie Potřísalová', 'ISBN': '1122334455', 'dostupny': True},
    {'nazev': 'Fortnite mýma očima 2', 'autor': 'Lucie Potřísalová', 'ISBN': '1235463455', 'dostupny': True}
]
for kniha in knihy:
    pocet_knih = pocet_knih + 1 

# print(pocet_knih)
# x= pocet_knih 
# print("kniha" + str(x)) 
# FUNGUJE, lze zjistit kolik je knih a podle toho přidat knihu číslo ---)

def o_knize():
    vybrana_moznost = input("Chcete hledat podle názvu nebo podle autora? (nazev, autor): ")
    if vybrana_moznost == "nazev":
        hledany_nazev = input("Zadejte název knihy: ")
        for kniha in knihy:
            if kniha["nazev"] == hledany_nazev:
                print("Kniha nalezena")
                print("◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘")
                print("Název: " + kniha["nazev"])

                print("ISBN: " + kniha["ISBN"])
                if kniha["dostupny"] == True:
                    print("Kniha je dostupná")
                else:
                    print("Kniha není dostupná")
                break
        else:
            print("Kniha nenalezena")
    elif vybrana_moznost == "autor":
        hledany_autor = input("Zadejte autora knihy: ")
        for kniha in knihy:
            if kniha["autor"] == hledany_autor:
                print("Kniha nalezena")
                print("◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘")
                print("Název: " + kniha["nazev"])

                print("ISBN: " + kniha["ISBN"])
                if kniha["dostupny"] == True:
                    print("Kniha je dostupná")
                else:
                    print("Kniha není dostupná")
                continue
            
        else:
            print("Konec seznamu knih")

o_knize()