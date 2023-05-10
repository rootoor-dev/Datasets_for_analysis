Le jeu de données généré représente les réponses aléatoires d'un questionnaire basé sur une échelle de Likert à 7 niveaux, complété par 400 participants. Le questionnaire aborde différents facteurs liés à l'extrémisme violent radicalisé, notamment : vols_betail, injustice, mal_gouvernance, religion, pauvrete, mimetisme, politique, ignorance, probleme_education, egoisme, conflit_ethnique, chomage, orgueil, âge et sexe.

Chaque participant a fourni des réponses pour chaque facteur. Les réponses pour les facteurs vols_betail, injustice, mal_gouvernance, religion, pauvrete, mimetisme, politique, ignorance, probleme_education, egoisme, conflit_ethnique, chomage et orgueil sont évaluées sur une échelle de Likert à 7 niveaux, allant de 1 (très faible) à 7 (très élevé).

Le facteur "âge" représente l'âge des participants et prend des valeurs dans l'intervalle de 12 à 70 ans. Le facteur "sexe" indique le sexe des participants, avec une proportion d'hommes légèrement supérieure à celle des femmes dans ce jeu de données.

Le jeu de données est enregistré dans un fichier Excel nommé "questionnaire_reponses.xlsx". Chaque ligne du fichier correspond à un participant différent, tandis que les colonnes représentent les facteurs du questionnaire. Les réponses aléatoires sont enregistrées dans les cellules correspondantes, avec les entiers de 1 à 7 pour les échelles de Likert, l'âge pour le facteur "âge", et les valeurs "Homme" ou "Femme" pour le facteur "sexe".

```R
# Installer le package "writexl" si nécessaire
if (!requireNamespace("writexl", quietly = TRUE)) {
  install.packages("writexl")
}

# Charger le package "writexl"
library(writexl)

# Définir les facteurs et les participants
facteurs <- c("vols_betail", "injustice", "mal_gouvernance", "religion", "pauvrete",
              "mimetisme", "politique", "ignorance", "probleme_education", "egoisme",
              "conflit_ethnique", "chomage", "orgueil", "age", "sexe")
participants <- 3000

# Définir les bornes d'âge
age_min <- 12
age_max <- 70

# Générer les âges aléatoirement pour les participants
ages <- sample(age_min:age_max, participants, replace = TRUE)

# Définir les proportions de sexe
prop_hommes <- 0.55
prop_femmes <- 0.45

# Calculer le nombre d'hommes et de femmes en fonction des proportions
nb_hommes <- round(participants * prop_hommes)
nb_femmes <- participants - nb_hommes

# Générer les sexes aléatoirement pour les participants en respectant le nombre d'hommes et de femmes
sexes <- c(rep("Homme", nb_hommes), rep("Femme", nb_femmes))
sexes <- sample(sexes)

# Créer une matrice vide pour stocker les réponses
reponses <- matrix(nrow = participants, ncol = length(facteurs))

# Générer des réponses aléatoires pour chaque participant et chaque facteur
for (i in 1:participants) {
  for (j in 1:length(facteurs)) {
    if (facteurs[j] == "age") {
      reponses[i, j] <- ages[i]
    } else if (facteurs[j] == "sexe") {
      reponses[i, j] <- sexes[i]
    } else {
      reponses[i, j] <- sample(1:7, 1)
    }
  }
}

# Convertir la matrice en un data frame
reponses_df <- as.data.frame(reponses)

# Renommer les colonnes avec les noms des facteurs
colnames(reponses_df) <- facteurs

# Enregistrer le data frame dans un fichier Excel
write_xlsx(reponses_df, "qr_extremisme_violent_radicalise.xlsx")


```
