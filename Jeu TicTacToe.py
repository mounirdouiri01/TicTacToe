from tkinter import *  #importer la totalité de module tkinter
from tkinter import ttk  #importe ttk
from tkinter.messagebox import * #importe tkinter.messagebox

Mafenetre = Tk()
Mafenetre . title('Jeu du morpion ')  # titre de jeu
Mafenetre . geometry('637x570')      # les dimensions de la fenetre
Mafenetre . resizable(width=0, height=0)  # met la fenêtre en taille fixe

def quitter():
    Mafenetre.quit()    # quitte  mainloop
    Mafenetre.destroy() #détruit tous les widgets incorporés

def reset():
    global etatWedgets,Buttuonplay,L1,L2,L3,C1,C2,C3,G1,G2,img,imp1,imp2,ZP1,ZP2,ZSCP1,ZSCP2
    global XO1,XO2,SCORE1,SCORE2

    if (etatWedgets == 0):   # si widgets de frame 1 desactive (jeu active)
        p1.config(state=NORMAL)
        p2.config(state=NORMAL)
        XO1.config(state=NORMAL)
        XO2.config(state=NORMAL)
        etatWedgets=1   #widgets de frame 1 active (jeu desactive)

    p1 . delete(0,END)  #supprime le nom de player one
    p2 . delete(0, END) #supprime le nom de player two
    XO1 . current(0)   # valeur par defaut de symbol est X pour player One
    XO2 . current(1)  # valeur par defaut de symbol est O pour Player Two
    button1 . config(text='', state=DISABLED, bg='red')
    button2 . config(text='', state=DISABLED, bg='red')
    button3 . config(text='', state=DISABLED, bg='red')
    button4 . config(text='', state=DISABLED, bg='red')
    button5 . config(text='', state=DISABLED, bg='red')
    button6 . config(text='', state=DISABLED, bg='red')
    button7 . config(text='', state=DISABLED, bg='red')
    button8 . config(text='', state=DISABLED, bg='red')
    button9 . config(text='', state=DISABLED, bg='red')
    Buttuonplay.config(state=NORMAL)

    L1 = ['', '', '']  # vidé ligne1
    L2 = ['', '', '']  # vidé ligne2
    L3 = ['', '', '']  # vidé ligne3
    C1 = ['', '', '']   # vidé column 1
    C2 = ['', '', '']   # vidé column 2
    C3 = ['', '', '']   # vidé column 3
    G1 = ['', '', '']   #vidé diagonale 1
    G2 = ['', '', '']   #vidé diagonale 2

    imp1.config(image=img)
    imp2.config(image=img)
    wnr.config(text='')
    lsr.config(text='')

    ZP1.config(state=NORMAL)    # active la zone de saise qui affiche nom player one
    ZP2.config(state=NORMAL)    # active la zone de saise qui affiche nom player two
    ZP1.delete(0, END)          # supprimer nom de player one
    ZP2.delete(0, END)          # supprimer nom de player two
    ZP1.config(state=DISABLED)  # desactive la zone de saise qui affiche nom player one
    ZP2.config(state=DISABLED)  # desactive la zone de saise qui affiche nom player two

    ZSCP1.config(state=NORMAL)  # active la zone de saise qui affiche le score player one
    ZSCP2.config(state=NORMAL)  # active la zone de saise qui affiche le score player two
    ZSCP1.delete(0, END)        # supprimer score de player one
    ZSCP2.delete(0, END)        # supprimer score de player two
    ZSCP1.config(state=DISABLED) # desactive la zone de saise qui affiche le score player one
    ZSCP2.config(state=DISABLED) # desactive la zone de saise qui affiche le score player two
    SCORE1=0                     # le variable qui calcule score de player one
    SCORE2=0                     # le variable qui calcule score de player two

def check1():
    global temp,L1,C1,G1,XO1,p1,p2,imp1,imp2,img2,img3,SCORE1,SCORE2
    if (temp == 1):  # temp=1 indique le tour pour le player qui jouer avec X
        button1.config(state=DISABLED) # désactive le bouton
        button1.config(text='X')       # la valeur de bouton prend X
        temp = 0    # temp=1 indique le tour pour le player qui jouer avec O
        L1[0]='X'   # première valeur de ligne 1 prend X
        C1[0]='X'   # première valeur de column 1 prend X
        G1[0]='X'   # première valeur de diagonale 1 prend X

    elif (temp == 0):   # temp=0 indique le tour pour le player qui jouer avec O
        button1.config(state=DISABLED) # désactive le bouton
        button1.config(text='O')  # la valeur de bouton prend O
        temp = 1    # temp=1 indique le tour pour le player qui jouer avec X
        L1[0]='O'   # première valeur de ligne 1 prend O
        C1[0]='O'   # première valeur de column 1 prend O
        G1[0]='O'   # première valeur de diagonale 1 prend O

    if ((L1[0]=='X' and L1[1]=='X' and L1[2]=='X') or (C1[0]=='X' and C1[1]=='X' and C1[2]=='X') or
                                                         (G1[0]=='X' and G1[1]=='X' and G1[2]=='X')):
        selc=XO1.get()   # recuperer le symbole de jeu pour player 1
        name1=p1.get()   # recuperer le nom de joueur pour player 1
        name2=p2.get()   # recuperer le nom de joueur pour player 2
        if(selc=='X'):
            showinfo('Resultat','Mabrouuuuuk, Le joueur '+name1+' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1=SCORE1+1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0,END)
            ZSCP1.insert(0,SCORE1)
            ZSCP1.config(state=DISABLED)

        else:
            showinfo('Resultat','Mabrouuuuuk, Le joueur '+name2+' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)

    if ((L1[0]=='O' and L1[1]=='O' and L1[2]=='O') or (C1[0]=='O' and C1[1]=='O' and C1[2]=='O') or
                                                        (G1[0]=='O' and G1[1]=='O' and G1[2]=='O')):
        selc = XO1.get()
        name1 = p1.get()
        name2 = p2.get()
        if (selc == 'O'):
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name1 + ' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1 = SCORE1 + 1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0, END)
            ZSCP1.insert(0, SCORE1)
            ZSCP1.config(state=DISABLED)
        else:
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name2 + ' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)

def check2():
    global temp,L1,C2,ZSCP1,ZSCP2,SCORE1,SCORE2
    if (temp == 1):
        button2.config(state=DISABLED)
        button2.config(text='X')
        temp = 0
        L1[1]='X'
        C2[0]='X'

    elif (temp == 0):
        button2.config(state=DISABLED)
        button2.config(text='O')
        temp = 1
        L1[1]='O'
        C2[0]='O'

    if ((L1[0]=='X' and L1[1]=='X' and L1[2]=='X') or (C2[0]=='X' and C2[1]=='X' and C2[2]=='X') ):
        selc=XO1.get()
        name1=p1.get()
        name2=p2.get()
        if(selc=='X'):
            showinfo('Resultat','Mabrouuuuuk, Le joueur '+name1+' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1 = SCORE1 + 1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0, END)
            ZSCP1.insert(0, SCORE1)
            ZSCP1.config(state=DISABLED)
        else:
            showinfo('Resultat','Mabrouuuuuk, Le joueur '+name2+' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)

    if ((L1[0]=='O' and L1[1]=='O' and L1[2]=='O') or (C2[0]=='O' and C2[1]=='O' and C2[2]=='O') ):
        selc = XO1.get()
        name1 = p1.get()
        name2 = p2.get()
        if (selc == 'O'):
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name1 + ' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1 = SCORE1 + 1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0, END)
            ZSCP1.insert(0, SCORE1)
            ZSCP1.config(state=DISABLED)
        else:
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name2 + ' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)

def check3():
    global temp,L1,C3,G2,ZSCP1,ZSCP2,SCORE1,SCORE2
    if (temp == 1):
        button3.config(state=DISABLED)
        button3.config(text='X')
        temp = 0
        L1[2] = 'X'
        C3[0] = 'X'
        G2[0] = 'X'

    elif (temp == 0):
        button3.config(state=DISABLED)
        button3.config(text='O')
        temp = 1
        L1[2] = 'O'
        C3[0] = 'O'
        G2[0] = 'O'

    if ((L1[0] == 'X' and L1[1] == 'X' and L1[2] == 'X') or (C3[0] == 'X' and C3[1] == 'X' and C3[2] == 'X') or (G2[0]=='X' and G2[1]=='X' and G2[2]=='X')):
        selc = XO1.get()
        name1 = p1.get()
        name2 = p2.get()

        if (selc == 'X'):
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name1 + ' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1 = SCORE1 + 1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0, END)
            ZSCP1.insert(0, SCORE1)
            ZSCP1.config(state=DISABLED)

        else:
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name2 + ' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)

    if ((L1[0] == 'O' and L1[1] == 'O' and L1[2] == 'O') or (C2[0] == 'O' and C2[1] == 'O' and C2[2] == 'O') or (G2[0]=='O' and G2[1]=='O' and G2[2]=='O')):
        selc = XO1.get()
        name1 = p1.get()
        name2 = p2.get()
        if (selc == 'O'):
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name1 + ' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1 = SCORE1 + 1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0, END)
            ZSCP1.insert(0, SCORE1)
            ZSCP1.config(state=DISABLED)
        else:
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name2 + ' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)


def check4():
    global temp,L2,C1,ZSCP1,ZSCP2,SCORE1,SCORE2
    if (temp == 1):
        button4.config(state=DISABLED)
        button4.config(text='X')
        temp = 0
        L2[0] = 'X'
        C1[1] = 'X'

    elif (temp == 0):
        button4.config(state=DISABLED)
        button4.config(text='O')
        temp = 1
        L2[0] = 'O'
        C1[1] = 'O'

    if ((L2[0] == 'X' and L2[1] == 'X' and L2[2] == 'X') or (C1[0] == 'X' and C1[1] == 'X' and C1[2] == 'X') ):
        selc = XO1.get()
        name1 = p1.get()
        name2 = p2.get()

        if (selc == 'X'):
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name1 + ' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1 = SCORE1 + 1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0, END)
            ZSCP1.insert(0, SCORE1)
            ZSCP1.config(state=DISABLED)
        else:
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name2 + ' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)

    if ((L2[0] == 'O' and L2[1] == 'O' and L2[2] == 'O') or (C1[0] == 'O' and C1[1] == 'O' and C1[2] == 'O') ):
        selc = XO1.get()
        name1 = p1.get()
        name2 = p2.get()
        if (selc == 'O'):
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name1 + ' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1 = SCORE1 + 1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0, END)
            ZSCP1.insert(0, SCORE1)
            ZSCP1.config(state=DISABLED)
        else:
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name2 + ' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)

def check5():
    global temp,L2,C2,G1,G2,ZSCP1,ZSCP2,SCORE1,SCORE2
    if (temp == 1):
        button5.config(state=DISABLED)
        button5.config(text='X')
        temp = 0
        L2[1] = 'X'
        C2[1] = 'X'
        G1[1] = 'X'
        G2[1] = 'X'

    elif (temp == 0):
        button5.config(state=DISABLED)
        button5.config(text='O')
        temp = 1
        L2[1] = 'O'
        C2[1] = 'O'
        G1[1] = 'O'
        G2[1] = 'O'

    if ((L2[0] == 'X' and L2[1] == 'X' and L2[2] == 'X') or (C2[0] == 'X' and C2[1] == 'X' and C2[2] == 'X') or (G1[0]=='X' and G1[1]=='X' and G1[2]=='X') or (G2[0]=='X' and G2[1]=='X' and G2[2]=='X') ):
        selc = XO1.get()
        name1 = p1.get()
        name2 = p2.get()

        if (selc == 'X'):
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name1 + ' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1 = SCORE1 + 1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0, END)
            ZSCP1.insert(0, SCORE1)
            ZSCP1.config(state=DISABLED)
        else:
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name2 + ' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)

    if ((L2[0] == 'O' and L2[1] == 'O' and L2[2] == 'O') or (C2[0] == 'O' and C2[1] == 'O' and C2[2] == 'O') or (G1[0]=='O' and G1[1]=='O' and G1[2]=='O') or (G2[0]=='O' and G2[1]=='O' and G2[2]=='O') ):
        selc = XO1.get()
        name1 = p1.get()
        name2 = p2.get()
        if (selc == 'O'):
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name1 + ' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1 = SCORE1 + 1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0, END)
            ZSCP1.insert(0, SCORE1)
            ZSCP1.config(state=DISABLED)
        else:
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name2 + ' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)

def check6():
    global temp,L2,C3,ZSCP1,ZSCP2,SCORE1,SCORE2
    if (temp == 1):
        button6.config(state=DISABLED)
        button6.config(text='X')
        temp = 0
        L2[2] = 'X'
        C3[1] = 'X'

    elif (temp == 0):
        button6.config(state=DISABLED)
        button6.config(text='O')
        temp = 1
        L2[2] = 'O'
        C3[1] = 'O'

    if ((L2[0] == 'X' and L2[1] == 'X' and L2[2] == 'X') or (C3[0] == 'X' and C3[1] == 'X' and C3[2] == 'X') ):
        selc = XO1.get()
        name1 = p1.get()
        name2 = p2.get()

        if (selc == 'X'):
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name1 + ' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1 = SCORE1 + 1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0, END)
            ZSCP1.insert(0, SCORE1)
            ZSCP1.config(state=DISABLED)
        else:
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name2 + ' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)

    if ((L2[0] == 'O' and L2[1] == 'O' and L2[2] == 'O') or (C3[0] == 'O' and C3[1] == 'O' and C3[2] == 'O') ):
        selc = XO1.get()
        name1 = p1.get()
        name2 = p2.get()
        if (selc == 'O'):
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name1 + ' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1 = SCORE1 + 1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0, END)
            ZSCP1.insert(0, SCORE1)
            ZSCP1.config(state=DISABLED)
        else:
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name2 + ' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)

def check7():
    global temp,L3,C1,G2,ZSCP1,ZSCP2,SCORE1,SCORE2
    if (temp == 1):
        button7.config(state=DISABLED)
        button7.config(text='X')
        temp = 0
        L3[0] = 'X'
        C1[2] = 'X'
        G2[2] = 'X'

    elif (temp == 0):
        button7.config(state=DISABLED)
        button7.config(text='O')
        temp = 1
        L3[0] = 'O'
        C1[2] = 'O'
        G2[2] = 'O'

    if ((L3[0] == 'X' and L3[1] == 'X' and L3[2] == 'X') or (C1[0] == 'X' and C1[1] == 'X' and C1[2] == 'X') or (G2[0] == 'X' and G2[1] == 'X' and G2[2] == 'X') ):
        selc = XO1.get()
        name1 = p1.get()
        name2 = p2.get()

        if (selc == 'X'):
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name1 + ' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1 = SCORE1 + 1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0, END)
            ZSCP1.insert(0, SCORE1)
            ZSCP1.config(state=DISABLED)
        else:
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name2 + ' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)

    if ((L3[0] == 'O' and L3[1] == 'O' and L3[2] == 'O') or (C1[0] == 'O' and C1[1] == 'O' and C1[2] == 'O') or (G2[0] == 'O' and G2[1] == 'O' and G2[2] == 'O') ):
        selc = XO1.get()
        name1 = p1.get()
        name2 = p2.get()
        if (selc == 'O'):
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name1 + ' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1 = SCORE1 + 1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0, END)
            ZSCP1.insert(0, SCORE1)
            ZSCP1.config(state=DISABLED)
        else:
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name2 + ' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)

def check8():
    global temp,L3,C2,ZSCP1,ZSCP2,SCORE1,SCORE2
    if (temp == 1):
        button8.config(state=DISABLED)
        button8.config(text='X')
        temp = 0
        L3[1] = 'X'
        C2[2] = 'X'

    elif (temp == 0):
        button8.config(state=DISABLED)
        button8.config(text='O')
        temp = 1
        L3[1] = 'O'
        C2[2] = 'O'

    if ((L3[0] == 'X' and L3[1] == 'X' and L3[2] == 'X') or (C2[0] == 'X' and C2[1] == 'X' and C2[2] == 'X') ):
        selc = XO1.get()
        name1 = p1.get()
        name2 = p2.get()

        if (selc == 'X'):
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name1 + ' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1 = SCORE1 + 1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0, END)
            ZSCP1.insert(0, SCORE1)
            ZSCP1.config(state=DISABLED)
        else:
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name2 + ' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)

    if ((L3[0] == 'O' and L3[1] == 'O' and L3[2] == 'O') or (C2[0] == 'O' and C2[1] == 'O' and C2[2] == 'O') ):
        selc = XO1.get()
        name1 = p1.get()
        name2 = p2.get()
        if (selc == 'O'):
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name1 + ' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1 = SCORE1 + 1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0, END)
            ZSCP1.insert(0, SCORE1)
            ZSCP1.config(state=DISABLED)
        else:
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name2 + ' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)

def check9():
    global temp,L3,C3,G1,ZSCP1,ZSCP2,SCORE1,SCORE2
    if (temp == 1):
        button9.config(state=DISABLED)
        button9.config(text='X')
        temp = 0
        L3[2] = 'X'
        C3[2] = 'X'
        G1[2] = 'X'
    elif (temp == 0):
        button9.config(state=DISABLED)
        button9.config(text='O')
        temp = 1
        L3[2] = 'O'
        C3[2] = 'O'
        G1[2] = 'O'

    if ((L3[0] == 'X' and L3[1] == 'X' and L3[2] == 'X') or (C3[0] == 'X' and C3[1] == 'X' and C3[2] == 'X') or (G1[0] == 'X' and G1[1] == 'X' and G1[2] == 'X') ):
        selc = XO1.get()
        name1 = p1.get()
        name2 = p2.get()

        if (selc == 'X'):
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name1 + ' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1 = SCORE1 + 1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0, END)
            ZSCP1.insert(0, SCORE1)
            ZSCP1.config(state=DISABLED)
        else:
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name2 + ' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)

    if ((L3[0] == 'O' and L3[1] == 'O' and L3[2] == 'O') or (C3[0] == 'O' and C3[1] == 'O' and C3[2] == 'O') or (G1[0] == 'O' and G1[1] == 'O' and G1[2] == 'O') ):
        selc = XO1.get()
        name1 = p1.get()
        name2 = p2.get()
        if (selc == 'O'):
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name1 + ' est gagner!')
            imp1.config(image=img3)
            imp2.config(image=img2)
            wnr.config(text='Congratulations !')
            lsr.config(text='Hard luck... !')
            SCORE1 = SCORE1 + 1
            ZSCP1.config(state=NORMAL)
            ZSCP1.delete(0, END)
            ZSCP1.insert(0, SCORE1)
            ZSCP1.config(state=DISABLED)
        else:
            showinfo('Resultat', 'Mabrouuuuuk, Le joueur ' + name2 + ' est gagner!')
            imp1.config(image=img2)
            imp2.config(image=img3)
            lsr.config(text='Congratulations !')
            wnr.config(text='Hard luck... !')
            SCORE2 = SCORE2 + 1
            ZSCP2.config(state=NORMAL)
            ZSCP2.delete(0, END)
            ZSCP2.insert(0, SCORE2)
            ZSCP2.config(state=DISABLED)

        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)
def go():
    global etatWedgets, temp, p1, p2, XO1, XO2,Buttuonplay,imp1,imp2,img1,ZSCP1,ZSCP2
    if (p1.get()=='' or p2.get()==''):  # si le nom da P1 ou P2 vide
        if(p1.get()==''):
            p1.config(highlightbackground='red', highlightthicknes=1)
            showerror('Error', 'Nom de joueur 1 est vide.\nSVP saisir le nom de joueur')
        else:
            p2 . config(highlightbackground='red', highlightthicknes=1)
            showerror('Error', 'Nom de joueur 2 est vide.\nSVP saisir le nom de joueur')
    elif (XO1.get()==XO2.get()):
        showerror('Error', 'Impossibl les deux joueurs jouer avec le même symbole.\n'
                           'SVP chose X for player one and O for player two orvice versa')
    else:
        p1.config(state=DISABLED)    # desactive la zone de saise nom P1
        p2.config(state=DISABLED)   # desactive la zone de saise nom P2
        XO1.config(state=DISABLED)  # desactive la liste de choix de symbol pour P1
        XO2.config(state=DISABLED)  # desactive la liste de choix de symbol pour P2
        etatWedgets = 0            # P1,P2,X01,X02 sont désactive (jeu active)

        button1.config(text='', state=NORMAL, bg='black')
        button2.config(text='', state=NORMAL, bg='black')
        button3.config(text='', state=NORMAL, bg='black')
        button4.config(text='', state=NORMAL, bg='black')
        button5.config(text='', state=NORMAL, bg='black')
        button6.config(text='', state=NORMAL, bg='black')
        button7.config(text='', state=NORMAL, bg='black')
        button8.config(text='', state=NORMAL, bg='black')
        button9.config(text='', state=NORMAL, bg='black')

        temp = 1                        #le tour de jeu avec le joueur qui joue avec X

        imp1 . config(image=img1)
        imp2 . config(image=img1)

        nm1=p1.get()                 # recuperer le nom de player one
        nm2=p2.get()                 # recuperer le nom de player two
        ZP1.config(state=NORMAL)     # active la zone qui affiche nom de player qui existe dans frame3
        ZP2.config(state=NORMAL)     # active la zone qui affiche nom de player qui est dans frame4
        ZP1.insert(0,nm1)            # rempler la zone avec le nom de player one
        ZP2.insert(0,nm2)            # rempler la zone avec le nom de player two
        ZP1.config(state=DISABLED)    # desactive zone 1 qui existe dans frame 3
        ZP2.config(state=DISABLED)     # desactive zone 2 qui existe dans frame 4

        ZSCP1.config(state=NORMAL)     # active la zone de score qui existe dans frame3
        ZSCP2.config(state=NORMAL)      # active la zone de score qui existe dans frame4
        ZSCP1.insert(0,0)               # rempler la zone de score avec 0 pour frame 3
        ZSCP2.insert(0,0)                # rempler la zone de score avec 0 pour frame 4
        ZSCP1.config(state=DISABLED)   # desactive zone de score 1
        ZSCP2.config(state=DISABLED)   # desactive zone de score 2

        Buttuonplay.config(state=DISABLED)   # desactive le botoun Jouer

def Recommancer():
    global temp, etatWedgets,L1,L2,L3,C1,C2,C3,G1,G2,img1,imp1,imp2,wnr,lsr
    if (etatWedgets==0):            # si le jeu active (les wedgits de frame 1 desactive)
        temp = 1                    # le tour de jeu avec le joueur qui joue avec X
        button1.config(text='', state=NORMAL)
        button2.config(text='', state=NORMAL)
        button3.config(text='', state=NORMAL)
        button4.config(text='', state=NORMAL)
        button5.config(text='', state=NORMAL)
        button6.config(text='', state=NORMAL)
        button7.config(text='', state=NORMAL)
        button8.config(text='', state=NORMAL)
        button9.config(text='', state=NORMAL)
        L1 = ['', '', '']    # vidé la ligne 1
        L2 = ['', '', '']    # vidé la ligne 2
        L3 = ['', '', '']    # vidé la ligne 3
        C1 = ['', '', '']    # vidé  column 1
        C2 = ['', '', '']    # vidé  column 2
        C3 = ['', '', '']    # vidé  column 3
        G1 = ['', '', '']    #vidé diagonale 1
        G2 = ['', '', '']    #vidé diagonale 2

        imp1.config(image=img1)  # image pour affiche état des joueur 1 dans état en jeu
        imp2.config(image=img1)  # image pour affiche état des joueur 2 dans état en jeu
        wnr.config(text='')       # vidé le Un message de félicitations pour joueur 1
        lsr.config(text='')       # vidé le Un message de félicitations pour joueur 2

def ChangeColor(event):
    p1.config(highlightbackground='black', highlightthicknes=1)
    p2.config(highlightbackground='black', highlightthicknes=1)

etatWedgets = 1        # etat des wedgest  1 = ACTIVE, 0 = DESACTIVE (si etatWedgets =0 --> le jeu active)

frame1 = Frame(Mafenetre,highlightbackground='black', highlightthicknes=3)
frame1 . place(x=10,y=10, height=120, width=616)           # placer sur la fenêtre

frame2 = Frame(Mafenetre,highlightbackground='black', highlightthicknes=3)
frame2 . place(x=10,y=135, height=400, width=616)            # placer sur la fenêtre

frame3 = Frame(frame2, highlightbackground='blue', highlightthicknes=3)
frame3 . place(x=5,y=12.3, height=299.5, width=145)

frame4 = Frame(frame2, highlightbackground='green', highlightthicknes=3)
frame4 . place(x=460,y=12.3, height=299.5, width=145)

frame5 = Frame(frame2, highlightbackground='black', highlightthicknes=3)
frame5 . place(x=5,y=320, height=70, width=600)

var = StringVar()
var . set('Chaque joueur choisit une forme de jeton. A tour de rôle, les joueurs placent un de leurs\n'
          ' jetons dans une case du quadrillage. Le but est d’être le premier à compléter une rangée \n'
          ' des ses trois poins horizontalement, verticalement ou disgonale.')

regle_jeu = Label(frame5,text='Règle du jeu: ' ,justify=LEFT,font=('Arial Black',13))
regle_jeu . place(x=0,y=0)
rg = Label(frame5,textvariable=var,justify=LEFT)
rg . place(x=120,y=7)

JR01 = Label(frame3,text='Player One: ', font=('',15) )
JR01 . place(x=1,y=1)   # Label pour affiche le nom de joueur 1
ZP1 = Entry(frame3 ,highlightbackground='black', highlightthicknes=1,fg='blue',justify=CENTER,font=('Arial Black',13))
ZP1 . place(x=20,y=30,width=100,height=20)  # zones de saisie nom joueur 1
ZP1 . config(state=DISABLED)

JR02 = Label(frame4,text='Player Two: ', font=('',15) )
JR02 . place(x=1,y=1)
ZP2 = Entry(frame4 ,highlightbackground='black', highlightthicknes=1,fg='green',justify=CENTER,font=('Arial Black',13))
ZP2 . place(x=20,y=30,width=100,height=20)
ZP2 . config(state=DISABLED)


img1 = PhotoImage(file='Images/nrlm.png')       # image no winner no loser
img2 = PhotoImage(file='Images/loser.png')     # image loser
img3 = PhotoImage(file='Images/winner.png')   # image winner
img = PhotoImage(file='Images/BG.PNG')       #image vide

imp1 = Label(frame3,image=img,bd=0)
imp1 . place(x=5,y=70,width=130,height=150)

imp2 = Label(frame4,image=img,bd=0)
imp2 . place(x=5,y=70,width=130,height=150)

SCP1 = Label(frame3,text='SCORE: ', fg='blue')
SCP1 . place(x=15,y=270)     # score player one
ZSCP1 = Entry(frame3 ,highlightbackground='blue', highlightthicknes=1)
ZSCP1 . place(x=65,y=270,width=50)   # zone de saise score player one
ZSCP1 . config(state=DISABLED)

SCP2 = Label(frame4,text='SCORE: ', fg='green')
SCP2 . place(x=15,y=270)   # score player two
ZSCP2 = Entry(frame4 ,highlightbackground='green', highlightthicknes=1)
ZSCP2 . place(x=65,y=270,width=50)  # zone de saise score player two
ZSCP2 . config(state=DISABLED)

SCORE1=0      # la valeur par defaut de la zone de score qui existe dans frame 3
SCORE2=0        # la valeur par defaut de la zone de score qui existe dans frame 4

wnr = Label(frame3,text='',font=('Arial Black',10),justify=CENTER,width=14)
wnr . place(x=5,y=220) # pour msg dans la fin de jeu pour player one

lsr = Label(frame4,text='',font=('Arial Black',10),justify=CENTER,width=14)
lsr . place(x=5,y=220)  # pour msg dans la fin de jeu pour player two


lbl = Label(frame1, text='Players Name :').place(x=2,y=2)

player1 = Label(frame1, text='Player One :').place(x=20,y=30)
player2 = Label(frame1, text='Player Two :').place(x=20,y=65)


# La méthode bind() permet de lier un événement avec une fonction :

p1 = Entry(frame1,highlightbackground='black', highlightthicknes=1)
p1.place(x=100, y=30)    # p1 --> zone de saisie le nom de joueur 1
p1.bind('<Button-1>', ChangeColor)

p2 = Entry(frame1,highlightbackground='black', highlightthicknes=1)
p2.place(x=100, y=65)     # p2 --> zone de saisie le nom de joueur 2
p2.bind('<Button-1>', ChangeColor)

SymbolPlayer1 = Label(frame1, text='Symbol :').place(x=470,y=30)
SymbolPlayer2 = Label(frame1, text='Symbol :').place(x=470,y=65)

XO1 = ttk.Combobox(frame1,values=['X','O'],width=5)  # liste pour choisir X ou O pour joueur 1
XO1 . place(x=535, y=30)
XO1 . current(0)        # la valeur par defaut est la valeur qui est dans l'index 0 (X)

XO2 = ttk.Combobox(frame1,values=['X','O'],width=5)   # liste pour choisir X ou O pour joueur 1
XO2 . place(x=535, y=65)
XO2 . current(1)         # la valeur par defaut est la valeur qui est dans l'index 1 (O)

Buttuonplay = Button(frame1, text = 'Jouer', fg='#0D1386', command=go,font=('Arial Black',8))
Buttuonplay . place(x=230, y= 85, width=60)       # Buttuonplay ---> bouton Jouer
ButtuonReset = Button(frame1, text = 'Annuler', fg='#A11411', command=reset,font=('Arial Black',8))
ButtuonReset . place(x=310, y= 85, width=60)      # ButtuonReset ---> bouton Annuler
ButtonRecommencer=Button(frame1,text='Recommencer',fg='#1B740B',command=Recommancer,font=('Arial Black',8))
ButtonRecommencer . place(x=390, y=85)             # ButtonRecommencer ---> bouton Recommencer

temp = 1  # tour de jeu par defaut le joueur qui joue avec X qui est jouer première

L1 = ['','','']   # ligne 1 de la grille
L2 = ['','','']   # ligne 2 de la grille
L3 = ['','','']   # ligne 3 de la grille

C1 = ['','','']  # column 1 de la grille
C2 = ['','','']  # column 2 de la grille
C3 = ['','','']  # column 3 de la grille

G1 = ['','','']     # diagonale 1 de la grille
G2 = ['','','']     # diagonale 1 de la grille


Canevas = Canvas(frame2, bg="white")
Canevas.place(x=152, y=10, width=304, height=304)

# ici on créer les lignes qui délimite les colones et les cases
Canevas.create_line(0, 100, 300, 100, fill="red", width=4)
Canevas.create_line(0, 200, 300, 200, fill="red", width=4)
Canevas.create_line(0, 300, 300, 300, fill="red", width=4)
Canevas.create_line(0, 3, 300, 3, fill="red", width=4)

Canevas.create_line(3, 300, 300, -100000, fill="red", width=4)
Canevas.create_line(100, 300, 300, -100000, fill="red", width=4)
Canevas.create_line(200, 300, 300, -100000, fill="red", width=4)
Canevas.create_line(300, 302, 300, -100000, fill="red", width=4)

button1 = Button(frame2,bg='red',text='',font=('',60), state=DISABLED, command=check1)
button1 . place(x=157, y=15, height=93.5, width=94)

button2 = Button(frame2, bg='red', text='',font=('',60), state=DISABLED, command=check2)
button2 . place(x=254, y=15, height=93.5, width=98)

button3 = Button(frame2,bg='red',fg='white',text='', font=('',60), state=DISABLED, command=check3)
button3 . place(x=354, y=15, height=93.5, width=96)

button4 = Button(frame2,bg='red',text='', font=('',60), state=DISABLED, command=check4)
button4 . place(x=157, y=112, height=96, width=94)

button5 = Button(frame2, bg='red', text='',font=('',60) , state=DISABLED, command=check5)
button5 . place(x=254, y=112, height=96, width=98)

button6 = Button(frame2,bg='red',fg='white',text='', font=('',60), state=DISABLED, command=check6)
button6 . place(x=354, y=112, height=96, width=96)

button7 = Button(frame2,bg='red',text='', font=('',60), state=DISABLED, command=check7)
button7 . place(x=157, y=212, height=96, width=94)

button8 = Button(frame2, bg='red', text='',font=('',60), state=DISABLED, command=check8)
button8 . place(x=254, y=212, height=96, width=98)

button9 = Button(frame2,bg='red',fg='white',text='', font=('',60), state=DISABLED, command=check9)
button9 . place(x=354, y=212, height=96, width=96)

qtr = Button(Mafenetre,text='Quitter',fg='red',font=('Arial Black',10), command=quitter)
qtr.place(x=10,y=538,width=80,height=30)

Jact = Label(Mafenetre,text='*Rouge:   le jeu est désactive', fg='red').place(x=250,y=540) # jeu active
Jdesct = Label(Mafenetre,text='*Noir:   le jeu est active').place(x=470,y=540)  # jeu désactive

Mafenetre . mainloop()      # le gestionnaire d'événements