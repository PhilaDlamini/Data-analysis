'''Import data from csv file'''
from pandas import read_csv;
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data';
dataframe = read_csv(url, header = None);
dataframe.columns = ['symboling', 'normalized-loses', 'make', 'fuel type', 'aspiration', 'num of doors', 'body style', 'drive wheels'
                , 'engine location', 'wheel base', 'length', 'width', 'height', 'curb weight', 'engine type', 
                'number of cylinders', 'engine size', 'fuel systems', 'bore', 'stroke', 'compression ratio', 'horsepower', 'peak', 'city', 'highway', 'price'];

print('The top 10 rows of data');
print(dataframe.head(10));
dataframe.to_csv('data.csv');

#More methods on the dataframe
print(dataframe.dtypes); #Shows the type for each column
print(dataframe.describe(include = "all")); #Gives statistical summary for all columns (by default, avoids non-int ones)
print(dataframe.info()); #Apparantly, snows info about top 30 and bottom 30 rows of dataframe (but it does not look like this here)

#When we use the option describe(include = "all"), all columns (including ones of object type) will be shown in the statistical summary, but will just shown NaN (not a number). 
#We do add unique (number of distinct objects), top (the most frequently appearing object), and freq (number of times first obj appears) though