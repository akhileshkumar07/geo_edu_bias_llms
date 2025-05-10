import geopandas as gpd
from thefuzz import process
import numpy as np

# Load the shapefile containing world country boundaries
WORLD = gpd.read_file("ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp")

def create_world_map(df, ax, title, threshold=80):
    """
    Plots a world map showing frequencies by country with fuzzy matching.

    Parameters:
    - df: DataFrame with 'country' and 'frequency' columns
    - ax: Matplotlib axis to plot on
    - title: Title for the map
    - threshold: Fuzzy matching threshold score (default is 80)

    Returns:
    - unmatched_countries: Dictionary of unmatched countries with their best match and score
    """
    # Get list of countries from the shapefile
    country_list_world = WORLD['NAME'].unique()

    # Dictionaries to hold matched and unmatched countries
    matched_countries = {}
    unmatched_countries = {}

    # Perform fuzzy matching for each country in the input DataFrame
    for country in df['country'].unique():
        match, score = process.extractOne(country, country_list_world)
        if score >= threshold:
            matched_countries[country] = match
        else:
            unmatched_countries[country] = (match, score)

    # Add a new column with matched country names based on fuzzy matching
    df['matched_country'] = df['country'].map(matched_countries)

    # Merge the GeoDataFrame with the input data using matched country names
    merged = WORLD.merge(df, how='left', left_on='NAME', right_on='matched_country')

    # Ensure 'frequency' column has NaN where data is missing
    merged['frequency'] = merged['frequency'].fillna(np.nan)

    # Split merged data into those with and without frequency data
    with_data = merged[merged['frequency'].notna()]
    without_data = merged[merged['frequency'].isna()]

    # Plot countries with frequency data using a color map
    with_data.plot(
        column='frequency',
        cmap='coolwarm',
        linewidth=0.6,
        ax=ax,
        edgecolor='white',
        legend=True,
        legend_kwds={
            'label': 'Frequency',
            'shrink': 0.6,
            'orientation': "vertical",
        }
    )

    # Overlay unmatched countries using a hatch pattern
    without_data.plot(
        color='white',
        edgecolor='lightgray',
        hatch='///',
        ax=ax
    )

    ax.set_title(title, fontsize=14)
    ax.set_axis_off()

    return unmatched_countries