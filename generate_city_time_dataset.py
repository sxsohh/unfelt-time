import pandas as pd
import numpy as np

# Physical constants
G = 6.67430e-11                    # gravitational constant
M = 5.972e24                       # mass of Earth
R = 6_371_000                      # radius of Earth (meters)
c = 299_792_458                    # speed of light
omega = 7.292115e-5                # Earth's rotation rad/s

# -------------------------------------------------------------------
# 1. Load the dataset
# -------------------------------------------------------------------
df = pd.read_csv("data/worldcities.csv")

# Keep only rows with coordinates
df = df[df["lat"].notnull() & df["lng"].notnull()].copy()

# -------------------------------------------------------------------
# 2. Generate realistic synthetic altitudes
# -------------------------------------------------------------------
# Base altitude by continent trend (rough approximation)
continent_alt = {
    "Asia": 400,
    "Africa": 350,
    "Europe": 300,
    "North America": 320,
    "South America": 600,
    "Oceania": 250,
    "Antarctica": 1000
}

def guess_continent(country):
    # Basic mapping for synthetic altitudes
    if country in ["United States", "Canada", "Mexico"]:
        return "North America"
    if country in ["Brazil", "Argentina", "Chile", "Peru", "Colombia"]:
        return "South America"
    if country in ["Kenya", "Egypt", "Nigeria", "South Africa"]:
        return "Africa"
    if country in ["China", "India", "Japan", "Russia"]:
        return "Asia"
    if country in ["France", "Germany", "UK", "Italy", "Spain"]:
        return "Europe"
    if country in ["Australia", "New Zealand"]:
        return "Oceania"
    return "Europe"  # default

# Assign continent
df["continent_guess"] = df["country"].apply(guess_continent)

# Generate synthetic altitude:
# Base + noise + small variation based on density
np.random.seed(42)
df["altitude_m"] = (
    df["continent_guess"].map(continent_alt)
    + np.random.normal(0, 80, size=len(df))     # random terrain variation
    + (df["population"].fillna(0) / 1e6) * 5    # slight bump for megacities
)

# Clamp altitudes to real-world range
df["altitude_m"] = df["altitude_m"].clip(lower=-50, upper=4500)

# -------------------------------------------------------------------
# 3. Compute gravitational + rotational aging factors
# -------------------------------------------------------------------

def aging_factor(lat_deg, altitude_m):
    lat = np.radians(lat_deg)
    r = R + altitude_m

    # gravitational potential term
    grav = 2 * G * M / (r * c**2)

    # rotational velocity term
    v = omega * r * np.cos(lat)
    rot = (v**2) / (c**2)

    # total dilation factor (1 - small terms)
    factor = np.sqrt(1 - grav - rot)
    return factor

df["aging_factor"] = df.apply(
    lambda row: aging_factor(row["lat"], row["altitude_m"]), axis=1
)

# human experienced time per year
SECONDS_PER_YEAR = 31_557_600
df["experienced_seconds_per_year"] = df["aging_factor"] * SECONDS_PER_YEAR

# difference from ideal sea level (0 m, equator)
ideal_factor = aging_factor(0, 0)
ideal_time = ideal_factor * SECONDS_PER_YEAR

df["microseconds_difference_per_year"] = (
    (df["experienced_seconds_per_year"] - ideal_time) * 1e6
)

# -------------------------------------------------------------------
# 4. Save final dataset
# -------------------------------------------------------------------
df.to_csv("worldcities_time_dilation.csv", index=False)

print("Saved worldcities_time_dilation.csv")
print(df[["city", "country", "lat", "lng", "altitude_m",
          "aging_factor", "microseconds_difference_per_year"]].head())
