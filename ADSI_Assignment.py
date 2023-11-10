# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 10:35:22 2023

@author: aishw
"""

import pandas as pd
import matplotlib.pyplot as plt

# Visualisation 1 : (Line Plots)

#Function1 : Reading file into DataFrame and customising the rows and columns
     
def process_and_print_seasonal_data(file_path, start_year=2000, end_year=2022):
    
    """ Defining the function1 to : 
        Read file into dataframe 
        filter data for the years 2000-2022
        Calculate max and min rainfall during the seasons over the years (2000-2022)
        Rename the columns"""
    
    df_UK = pd.read_excel(file_path)
    
    df_seasonal = pd.DataFrame(df_UK[(df_UK["year"] >= start_year) & (df_UK["year"] <= end_year)],
                               columns=["year", "win", "spr", "sum", "aut"])


    df_seasonal["max"] = df_seasonal[["win", "spr", "sum", "aut"]].max(axis=1)
    df_seasonal["min"] = df_seasonal[["win", "spr", "sum", "aut"]].min(axis=1)
    
    df_seasonal.rename(columns={"year": "Year",
                                "win": "Winter",
                                "spr": "Spring",
                                "sum": "Summer",
                                "aut": "Autumn",
                                "max": "Maximum_rainfall",
                                "min": "Minimum_rainfall"}, inplace=True)

    return df_seasonal


#Function2: To Line plot1-Max and Min seasonal rainfall in UK from 2000 to 2022

def plot_max_min_rainfall(df_seasonal):
    
    """ Defining the function2 to create a line plot1 to represent 
        max and min rainfall during seasons over the years with labels, 
        customizing visualization and to set title, X and Y axis labels 
        and show the legend for lineplot1"""
        
    plt.subplot(1, 2, 1)
    plt.plot(df_seasonal["Year"], df_seasonal["Maximum_rainfall"], marker="o", label="Maximum rainfall", color="green")
    plt.plot(df_seasonal["Year"], df_seasonal["Minimum_rainfall"], marker="o", label="Minimum rainfall", color="red")
    plt.legend(title="Max and Min rainfall", borderpad=0.5, fontsize=9)
    plt.title("Max and Min seasonal rainfall in UK")
    plt.xlabel("Years")
    plt.ylabel("Rainfall precipitation in millimetres (mm)")
    plt.xticks(df_seasonal["Year"])
    
    
#Function3: To Line plot2- Seasonal rainfall in UK from 2000 to 2022

def plot_seasonal_rainfall(df_seasonal):
    
    """ Defining the function3 to create a line plot2 to represent 
        rainfall for four seasons in UK from 2000 to 2022 and customizing 
        visualization with labels,color. Also to Set title & X and Y axis labels 
        and show the legend for lineplot2"""
    
    plt.subplot(1, 2, 2)
    plt.plot(df_seasonal["Year"], df_seasonal["Winter"], label="winter", color="green")
    plt.plot(df_seasonal["Year"], df_seasonal["Spring"], label="spring", color="red")
    plt.plot(df_seasonal["Year"], df_seasonal["Summer"], label="summer", color="orange")
    plt.plot(df_seasonal["Year"], df_seasonal["Autumn"], label="autumn", color="brown")
    plt.legend(title="Seasonal Rainfall", borderpad=0.5, fontsize=9)
    plt.title("Seasonal rainfall in UK")
    plt.xlabel("Years")
    plt.ylabel("Rainfall precipitation in millimetres (mm)")
    plt.xticks(df_seasonal["Year"])

# Defining filename
file_path = "UK_rainfall.xlsx"

# Assigning the functions to a variable
df_seasonal_data = process_and_print_seasonal_data(file_path)

# print the data
print(df_seasonal_data)

# plot the line plots1 & 2
plt.figure(figsize=(30, 8))
plot_max_min_rainfall(df_seasonal_data)
plot_seasonal_rainfall(df_seasonal_data)

# save and show the plot
plt.savefig("UK_seasonal_rainfall.png")
plt.show()


# Visualisation 2 : (Pie chart)

#Function4:To read the file into DataFrame 

def read_and_print_data(file_path):
    
    """ Defining the function4 to read the data from CSV file"""
    
    df_diversity = pd.read_csv(file_path)
    print(df_diversity)
 

#Function5:To plot pie of Ethnicity Percentage of Asians in England and Wales Regions

def plot_ethnicity_percentage(df_diversity, ethnicity="Asian"):
    
     """ Defining the function5 to filter data for the specified ethnicity and 
          to extract the necessary columns and region and percentage of ethnic 
          group. Setting explode values, title and show the legend to 
          plot the pie and save and show the pie"""
    
     df_ethnicity = pd.DataFrame(df_diversity[df_diversity["Ethnicity"] == ethnicity], 
                                 columns=["Ethnicity", 
                                          "Region", 
                                          "percentage of ethnic group"])
     print(df_ethnicity)
     
     region = df_ethnicity["Region"] 
     per_ethnic = df_ethnicity["percentage of ethnic group"]
     explode = (0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0) 
    
     
     plt.figure(figsize=(40, 20))
     plt.pie(per_ethnic, explode=explode, labels=region, startangle=45, autopct='%1.1f%%') 
     plt.legend(region, title="Region", borderpad=1, fontsize=11)
     plt.title(f"Ethnicity Percentage of {ethnicity}s in England and Wales Regions", 
               fontsize=25)
     plt.savefig(f"Ethnicity_Percentage_{ethnicity}.png")
     plt.show()

# Defining the filename and calling the functions
file_path = "Diversity.csv"
read_and_print_data(file_path)
plot_ethnicity_percentage(pd.read_csv(file_path), ethnicity="Asian")


#Visualisation 3: (Bar chart) 

#Function6:To read the file into DataFrame 

def read_and_process_data(file_path, start_year, end_year):
    
    """ Defining function6 to Read file into dataframe, 
       filtering data for the specified years, to 
       Calculate average precipitation per year and to rename the columns """
     
    df_UK = pd.read_excel(file_path)
 
    df_yearly = pd.DataFrame(df_UK[(df_UK["year"] >= start_year) & (df_UK["year"] <= end_year)],
                             columns=["year", "jan", "feb", 
                                      "mar", "apr", "may", 
                                      "jun", "jul", "aug", 
                                      "sep", "oct", "nov", "dec"])
     
    df_yearly["Average"] = df_yearly[["jan", "feb", "mar", 
                                      "apr", "may", "jun", 
                                      "jul", "aug", "sep", 
                                      "oct", "nov", "dec"]].mean(axis=1)
     
    df_yearly.rename(columns={"year": "Year",
                              "jan": "January",
                              "feb": "February",
                              "mar": "March",
                              "apr": "April",
                              "may": "May",
                              "jun": "June",
                              "jul": "July",
                              "aug": "August",
                              "sep": "September",
                              "oct": "October",
                              "nov": "November",
                              "dec": "December",
                              "Average": "Average"}, inplace=True)
    
    return df_yearly

#Function7 : To plot Bar Chart of Average rainfall per year (2000 – 2022)

def plot_average_rainfall(df_yearly):
    
    """ Defining function7 to plot the bar chart and custamizing it to set 
    a title,labelling X and Y axis and legend. Saving the output as png 
    and to Show the plot"""
    
    plt.figure(figsize=(20, 8))
    plt.bar(df_yearly["Year"], df_yearly["Average"])
    plt.title("Average precipitation of rainfall per years (2000 - 2022)", 
              fontweight='bold', fontsize=10)
    plt.xlabel("Years (2000-2022)", fontweight='bold', fontsize=13) 
    plt.ylabel("Rainfall precipitation (mm)", fontweight='bold', fontsize=13)
    plt.xticks(df_yearly["Year"])
    plt.legend(df_yearly["Year"], title="Max Average rainfall", borderpad=1, fontsize=11)
    plt.savefig("Average_rainfall_per_year.png")
    plt.show()

# Defining the filename, start and end year
file_path = "UK_rainfall.xlsx"
start_year = 2000
end_year = 2022

# Assigning function to a variable and to print it
df_yearly_data = read_and_process_data(file_path, start_year, end_year)
print(df_yearly_data)
plot_average_rainfall(df_yearly_data)

