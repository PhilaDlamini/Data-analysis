'''Load data from either a url, or an excel file, as specified'''
from pandas import read_csv, read_excel;

FROM_CSV = 1;
FROM_EXCEL = 2;

def loadData(source, path, headers):
    if source == FROM_CSV:
        dataframe = read_csv(path, header = None);
    else:
        dataframe = read_excel(path, header = None);
        
    dataframe.columns = headers;
        
    print('All read data');
    print(dataframe.head(5));
    print('Information about this data');
    print(dataframe.dtypes);
    print(dataframe.describe(include = 'all'));
    print(dataframe.info());
    
    #Save the data to a file here
    dataframe.to_csv('read_data.csv');


loadData(FROM_EXCEL, r'C:\Users\phila\Downloads\sample_data.xlsx', ['Year', 'GPA', 'Salary']);
    

loadData(FROM_CSV, 'http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data', 
         ['symboling', 'normalized-loses', 'make', 'fuel type', 'aspiration', 'num of doors', 'body style', 'drive wheels'
                , 'engine location', 'wheel base', 'length', 'width', 'height', 'curb weight', 'engine type', 
                'number of cylinders', 'engine size', 'fuel systems', 'bore', 'stroke', 'compression ratio', 'horsepower', 'peak', 'city', 'highway', 'price']);
    
    
