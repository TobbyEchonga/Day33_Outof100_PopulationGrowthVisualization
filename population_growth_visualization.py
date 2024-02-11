import matplotlib.pyplot as plt

def visualize_population_growth(years, population):
    """
    Visualize population growth over time.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(years, population, marker='o', linestyle='-', color='b')
    plt.title('Population Growth Over Time')
    plt.xlabel('Year')
    plt.ylabel('Population (in billions)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Sample data: years and corresponding population
    years = [2000, 2005, 2010, 2015, 2020]
    population = [6.12, 6.52, 6.92, 7.35, 7.8]  # in billions

    # Visualize population growth
    visualize_population_growth(years, population)
