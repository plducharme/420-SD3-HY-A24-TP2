import math

from PySide6.QtCore import QPoint, QTimer, Qt, QRect
from PySide6.QtGui import QPixmap, QColor, QPainter, QPen, QColorConstants, QBrush
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout

from random import randint, choice


class RefrAction(QMainWindow):
    def __init__(self):
        super().__init__()

        # Le QTimer appelera la méthode boucle_jeu toutes les 200 ms
        self.jeu = JeuRefrAction(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.jeu.boucle_jeu)
        self.timer.start(200)



class Division:

    def __init__(self):
        self.position = QPoint(400, 200)


class SourceLumineuse:

    def __init__(self, position: QPoint, angle: float):
        pass


class JeuRefrAction:

    DEBUT_TOUR = 0
    FIN_TOUR = 1
    FIN_PARTIE = 2


    def __init__(self, vue: RefrAction):
        pass

    def nouveau_tour(self):
        pass

    def boucle_jeu(self):
        match self.etat:

            case JeuRefrAction.DEBUT_TOUR:
                # dessiner
                pass
            case JeuRefrAction.FIN_TOUR:
                # dessiner
                pass
            case JeuRefrAction.TERMINE:
                # dessiner
                pass

    def jouer_tour(self):
        pass

    def calcul_score(self):
        pass

    def dessiner_fond_ecran(self):
        pass

    def dessiner_division(self):
        pass

    def dessiner_milieu_incident(self):
        pass

    def dessiner_milieu_refracte(self):
        pass

    def dessiner_source_lumineuse(self):
        pass

    def dessiner_rayon_refracte(self):
        pass

    def dessiner_cible(self):
        pass

    def dessiner_hud(self):
        pass

    def afficher_ecran_fin(self):
        pass

    # Classe interne représentant un milieu
    # Doit être utilisée de façon statique
    # Ne pas modifier (à moins que vous vouliez changer les couleurs)
    class Milieu:

        def __init__(self, indice_refraction: float, nom: str, couleur: QColor):
            self.indice_refraction = indice_refraction
            self.nom = nom
            self.couleur = couleur

        @staticmethod
        def glace():
            return JeuRefrAction.Milieu(1.31, "Glace", QColor(173, 173, 204))

        @staticmethod
        def eau():
            return JeuRefrAction.Milieu(1.33, "Eau", QColor(50, 50, 227))

        @staticmethod
        def ethanol():
            return JeuRefrAction.Milieu(1.36, "Ethanol", QColor(91, 91, 140))

        @staticmethod
        def glycerine():
            return JeuRefrAction.Milieu(1.47, "Glycerine", QColor(108, 115, 29))

        @staticmethod
        def diamant():
            return JeuRefrAction.Milieu(2.42, "Diamant", QColor(87, 161, 143))

        @staticmethod
        def huile_minerale():
            return JeuRefrAction.Milieu(1.47, "Huile minérale", QColor(145, 166, 113))

        @staticmethod
        def air():
            return JeuRefrAction.Milieu(1.00, "Air", QColor(111, 112, 103))





app = QApplication()
refraction = RefrAction()
refraction.show()
app.exec()