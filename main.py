import pandas as pd
from src.load_data import load_config, load_well_data, load_zones
from src.profiling import generate_quality_report
from src.zone_join import add_zones_to_well
from src.analytics import add_dz, add_net_flag, build_analytical_table
from src.sensitivity import run_vsh_sensitivity
from src.visualization import plot_vsh_sensitivity
from src.field_views import (
    plot_zone_across_wells,
    plot_zones_within_well,
    plot_field_distribution,
)
from src.subzones import create_subzones


def main():
    config = load_config()
    wells = load_well_data(config)
    zones = load_zones(config)

    report = generate_quality_report(wells)
    report.to_csv(config["output_report"], index=False)

    print("Data quality report saved.")

    combined_version = []
    for well_name, df in wells.items():
        merged = add_zones_to_well(df, zones, well_name)
        combined_version.append(merged)

    final_df = pd.concat(combined_version, ignore_index=True)
    final_df.to_csv(config["output_combined"], index=False)
    print("Combines well log table saved.")

    final_df = add_dz(final_df)
    final_df = add_net_flag(final_df)
    analytical_table = build_analytical_table(final_df)
    analytical_table.to_csv("outputs/analytical_table.csv", index=False)
    print("Analytical table created.")

    sensitivity_df = run_vsh_sensitivity(final_df)
    sensitivity_df.to_csv("outputs/vsh_sensitivity.csv", index=False)
    print("VSH sensitivity analysis created.")
    plot_vsh_sensitivity(sensitivity_df)

    # View 1: pick a zone
    for zone in analytical_table["zone"].unique():
        plot_zone_across_wells(analytical_table, zone)

    # View 2: pick a well
    for well in analytical_table["well"].unique():
        plot_zones_within_well(analytical_table, well)

    # View 3: field-wide
    plot_field_distribution(analytical_table)

    selected_zone = final_df["zone"].dropna().unique()[0]

    subzone_df = create_subzones(final_df, selected_zone, n_clusters=3)
    subzone_df.to_csv("outputs/subzones.csv", index=False)
    print("Sub-zone analysis created.")


if __name__ == "__main__":
    main()
