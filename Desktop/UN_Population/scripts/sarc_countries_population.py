"""
This script analyzes and visualizes the population trends of SAARC countries
based on UN population data.
"""

import csv
import matplotlib.pyplot as plt

# File paths
DATA_FILE = "data/population-estimates.csv"
PLOT_FILE = "plots/saarc_total_population.png"

# CSV Columns
REGION_COLUMN = "Region"
YEAR_COLUMN = "Year"
POPULATION_COLUMN = "Population"

# SAARC countries
SAARC_COUNTRIES = [
    "Afghanistan",
    "Bangladesh",
    "Bhutan",
    "India",
    "Maldives",
    "Nepal",
    "Pakistan",
    "Sri Lanka"
]

def calculate_saarc_population_over_years(file_path):
    """Calculates total population of SAARC countries per year."""
    saarc_population = {}

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for record in reader:
            try:
                country = record[REGION_COLUMN].strip()
                year = int(record[YEAR_COLUMN])
                population = record[POPULATION_COLUMN].strip()

                if not population or population == "None":
                    continue

                if country in SAARC_COUNTRIES:
                    population = float(population)
                    saarc_population[year] = saarc_population.get(year, 0) + population

            except (ValueError, KeyError):
                continue

    return dict(sorted(saarc_population.items()))


def plot_saarc_population(saarc_population):
    """Plots total SAARC population per year."""
    years = list(saarc_population.keys())
    populations = list(saarc_population.values())

    plt.figure(figsize=(10, 6))
    plt.bar(years, populations, color='blue')
    plt.title('Total SAARC Population Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Total Population(in billions)')
    plt.xticks(years[::5], rotation=45, fontsize=8)  # Show every 5th year
    plt.tight_layout()
    plt.savefig(PLOT_FILE)
    plt.show()


def execute():
    """Main function to process and visualize SAARC countries' population data."""
    saarc_population = calculate_saarc_population_over_years(DATA_FILE)
    plot_saarc_population(saarc_population)


if __name__ == "__main__":
    execute()
