"""
This script calculates and plots the population of ASEAN countries
for the year 2014 using data from a CSV file.
"""

import csv
import matplotlib.pyplot as plt

# File path
DATA_FILE = "data/population-estimates.csv"
PLOT_FILE = "plots/asean_population_2014.png"

# Column names in your CSV
REGION_COLUMN = "Region"
COUNTRY_COLUMN = "Country Code"
YEAR_COLUMN = "Year"
POPULATION_COLUMN = "Population"

# ASEAN Countries
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

def calculate_asean_population_2014(file_path):
    """Reads population data and returns ASEAN countries' populations for 2014."""
    asean_population = {}

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for record in reader:
            try:
                country = record[REGION_COLUMN].strip()
                year = int(record[YEAR_COLUMN])
                population = record[POPULATION_COLUMN].strip()

                if not population or population == "None":
                    continue

                if country in ASEAN_COUNTRIES and year == 2014:
                    asean_population[country] = float(population)

            except (ValueError, KeyError):
                continue

    return asean_population


def plot_asean_population_2014(asean_population):
    """Plots a bar chart for ASEAN populations in 2014."""
    countries = list(asean_population.keys())
    populations = list(asean_population.values())

    plt.figure(figsize=(10, 6))
    plt.bar(countries, populations, color='blue')
    plt.title('ASEAN Countries Population - 2014')
    plt.xlabel('Country')
    plt.ylabel('Population(in millions)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(PLOT_FILE)
    plt.show()


def execute():
    """Main function that calculates and plots ASEAN population for 2014."""
    asean_population = calculate_asean_population_2014(DATA_FILE)
    plot_asean_population_2014(asean_population)


if __name__ == "__main__":
    execute()
