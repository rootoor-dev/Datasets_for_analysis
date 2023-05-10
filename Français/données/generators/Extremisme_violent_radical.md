# DESCRIPTION

Le jeu de données généré représente les réponses aléatoires d'un questionnaire basé sur une échelle de Likert à 7 niveaux, complété par 3000 participants. Le questionnaire aborde différents facteurs liés à l'extrémisme violent radicalisé, notamment : age, sexe, vols_betail, injustice, mal_gouvernance, religion, pauvrete, mimetisme, politique, ignorance, probleme_education, egoisme, conflit_ethnique, chomage et orgueil.

Chaque participant a fourni des réponses pour chaque facteur. Les réponses pour les facteurs vols_betail, injustice, mal_gouvernance, religion, pauvrete, mimetisme, politique, ignorance, probleme_education, egoisme, conflit_ethnique, chomage et orgueil sont évaluées sur une échelle de Likert à 7 niveaux, allant de 1 (très faible) à 7 (très élevé).

Le facteur "age" représente l'âge des participants et prend des valeurs dans l'intervalle de 12 à 70 ans. Le facteur "sexe" indique le sexe des participants, avec une proportion d'hommes légèrement/complètement (à vous d'ajuster selon vos besoin) supérieure à celle des femmes dans ce jeu de données.

Le jeu de données est enregistré dans un fichier Excel nommé "qr_extremisme_violent_radicalise.xlsx". Chaque ligne du fichier correspond à un participant différent, tandis que les colonnes représentent les facteurs du questionnaire. Les réponses aléatoires sont enregistrées dans les cellules correspondantes, avec les entiers de 1 à 7 pour les échelles de Likert, l'âge pour le facteur "age", et les valeurs "Homme" ou "Femme" pour le facteur "sexe".

# CODE DE GENERATION DES DONNEES

```R
# Installer le package "writexl" si nécessaire
if (!requireNamespace("writexl", quietly = TRUE)) {
  install.packages("writexl")
}

# Charger le package "writexl"
library(writexl)

# Définir les facteurs et les participants
facteurs <- c( "age", "sexe", "vols_betail", "injustice", "mal_gouvernance", "religion", "pauvrete",
              "mimetisme", "politique", "ignorance", "probleme_education", "egoisme",
              "conflit_ethnique", "chomage", "orgueil")
participants <- 3000

# Définir les bornes d'âge
age_min <- 12
age_max <- 70

# Générer les âges aléatoirement pour les participants
ages <- sample(age_min:age_max, participants, replace = TRUE)

# Définir les proportions de sexe
prop_hommes <- 0.75     # changer selon vos besoins : 0.55
prop_femmes <- 0.25     # changer selon vos besoins : 0.45

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
# TRAVAIL A FAIRE

Enoncé: 
On se propose de déterminer la perception des populations d'un pays fictif nommé "Kamitland" sur les causes de la radicalité de l'extrémisme violent qui y sévit. Il s'agit de savoir les réelles causes qui contribuent à la radicalisation de l'extrémisme violent qui se pratique dans certaines contrées de ce pays. Pour cela, un questionnaire basé sur une échelle de Likert à 7 niveaux (1- totalement en désaccord,..., 4-neutre,...,7-totalement d'accord) ,a éte soumis aux populations de Kamitland en vue de mesurer les attitudes ou avis sur le sujet de radicalisation de l'extrémisme violent dont elles sont la cible.
1. Faire une Analyse Factorielle Exploratoire (AFE) pour déterminer les facteurs induits par les items.
2. Faire une Analyse Factorielle Confirmatoire pour confirmer, valider votre étude 

# DONNEES

Les données peuvent être générées par le code R ci-dessus. Mais pour que tout le monde puisse travailler sur les mêmes 
données, il est récommandées de se servir du jeu de données "qr_" de ce dépôt, disponible à l'adresse suivante: 



# Contribution
Vous pouvez contribuer en postant vos analyses ou partageant vos ressources.










