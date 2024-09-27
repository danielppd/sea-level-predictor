import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Função para gerar e plotar a linha de melhor ajuste
    def plot_best_fit_line(data, start_year, color):  
        intervalo = data[data['Year'] >= start_year]  # Filtra os dados para incluir apenas os anos a partir de 'start_year'
        # usa linregress para calcular a inclinação (slope) e o intercepto da linha de melhor ajuste para o subconjunto de dados
        slope, intercept, *_ = linregress(intervalo['Year'], intervalo['CSIRO Adjusted Sea Level'])  
        years = pd.Series(range(start_year, 2051))  
        plt.plot(years, intercept + slope * years, color=color)  
        
    # Create first line of best fit
    plot_best_fit_line(df, df['Year'].min(), 'red')  
    # plota a linha de melhor ajuste para todos os dados
    
    # Create second line of best fit
    plot_best_fit_line(df, 2000, 'green')  
    # plota a linha de melhor ajuste para os dados a partir do ano 2000



    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()