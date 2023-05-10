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
