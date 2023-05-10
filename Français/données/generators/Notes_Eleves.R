# Installation de la bibliothèque openxlsx si nécessaire
# if (!requireNamespace("openxlsx", quietly = TRUE)) {
#   install.packages("openxlsx")
# }

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
