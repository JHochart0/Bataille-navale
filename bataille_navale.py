import numpy as np
import random as rd
from tkinter import *


def creation (j): #sous-programme pour créer un tableau de dimensions 2 remplis de 0
    tab = np.zeros((j,j))
    return(tab)


#on associe les variables avec leurs types 'creation'
tableauBOT = creation (10)
tableauPlayer = creation(10)
tableauTirJoueur = creation(10)
tableauTirIA = creation(10)






#différentes variables servant pour la version graphique
tailleX=1600
tailleY=900
fenetre = Tk()
cadre = Canvas(fenetre, width=tailleX, height=tailleY, bg="#008080")
cadre.pack()

bateau=5
sensbateau=1
text=cadre.create_text(800, 840, text="Vertical", fill="black", font="60" )
text2=cadre.create_text(800, 880, text="bateau de taille ", fill="black", font="60" )
text3=cadre.create_text(860, 880, text=5, fill="black", font="60" )
batcoordsX=[-1]*17
batcoordsY=[-1]*17
nbbat=0



def ChangeSens(): #sous-programme qui permet de changer le sens du bâteau quand on appuie sur le bouton du graphique
    global sensbateau
    global text
    cadre.delete(text)
    if sensbateau==1:
        sensbateau=2
        text=cadre.create_text(800, 840, text="Horizontal", fill="black", font="60" )

    elif sensbateau==2:
        sensbateau=1
        text=cadre.create_text(800, 840, text="Vertical", fill="black", font="60" )


def clicGauche(event) : #sous-programme qui s'occupe de gérer toutes les actions quand on clique sur le graphique. Il est séparé en 2 parties : le placement des bâteaux     et les attaques sur la grille de droite.


    #partie placement des bâteaux sur le graphique
    x = event.x
    y = event.y
    x=int(x/80)
    y=int(y/80)
    global text
    global text2
    global text3
    global sensbateau
    global bateau
    global batcoordsX
    global batcoordsY
    global nbbat
    testcolli=False

    if bateau==1:
        taillebateau=3
    else:
        taillebateau=bateau
    cadre.delete(text3)

    if bateau !=0:
        if sensbateau==1: #vertical

            for i in range(0,taillebateau):
                for u in range(0,17):

                    if x+1==batcoordsX[u] and y+1+i==batcoordsY[u]:
                        testcolli=True
                        break
                if testcolli==True:
                    break




            if y>=0 and y<11-taillebateau and x<10 and testcolli==False:
                placerbateaugraph(x,y,sensbateau,taillebateau,bateau)
                bateau=bateau-1



        if sensbateau==2: #horizontal
            for i in range(0,taillebateau):
                for u in range(0,17):

                    if x+1+i==batcoordsX[u] and y+1==batcoordsY[u]:
                        testcolli=True
                        break
                if testcolli==True:
                    break


            if x>=0 and x<11-taillebateau and y<10 and testcolli==False:
                placerbateaugraph(x,y,sensbateau,taillebateau,bateau)
                bateau=bateau-1

    if bateau==1:
        taillebateau=3
    else:
        taillebateau=bateau
    text3=cadre.create_text(860, 880, text=taillebateau, fill="black", font="60" )
    if bateau==0:
        cadre.delete(text)
        cadre.delete(text2)
        cadre.delete(text3)
        text=cadre.create_text(800, 840, text="A l'attaque !", fill="black", font="60" )
        boutonSens.destroy()


    #partie attaques graphique
    X=event.x
    Y=event.y
    if X>800 and Y<800 and nbbat==17:

        global tableauBOT
        print("")
        print(tableauBOT)
        testattack=False
        X=int(X/80)-10
        Y=int(Y/80)

        if tableauBOT[Y][X]!=0:
            X=((X+10)*80)-60
            Y=((Y)*80)-60
            cadre.create_oval(X+80, Y+80,X+40+80,Y+40+80, fill="red"  )
        else:
            X=((X+10)*80)-60
            Y=((Y)*80)-60
            cadre.create_oval(X+80, Y+80,X+40+80,Y+40+80, fill="black"  )





#création du bouton
boutonSens=Button(fenetre, text="Changez le sens du bâteau",background="darkgreen",activebackground="lightgreen",width="100" ,command=ChangeSens )
boutonSens.pack()

cadre.bind("<Button-1>", clicGauche)








def placerbateaugraph(x,y,sens,taillebateau,id): #place les bateaux dans le graphique adaptés aux coordonnées données
    global batcoordsX
    global batcoordsY
    global nbbat
    if id==5:
        couleur="red"
    elif id==4:
        couleur="blue"
    elif id==3:
        couleur="green"
    elif id==1:
        couleur="yellow"
    elif id==2:
        couleur="black"

    if sens==1:
        for i in range(0, taillebateau):
            batcoordsX[nbbat]=x+1
            batcoordsY[nbbat]=y+1+i
            nbbat=nbbat+1
        x=((x+1)*80)-60
        y=((y+1)*80)-60

        for i in range(0,80*taillebateau, 80):
            cadre.create_oval(x, y+i,x+40,y+40+i, fill=couleur  )






    if sens==2:
        for i in range(0, taillebateau):
            batcoordsX[nbbat]=x+1+i
            batcoordsY[nbbat]=y+1
            nbbat=nbbat+1
        x=((x+1)*80)-60
        y=((y+1)*80)-60
        for i in range(0,80*taillebateau, 80):
            cadre.create_oval(x+i, y, x+40+i, y+40 , fill=couleur )




def placer_bateau(taillebateau, tableau, id): #sous-programme pour placer un bateau dans un tableau de manière aléatoire
    sens=rd.randint(1,2)
    collision=0
    if sens==1: #vertical
        y=rd.randint(0,10-taillebateau)
        x=rd.randint(0,9)
        while collision!=taillebateau:
            if tableau[y+collision][x]!=0:

                x=rd.randint(0,9)
                y=rd.randint(0,10-taillebateau)
                collision=0
            else:
                collision=collision+1

        for i in range(0,taillebateau):
            tableau[y][x]=id
            y=y+1



    if sens==2: #horizontal
        y=rd.randint(0,9)
        x=rd.randint(0,10-taillebateau)
        while collision!=taillebateau:
            if tableau[y][x+collision]!=0:

                y=rd.randint(0,9)
                x=rd.randint(0,10-taillebateau)
                collision=0
            else:
                collision=collision+1

        for i in range(0,taillebateau):
            tableau[y][x]=id
            x=x+1





#placer les bâteaux dans grille de l'ordinateur
placer_bateau(2, tableauBOT,2)
placer_bateau(3,tableauBOT,3)
placer_bateau(3, tableauBOT, 1)
placer_bateau(4, tableauBOT, 4)
placer_bateau(5, tableauBOT, 5)





def placer(tableau, taillebateau, id_bat): #sous-programme pour le placement des bateaux du joueur sur la console
    print("*******************************************")
    print("placement du bateau de taille",taillebateau)
    print("*******************************************")
    sens=int(input("Donnez le sens du bâteau (2 pour horizontal / 1 pour vertical) : "))
    while sens<1 or sens>2:
        print("Erreur : Le numéro pour le sens est incorrect")
        sens=int(input("Donnez le sens du bâteau (2 pour horizontal / 1 pour vertical) : "))
    collisionbateau=0
    if sens==1: #vertical
        #demandepositions
        X=int(input("Donnez la coordonnée X de votre bâteau (entre 0 et 9) : "))
        while X<0 or X>9:
            print("Erreur : Votre coordonnée X est incorrecte")
            X=int(input("Donnez la coordonnée X de votre bâteau (entre 0 et 9) : "))
        print("Donnez la coordonnée Y de votre bâteau (entre 0 et ",10-taillebateau,") : ")
        Y=int(input())
        while Y<0 or Y>10-taillebateau:
            print("Erreur : Votre coordonnée Y est incorrecte")
            print("Donnez la coordonnée Y de votre bâteau (entre 0 et ",10-taillebateau,") : ")
            Y=int(input())

        #testcollisions
        while collisionbateau!=taillebateau:
            if tableau[Y+collisionbateau][X]!=0:
                print("Erreur : On ne peut pas poser de bâteau s'il y en a déja 1 :")
                print(tableau)
                print("Veuillez rechoisir des nouvelles coordonnées de bâteaux : ")

                X=int(input("Donnez la coordonnée X de votre bâteau (entre 0 et 9) : "))
                while X<0 or X>9:
                    print("Erreur : Votre coordonnée X est incorrecte")
                    X=int(input("Donnez la coordonnée X de votre bâteau (entre 0 et 9) : "))

                print("Donnez la coordonnée Y de votre bâteau (entre 0 et ",10-taillebateau,") : ")
                Y=int(input())
                while Y<0 or Y>10-taillebateau:
                    print("Erreur : Votre coordonnée Y est incorrecte")
                    print("Donnez la coordonnée Y de votre bâteau (entre 0 et ",10-taillebateau,") : ")
                    Y=int(input())
                collisionbateau=0
            else:
                collisionbateau=collisionbateau+1

        placerbateaugraph(X,Y,sens,taillebateau,id_bat)

        for i in range(0,taillebateau):
            tableau[Y][X]=id_bat
            Y=Y+1

    if sens==2: #horizontal
        Y=int(input("Donnez la coordonnée Y de votre bâteau (entre 0 et 9) : "))
        while Y<0 or Y>9:
            print("Erreur : Votre coordonnée Y est incorrecte")
            X=int(input("Donnez la coordonnée Y de votre bâteau (entre 0 et 9) : "))
        print("Donnez la coordonnée X de votre bâteau (entre 0 et ",10-taillebateau,") : ")
        X=int(input())
        while X<0 or X>10-taillebateau:
            print("Erreur : Votre coordonnée X est incorrecte")
            print("Donnez la coordonnée X de votre bâteau (entre 0 et ",10-taillebateau,") : ")
            X=int(input())

        #testcollisions
        while collisionbateau!=taillebateau:
            if tableau[Y][X+collisionbateau]!=0:
                print("Erreur : On ne peut pas poser de bâteau s'il y en a déja 1 :")
                print(tableau)
                print("Veuillez rechoisir des nouvelles coordonnées de bâteaux : ")

                Y=int(input("Donnez la coordonnée Y de votre bâteau (entre 0 et 9) : "))
                while Y<0 or Y>9:
                    print("Erreur : Votre coordonnée Y est incorrecte")
                    Y=int(input("Donnez la coordonnée Y de votre bâteau (entre 0 et 9) : "))

                print("Donnez la coordonnée X de votre bâteau (entre 0 et ",10-taillebateau,") : ")
                X=int(input())
                while X<0 or X>10-taillebateau:
                    print("Erreur : Votre coordonnée X est incorrecte")
                    print("Donnez la coordonnée X de votre bâteau (entre 0 et ",10-taillebateau,") : ")
                    X=int(input())
                collisionbateau=0
            else:
                collisionbateau=collisionbateau+1
        placerbateaugraph(X,Y,sens,taillebateau,id_bat)
        for i in range(0,taillebateau):
            tableau[Y][X]=id_bat
            X=X+1

def Jeu(tabJoueur, tabIA, tabTirJ, tabTirIA): #sous-programme pour s'occuper de la phase des tirs et de l'écran de fin sur la console

    BateauxJoueur=5+4+3+3+2
    BateauxIA=5+4+3+3+2
    touchebot=False
    while BateauxJoueur!=0 and BateauxIA!=0:
        print("C'est à vous d'attaquer !")
        print("Vous avez 3 tirs !")
        print("")
        print("*******************")
        print("Voici votre grille d'attaques")
        print("*******************")
        print(tabTirJ)
        print("")
        for i in range(0,3):
            if BateauxIA==0:
                break
            print("**********************************")
            print("Choix de coordonnées pour le tir numéro ",i+1)
            print("**********************************")
            print("")
            X=int(input("Donnez une coordonnée X pour attaquer (entre 0 et 9) : "))
            while X<0 or X>9:
                print("Erreur : Votre coordonnée X est incorrecte")
                X=int(input("Donnez une coordonnée X pour attaquer (entre 0 et 9) : "))
            Y=int(input("Donnez une coordonnée Y pour attaquer (entre 0 et 9) : "))
            while Y<0 or Y>9:
                print("Erreur : Votre coordonnée Y est incorrecte")
                Y=int(input("Donnez une coordonnée Y pour attaquer (entre 0 et 9) : "))

            while tabTirJ[Y][X]!=0: #vérification si déja attaqué
                print("Vous avez déjà attaquer cette case, veuillez resaisir des coordonnées")
                X=int(input("Donnez une coordonnée X pour attaquer (entre 0 et 9) : "))
                while X<0 or X>9:
                    print("Erreur : Votre coordonnée X est incorrecte")
                    X=int(input("Donnez une coordonnée X pour attaquer (entre 0 et 9) : "))
                Y=int(input("Donnez une coordonnée Y pour attaquer (entre 0 et 9) : "))
                while Y<0 or Y>9:
                    print("Erreur : Votre coordonnée Y est incorrecte")
                    Y=int(input("Donnez une coordonnée Y pour attaquer (entre 0 et 9) : "))
            if tabIA[Y][X]!=0:
                print("============================================")
                print("                 Touché !!")
                print("============================================")
                tabTirJ[Y][X]=9
                BateauxIA=BateauxIA-1
            else:
                print("============================================")
                print("                 Raté !!")
                print("============================================")
                tabTirJ[Y][X]=8
            print("")
            print("****************************************")
            print("Voici la grille de vos attaques")
            print("****************************************")
            print("")
            print(tabTirJ)
            print("")

        if BateauxIA!=0 and BateauxJoueur!=0:
            print("C'est à l'ordinateur d'attaquer !")
            print("Il possède 3 tirs !")

        for i in range(0, 3):
            if BateauxJoueur==0 or BateauxIA==0:
                break
            print("")
            print("**********************************")
            print("Choix de coordonnées du tir numéro ", i+1," pour l'ordinateur")
            print("**********************************")
            print("")
            if touchebot==False: #s'il a raté, alors il retire de manière aléatoire
                x=rd.randint(0,9)
                y=rd.randint(0,9)
                while tabTirIA[y][x]!=0: #regénère des valeurs de x et y s'il a déja attaqué dans la case donnée
                    x=rd.randint(0,9)
                    y=rd.randint(0,9)

            if touchebot==True:  #s'il a touché un bateau, il cherche a attaquer les 4 cases autours
                contour=rd.randint(1,4)
                if contour==1:  #vérifie en premier le dessus de la case touchée
                    if  y<1 or tabTirIA[y-1][x]!=0:
                        if x>8 or tabTirIA[y][x+1]!=0 :
                            if y>8 or tabTirIA[y+1][x]!=0 :
                                if x<1 or tabTirIA[y][x-1]!=0 :
                                    touchebot=False
                                    x=rd.randint(0,9)
                                    y=rd.randint(0,9)
                                else:
                                    x=x-1

                            else:
                                y=y+1
                        else:
                            x=x+1
                    else:
                        y=y-1

                if contour==2: #vérifie en premier la droite de la case touchée
                    if  x>8  or tabTirIA[y][x+1]!=0:
                        if y>8  or tabTirIA[y+1][x]!=0 :
                            if x<1 or  tabTirIA[y][x-1]!=0 :
                                if y<1 or tabTirIA[y-1][x]!=0:
                                    touchebot=False
                                    x=rd.randint(0,9)
                                    y=rd.randint(0,9)
                                else:
                                    y=y-1
                            else:
                                x=x-1
                        else:
                            y=y+1
                    else:
                        x=x+1

                if contour==3: #vérifie en premier le dessous de la case touchée
                    if y>8 or tabTirIA[y+1][x]!=0 :
                        if x<1 or tabTirIA[y][x-1]!=0:
                            if y<1 or  tabTirIA[y-1][x]!=0 :
                                if x>8 or tabTirIA[y][x+1]!=0 :
                                    touchebot=False
                                    x=rd.randint(0,9)
                                    y=rd.randint(0,9)
                                else:
                                    x=x+1
                            else:
                                y=y-1
                        else:
                            x=x-1
                    else:
                        y=y+1

                if contour==4: #vérifie en premier la gauche de la case touchée
                    if x<0 or tabTirIA[y][x-1]!=0 :
                        if  y<0 or tabTirIA[y-1][x]!=0 :
                            if x>9 or tabTirIA[y][x+1]!=0 :
                                if y>9  or tabTirIA[y+1][x]!=0 :
                                    touchebot=False
                                    x=rd.randint(0,9)
                                    y=rd.randint(0,9)
                                else:
                                    y=y+1
                            else:
                                x=x+1
                        else:
                            y=y-1
                    else:
                        x=x-1


            print("L'ordinateur a decidé d'attaquer en X=",x," et Y=", y)
            if tabJoueur[y][x]!=0:
                print("============================================")
                print("         L'ordinateur vous a touché !!")
                print("============================================")
                tabTirIA[y][x]=9
                BateauxJoueur=BateauxJoueur-1
                touchebot=True
            else:
                print("============================================")
                print("         L'ordinateur vous a raté !!")
                print("============================================")
                tabTirIA[y][x]=8
                touchebot=False
        print("")
        print("****************************************")
        print("Voici la grille des attaques de l'adversaire")
        print("****************************************")
        print("")
        print(tabTirIA)
        print("")

    if BateauxJoueur==0:
        print("****************************************")
        print("L'ordinateur vous a détruit votre dernier bâteau, Vous avez perdu !!")
        print("****************************************")
    elif BateauxIA==0:
        print("****************************************")
        print("Vous avez détruit le dernier navire de l'adversaire , Vous avez gagné !!")
        print("****************************************")

def dessinercadre(): #sous-programme pour créer la grille graphique
    for i in range(0, 800, 80):
        for u in range(3, 800, 80):
            cadre.create_rectangle(u,i,u+80,i+80, fill="#6495ed", outline='black',activefill="grey")

    for i in range(0, 800, 80):
        for u in range(800, 1600, 80):
            cadre.create_rectangle(u,i,u+80,i+80, fill="#6495ed", outline='black',activefill="darkred")
    cadre.create_rectangle(3,3,800,800, width=5)
    cadre.create_rectangle(800,3,1600,800, width=5)
    cadre.create_rectangle(3,800,1600,900, width=5)
    cadre.create_text(400, 840, text="Vos bâteaux", fill="black", font="60" )
    cadre.create_text(1200, 840, text="Vos attaques", fill="black", font="60" )



def choixplacement(tableauPlayer): #sous-programme pour demander au joueur comment il veut placer ses bâteaux (aléatoirement ou par choix) sur la console

    choix=int(input("Choisissez la manière dont vos bâteaux seront placés (1 pour placer vous même / 2 pour les placer aléatoirement) : "))
    while choix<1 or choix>2:
        print("Erreur : Le choix que vous avez fait n'existe pas")
        choix=int(input("Choisissez la manière dont vos bâteaux seront placés (1 pour placer vous même / 2 pour les placer aléatoirement) : "))
    if choix==1: #on appelle le sous-programme pour placer ses bâteaux pour chaque bâteau correspondant
        print("***************************************")
        print("Vous avez choisi de placer vos bâteaux vous même")
        print("***************************************")
        placer(tableauPlayer,2,2)
        print(tableauPlayer)
        placer(tableauPlayer,3,3)
        print(tableauPlayer)
        placer(tableauPlayer,3,1)
        print(tableauPlayer)
        placer(tableauPlayer,4,4)
        print(tableauPlayer)
        placer(tableauPlayer,5,5)



    elif choix==2: #on appelle le sous-programme pour générer le tableau du joueur avec les bâteaux aléatoires
        print("***************************************")
        print("Vous avez choisi de placer vos bâteaux de manière aléatoire")
        print("***************************************")
        placer_bateau(2, tableauPlayer, 2)
        placer_bateau(3, tableauPlayer, 3)
        placer_bateau(3, tableauPlayer, 1)
        placer_bateau(4, tableauPlayer, 4)
        placer_bateau(5, tableauPlayer, 5)





#appels pour lancer la fenêtre graphique
dessinercadre()
fenetre.mainloop()


#appels pour lancer la version du jeu sur la console
choixplacement(tableauPlayer)

print("*******************")
print("Voici votre grille !!")
print("*******************")
print(tableauPlayer)

Jeu(tableauPlayer, tableauBOT, tableauTirJoueur, tableauTirIA)


