import pandas as pd
import matplotlib.pyplot as plt


# How does ONE zone vary across wells?
def plot_zone_across_wells(df, zone_name):
    zone_df = df[df["zone"] == zone_name]
    plt.figure()
    plt.bar(zone_df["well"].astype(str), zone_df["net_thickness"])
    plt.title(f"Zone {zone_name} - Net Thickness Across Wells")
    plt.xlabel("Well")
    plt.ylabel("Net Thickness")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"outputs/zone_{zone_name}_across_wells.png")
    plt.show()


# Which zones are best in one well?
def plot_zones_within_well(df, well_name):
    well_df = df[df["well"] == well_name].sort_values("net_thickness", ascending=False)
    plt.figure()
    plt.bar(well_df["zone"], well_df["net_thickness"])
    plt.title(f"Well {well_name} - Zone Ranking")
    plt.xlabel("Zone")
    plt.ylabel("Net Thickness")
    plt.tight_layout()
    plt.savefig(f"outputs/well_{well_name}_zone_ranking.png")
    plt.show()


# How variable is reservoir quality across field?
def plot_field_distribution(df):
    plt.figure()
    plt.hist(df["net_thickness"], bins=10)
    plt.title("Field Distribution of Net Thickness")
    plt.xlabel("Net Thickness")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("outputs/field_net_thickness_distribution.png")
    plt.show()
