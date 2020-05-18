#Here is the cleaner python file
#  It's used to clean data before going further in the data preparation

#Here the importation
import pandas as pd
import numpy as np

#The functions used by the DataCleaner

def IgnoreInstances(Datas, cols=[-1]):
    """ Ignore instances with error values or missing values.
        It returns the clean DataSet.
        
    Attributes:
        Datas -- the pandas data set which will be cleaned.
        cols -- the columns index, [-1] for all the columns
    """
    try:
        if (cols[0] == -1):
            return Datas.dropna()
        else:
            #Prepare the drop list
            dropL = []
            for i in cols:
                dropL.append(Datas.columns[i])
            #Drop the row with NA in specific location
            return Datas.dropna(subset=dropL)
    except:
        if not (isinstance(Datas, pd.DataFrame)):
            print("Error. Datas is not pd.DataFrame, need proper type...")
        else:    
            print("Error. Can't drop NA values...")

def MostCommonValue(Datas, cols=[-1]):
    """ The most common value of the feature replace the missing values of this feature.
        For example:
            if 2 is the most common value of the feature number_of_child
            the missing value of number_of_child will be change to 2.
        It returns the changed DataSet.
        
    Attributes:
        Datas -- the pandas data set which will be cleaned.
        cols -- the columns index, [-1] for all the columns
    """
    if (isinstance(Datas, pd.DataFrame)):
        if (cols[0] == -1):
            try:
                #We take the number of columns
                nb_col = len(Datas.columns)
                #Prepare a common_value dictionnary
                common_values = {}
                #And for each column give it the most common value
                for i in range(nb_col):
                  common_values[Datas.columns[i]] = (Datas.iloc[:,i].mode()[0])
                #Finally we return the Data set filled with most common value by column
                return Datas.fillna(value=common_values)
            except:
                print("Error (all columns). Can't fill the NA values with most common values...")
        else:
            try:
                #Prepare a common_value dictionnary
                common_values = {}
                #And for the specified column we find the most common value
                for i in cols:
                  common_values[Datas.columns[i]] = (Datas.iloc[:,i].mode()[0])
                #Finally we return the Data set filled with most common value by column
                return Datas.fillna(value=common_values)
            except:
                print("Error (list of columns). Can't fill the NA values with most common values...")
    else:
        print("Error. Datas is not pd.DataFrame, need proper type...")
        
def MeanSubstitution(Datas, cols=[-1]):
    """ Replace missing features by the mean value of the column.
        
    Attributes:
        Datas -- the pandas data set which will be cleaned.
        cols -- the columns index, [-1] for all the columns
    """
    if (isinstance(Datas, pd.DataFrame)):
        if (cols[0] == -1):
            try:
                Means = Datas.mean(axis = 0)
                print(Means)
            except:
                print("Error (all columns). Can't change the rows with NA values by most common class...")
        else:
            try:
                
            except:
                print("Error (list of columns). Can't change the rows with NA values by most common class...")
    else:
        print("Error. Datas is not pd.DataFrame, need proper type...")
