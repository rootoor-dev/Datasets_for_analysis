# Principe de l'Analyse Factorielle Exploratoire (AFE)

Nous allons d’abord faire une Analyse Factorielle Exploratoire (AFE) dont le principe général par exemple est de postuler que les variables observées sont des combinaisons linéaires de variables que l'on appelle facteurs (variables latentes sous-jacentes). Dans l’analyse factorielle exploratoire (AEF), nous explorons essentiellement les corrélations entre les variables observées pour découvrir tout facteur sous-jacent (latent) intéressant et important qui est identifié lorsque les variables observées covarient.

# Hypothèses de l'Analyse Factorielle Exploratoire (AFE)
- **La première hypothèse** est la **sphéricité**, qui vérifie essentiellement que les variables de votre ensemble de données sont suffisamment corrélées entre elles pour être résumées avec un ensemble plus restreint de facteurs. **Le test de sphéricité de Bartlett vérifie si la matrice de corrélation observée s’écarte significativement d’une matrice à corrélation nulle**. Ainsi, si le **test de Bartlett est significatif (p<.05)**, **cela indique que la matrice de corrélation** observée est significativement divergente de la matrice nulle, et donc **convient à l’AFE**.
- **La deuxième hypothèse** est l’**adéquation** de l’échantillonnage et est vérifiée à l’aide de la mesure de l’adéquation de l’échantillonnage (Measure of sampling adequation ou MSA) de Kaiser-Meyer-Olkin (KMO). **L’indice KMO est une mesure de la proportion de variance parmi les variables observées qui pourrait être une variance commune**. Il vérifie les corrélations partielles, c’est-à-dire lorsqu’il y a des facteurs qui ne saturent que deux éléments. Nous voulons rarement, sinon jamais, que l’AFE produise beaucoup de facteurs en ne saturant que deux éléments chacun. Le KMO concerne l’adéquation de l’échantillonnage car des corrélations partielles sont généralement observées avec des échantillons inadéquats. 
- **Si l’indice KMO est élevé (≈ 1)**, le CFC est efficace alors que 
- **si le KMO est faible (≈ 0)**, l’AFE n’est pas pertinente. 
-- Des valeurs KMO inférieures à 0,5 indiquent que l’AFE n’est pas appropriée et 
-- une valeur KMO de 0,6 devrait être confirmée avant que l’AFE soit considérée comme appropriée. 
-- **Les valeurs entre 0,5 et 0,7 sont considérées comme adéquates**, 
-- **les valeurs entre 0,7 et 0,9 sont bonnes** et 
-- **les valeurs entre 0,9 et 1,0 sont excellentes**.

# Rôle de l’AFE 

l’AFE permet de voir quels items d’un questionnaire « vont ensemble » comme facteurs latents, puis elle évalue si certains items devraient être supprimés parce qu’ils ne mesurent pas de façon utile ou distincte un des facteurs latents.

# Nombre des composantes
 - le critère de Kayser (ou Kayser -Guttman) : critère simple mais imparfait et ne devrait plus être utilisé. Selon ce critère, seuls les facteurs dont la valeur propre est supérieure à 1 sont retenus. 
 - Le test d'accumulation de variance ou scree-test (un autre nom est parfois donné "test du coude"). Le graphique des valeurs propres appelé encore "éboulis des valeurs propres" présente un point d’inflexion (coude) changeant ou cassant son allure. Le nombre de points situé au dessus de l’intersection entre la courbe et la droite d’équation x=1 indique le nombre de facteurs à garder.
 - L'analyse parallèle on trace l’éboulis des valeurs propres et celui des valeurs générées aléatoirement. L’intersection des deux courbes isole un certain nombre de points à gauche du point d’intersection, correspondant au nombre de facteurs à garder.
 - La pratique dite « Little Jiffy » (à éviter). La méthode « Litte Jiffy » consiste à retenir tous les facteurs dont la valeur propre est supérieure à 1 (voir 5.1) puis d’effectuer une rotation Varimax. Il s’agirait de la méthode la plus utilisée par les chercheurs, bien qu’elle ne soit pas la meilleure.

# Contrôle de la pertinence du nombre des facteurs sélectionnés.

# APPLICATION AU JEU DE DONNEES "extremisme.csv"

## Avec JASP

our effectuer l'analyse factorielle exploratoire (AFE) de votre jeu de données "questionnaire_reponses.xlsx" dans le logiciel JASP, vous pouvez suivre les étapes suivantes :

Téléchargez et installez JASP depuis le site officiel : https://jasp-stats.org/

Lancez JASP sur votre ordinateur.

Dans JASP, cliquez sur "Ouvrir un fichier de données" dans l'écran d'accueil.

Sélectionnez le fichier "questionnaire_reponses.xlsx" que vous avez généré précédemment.

JASP va charger les données du fichier Excel.

Dans la fenêtre principale de JASP, sélectionnez l'option "Exploratory Factor Analysis" (Analyse factorielle exploratoire) dans la liste des analyses disponibles.

Faites glisser les variables pertinentes (facteurs) de votre jeu de données dans la zone "Variable(s) à analyser" de l'onglet AFE.

Configurez les options d'AFE selon vos besoins, telles que le nombre de facteurs à extraire, la méthode de rotation, etc.

Cliquez sur le bouton "Run" (Exécuter) pour lancer l'analyse factorielle exploratoire.

JASP générera des résultats interactifs et des graphiques pour interpréter les résultats de l'AFE. Explorez les résultats pour comprendre la structure factorielle de votre jeu de données.

Il est important de noter que l'analyse factorielle exploratoire est une méthode statistique complexe qui nécessite une interprétation et une expertise adéquates. Les résultats de l'AFE doivent être interprétés avec prudence et en tenant compte du contexte spécifique de votre étude.


## Avec R

Pour faire l'AFE avec R, nous commençons par installer et charger le package **"psych"**, qui contient des fonctions pour effectuer des analyses factorielles. Ensuite, nous utilisons la fonction read_xlsx() du package "readxl" pour lire le fichier Excel contenant les réponses du questionnaire.

Ensuite, nous sélectionnons les variables pertinentes pour l'AFE en spécifiant les noms des facteurs dans la fonction data[, c("vols_betail", "injustice", ...)].

Nous utilisons ensuite la fonction fa() du package "psych" pour effectuer l'analyse factorielle exploratoire. Nous spécifions le nombre de facteurs à extraire avec nfactors (dans cet exemple, nous en extrayons 3) et nous choisissons la méthode de rotation "varimax" avec rotate pour faciliter l'interprétation.

Enfin, nous affichons les résultats de l'AFE en utilisant la fonction print(afe).

Vous pouvez personnaliser ce code en ajustant le nombre de facteurs à extraire, la méthode de rotation ou en ajoutant d'autres options selon vos besoins spécifiques.

L'AFE dans R générera des résultats comprenant des statistiques descriptives, des matrices de corrélation, des valeurs propres, des charges factorielles, etc., pour vous aider à interpréter la structure factorielle de votre jeu de données.

```R
# Installer le package "psych" si nécessaire
if (!requireNamespace("psych", quietly = TRUE)) {
  install.packages("psych")
}

# Charger le package "psych"
library(psych)

# Lire le fichier Excel avec les réponses
data <- readxl::read_xlsx("questionnaire_reponses.xlsx")

# Sélectionner les variables pertinentes pour l'AFE (facteurs)
variables <- data[, c("vols_betail", "injustice", "mal_gouvernance", "religion", "pauvrete",
                      "mimetisme", "politique", "ignorance", "probleme_education", "egoisme",
                      "conflit_ethnique", "chomage", "orgueil")]

# Effectuer l'analyse factorielle exploratoire
afe <- fa(variables, nfactors = 3, rotate = "varimax")

# Afficher les résultats de l'AFE
print(afe)
```



