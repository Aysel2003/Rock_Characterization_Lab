import pandas as pd
import numpy as np


def add_dz(df):
    df = df.sort_values(["well", "depth"]).copy()
    df["dz"] = df.groupby("well")["depth"].diff()
    df["dz"] = df["dz"].fillna(0)

    return df


def add_net_flag(df):

    df["is_net"] = (df["vsh"] <= 0.5) & (df["phit"] >= 0.08)

    return df


def build_analytical_table(df):

    results = []
    grouped = df.groupby(["well", "zone"])

    for (well, zone), group in grouped:

        gross_thickness = group["dz"].sum()
        net = group[group["is_net"]]
        net_thickness = net["dz"].sum()

        avg_phit = net["phit"].mean()
        avg_perm = net["perm"].mean()
        kh = (net["perm"] * net["dz"]).sum()

        results.append(
            {
                "well": well,
                "zone": zone,
                "gross_thickness": gross_thickness,
                "net_thickness": net_thickness,
                "avg_phit_net": avg_phit,
                "avg_perm_net": avg_perm,
                "kh_net": kh,
            }
        )

    return pd.DataFrame(results)
