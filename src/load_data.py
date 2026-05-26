from pathlib import Path
import pandas as pd
import yaml
import glob
import os


def load_config(config_path="config.yaml"):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)  ## in order to change data structure to dict format


def load_well_data(config):
    data_dir = config["data_dir"]
    pattern = config["well_pattern"]

    files = glob.glob(f"{data_dir}/{pattern}")  # find the exact loc of the wells
    wells = {}
    for file in files:
        df = pd.read_csv(file)
        base = os.path.basename(file)  # well_1.csv
        well_id = base.replace("well_", "").replace(".csv", "")
        df["well"] = int(well_id)

        wells[well_id] = df

    return wells


def load_zones(config):
    zones_path = f"{config['data_dir']}/zones.csv"
    return pd.read_csv(zones_path)
