import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    df.head(10)     # checking if the data was truly read

    # Create scatter plot
    year = df['Year']
    casl = df['CSIRO Adjusted Sea Level']

    plt.scatter(x = year, y = casl)                 # plot the scatter graph


    # Create first line of best fit
    temp = linregress(year, casl)                   # linear regression from 1880 to 2050

    year_1880_2050 = pd.Series([i for i in range(1880, 2051)])    # year starting from 1880 to 2050
    pred_1 = (temp.slope * year_1880_2050) + temp.intercept       # y = mx + b, which means prediction = (slope * year) + y_int

    plt.plot(year_1880_2050, pred_1)                # plotting the first line


    # Create second line of best fit
    new_df = df[df['Year'] >= 2000]                 # filtering the data, only year from 2000+
    new_year = new_df['Year']                       # getting the year column (so, it was easy to access and read)
    new_casl = new_df['CSIRO Adjusted Sea Level']   # getting the casl column (so, it was easy to access and read)

    temp = linregress(new_year, new_casl)           # linear regression from 2000 to 2050

    year_2000_2050 = pd.Series([i for i in range(2000, 2051)])    # year starting from 2000 to 2050
    pred_2 = (temp.slope * year_2000_2050) + temp.intercept       # y = mx + b, which means prediction = (slope * year) + y_int

    plt.plot(year_2000_2050, pred_2)                # plotting the second line


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()