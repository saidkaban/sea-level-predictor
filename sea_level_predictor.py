import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"]);

    # Create first line of best fit
    result = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    slope = result.slope
    intercept = result.intercept
    years = df["Year"]
    years = years.append(pd.Series(range(2014, 2050)))
    plt.plot(years, intercept+slope*years)

    # Create second line of best fit
    recent_years = df["Year"][-14:]
    recent_sea_levels = df["CSIRO Adjusted Sea Level"][-14:]
    recent_result = linregress(x=recent_years, y=recent_sea_levels)
    recent_slope = recent_result.slope
    recent_intercept = recent_result.intercept
    recent_years = recent_years.append(pd.Series(range(2014, 2050)))
    plt.plot(recent_years, recent_intercept+recent_slope*recent_years)

    # Add labels and title
    plt.title("Rise in Sea Level");
    plt.xlabel("Year");
    plt.ylabel("Sea Level (inches)");
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()