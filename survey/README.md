# FRENCH
on veut faire les choses de façon inversée. En effet, on souhaite produire des données de types likert qui 
serviront à faire une analyse factorielle exploratoire. La génération aléatoire ne produit pas les résultats 
escomptés ou attendus.

Ces résultats attendus sont les suivants:

- possibilité d'avoir un coefficient alpha de Cronbach supérieur à 0.7 et inférieur à 1
- possibilité d'avoir un nombre raisonnable de facteurs distincs (supérieur à 2)

Pour cela, on voudrait donner la possibilité à l'utilisateur de saisir l'alpha de son choix respectant la condition ci-dessus. 
Donner égalément la possibilité à l'utilisateur de saisir le nombre de facteurs qu'il veut.
Lui donner la possibilité de fournir le nombre d'items, le type de likert, le nombre de participants aussi.

**Comment faire en python ?**

Pour générer des données de type Likert, nous pouvons utiliser la bibliothèque Python ***random*** 
pour générer des nombres entiers aléatoires correspondant aux valeurs de l'échelle de Likert 
(par exemple, de 1 à 5 pour une échelle de 5 points). 
Nous pouvons ensuite utiliser ces nombres entiers pour simuler les réponses des participants à chaque question de l'enquête.
Pour simuler des données qui répondent à vos critères spécifiques, nous pouvons utiliser une approche itérative 
pour générer des ensembles de données aléatoires et évaluer chaque ensemble de données pour voir s'il répond à nos critères. 
Nous pouvons ensuite sélectionner l'ensemble de données qui répond le mieux à nos critères.

# ENGLISH

we want to do things in reverse. Indeed, we want to produce data of likert types which
will be used for an exploratory factor analysis. Random generation does not produce the results
expected or expected.

These expected results are as follows:

- possibility of having a Cronbach's alpha coefficient greater than 0.7 and less than 1
- possibility of having a reasonable number of distinct factors (greater than 2)

For this, we would like to give the possibility to the user to enter the alpha of his choice respecting the condition above.
Also give the possibility to the user to enter the number of factors he wants.
Give him the possibility to provide the number of items, the type of likert, the number of participants too.

**How to do it in python?**

To generate Likert type data, we can use Python library ***random***
to generate random integers corresponding to Likert scale values
(for example, from 1 to 5 for a 5-point scale).
We can then use these integers to simulate participants' responses to each survey question.
To simulate data that meets your specific criteria, we can use an iterative approach
to generate random datasets and evaluate each dataset to see if it meets our criteria.
We can then select the dataset that best meets our criteria.


# COMMENTAIRE DU CODE DU SCRIPT 'survey-likert-data-generator.py'

```
Ce code génère des données aléatoires en utilisant une matrice de covariance 
basée sur des facteurs aléatoires et des charges factorielles aléatoires avec 
une variance unitaire. Il ajoute également de l'erreur de mesure pour simuler 
la variabilité des réponses des participants. Le code utilise ensuite une boucle 
while pour générer de nouvelles données jusqu'à ce que les critères d'alpha et d
e nombre de facteurs soient satisfaits.

Vous pouvez ensuite utiliser cette fonction pour générer des données en spécifiant 
les paramètres num_items (le nombre d'items dans votre questionnaire), num_participants 
(le nombre de participants pour lesquels vous voulez simuler des réponses), num_factors 
(le nombre de facteurs que vous voulez obtenir) et alpha (la valeur minimale que vous voulez
pour l'alpha de Cronbach). Voici un exemple de code pour générer des données avec 10 items, 
100 participants, 3 facteurs distincts et un alpha de Cronbach minimum de 0.7 :
```





