#%% md
# # Phase 1 - Import et exploration des données
#%% md
# ### Sources utilisées
# - **FAO/CTS Database** (via World Bank) : températures moyennes annuelles (1970–2022)
# - **Berkeley Earth (via Kaggle)** : températures mensuelles mondiales (depuis 1743)
# - **EM-DAT (Université Catholique de Louvain)** : base de données sur les catastrophes naturelles
# 
#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import plotly.express as px

temp_df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
climate_df = pd.read_csv("climate_change_indicators.csv")
emdat_df = pd.read_excel("emdat.xlsx")  #

#%% md
# # --- Phase 2 : Prétraitement ---
# # 1. Températures Kaggle : GlobalLandTemperaturesByCountry
# # Extraction de la France
#%%
temp_df["dt"] = pd.to_datetime(temp_df["dt"])
temp_fr = temp_df[temp_df["Country"] == "France"].copy()
temp_fr["Year"] = temp_fr["dt"].dt.year
temp_fr = temp_fr.groupby("Year")["AverageTemperature"].mean().reset_index()

#%% md
# # 2. Anomalies climatiques : climate_change_indicators.csv
#%%
climate_fr = climate_df[climate_df["Country"] == "France"].copy()
climate_melt = climate_fr.melt(
    id_vars=["Country"],
    value_vars=[col for col in climate_fr.columns if col.startswith("F")],
    var_name="Year", value_name="Temp_Anomaly"
)
climate_melt["Year"] = climate_melt["Year"].str.extract(r"F(\d+)").astype(int)
#%% md
# # 3. Catastrophes naturelles : EM-DAT
#%%
emdat_fr = emdat_df[emdat_df["Country"] == "France"].copy()
disasters_by_year = emdat_fr.groupby("Start Year").size().reset_index(name="Disaster_Count")
#%% md
# # --- Phase 3 : Fusion des données ---
#%%
merged = pd.merge(temp_fr, climate_melt, on="Year", how="inner")
merged = pd.merge(merged, disasters_by_year, left_on="Year", right_on="Start Year", how="left")
merged.drop(columns=["Start Year"], inplace=True)
merged.fillna(0, inplace=True)
#%% md
# # --- Phase 4 : Visualisations ---
# # Normalisation pour comparaison des tendances
#%%
scaler = MinMaxScaler()
merged[["Temp_norm", "Anomaly_norm"]] = scaler.fit_transform(
    merged[["AverageTemperature", "Temp_Anomaly"]]
)

plt.figure(figsize=(10, 5))
sns.lineplot(data=merged, x="Year", y="Temp_norm", label="Temp moyenne (normée)")
sns.lineplot(data=merged, x="Year", y="Anomaly_norm", label="Anomalie (normée)")
plt.title("Tendances normalisées des températures en France")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 4))
sns.barplot(data=merged, x="Year", y="Disaster_Count", color="tomato")
plt.title("Nombre de catastrophes naturelles (France, EM-DAT)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#%% md
# 
# # --- Phase 5 : Corrélation ---
#%%
correlation = merged[["AverageTemperature", "Temp_Anomaly", "Disaster_Count"]].corr()
print("\nCorrélations :")
print(correlation)
#%%
