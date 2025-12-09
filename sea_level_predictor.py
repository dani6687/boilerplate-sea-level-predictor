import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.5)

    # Create first line of best fit
    full_results = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    full_years = np.arange(1880, 2051)
    full_pred = full_results.slope * full_years + full_results.intercept

    ax.plot(
        full_years,
        full_pred,
        color='red',
        label="Trend 1880-Present"
        )

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    recent_results = linregress(
        df_recent['Year'],
        df_recent['CSIRO Adjusted Sea Level']
        )

    recent_years = np.arange(2000, 2051)
    recent_pred = recent_results.slope * recent_years + recent_results.intercept

    ax.plot(
        recent_years,
        recent_pred,
        color='green',
        label='Trend 2000-Present'
        )

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
