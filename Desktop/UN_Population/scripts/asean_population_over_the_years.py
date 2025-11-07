"""
This script calculates and plots a grouped bar chart showing ASEAN countries' populations
from 2004 to 2014 using data from a CSV file.
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

# File paths
DATA_FILE = "data/population-estimates.csv"
PLOT_FILE = "plots/asean_population_grouped.png"

# CSV Columns
REGION_COLUMN = "Region"
YEAR_COLUMN = "Year"
POPULATION_COLUMN = "Population"

# ASEAN countries
ASEAN_COUNTRIES = [
    "Brunei Darussalam",
    "Cambodia",
    "Indonesia",
    "Lao People's Democratic Republic",
    "Malaysia",
    "Myanmar",
    "Philippines",
    "Singapore",
    "Thailand",
    "Viet Nam"
]

def calculate_asean_population(file_path):
    """Calculate population data for ASEAN countries (2004–2014)."""
    data = {country: {} for country in ASEAN_COUNTRIES}

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for record in reader:
            try:
                country = record[REGION_COLUMN].strip()
                year = int(record[YEAR_COLUMN])
                population = record[POPULATION_COLUMN].strip()

                if not population or population == "None":
                    continue

                if country in ASEAN_COUNTRIES and 2004 <= year <= 2014:
                    data[country][year] = float(population)

            except (ValueError, KeyError):
                continue

    return data


def plot_asean_grouped_chart(asean_data):
    """Plot grouped bar chart for ASEAN countries over years."""
    years = list(range(2004, 2015))
    x = np.arange(len(years))  # X-axis positions
    bar_width = 0.08  # Width of each bar

    plt.figure(figsize=(12, 6))

    for i, country in enumerate(ASEAN_COUNTRIES):
        populations = [asean_data[country].get(year, 0) for year in years]
        plt.bar(x + i * bar_width, populations, width=bar_width, label=country)

    plt.xlabel("Year")
    plt.ylabel("Population(in millions)")
    plt.title("ASEAN Countries Population (2004–2014)")
    plt.xticks(x + bar_width * len(ASEAN_COUNTRIES) / 2, years, rotation=45)
    plt.legend(fontsize=8, ncol=2)
    plt.tight_layout()
    plt.savefig(PLOT_FILE)
    plt.show()


def execute():
    """Main function to calculate and plot ASEAN population grouped by year (2004–2014)."""
    asean_data = calculate_asean_population(DATA_FILE)
    plot_asean_grouped_chart(asean_data)



if __name__ == "__main__":
    execute()
