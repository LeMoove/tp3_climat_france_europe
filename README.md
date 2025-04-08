# 🌍 TP3 – Analyse de l’impact du changement climatique (France-Europe 1970–2024)

## 👨‍🎓 Auteur
**Mathieu**  
https://mathieuastruc.com/
[ESAIP – 2025]

## 🎯 Objectif du projet
Ce projet a pour but d’analyser l’évolution climatique en France (et potentiellement en Europe) à travers l’étude :
- Des températures moyennes annuelles
- Des anomalies climatiques
- Des catastrophes naturelles

Il s’inscrit dans le cadre du **TP3 Open Data** 

---

## 📁 Contenu du dépôt

| Fichier                             | Description                                                       |
|------------------------------------|-------------------------------------------------------------------|
| `climateOperate.ipynb`             | Notebook principal avec toutes les étapes du projet              |
| `GlobalLandTemperaturesByCountry.csv` | Températures mondiales historiques (source : Berkeley Earth)      |
| `climate_change_indicators.csv`    | Anomalies climatiques (source : World Bank)                      |
| `emdat.xlsx`                       | Données sur les catastrophes naturelles (source : EM-DAT)         |
| `README.md`                        | Ce fichier explicatif                                              |
| `metadata.md`                      | Fiche de métadonnées simulant une publication OpenData            |

---

## 🔬 Étapes réalisées

### 🔹 Phase 1 – Import & Exploration
- Chargement des fichiers `.csv` et `.xlsx`
- Filtrage des données pour la France
- Analyse des années disponibles

### 🔹 Phase 2 – Prétraitement
- Transformation des dates en années
- Agrégation par année
- Mise en forme des anomalies climatiques et catastrophes naturelles

### 🔹 Phase 3 – Fusion et Visualisation
- Fusion des 3 sources de données principales
- Graphiques temporels : températures, anomalies, catastrophes
- Carte choroplèthe interactive avec Plotly

### 🔹 Phase 4 – Analyse statistique
- Calcul d'anomalies vs baseline 1951–1980
- Corrélation température ↔ catastrophes
- Régression linéaire avec `statsmodels`

### 🔹 Phase 5 – Scénarios climatiques
- Modélisation simple d’impacts selon le niveau de réchauffement
- Tableaux de solutions pour chaque scénario (+1.5°C, +2°C, +3°C)

### 🔹 Phase 6 – Prévention
- Tableau des mesures d’atténuation et d’adaptation
- Propositions ciblées par zone à risque

---

## Sources de données

- **Berkeley Earth** – Températures historiques : https://berkeleyearth.org
- **World Bank** – Indicateurs climatiques : https://data.worldbank.org
- **EM-DAT** – Catastrophes naturelles : https://emdat.be


---

## 📖 Licence
Projet sous licence ??
