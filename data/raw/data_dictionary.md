# well_<id>.csv

One file per well. Each row is a single depth sample — a measurement taken at a specific depth in the borehole. Rows are ordered top-to-bottom (increasing depth).

depth
  Type: float
  Unit: metres (measured depth)

vsh — Volume of Shale
  Type: float
  Unit: fraction (dimensionless)
  Valid range: 0.0 to 1.0
  The proportion of the rock at this depth that is shale — clay-rich, non-reservoir material. A value of 0 means clean sand; a value of 1 means pure shale. Low values are desirable for a reservoir.

phit — Total Porosity
  Type: float
  Unit: fraction (dimensionless)
  Valid range: 0.0 to 0.5
  The fraction of the rock volume that is pore space — voids that can hold fluids. A value of 0.20 means 20% of the rock is empty space. 

sw — Water Saturation
  Type: float
  Unit: fraction (dimensionless)
  Valid range: 0.0 to 1.0
  The fraction of the pore space that is filled with water rather than hydrocarbons. A value of 1.0 means the pores are 100% water-filled with no hydrocarbons present. Low values indicate hydrocarbon presence.

perm — Permeability
  Type: float
  Unit: millidarcies (mD)
  Valid range: 0.001 to 15,000
  How easily fluid can flow through the rock. Values span several orders of magnitude and are approximately log-normally distributed. Values near zero indicate tight, low-flow rock. Values at or below zero are invalid.


# zones.csv

Maps named stratigraphic zones to depth intervals within each well.

well
  The well identifier. Matches the <id> part of the corresponding well_<id>.csv filename.

depth
  The top depth of the zone within this well, in metres.

name
  The zone name, for example "A", "B", "C".

Zone extent rule: a zone begins at its listed depth and ends at the depth of the next zone in the same well (when sorted ascending by depth). The last zone in each well extends down to the bottom of the log. Every depth sample in the well log belongs to exactly one zone.


# Derived Quantities

These are not columns in the source files. You compute them as part of the task.

dz — depth interval
  The thickness represented by a single depth sample, in metres. Compute it as the difference between consecutive depth values:
    dz[i] = depth[i+1] - depth[i]   for all rows except the last
    dz[last] = dz[last-1]            repeat the previous step for the final row

Net reservoir flag
  A depth sample is net reservoir if: vsh <= 0.5 AND phit >= 0.08
  This means the rock is sufficiently clean and porous to be considered reservoir quality.
  The default cutoff values (0.5 / 0.08) are starting points. Part C asks you to vary the vsh cutoff and observe the effect.

Gross thickness
  sum(dz) over all samples in a zone.
  Unit: metres. The total depth extent of the zone.

Net reservoir thickness
  sum(dz) over samples where the net reservoir flag is True.
  Unit: metres. Cumulative thickness of reservoir-quality rock within the zone.

Average phit (net reservoir)
  mean(phit) over net reservoir samples.
  Unit: fraction. Average porosity of the reservoir interval.

Average perm (net reservoir)
  mean(perm) over net reservoir samples.
  Unit: millidarcies. Average permeability of the reservoir interval.

kh (net reservoir) — permeability-thickness product
  sum(perm * dz) over net reservoir samples.
  Unit: mD·m. Proportional to how much fluid a zone can deliver. This is the primary indicator of well productivity.
