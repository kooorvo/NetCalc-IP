from tkinter import *

#%% Modèle
def dec_to_bits(dec):
    assert 0 <= dec <= 255
    bits = [0]*8
    i = 7
    while dec > 0:
        bits[i] = dec % 2
        dec //= 2
        i -= 1
    return bits


def bits_to_dec(bits):
    dec = 0
    for i in range(8):
        dec += bits[7 - i] * (2 ** i)
    return dec


def ip_to_bits(ip):
    bits = []
    for p in ip.split("."):
        bits += dec_to_bits(int(p))
    return bits


def bits_to_ip(ip_bits):
    return ".".join(str(bits_to_dec(ip_bits[i*8:(i+1)*8])) for i in range(4))


def verifier_ip(ip):
    try:
        p = ip.split(".")
        return len(p) == 4 and all(0 <= int(x) <= 255 for x in p)
    except:
        return False


def prefixe_reseau(ip_bits, mask):
    return [ip_bits[i] if i < mask else 0 for i in range(32)]


def calcul_ip():
    ip = adresse_ip.get()
    if not verifier_ip(ip):
        message_erreur.set("Adresse non conforme")
        return

    message_erreur.set("")
    ip_bits = ip_to_bits(ip)
    reseau = prefixe_reseau(ip_bits, masque.get())
    adresse_reseau.set("Adresse réseau : " + bits_to_ip(reseau))

    premiere = reseau.copy()
    premiere[31] = 1
    premiere_adresse.set("Première adresse : " + bits_to_ip(premiere))

    broadcast = reseau.copy()
    for i in range(masque.get(), 32):
        broadcast[i] = 1
    adresse_broadcast.set("Adresse broadcast : " + bits_to_ip(broadcast))

    derniere = broadcast.copy()
    derniere[31] = 0
    derniere_adresse.set("Dernière adresse : " + bits_to_ip(derniere))

    nombre_adresses_ip.set(
        "Nombre d'adresses IP : " + str(2 ** (32 - masque.get()) - 2)
    )


#%% Interface graphique
fen = Tk()
fen.title("Calculateur d'adresses IP")
fen.geometry("640x420")

# --- Thèmes modernes ---
theme_sombre = False

THEME_CLAIR = {
    "bg": "#f5f6fa",
    "card": "#ffffff",
    "fg": "#2f3640",
    "entry": "#ffffff",
    "accent": "#40739e"
}

THEME_SOMBRE = {
    "bg": "#1e272e",
    "card": "#2f3640",
    "fg": "#f5f6fa",
    "entry": "#353b48",
    "accent": "#4cd137"
}

def appliquer_theme():
    theme = THEME_SOMBRE if theme_sombre else THEME_CLAIR
    fen.configure(bg=theme["bg"])

    for w in fen.winfo_children():
        try:
            w.configure(bg=theme["card"])
        except:
            pass
        for c in w.winfo_children():
            try:
                c.configure(
                    bg=theme["card"],
                    fg=theme["fg"]
                )
            except:
                pass
            if isinstance(c, Entry):
                c.configure(
                    bg=theme["entry"],
                    fg=theme["fg"],
                    insertbackground=theme["fg"]
                )
            if isinstance(c, Button):
                c.configure(
                    bg=theme["accent"],
                    fg="white",
                    activebackground=theme["accent"],
                    relief=FLAT
                )


def toggle_theme():
    global theme_sombre
    theme_sombre = not theme_sombre
    appliquer_theme()


# Bouton thème
Button(
    fen,
    text="clair / sombre",
    command=toggle_theme,
    font=("Arial", 11),
    relief=FLAT
).pack(anchor="ne", padx=10, pady=8)

# Variables
adresse_ip = StringVar()
premiere_adresse = StringVar(value="Première adresse : ")
adresse_reseau = StringVar(value="Adresse réseau : ")
derniere_adresse = StringVar(value="Dernière adresse : ")
adresse_broadcast = StringVar(value="Adresse broadcast : ")
nombre_adresses_ip = StringVar(value="Nombre d'adresses IP : ")
message_erreur = StringVar()
masque = IntVar(value=24)

# Cadres
def carte():
    return Frame(fen, padx=15, pady=10)

cadre_adresse = carte()
Label(cadre_adresse, text="Adresse IP", font=("Arial", 16, "bold")).pack(anchor="w")
Entry(cadre_adresse, textvariable=adresse_ip, font=("Arial", 16)).pack(fill="x")
cadre_adresse.pack(fill="x", padx=20, pady=10)

cadre_masque = carte()
Label(cadre_masque, text="Masque réseau", font=("Arial", 16, "bold")).pack(anchor="w")
Scale(
    cadre_masque, from_=1, to=31, orient=HORIZONTAL,
    variable=masque
).pack(fill="x")
cadre_masque.pack(fill="x", padx=20)

cadre_calcul = carte()
Button(
    cadre_calcul,
    text="Calculer",
    font=("Arial", 14),
    command=calcul_ip
).pack(pady=10)

Label(cadre_calcul, textvariable=adresse_reseau).pack(anchor="w")
Label(cadre_calcul, textvariable=premiere_adresse).pack(anchor="w")
Label(cadre_calcul, textvariable=derniere_adresse).pack(anchor="w")
Label(cadre_calcul, textvariable=adresse_broadcast).pack(anchor="w")
Label(cadre_calcul, textvariable=nombre_adresses_ip).pack(anchor="w")

cadre_calcul.pack(fill="x", padx=20, pady=10)

# Appliquer thème initial
appliquer_theme()

fen.mainloop()
