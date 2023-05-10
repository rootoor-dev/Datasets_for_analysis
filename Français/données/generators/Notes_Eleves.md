

# NOTES DES ELEVES D'UN LYCEE FICTIF nommé "Junior Olympia Academy"

## Langage naturel de génération

```
Générer un fichier Excel contenant 5 notes  aléatoires sur 20 (de type float ou Real) de 50 élèves d'une classe de Terminale en série scientifique dans les matières suivantes : Français, Histoire, Géographie, Mathématiques, Physique, Chimie, Informatique, EPS, SVT, Anglais, Musique et Arts Plastiques pendant les trois trimestres de l'année académique 2023.

Récommandations:
- la note minimale est 0.00,
- la note maximale est 20.00,
- il y a uniquement deux chiffres après la virgule,
- les nombres après la virgule sont 00, 25, 50 ou 75 si la note est strictement inférieure à 20 et 00 si elle est égale à 20.

```

## Code R de génération

Ce code générera un fichier Excel appelé "notes_eleves.xlsx" contenant les notes aléatoires des élèves. Chaque élève est identifié par un numéro, et les notes sont générées aléatoirement dans la plage de 0 à 20.

Ce code R met à jour la génération des notes en utilisant la fonction sample pour générer un nombre entier entre notes_min et notes_max. Ensuite, pour les notes strictement inférieures à notes_max, un chiffre décimal de 00, 25, 50 ou 75 est généré et ajouté à la note entière pour obtenir une note finale avec deux chiffres après la virgule. Pour les notes supérieures ou égales à notes_max, la partie décimale est fixée à 00.


```R
# Installation de la bibliothèque openxlsx si nécessaire
if (!requireNamespace("openxlsx", quietly = TRUE)) {
  install.packages("openxlsx")
}

# Chargement de la bibliothèque openxlsx
library(openxlsx)

# Définition des matières
matieres <- c('Français', 'Histoire', 'Géographie', 'Mathématiques', 'Physique', 'Chimie', 'Informatique', 'EPS', 'SVT', 'Anglais', 'Musique', 'Arts Plastiques')

# Définition du nombre d'élèves et des trimestres
nb_eleves <- 50
trimestres <- c('Trimestre 1', 'Trimestre 2', 'Trimestre 3')

# Génération des notes aléatoires pour chaque élève et chaque matière
notes_min <- 0.0
notes_max <- 20.0

# Création de la matrice de données
donnees <- matrix(nrow = nb_eleves, ncol = length(matieres) * length(trimestres) + 1)
colnames(donnees) <- c('Élève', outer(matieres, trimestres, paste, sep = ' '))

for (eleve in 1:nb_eleves) {
  ligne_notes <- c(paste('Élève', eleve))
  for (trimestre in trimestres) {
    for (matiere in matieres) {
      # Génération de 5 notes aléatoires sur 20
      note_entiere <- sample(notes_min:notes_max, 1)
      note_decimal <- 0
      if (note_entiere < notes_max) {
        note_decimal <- sample(c(0, 25, 50, 75), 1)
      }
      note <- note_entiere + note_decimal / 100
      ligne_notes <- c(ligne_notes, note)
    }
  }
  
  donnees[eleve, ] <- ligne_notes
}

# Création du fichier Excel
nom_fichier <- 'notes_eleves.xlsx'
write.xlsx(donnees, file = nom_fichier)

cat("Le fichier", nom_fichier, "a été généré avec succès.\n")

```

## Code Python de génération

Ce code générera un fichier Excel appelé "notes_eleves.xlsx" contenant 5 notes aléatoires sur 20 pour chaque élève et chaque matière sur les trois trimestres de l'année académique 2023. Chaque élève est identifié par un numéro, et les notes sont générées aléatoirement dans la plage de 0 à 20.

Ce code met à jour la génération des notes en utilisant la fonction randint pour générer un chiffre entier entre notes_min et notes_max. Ensuite, un chiffre décimal de 0, 25, 50 ou 75 est généré et ajouté à la note entière pour obtenir une note finale avec deux chiffres après la virgule.

En effet, 
Ce code met à jour la génération des notes en utilisant la fonction randint pour générer un chiffre entier entre notes_min et notes_max. Ensuite, pour les notes strictement inférieures à notes_max, un chiffre décimal de 00, 25, 50 ou 75 est généré et ajouté à la note entière pour obtenir une note finale avec deux chiffres après la virgule. Pour les notes supérieures ou égales à notes_max, la partie décimale est fixée à 00.

```Python
import openpyxl
from random import randint

# Création du classeur Excel
classeur = openpyxl.Workbook()
feuille = classeur.active

# En-têtes des colonnes
matieres = ['Français', 'Histoire', 'Géographie', 'Mathématiques', 'Physique', 'Chimie', 'Informatique', 'EPS', 'SVT', 'Anglais', 'Musique', 'Arts Plastiques']
trimestres = ['Trimestre 1', 'Trimestre 2', 'Trimestre 3']
feuille.append(['Élève'] + matieres * len(trimestres))

# Génération des notes aléatoires pour chaque élève et chaque matière
nb_eleves = 50
notes_min = 0.0
notes_max = 20.0

for eleve in range(1, nb_eleves + 1):
    ligne_notes = [f'Élève {eleve}']
    for trimestre in trimestres:
        for matiere in matieres:
            # Génération de 5 notes aléatoires sur 20
            note_entiere = randint(int(notes_min), int(notes_max))
            note_decimal = 0
            if note_entiere < notes_max:
                note_decimal = randint(0, 3) * 25
            note = note_entiere + note_decimal / 100
            ligne_notes.append(note)
    
    feuille.append(ligne_notes)

# Enregistrement du fichier Excel
nom_fichier = 'notes_eleves.xlsx'
classeur.save(nom_fichier)
print(f"Le fichier {nom_fichier} a été généré avec succès.")

```

