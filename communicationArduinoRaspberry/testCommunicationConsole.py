# Ce programme permet d'entrer un message du côté raspberry et de le lire du côté arduino
import serial, time

# Connecte le port serie a l'arduino
with serial.Serial("/dev/ttyS0", 9600, timeout=.1) as arduino:
    time.sleep(0.1)
    # Si le port est accessible
    if arduino.isOpen():
        print("{} connected".format(arduino.port))
        try:
            # On boucle pour ecrire dans le bus uart de données
            while True:
                entree = input("Valeur a envoyer")
                # on ecrit la valeur saisie dans l'input
                arduino.write(entree.encode())
        except KeyboardInterrupt:
            print("Controle c pressé")
