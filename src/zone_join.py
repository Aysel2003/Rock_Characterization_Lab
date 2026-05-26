import pandas as pd


def add_zones_to_well(well_df, zones_df, well_name):

    zones_df = zones_df.copy()
    well_df = well_df.copy()

    zones_df["well"] = zones_df["well"].astype(int)
    well_name = int(well_name)
    well_zones = zones_df[zones_df["well"] == well_name].copy()

    if well_zones.empty:
        raise ValueError(f"No zones found for well {well_name}")

    well_zones = well_zones.sort_values("depth")
    well_df = well_df.sort_values("depth")
    merged = pd.merge_asof(
        well_df, well_zones[["depth", "name"]], on="depth", direction="backward"
    )

    merged = merged.rename(columns={"name": "zone"})

    return merged
