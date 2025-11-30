import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

def plot_world_time_heatmap():
    # Load world shapefile
    world = gpd.read_file("data/world_shapefile/ne_110m_admin_0_countries.shp")

    # Load processed city dataset
    df = pd.read_csv("data/processed/worldcities_time_dilation.csv")

    # Convert to GeoDataFrame
    gdf = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(df.lng, df.lat),
        crs="EPSG:4326"
    )

    # Plot
    fig, ax = plt.subplots(figsize=(16, 10))
    world.plot(ax=ax, color="lightgray", edgecolor="white")

    gdf.plot(
        ax=ax,
        column="microseconds_difference_per_year",
        cmap="viridis",
        markersize=2,
        legend=True
    )

    plt.title("Relative Aging Difference by City (Microseconds per Year)")
    plt.show()
