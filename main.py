# -*- coding: utf-8 -*- 
#                                                      #
#  Projet final : SPECTRES IR                          #
#                                                      #
#  Clémence Vast & Jérome Cazelles                    #
#                                                      #
#                                                      #
######****** Lycée Chaptal 2016 - PCSI B ********#######





#********* MODULES NECESSAIRES ***********************************
from tkinter import*
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from tkinter.messagebox import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter.filedialog
import webbrowser

TITLE_FONT = ("Helvetica", 18, "bold")



#******** Couleurs TKINTER ***************************************
COLORS= ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff','navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray','light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue','blue','dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue','light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green','dark sea green', 'sea green', 'medium sea green', 'light sea green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green','indian red', 'saddle brown', 'sandy brown','dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink','snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2','PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4','LemonChiffon2', 'LemonChiffon3']




#*********** DEBUT DU PROGRAMME *********************************

class SampleApp(Tk):
    
    """ Programme permettant de lire les spectres IR au format JDX et permettant d'analyser
les différentes fonctions s'affichant dans ce type de spectres. Créé par Jérome Cazelles et
Clémence Vast. Lycée Chaptal. 2016"""

    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        
        Tk.wm_title(self, "Chimimaxx")
        Tk.iconbitmap(self)#, default="logo.ico")
        
        self.geometry("1270x700")
        container = Frame(self)        # le container permet de stocker différents "Frames" les uns sur les autres avec celui que l'on veut voir au dessus
        self.frame = Frame(*args)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        #Fonction pour sélectionner la classe à afficher et lui donner ses caractéristiques
        for F in (StartPage, PageSpectre, PageInformation, PageAide, PageFonction, PageTableau1, PageTableau2, PageTableauSpectre1,PageTableauSpectre2):
            page_name = F.__name__ 
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.config(bg='lemon chiffon')
            frame.grid(row=0, column=0, sticky="nsew")

        
        self.addMenu()#créer un menu
        self.show_frame("StartPage") #afficher la page d'accueil

        
    def addMenu(self): #Fonction du menu en haut
        """ Menu pour aider l'utilisateur """
        self.menu = Menu(self.frame)
        Tk.config(self,menu=self.menu)
        self.menu1= Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Fichier", menu=self.menu1)
        self.menu1.add_command(label="Accueil", command= lambda: self.show_frame("StartPage"))
        self.menu1.add_command(label="Analyser un spectre", command=lambda: self.show_frame("PageSpectre"))
        self.menu1.add_command(label="Informations Molécules", command= lambda: self.show_frame("PageInformation"))
        self.menu1.add_command(label="Fonctions Chimiques", command= lambda: self.show_frame("PageFonction"))
        self.menu1.add_command(label="Aide", command= lambda: self.show_frame("PageAide"))
        self.menu1.add_separator()
        self.menu1.add_command(label="Quitter", command=Fermer)

        self.menu2 = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Tableaux", menu=self.menu2)
        self.menu2.add_command(label="Tableau périodique simple", command= lambda: self.show_frame("PageTableau1"))
        self.menu2.add_command(label="Tableau périodique fantaisie", command= lambda: self.show_frame("PageTableau2"))
        self.menu2.add_command(label="Les différentes fonctions", command= lambda: self.show_frame("PageTableauSpectre1"))
        self.menu2.add_command(label="RMN", command= lambda: self.show_frame("PageTableauSpectre2"))

        self.menu3 = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Aide", menu=self.menu3)
        self.menu3.add_command(label="A propos", command=About)


    def show_frame(self, page_name):
        '''Affiche la page selon le nom donné'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(Frame):
    """Page d'accueil de l'interface graphique"""

    def __init__(self, parent, controller):
        
        Frame.__init__(self, parent)
        self.controller = controller
        
        texte=Label(self,text="THE SPECTROR",font=("comic",30),bg="PeachPuff2") 
        texte.grid(row=10,column=0)
        
        #Fond d'écran
        self.photox=PhotoImage(file='fondecprinc2.gif')
        fondec=Label(self,image=self.photox)
        fondec.place(x=0,y=0,relwidth=1,relheight=1)
        
        #Photos
        self.photo1 = PhotoImage(file='Chimie.gif')
        self.photo2 = PhotoImage(file='Chimie2.gif')
        self.photo3 = PhotoImage(file='Chimie3.gif')
        
        #Boutons Texte (TXT)
        BoutonSpectre=Button(self, text="   SPECTRE   ", bg='pale turquoise',font=("Helvetica", 14, "bold"), command=lambda: controller.show_frame("PageSpectre"))
        BoutonInformationTXT=Button(self, text="  INFOS SUR LES MOLECULES ",bg='medium sea green', command=lambda: controller.show_frame("PageInformation"))
        BoutonInformation=Button(self,bg='medium sea green', image=self.photo2, command=lambda: controller.show_frame("PageInformation"))
        BoutonFonctionTXT=Button(self ,text="       FONCTIONS CHIMIQUES       ", bg='dark turquoise', command=lambda: controller.show_frame("PageFonction")) 
        BoutonFonction=Button(self, bg='dark turquoise', image=self.photo1, command=lambda: controller.show_frame("PageFonction")) 
        BoutonAideTXT=Button(self,text="                                 AIDE                                 ", bg='red', command=lambda: controller.show_frame("PageAide")) 
        BoutonAide=Button(self, bg='red', image=self.photo3, command=lambda: controller.show_frame("PageAide")) 
                
        #Activation des boutons
        BoutonSpectre.grid(row=0,column=1000, padx=60, pady=75)
        BoutonInformationTXT.grid(row=650,column=0, padx=55, pady=5)
        BoutonInformation.grid(row=651,column=0, padx=120, rowspan=40)
        BoutonFonctionTXT.grid(row=650,column=1000, padx=55, pady=5)
        BoutonFonction.grid(row=660,column=1000, padx=140, rowspan=40)
        BoutonAideTXT.grid(row=650,column=4000, padx=55)
        BoutonAide.grid(row=650,column=4000, padx=120, pady=35, rowspan=40)


class PageFonction(Frame):
    """Informations sur les fonctions chimiques et tableaux périodiques"""
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        #Fond d'écran
        self.photox=PhotoImage(file='fondecfct3.gif')
        fondec=Label(self,image=self.photox)
        fondec.place(x=0,y=0,relwidth=1,relheight=1)
        
        #Texte
        label = Label(self, text="Fonctions chimiques", bg= "pale turquoise", font=("Helvetica", 16, "bold"))
        label.grid(row=0,column=0, pady=5)
        
        label2= Label(self, text="Les fonctions principales que l'on retrouve sur le spectre", bg="Dark turquoise", font=("Helvetica", 11, "bold italic"))
        label2.grid(row=600, column=0, rowspan=2)
        
        label3= Label(self, text="Si vous souhaitez avoir plus d'informations", bg="Dark turquoise", font=("Helvetica", 11, "bold italic"))
        label3.grid(row=100, column=2)
        
        label4= Label(self, text="A propos des déplacements chimiques", bg="Dark turquoise", font=("Helvetica", 11, "bold italic"))
        label4.grid(row=601, column=2)
        
        #Boutons
        button = Button(self, text="Retour", bg="lime green", command=lambda: controller.show_frame("StartPage"))
        button.grid(row=100,column=0, padx=20, pady=4)
        
        button = Button(self, text="Plus d'information", bg='medium sea green', command=lambda: controller.show_frame("PageInformation"))
        button.grid(row=102,column=0, padx=0, pady=4)
        
        button = Button(self, text="Aide", bg= 'dark turquoise', command=lambda: controller.show_frame("PageAide"))
        button.grid(row=101,column=0, padx=0, pady=4)
        
        button = Button(self, text="\n        VERS LES SPECTRES      \n", bg='indian red', font=("Helvetica", 15, "bold"), command=lambda: controller.show_frame("PageSpectre"))
        button.grid(row=170,column=0, padx=0, pady=4)
        
        #Boutons photos
        self.photo0=PhotoImage(file='tableau_fct.gif')
        button = Button(self, image=self.photo0, command=lambda: controller.show_frame("PageTableauSpectre1"))
        button.grid(row=100,column=2, padx=20, pady=40, rowspan=200)
        
        self.photo1=PhotoImage(file='RMN.gif')
        button = Button(self, image=self.photo1, command=lambda: controller.show_frame("PageTableauSpectre2"))
        button.grid(row=602,column=2,  padx=40, pady=10)
        
        #Photos
        self.photo=PhotoImage(file='obs1_2.gif')
        photo=Label(self, image=self.photo) 
        photo.grid(row=600,column=0, padx=70, rowspan=20)
        
        

class PageAide(Frame):
    """Page d'aide à l'utilisateur et liens vers des sites utiles"""
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        #Fond d'écran
        self.photox=PhotoImage(file='fondecfct3.gif')
        fondec=Label(self,image=self.photox)
        fondec.place(x=0,y=0,relwidth=1,relheight=1)
        
        #Label titre
        label0 = Label(self, text="Aide", bg="PeachPuff2", font=TITLE_FONT)
        label0.grid(row=0,column=1, padx=10, pady=10)
        
        label02= Label(self, text="Quelques liens à propos des spectres IR \n Cliquez sur le nom du site pour aller vers la page web", bg="PeachPuff2", font=("Helvetica", 9,'bold'))
        label02.grid(row=20, column=1, padx=5, pady=30)
        
        label03= Label(self, text="Tableaux périodiques", bg="PeachPuff2", font=("Helvetica", 11,'bold'))
        label03.grid(row=120, column=1, padx=5, pady=30)

        #Label colonne1
        label11= Label(self, text="  Spectrothèque : Integrated Spectral Data Base System for Organic Compounds. Top site !! ;-)" , bg="ghost white",relief=RAISED)
        label11.grid(row=100, column=1, padx=3)
        label11.bind("<Button-1>", self.callback1)
        
        label12= Label(self, text="     Problèmes de spectroscopie en ligne : Spectroscopie IR et RMN : WebSpectra Top site !! ;-)" , bg="ghost white",relief=RAISED)
        label12.grid(row=101, column=1, padx=3, pady=5)
        label12.bind("<Button-1>", self.callback2)
        
        label13= Label(self, text="Organic Synthesis (le plus célébre des recueils de procédures expérimentales) MégaTop site !! ;-)" , bg="ghost white",relief=RAISED)
        label13.grid(row=102, column=1, padx=3)
        label13.bind("<Button-1>", self.callback)

        #Label colonne2
        texte0= Label(self, text="Quel est le but de cette application? ", bg="PeachPuff2", font=("Helvetica", 11, "bold"))
        texte0.grid(row=102,column=2, padx=5, pady=5)
        
        texte1=Label(self,text="Les fichiers JDX sont des fichiers divers principalement associés \n avec JSpell UNICODE Dictionary ou avec JCAMP Chemical Spectroscopic Data. Cette application \n vous permettra d'afficher les spectres IR de ces fichiers. \n\n Principe de la Spectroscopie Infrarouge : \n\n Les molécules subissent des mouvements de vibration internes (d'élongation et de déformation).\n Quand une lumière IR traverse un échantillon, certaines liaisons\n absorbent de l'énergie pour changer de fréquence de vibration,\n faisant apparaître des bandes dans le spectre.\n Le nombre d'onde σ (m-1) est l'inverse de la longueur d'onde λ.\n\n Le spectre infrarouge représente la transmittance en fonction du nombre d'onde.\n\n L'analyse des spectres montre\n que plus la liaison est forte, plus le nombre d'onde\n d'absorption σ est élevé.",justify='left', bg="ghost white")
        texte1.grid(row=25,column=2,rowspan=200, padx=100)
        
        #Boutons
        button = Button(self, text="Retour", bg="lime green", command=lambda: controller.show_frame("StartPage"))
        button.grid(row=20,column=0, padx=20, pady=0)
        
        self.photo1 = PhotoImage(file='tablper1.gif')
        self.photo2 = PhotoImage(file='tablper2.gif')
        
        BoutonTableau1=Button(self,bg='medium sea green', image=self.photo1, command=lambda: controller.show_frame("PageTableau1"))
        BoutonTableau1.grid(row=130,column=1, pady=20, rowspan=30)
        
        BoutonTableau1=Button(self,bg='medium sea green', image=self.photo2, command=lambda: controller.show_frame("PageTableau2"))
        BoutonTableau1.grid(row=160,column=1)
            
    def callback(self,event): #Ces fonctions permettent d'envoyer vers un navigateur Web au clic sur le lien
        webbrowser.open_new(r"http://jymagna.com/")
        
    def callback1(self,event):
        webbrowser.open_new(r"http://sdbs.db.aist.go.jp/")
        
    def callback2(self,event):
        webbrowser.open_new(r"http://www.chem.ucla.edu/~webspectra/")
        
    
class PageTableau1(Frame):
    """Tableau périodique des éléments simple"""
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        #Fond d'écran
        self.photox=PhotoImage(file='fondecfct3.gif')
        fondec=Label(self,image=self.photox)
        fondec.place(x=0,y=0,relwidth=1,relheight=1)

        #Différents Widgets        
        label= Label(self, text="Tableau périodique", bg="PeachPuff2", font=TITLE_FONT)
        label.grid(row=0,column=0, padx=5, pady=5)
        
        button = Button(self, text="Retour", bg="lime green", command=lambda: controller.show_frame("PageAide"))
        button.grid(row=20,column=0, padx=20, pady=20)
        
        self.photo=PhotoImage(file='tablpergrd1.gif')
        photo=Label(self, image=self.photo) 
        photo.grid(row=600,column=0, padx=250)

class PageTableau2(Frame):
    """Tableau périodique des éléments fantaisie"""
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        #Fond d'écran
        self.photox=PhotoImage(file='fondecfct3.gif')
        fondec=Label(self,image=self.photox)
        fondec.place(x=0,y=0,relwidth=1,relheight=1)

        #Différents Widgets        
        label= Label(self, text="Tableau périodique", bg="PeachPuff2", font=TITLE_FONT)
        label.grid(row=0,column=0, padx=5, pady=5)
        
        button = Button(self, text="Retour", bg="lime green", command=lambda: controller.show_frame("PageAide"))
        button.grid(row=20,column=0, padx=20, pady=20)
        
        self.photo=PhotoImage(file='tablpergrd2.gif')
        photo=Label(self, image=self.photo) 
        photo.grid(row=600,column=0, padx=250)

class PageTableauSpectre1(Frame):
    """Tableau avec les liaisons possibles et leurs nombres d'ondes"""
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        #Fond d'écran
        self.photox=PhotoImage(file='fondecfct3.gif')
        fondec=Label(self,image=self.photox)
        fondec.place(x=0,y=0,relwidth=1,relheight=1)
        
        #Différents Widgets
        label= Label(self, text="Plus de détails sur les fonctions", bg="PeachPuff2", font=TITLE_FONT)
        label.grid(row=0,column=0, padx=5, pady=5)
        
        button = Button(self, text="Retour", bg="lime green", command=lambda: controller.show_frame("PageFonction"))
        button.grid(row=20,column=0, padx=20, pady=20)
        
        self.photo=PhotoImage(file='tableau_fct_grd.gif')
        photo=Label(self, image=self.photo) 
        photo.grid(row=600,column=0, padx=250)


class PageTableauSpectre2(Frame):
    """Tableau avec les liaisons possibles sur un spectre RMN : informations bonus"""
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        #Fond d'écran
        self.photox=PhotoImage(file='fondecfct3.gif')
        fondec=Label(self,image=self.photox)
        fondec.place(x=0,y=0,relwidth=1,relheight=1)

        #Différents Widgets
        label= Label(self, text="Quelques informations sur la RMN", bg="PeachPuff2", font=TITLE_FONT)
        label.grid(row=0,column=0, padx=5, pady=5)
        
        button = Button(self, text="Retour", bg="lime green", command=lambda: controller.show_frame("PageFonction"))
        button.grid(row=20,column=0, padx=20, pady=20)
        
        self.photo=PhotoImage(file='RMN_grd.gif')
        photo=Label(self, image=self.photo) 
        photo.grid(row=600,column=0, padx=420)
        

class PageSpectre(Frame):
    """Page permettant l'affichage d'un spectre au choix et l'analyse de ses bandes"""

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.file_opt = options = {}
        options['filetypes']=[('JDX Files','.jdx')]
        options['title']='QUEL SPECTRE VEUX-TU OUVRIR ?'
        
        #Fond d'écran
        self.photox=PhotoImage(file='fondecfct3.gif')
        fondec=Label(self,image=self.photox)
        fondec.place(x=0,y=0,relwidth=1,relheight=1)
            
        #Boutons
        button = Button(self, text="\n  Retour à la page d'accueil  \n",font=("Helvetica", 11, "bold"), bg='seashell3', command=lambda: controller.show_frame("StartPage"))
        button.grid(row=10, column=1, padx=5, pady=30)
        buttonfich = Button(self, text="\n  Ouvrir un spectre JDX  \n", bg='pale turquoise',font=("Helvetica", 11, "bold"), command=self.askopenfilename)
        buttonfich.grid(row=70, column=1, pady=30)

        #Texte
        texteb=Label(self,text="A quelle fonction correspond cette bande ?", bg='indian red', font=("Helvetica", 12, "bold"))
        texteb.grid(row=10,column=2,columnspan=4, sticky='w')
        texteb1=Label(self,text="          Largeur de la bande         Min :                                1/cm   Max:                                1/cm     ", bg='indian red', font=("Helvetica", 10, "bold"))
        texteb1.grid(row=11,column=1, columnspan=5, padx=20, pady=20)
                     
        #Variables utilisées
        self.varF=IntVar()
        self.varF.set(0)
        self.varm=IntVar()
        self.varm.set(0)
        self.varf=IntVar()
        self.varf.set(0)
        case1=Checkbutton(self,text="      Fort                 ", variable=self.varF, bg='indian red', font=("Helvetica", 8, "bold"), relief=GROOVE, onvalue=1, offvalue=0).grid(row=12,column=2, sticky='w')
        case2=Checkbutton(self,text="      Moyen            ", variable=self.varm, bg='indian red', font=("Helvetica", 8, "bold"), relief=GROOVE, onvalue=1, offvalue=0).grid(row=13,column=2, sticky='w')
        case3=Checkbutton(self,text="       Faible             ", variable=self.varf, bg='indian red', font=("Helvetica", 8, "bold"), relief=GROOVE, onvalue=1, offvalue=0).grid(row=14,column=2, sticky='w')
        
        self.var2=IntVar()
        self.var2.set(0)
        case4=Radiobutton(self,text="    1 bande           ",variable=self.var2,value=1, bg='seashell4', font=("Helvetica", 8, "bold"), relief=RAISED).grid(row=22,column=2, sticky='w')
        case5=Radiobutton(self,text="    2 bandes         ",variable=self.var2,value=2,  bg='seashell4', font=("Helvetica", 8, "bold"), relief=RAISED).grid(row=23,column=2, sticky='w')
        case6=Radiobutton(self,text="+ de 2 bandes    ",variable=self.var2,value=3,  bg='seashell4', font=("Helvetica", 8, "bold"), relief=RAISED).grid(row=24,column=2, sticky='w')

        self.var3=IntVar()
        self.var3.set(0)
        fine=Radiobutton(self,text="    Bande fine          ",font=("Helvetica", 8, "bold"), bg='seashell3', variable=self.var3, value=1, relief=RAISED).grid(row=12,column=3, sticky='w')
        large=Radiobutton(self,text="     Bande large       ", font=("Helvetica", 8, "bold"), bg='seashell3', variable=self.var3, value=2, relief=RAISED).grid(row=13,column=3, sticky='w')
        
        self.entree1=Entry(self)
        self.entree1.grid(row=11,column=2, sticky='w', padx=5)
        self.entree2=Entry(self)
        self.entree2.grid(row=11,column=3, sticky='e', padx=10)
                
        boutontest=Button(self, text="Rechercher",command=self.quelband).grid(row=18,column=3)
        self.show_plot=False
        self.show_inf=False

    def askopenfilename(self): #Ouvre une fenêtre et permet de sélectionner le fichier spectre à afficher
        filename=tkinter.filedialog.askopenfilename(**self.file_opt)
        if filename:
            li=list() #crée une liste
            f=open(filename,'r') #ouvre le fichier
            li=f.readlines() #lit toutes les lignes du fichier et les met dans la liste li
            f.close() #ferme le fichier
            self.donneesgraph(li)
            
    def nommolecule(self,l): #Récupère le nom de la molécule dans le fichier spectre
        li=l
        r=li[0].strip("##TITLE= ")
        r=r.strip(" ")
        return r 
        
    
    def datatabl(self,n,lo): #Récupère les points désirés dans le fichier spectre
        li=lo
        l=[]
        for i in range(37,len(li)-2) :
            m=li[i].strip('\n')
            p=m.split(" ",5)
            l.append(float(p[n]))
        return l

    def exploit(self,a,b,fort,moyen,faible,nbbandes,largeur): #Fonction d'analyse des points sélectionnés
        l=[]
        R="Rentrez plus \n d'informations svp" #initialise la réponse
        if nbbandes==2: # si on int(a) deux bandes
            if moyen==1 or fort==1: # si Moyen est coché
                if (int(a)>=2680 and int(b)<=2900):
                    R="Ctrigo lié à un H, aldéhyde"
                    l.append(R)
                if (int(a)>=3100 and int(b)<=3510):
                    R="NH amine primaire"
                    l.append(R)
            if fort==1: #si Fort est coché
                if (int(a)>=1700 and int(b)<=1840):
                    R="C=O anhydride"
                    l.append(R)
                if(int(a)>=1510 and int(b)<=1580) or (int(a)>=1325 and int(b)<=1365):
                    R="N=O"
                    l.append(R)
                if (int(a)>=1365 and int(b)<=1385):
                    R="Ctetra lié à un H et à un CH3"
                    l.append(R)

        if nbbandes==1: #si on int(a) une bande
            if moyen==1: #si Moyen est coché
                if largeur==1 or (int(a)>=3580 and int(b)<=3670):
                    R="OH alcool libre"
                    l.append(R)
                if (int(a)>=3100 and int(b)<=3370):
                    R="NH amine secondaire ou NH imine"
                    l.append(R)
                if (int(a)>=3000 and int(b)<=3100):
                    if (int(a)>=3030 and int(b)<=3080):
                        R="Ctrig lié à un H, composé aromatique"
                        l.append(R)
                    else :
                        R="Ctrig lié à un H"
                        l.append(R)
                if (int(a)>=1625 and int(b)<=1685):
                    R="C=C"
                    l.append(R)
                if (int(a)>=1020 and int(b)<=1220):
                    R="C-N"
                    l.append(R)                    
            if (int(a)>=1450 and int(b)<=1600):
                R="C=C aromatique si 3 pics"
                l.append(R)

            if fort==1: #si F est coché
                if largeur==2 or (int(a)>=3200 and int(b)<=3400):
                    R="OH alcool lié"
                    l.append(R)
                if (int(a)>=3050 and int(b)<=3500):
                    R="NH amide"
                    l.append(R)
                if (int(a)>=2730 and int(b)<=3050):
                    R="Ctetra lié à un H"
                    l.append(R)
                if (int(a)>=1770 and int(b)<=1820):
                    R="C=O chlorure d'acide"
                    l.append(R)
                if (int(a)>=1700 and int(b)<=1740):
                    R="C=O ester"
                    l.append(R)
                if (int(a)>=1650 and int(b)<=1730):
                    R="C=O aldéhyde ou cétone"
                    l.append(R)
                if (int(a)>=1680 and int(b)<=1760):
                    R="C=O acide"
                    l.append(R)
                if (int(a)>=1650 and int(b)<=1700):
                    R="C=O amide"
                    l.append(R)
                if (int(a)>=1600 and int(b)<=1680):
                    R="C=N"
                    l.append(R)
                if (int(a)>=1415 and int(b)<=1470):
                    R="Ctetra lié à un H"
                    if R not in l:
                        l.append(R)
                if (int(a)>=1050 and int(b)<=1450):
                    R="C-O"
                    l.append(R)
                if (int(a)>=1250 and int(b)<=1310):
                    R="P=O"
                    l.append(R)
                if (int(a)>=1000 and int(b)<=1250):
                    R="C-C"
                    l.append(R)
                if (int(a)>=1000 and int(b)<=1040):
                    R="C-F"
                    l.append(R)

            if fort==1 or moyen==1: #Si fort ou moyen sont cochés
                if largeur==2 and (int(a)>=2500 and int(b)<=3200):
                    R="OH acide carboxylique"
                    l.append(R)
                if (int(a)>=2120 and int(b)<=2260):
                    R="C triple liaison N"
                    l.append(R)
                if (int(a)>=1560 and int(b)<=1640):
                    R="N-H amine ou amide"
                    l.append(R)
                if (int(a)>=2730 and int(b)<=3050):
                    R="Ctetra lié à un H"
                    if R not in l:
                        l.append(R)
                if largeur==2 or (int(a)>=3200 and int(b)<=3400):
                    R="OH alcool lié"
                    if R not in l:
                        l.append(R)
                        
            if (faible==1 or moyen==1) and (int(a)>=3300 and int(b)<=3310): #si faible ou moyen sont cochés
                R="Cdiag lié à un H"
                l.append(R)
            if faible==1 and (int(a)>=2100 and int(b)<=2250): #si seul faible est coché
                R="C=C"
                l.append(R)
        return [R,l]
    
    def donneesgraph(self,l): #Affiche le spectre sélectionné sur la fenetre Tkinter
        f = Figure(figsize=(7,6), dpi=78) #figsize =(largeur,hauteur), dpi=dimension du spectre (pourcents)
        a=f.add_subplot(111)
        a.plot(self.datatabl(0,l),self.datatabl(1,l),'-r')
        a.plot(self.datatabl(0,l),self.datatabl(2,l),'-r')
        a.plot(self.datatabl(0,l),self.datatabl(3,l),'-r')
        a.plot(self.datatabl(0,l),self.datatabl(4,l),'-r')
        a.plot(self.datatabl(0,l),self.datatabl(5,l),'-r')
        a.set_title("Spectre de "+self.nommolecule(l))
        a.set_xlabel("Nombre d'onde (en 1/cm)", fontsize=16)   
        a.set_ylabel("Transmittance en %", fontsize=16) 
        a.axis([0,4000,0,1])             
        a.grid()
        a.invert_xaxis()
        canvas= FigureCanvasTkAgg(f,master=self)
        if self.show_plot:
            canvas.get_tk_widget().grid_forget()
        if self.show_inf:
            repo=Label(self,text='', bg='black', width=50, height=9)
            repo.grid(row=151,column=9,columnspan=11, rowspan=300, pady=5, sticky='nsew')
        canvas.get_tk_widget().grid(row=0, column=6, rowspan=100, columnspan=30, padx=40, pady=10)
        self.toolbarframe=Frame(self)
        self.toolbarframe.grid(row=100,column=10,sticky='nw')

        self.toolbar = NavigationToolbar2Tk(canvas,self.toolbarframe)
        self.toolbar.grid(row=25,column=5,sticky='nw')

        self.show_plot=True
        self.var4=IntVar()
        self.var4.set(0)
        fine=Radiobutton(self,text="    Bande fine          ",font=("Helvetica", 9, "bold"), bg='seashell3', variable=self.var4, value=1, relief=RAISED).grid(row=151, padx=20, pady=10, column=6,sticky='w')
        large=Radiobutton(self,text="     Bande large       ", font=("Helvetica", 9, "bold"), bg='seashell3', variable=self.var4, value=2, relief=RAISED).grid(row=152, padx=20,column=6,sticky='w')

        def quelband_A(event):   #Récupère les données lors d'un clic sur le spectre et lance l'analyse de la bande choisie
            x1=event.xdata
            y1=event.ydata
            largeur=self.var4.get()
            fort,moyen,faible=0,0,0
            if 0.5<y1<=0.8:
                faible=1
            if 0.2<y1<=0.5:
                moyen=1
            if 0<y1<=0.2:
                fort=1
            a=x1-10
            b=x1+10
            nbbandes=1
            R,l=self.exploit(a,b,fort,moyen,faible,nbbandes,largeur)[0],self.exploit(a,b,fort,moyen,faible,nbbandes,largeur)[1]
            if len(l)>1:
                R=""
                for i in range(len(l)):
                    R+="\n"+l[i]
                
            repo=Label(self,text='', bg='black', width=50, height=9)
            repo.grid(row=151,column=9,columnspan=11, rowspan=300, pady=5, sticky='nsew')
            rep1=Label(self,text=R, bg='black', fg='snow',font=("Helvetica",16))
            rep1.grid(row=151,column=9,columnspan=11, rowspan=300, pady=5)
            self.show_inf=True
            
        c=f.canvas.mpl_connect('button_press_event',quelband_A)

    def quelband(self):    #Récupère les paramètres lors d'une analyse manuelle des bandes d'un spectre
        a=self.entree1.get()
        b=self.entree2.get()
        fort=self.varF.get()
        nbbandes=self.var2.get()
        moyen=self.varm.get()
        faible=self.varf.get()
        largeur=self.var3.get()
        R,l=self.exploit(a,b,fort,moyen,faible,nbbandes,largeur)[0],self.exploit(a,b,fort,moyen,faible,nbbandes,largeur)[1]

        if len(l)>1:
            R=""
            for i in range(len(l)):
                R+="\n"+l[i]
                
        repv=Label(self,text='', bg='black', width=50, height=9)
        repv.grid(row=25,column=2,columnspan=3, rowspan=300, pady=5)
        rep=Label(self,text=R, bg='black', fg='snow',font=("Helvetica",16))
        rep.grid(row=25,column=2,columnspan=3, rowspan=300, pady=5)


class PageInformation(Frame):
    """Informations sur les groupes des molécules en chimie"""

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        #Fond d'écran
        self.photox=PhotoImage(file='fondecfct3.gif')
        fondec=Label(self,image=self.photox)
        fondec.place(x=0,y=0,relwidth=1,relheight=1)
        
        #Label
        label = Label(self, text="Fonctions Détaillées", bg= "PeachPuff2", font=("Helvetica", 16, "bold"))
        label.grid(row=0,column=0, columnspan=5, padx=4,pady=4, sticky='w')
        
        #Boutons
        button = Button(self, text="Retour", bg= "lime green", command=lambda: controller.show_frame("StartPage"))
        button.grid(row=1,column=0,columnspan=5, padx=70, pady=10, sticky='nw')
        
        self.listed=["Halogénures d'alkyle","              Alcools            ",'             Amines             ','Aldéhydes et cétones',"Acides carboxyliques","               Esters               ","              Amides                ","              Alcanes                 ","              Alcènes                  ","              Alcynes               ","         Acides Sulfoniques       ","     Anhydrides d'acides     ","             Amidines             ","              Nitriles              ","             Peroxydes              "]
        #Listbox
        self.liste=Listbox(self, width=20)
        
        for i in range(len(self.listed)):    # Permet de construire une liste d'éléments et une scrollbar associée
            self.liste.insert(i,self.listed[i])
        self.liste.grid(row=3,column=0, sticky='nw', padx=10, pady=180)
        scrollbar=Scrollbar(self,width=15)
        scrollbar.grid(row=3,column=1, sticky='w')
        scrollbar.config(command=self.liste.yview)

        self.ff=["1.gif","2.gif","3.gif","4.gif","5.gif","6.gif","7.gif","8.gif","9.gif","10.gif","11.gif","12.gif","13.gif","14.gif","15.gif"]     
        self.liste.bind('<<ListboxSelect>>', self.onselect)

    def onselect(self,evt):     # Permet de sélectionner un élément de la listbox conçue plus haut
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.pf1=PhotoImage(file=self.ff[index])
        photof1=Label(self,image=self.pf1)
        photof1.grid(row=3,column=3,rowspan=100, padx=10, sticky='n')
        texte1=Label(self,text=self.listed[index],font=("Helvetica", 12, "bold"))
        texte1.grid(row=1,column=3, padx=5,rowspan=100, sticky='n')


## Definition des fonctions du menu **********************************************
def Fermer():
    if askyesno('Quitter', 'Etes-vous sûr de vouloir fermer ?'):
        showinfo('Quitter', 'Merci de votre visite, à bientôt !')
        app.destroy()
    else:
        showwarning('Quitter', 'Bonne continuation !')

def alert(): showinfo("alerte", "Bravo !")

def Affiche(): showinfo("Editer","Exemple d'un Menu : on pourra peut-être mettre des choses cools dans ces menus") 

def About(): showinfo("A propos", "Version 3.2.0 de Clemou et Jéjé") 


#****** Lancement du programme****************************************************
app = SampleApp()
app.mainloop()
