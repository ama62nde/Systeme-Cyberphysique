
Dans un premier temps on va commencer par réaliser une simulation via simulink pour rendre le système commandable.

On va dans un premier temps chercher à traduire le comportement de systèmes commande en algorithmes. 
On veut ensuite récupérer les mesures des capteurs et transmettre les commandes aux actionneurs.
Ensuite, il nous faudra mettre en place une communication efficace entre les sous-systèmes.
Il nous faut finalement nous occuper de la cinématique du robot en obtenant ses équations. 

Dans la première partie, on va chercher à mettre en place l'observateur. 


l'asservissement du moteur 
On devra ensuite appliquer la même chose au second moteur 
On veut ensuite le rendre commandable
Il nous faudra ensuite calculer les vitesses VG et VD des 2 moteurs 


Au niveau du matériel fourni, nous travaillerons avec un Arduino MEGA qui sera connecté aux moteurs et à l'encodeur qui seront eux mêmes connectés aux GPIO. 
Nous aurons également un gyroscope et un accéléromètre qui nous permettrons de gérer la vitesse de rotation et l'accélération en translation depuis les ports I2C. 
Finalement, un Raspberry PI connecté en UART2 à l'Arduino. 

Nous rendrons dans notre rapport, des graphiques pour expliquer nos résultats, un diagramme UML, un diagramme d'activité pour expliquer les liens entre nos différents modules ainsi que des diagrammes de séquences et l'affichage de nos données. 
Il nous faudra définir des spécification et les contraintes liées à notre projet. 

Nous fournirons finalement notre code produit via GIT. 

On commence par asservir le moteur avec un code arduino, il nous faut au préalable charger les librairies TimerFive et la Librairie MakeBlock.
Si on veut visualiser l'angle avec le gyro dans le moniteur, il faut passer en Bode 115200
