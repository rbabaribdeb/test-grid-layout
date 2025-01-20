from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit


def somme_moyenne(tab):
    somme =0
    for x in tab:
        somme = somme + int(x.text())
    moyenne = somme / len(tab)
    return somme, moyenne

def btn_charger_action():
    print("btn charger action")
def btn_sauvegarder_action():
    print("btn sauvegarder action")
def btn_analyser_action():
    print("btn analyser action")
    print(str(somme_moyenne(liste_scores)[0]))
    lbl_moyenne.setText("Moyenne : " + str(somme_moyenne(liste_scores)[1]))
    lbl_totalPoint.setText("Total : " + str(somme_moyenne(liste_scores)[0]))



app = QApplication([])
fen = QWidget()

# Créer un  Grid layout et l'associer a la fenetre
grid = QGridLayout()
fen.setLayout(grid)

grid.addWidget(QLabel("Nom_Joueur"),0,1)
grid.addWidget(QLabel("Points_Joueur"),0,2)

liste_nom    = []
liste_scores = []

for i in range(4):
    grid.addWidget(QLabel("Joueur " + str(i + 1)), i + 1, 0)
    liste_nom.append(QLineEdit())
    grid.addWidget(liste_nom[i], i + 1, 1)
    liste_scores.append(QLineEdit())
    grid.addWidget(liste_scores[i], i + 1, 2)

#######################################################

lbl_totalPoint = QLabel("total_point : 0")
grid.addWidget(lbl_totalPoint, 5, 1)
lbl_moyenne = QLabel("moyenne : 0")
grid.addWidget(lbl_moyenne, 5, 2)
lbl_gagnant = QLabel("gagnant : x")
grid.addWidget(lbl_gagnant, 6, 1)

btn_charger = QPushButton("Charger")
grid.addWidget(btn_charger, 7, 0)
btn_charger.clicked.connect(btn_charger_action)

btn_sauvegarde = QPushButton("Sauvegarde")
grid.addWidget(btn_sauvegarde, 7, 1)
btn_sauvegarde.clicked.connect(btn_sauvegarder_action)

btn_analyse = QPushButton("Analyser")
grid.addWidget(btn_analyse, 7, 2)
btn_analyse.clicked.connect(btn_analyser_action)

fen.show()
app.exec()