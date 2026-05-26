import pandas as pd


def generate_quality_report(wells):
    reports = []

    for well_name, df in wells.items():

        depth_min = df["depth"].min()
        depth_max = df["depth"].max()

        sampling_step = (
            df["depth"].diff().median()
        )  ## the difference between consequetive rows for depths of wells

        row = {
            "well": well_name,
            "rows": len(df),
            "depth_min": depth_min,
            "depth_max": depth_max,
            "sampling_step": sampling_step,
        }

        for col in df.columns:
            row[f"missing_{col}"] = df[col].isna().sum()

        reports.append(row)

    return pd.DataFrame(reports)
