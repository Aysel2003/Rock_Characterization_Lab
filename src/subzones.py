import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def create_subzones(df, target_zone, n_clusters=3):

    zone_df = df[df["zone"] == target_zone].copy()
    features = ["vsh", "phit", "sw", "perm"]
    zone_df = zone_df.dropna(subset=features)
    X = zone_df[features]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    zone_df["subzone"] = kmeans.fit_predict(X_scaled)
    zone_df["subzone"] = "Subzone_" + zone_df["subzone"].astype(str)

    return zone_df
