

from tkinter import *


#%% Modèle
def dec_to_bits(dec):
    """
    Convertit en binaire un entier

    Parameters
    ----------
    dec :un entier entre 0 et 255

    Returns
    -------
    Représentation binaire de l'entier sous forme de liste de 8 bits

    """
    assert 0 <= dec <= 255
    bits = [0 for i in range(8)]
    i  = 7
    while dec > 0 : 
        bits[i] = dec % 2
        dec = dec // 2
        i = i -1
         
    return bits


def test_dec_to_bits():
    assert dec_to_bits(15) == [0, 0, 0, 0, 1, 1, 1, 1]
    assert dec_to_bits(132) == [1, 0, 0, 0, 0, 1, 0, 0]


def bits_to_dec(bits):
    """
    Convertit une liste de bits en décimal

    Parameters
    ----------
    bits : liste de 8 bits

    Returns
    -------
    entier entre 0 et 255

    """
    dec = 0
    puissance = 0
    for i in range (len(bits)-1,-1,-1) :
        dec = dec + bits[i] * 2**puissance
        puissance = puissance + 1
    return dec
    


def test_bits_to_dec():
    assert bits_to_dec([0, 0, 0, 0, 1, 1, 1, 1]) == 15
    assert bits_to_dec([1, 0, 0, 0, 0, 1, 0, 0]) == 132


def ip_to_bits(ip):
    """
    Convertit une adresse ip sous forme de str en liste de 32 bits

    Parameters
    ----------
    ip : adresse ip sous forme de str comme '172.17.232.6'

    Returns
    -------
    adresse ip sous forme de liste de 32 bits

    """
    # à compléter


def test_ip_to_bits():
    assert ip_to_bits("172.17.232.6") == [
        1,
        0,
        1,
        0,
        1,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        1,
        1,
        1,
        1,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        0,
    ]


def bits_to_ip(ip_bits):
    """
    Convertit une adresse ip sous forme de str en liste de 32 bits


    Parameters
    ----------
    ip_bits : adresse ip sous forme de liste de 32 bits

    Returns
    -------
    adresse ip sous forme de str comme '172.17.232.6'

    """
    # à compléter


def test_bits_to_ip():
    assert (
        bits_to_ip(
            [
                1,
                0,
                1,
                0,
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                1,
                1,
                1,
                1,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                1,
                0,
            ]
        )
        == "172.17.232.6"
    )


def verifier_ip(ip):
    """
    Vérifie si une adresse ip sous forme de  str comme '172.17.232.6'
    est valide

    Parameters
    ----------
    ip : adresse ip sous forme de str comme '172.17.232.6'
    Returns
    -------
    booléen
    """
    # à compléter
compléter

def test_verifier_ip():
    assert verifier_ip("172.17.232.6") == True
    assert verifier_ip("172.17.256.6") == False
    assert verifier_ip("172.17.256") == False
    assert verifier_ip("172.17.256") == False


def prefixe_reseau(ip_bits, mask):
    """
    Renvoie le préfixe réseau d'une adresse IP sous forme de liste de 32 bits
    à partir de la longueur du masque réseau

    Parameters
    ----------
    ip_bits : liste de bits (0 ou 1)
    masque : entier entre 1 et 31 bits

    Returns
    -------
    Renvoie une liste de 32 bits

    """
    prefixe = [0 for i in range(32)]
    ip_masque = [1 for i in range(mask)] + [0 for j in range(32 - mask)]
    # à complétercompléter


def test_prefixe_reseau():
    assert prefixe_reseau(
        [
            1,
            0,
            1,
            0,
            1,
            1,
            0,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            1,
            1,
            1,
            1,
            0,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            1,
            0,
        ],
        21,
    ) == [
        1,
        0,
        1,
        0,
        1,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        1,
        1,
        1,
        1,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]


def calcul_ip():
    """Fonction de rappel du bouton bouton_calcul
    Récupère l'adresse IP  de la variable de contrôle  adresse_ip
    Vérifie si cette adresse est valide avec verifier_ip
    Si elle est valide, convertit l'adresse en liste de 32 bits,
    puis calcule le préfixe réseau, la première adresse, la dernière adresse
    et l'adresse de broadcast (dernière adresse de la plage)
    Modifie pour cela les variables de contrôles liées aux étiquettes
    d'affichage de ces différents éléments
    """
    ip = adresse_ip.get()
    if not verifier_ip(ip):
        message_erreur.set("Adresse non conforme")
    else:
        message_erreur.set("")
        ip_bits = ip_to_bits(ip)
        adresse = prefixe_reseau(ip_bits, masque.get())
        adresse_reseau.set("Adresse  réseau : " + bits_to_ip(adresse))
        adresse[31] = 1
        premiere_adresse.set("Première adresse : " + bits_to_ip(adresse))
        # à compléter


#%% Vue : interface graphique


# Fenêtre racine
fen = Tk()
fen.title("Calculateur d'adresses IP")
fen.geometry("600x400")

### Variables de contrôles
adresse_ip = StringVar()
premiere_adresse = StringVar()
premiere_adresse.set("Première adresse : ")
adresse_reseau = StringVar()
adresse_reseau.set("Adresse réseau : ")
derniere_adresse = StringVar()
derniere_adresse.set("Dernière adresse : ")
adresse_broadcast = StringVar()
adresse_broadcast.set("Adresse broadcast : ")
message_erreur = StringVar()
nombre_adresses_ip = StringVar()
nombre_adresses_ip.set("Nombre d'adresses IP : ")
masque = IntVar()

# Cadre adresse
cadre_adresse = Frame(fen)
etiq_adresse = Label(cadre_adresse, text="Adresse IP : ", font=("Arial", 20))
saisie_adresse = Entry(
    cadre_adresse, textvariable=adresse_ip, font=("Arial", 20)
)
etiq_adresse.pack(side=LEFT)
saisie_adresse.pack(side=LEFT)
cadre_adresse.pack()

# Cadre masque
cadre_masque = Frame(fen)
# à compléter

# Cadre calcul
cadre_calcul = Frame(fen)
# à compléter

#%% Boucle infinie , réceptionnaire d'événement
fen.mainloop()
