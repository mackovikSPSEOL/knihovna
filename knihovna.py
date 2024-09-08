#vytvořit slovnik s knihami


import uzivatel


kniha1 = {}
kniha2 = {}
kniha3 = {}

knihy = [kniha1, kniha2, kniha3]
pocet_knih = 0

uzivatel.prihlaseni()




kniha1
{
    "nazev": "Jak mi spadl chléb",
    "autor": "Jan Rohlík",
    "ISBN": "15s89dd85g9r26",
    "dostupny": True 
}

kniha2  
{
    "nazev": "Učení s panem Soukupem",
    "autor": "Jaromír Soukup",
    "ISBN": "15s89dd85g9r26",
    "dostupny": True 
}

kniha3
{
    "nazev": "Dinokitty",
    "autor": "Marek preichert",
    "ISBN": "15s89dd85gs6556",
    "dostupny": True 
}


for kniha in knihy:
    pocet_knih = pocet_knih + 1 

# print(pocet_knih)
# x= pocet_knih 
# print("kniha" + str(x)) (FUNGUJE, lze zjistit kolik je knih a podle toho přidat knihu číslo ---)
    

