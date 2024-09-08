import time
import webbrowser

uzivatele = []
pocet_uzivatelu = 0
je_prihlasen = False
je_admin = False

Jan = {}


uzivatele= [
    {"jmeno": "Honza","id": 25,"pujcil_si":False,"USERNAME": "Jande"},
    {"jmeno": "Petr","id": 26,"pujcil_si":False,"USERNAME": "Petrde"},
    {"jmeno": "Jana","id": 27,"pujcil_si":False,"USERNAME": "Janade"},
    {"jmeno": "Jirka","id": 28,"pujcil_si":False,"USERNAME": "Jirkade"},
    {"jmeno": "Pavel","id": 29,"pujcil_si":False,"USERNAME": "Pavelde"},
    {"jmeno": "Jitka","id": 30,"pujcil_si":False,"USERNAME": "Jitkade"},
    {"jmeno": "Jaroslav","id": 31,"pujcil_si":False,"USERNAME": "ADMIN"},

]



# print(uzivatele[2]["jmeno"])
def prihlaseni():
    aktualni_uzivatel = input("Zadej uživatelské jméno: ")

    
    for uzivatel in uzivatele:
        if uzivatel["USERNAME"] == aktualni_uzivatel:

            id_uzivatele = uzivatel["id"]
            zadane_id = input("Zadej své ID: ")
            if zadane_id == zadane_id.isalpha():
                print("ID je špatně, tak jsme u toho zase")
                time.sleep(1.5)
                webbrowser.open("https://youtu.be/dQw4w9WgXcQ?si=yrhsmnqPEc9pr5Rs")
                break
            else:
                if int(id_uzivatele) == int(zadane_id):
                    je_prihlasen = True
                    print("funguje")
                    if uzivatel["USERNAME"] == "ADMIN":
                        return True
                    else:
                        return False
                
                break
        
       

def aktualni_uzivatel():
    return aktualni_uzivatel