import pandas as pd
import numpy as np


def run_vsh_sensitivity(df):
    cutoffs = np.arange(0.30, 0.75, 0.05)
    results = []

    for cutoff in cutoffs:
        temp_df = df.copy()
        temp_df["is_net"] = (temp_df["vsh"] <= cutoff) & (temp_df["phit"] >= 0.08)

        grouped = temp_df.groupby("zone")
        for zone, group in grouped:
            net = group[group["is_net"]]
            net_thickness = net["dz"].sum()

            results.append(
                {"zone": zone, "vsh_cutoff": cutoff, "net_thickness": net_thickness}
            )
    return pd.DataFrame(results)
