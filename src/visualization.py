import matplotlib.pyplot as plt


def plot_vsh_sensitivity(df):
    zones = df["zone"].unique()

    for zone in zones:
        zone_df = df[df["zone"] == zone]
        plt.plot(zone_df["vsh_cutoff"], zone_df["net_thickness"], label=zone)

    plt.xlabel("VSH Cutoff")
    plt.ylabel("Net Reservoir Thickness")
    plt.title("Net Thickness Sensitivity to VSH Cutoff")
    plt.legend()
    plt.savefig("outputs/vsh_sensitivity.png")
    plt.show()
