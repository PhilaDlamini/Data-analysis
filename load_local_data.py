'''Load from local excel file'''
from pandas import read_excel;

dataframe = read_excel(r'C:\Users\phila\Downloads\sample_data.xlsx', head = None);
dataframe.columns = ['Year','GPA', 'Salary'];
dataframe.to_csv('dataset2.csv');

#More methods on the dataframe
print(dataframe.dtypes); #Get all the types for each row
print(dataframe.describe(include = 'all')); #Get statistical summary for each column, includes even non-int ones
print(dataframe.info());

#Remember, unique = number of distinct objects, top = most frequently appearing object, freq = number of times first object appears