# imports
import pandas as pd
import matplotlib.pyplot as plt
import graph_plotter as gp

# get the students data
results_DF = pd.read_csv('results.csv', index_col='ID')

# average of each student
mean_students = results_DF.mean(axis='columns')

# insert average column into original dataframe
results_DF["AVERAGE MARKS"] = mean_students

# average of each subject and also the mean average
mean_subjects = results_DF.mean(axis='index')

# sort dataframe based on the average column
results_DF.sort_values("AVERAGE MARKS", inplace = True, ascending = False)

# get values to use for graphs
ids = results_DF.index
averages = results_DF["AVERAGE MARKS"]

# convert values obtained to floats
pd.to_numeric(ids, downcast="float")
pd.to_numeric(averages, downcast="float")

# create and save graphs
gp.hist_plotter(averages, "Students", "Marks", "hist_png", "png")
gp.hist_plotter(averages, "Students", "Marks", "hist_pdf", "pdf")

# create dictionary with values to insert
new_row = {}
for column, mean_subject in zip(results_DF.columns, mean_subjects):
    new_row[column] = mean_subject

# insert values of average into the main data frame
row_series = pd.Series(data=new_row, name="ALL AVERAGES")
results_DF = results_DF.append(row_series, ignore_index = False)

# store analysis in a csv file
results_DF.to_csv('general_analysis.csv')