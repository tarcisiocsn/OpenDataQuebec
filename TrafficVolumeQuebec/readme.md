## Fichier sur OneDrive

* [débit_circulation_québec](https://polymtlca0-my.sharepoint.com/:f:/g/personal/tarcisio_costa-de-souza-neto_polymtl_ca/Es42_1xrGx1EuIE6FHHBSBMBB05q0hX9axpftgjZcqmMaQ?e=L6TdUc)

Le code pour l'automatisation: fichier [telecharger_fichiers.py]. Ce code est utilisé pour télécharger des fichiers à partir d'URLs spécifiques et les stocker localement dans des dossiers correspondants. Voici un résumé des étapes principales :

1. Création d'un dossier de téléchargement.
2. Définition d'une fonction pour télécharger un fichier à partir d'une URL donnée.
3. Définition d'une fonction pour extraire les URLs à partir du code HTML en utilisant BeautifulSoup.
4. Parcours de chaque ligne d'un dataframe appelé 'df'.
5. Extraction des URLs de section et des URLs de données pour chaque ligne.
6. Création d'un dossier correspondant à la valeur de 'num_sectn_trafc' s'il n'existe pas déjà.
7. Téléchargement des fichiers à partir des URLs de section dans un sous-dossier spécifique.
8. Téléchargement des fichiers à partir des URLs de données dans un autre sous-dossier spécifique.
9. Affichage du nombre de nouveaux dossiers créés pour chaque 'num_sectn_trafc'.
10. Affichage du nombre total de nouveaux dossiers créés.
11. Affichage d'un message indiquant que le téléchargement des fichiers est terminé.

Cela résume les étapes principales de ce code.
