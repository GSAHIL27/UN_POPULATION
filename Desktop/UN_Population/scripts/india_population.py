"""
This script calculates and plots India's population growth over the years
using data from the UN Population dataset.
"""


import csv
import matplotlib.pyplot as plt

# ==============================
# CONSTANTS
# ==============================
REGION_COLUMN = "Region"
YEAR_COLUMN = "Year"
POPULATION_COLUMN = "Population"
TARGET_COUNTRY = "India"

# File paths (relative)
DATA_FILE = "data/population-estimates.csv"
OUTPUT_FILE = "plots/India_Population.png"

# ==============================
# CALCULATION FUNCTION
# ==============================
def calculate_india_population_over_years(file_path):
    """
    Reads the CSV file and returns a dictionary {year: population} for India.
    Skips rows with missing or invalid population values.
    """
    india_population_by_year = {}

    with open(file_path, newline="", encoding="utf-8") as csvfile:
        population_reader = csv.DictReader(csvfile)

        for record in population_reader:
            region = record[REGION_COLUMN].strip()
            if region.lower() != TARGET_COUNTRY.lower():
                continue

            year = record[YEAR_COLUMN].strip()
            population_value = record[POPULATION_COLUMN].strip()

            # Skip missing or invalid data
            if not population_value or population_value.lower() in {"none", "na", "n/a", ".."}:
                continue

            try:
                population = float(population_value)
                india_population_by_year[int(year)] = population
            except ValueError:
                continue

    return india_population_by_year


# ==============================
# PLOTTING FUNCTION
# ==============================
def plot_india_population(india_population_by_year, output_file):
    """
    Plots and saves a bar chart of India population vs. years.
    """
    if not india_population_by_year:
        print("No valid population data found for India.")
        return

    years = sorted(india_population_by_year.keys())
    populations = [india_population_by_year[year] for year in years]

    plt.figure(figsize=(10, 6))
    plt.bar(years, populations, color='blue')
    plt.title('India Population Over Years')
    plt.xlabel('Year')
    plt.ylabel('Population(in billions)')


    interval = 5  
    plt.xticks(ticks=years[::interval], labels=years[::interval], rotation=45, fontsize=8)

    plt.tight_layout()
    plt.savefig('plots/india_population_trend.png')
    plt.show()




# ==============================
# MAIN EXECUTION FUNCTION
# ==============================
def execute():
    """Main function to calculate and plot India's population growth."""
    india_population = calculate_india_population_over_years(DATA_FILE)
    plot_india_population(india_population, OUTPUT_FILE)


# ==============================
# RUN PROGRAM
# ==============================
if __name__ == "__main__":
    execute()
