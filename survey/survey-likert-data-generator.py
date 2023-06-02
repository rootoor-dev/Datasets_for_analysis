import numpy as np
import pandas as pd
from scipy.stats import ortho_group
from scipy.linalg import null_space

def generate_data(num_items, num_participants, num_factors, alpha):
    # Générer une matrice aléatoire de facteurs
    factors = ortho_group.rvs(num_factors)
    # Générer une matrice aléatoire de charges factorielles
    loadings = np.random.normal(size=(num_items, num_factors))
    # Normaliser les charges factorielles pour une variance unitaire
    loadings = loadings / np.sqrt(np.sum(loadings**2, axis=0))
    # Calculer la matrice de covariance des items
    cov = np.dot(loadings, loadings.T)
    # Ajouter de l'erreur de mesure
    cov = cov + np.eye(num_items) * (1 - cov.diagonal())
    # Générer des données aléatoires à partir de la matrice de covariance
    data = np.random.multivariate_normal(np.zeros(num_items), cov, size=num_participants)
    # Convertir les données en échelle de Likert
    data = np.round(4 * (data + 2) / 4) + 1
    # Vérifier si les données répondent aux critères d'alpha et de nombre de facteurs
    while True:
        # Calculer l'alpha de Cronbach
        item_means = np.mean(data, axis=0)
        total_var = np.var(item_means)
        error_var = np.mean(np.var(data, axis=0))
        alpha_hat = (num_items / (num_items - 1)) * (1 - error_var / total_var)
        # Vérifier si l'alpha est satisfaisant
        if alpha_hat >= alpha and alpha_hat < 1:
            # Calculer le nombre de facteurs
            corr = np.corrcoef(data.T)
            eigvals, eigvecs = np.linalg.eig(corr)
            eigvals = np.real(eigvals)
            eigvecs = np.real(eigvecs)
            eigvals = eigvals / np.sum(eigvals)
            num_factors_hat = np.sum(eigvals > 0.05)
            # Vérifier si le nombre de facteurs est satisfaisant
            if num_factors_hat >= num_factors:
                break
        # Si les critères ne sont pas satisfaits, générer de nouvelles données
        factors = ortho_group.rvs(num_factors)
        loadings = np.random.normal(size=(num_items, num_factors))
        loadings = loadings / np.sqrt(np.sum(loadings**2, axis=0))
        cov = np.dot(loadings, loadings.T)
        cov = cov + np.eye(num_items) * (1 - cov.diagonal())
        data = np.random.multivariate_normal(np.zeros(num_items), cov, size=num_participants)
        data = np.round(4 * (data + 2) / 4) + 1
    return data

def save_to_csv(data):
    # Convertir les données en DataFrame pandas
    df = pd.DataFrame(data)
    # Écrire les données dans un fichier XLSX
    writer = pd.ExcelWriter('donnees.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()
    print("Données enregistrées dans donnees.xlsx\n")

def save_to_xlsx(data):
    # Convertir les données en DataFrame pandas
    df = pd.DataFrame(data)
    # Écrire les données dans un fichier CSV
    df.to_csv('donnees.csv', index=False)
    print("Données enregistrées dans donnees.csv\n")

def main():
    print("##########################################################################################\n")
    print("# Bienvenue dans notre programme de génération automatique \nde données de types Likert, simulées mais fiables pour les essais ou tests.#")
    print("##########################################################################################\n")
    num_items = int(input("Nombre d'items : "))
    num_participants = int(input("Nombre de participants : "))
    num_factors = int(input("Nombre de facteurs : "))
    alpha = float(input("Alpha de Cronbach minimum : "))
    data = generate_data(num_items=num_items, num_participants=num_participants, 
                         num_factors=num_factors, alpha=alpha)
    print("Données générées :")

    save_to_csv(data)
    save_to_xlsx(data)

    # executer la fonction main()
if __name__ == '__main__':
    main()
