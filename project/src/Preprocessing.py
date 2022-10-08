import os
from pathlib import Path as path
import pandas as pd

# class - Preprocessing:
# a class that encapsulates some common functions to preprocess the data
# variant classes can be inherited if any customized functions need to be implemented
# all functions will be declared as @classmethod thus they can directly be accessed without any instantiation
class Preprocessing:

    @classmethod
    def load_data_csv(cls, filename:str) -> pd.DataFrame:
        print("loading dataset ...")
        # get file path - this should work on Windows / linux / Mac
        currentdir = os.path.join(os.path.dirname(__file__))
        filepath = currentdir + "/data/" + filename

        filename = path(filepath)
        if not filename.exists():
            print(" file doesn't exist ")
            return pd.DataFrame() # if file not found return an empty dataframe
        else:
            print(" found file ")
            data = pd.read_csv(filename)
            print("done")
            return data


    @classmethod
    def data_info(cls, data:pd.DataFrame) -> None:
        # print some basic info of the dataset

        # overview
        print("overview of the dataset: ")
        print(data.shape)

        # the first 5 lines
        print("the first 5 lines of the dataset: ")
        print(data.head(5))

        # print the column names
        print("the column names: ")
        print(data.columns)

        # print info about each field
        print("info about each field")
        print(data.info())


    # get missing data info
    # print the missing data info to the console
    # @return: None
    @classmethod
    def get_missing_data_info(cls, data:pd.DataFrame) -> None:
        # get the fields with NaN values and sort
        total_missing_data_info = data.isnull().sum().sort_values(ascending=False)
        print("field - with - NaN - values ----------------------------------------------------")
        print(total_missing_data_info)
        print()

        # get the percentage of the NaN fields
        # percentage allows us to apply different filling strategies, i.e., fill with median / remove the NaN records
        missing_data_percentage =(data.isnull().sum()/data.isnull().count()).sort_values(ascending=False)
        missing_data = pd.concat([total_missing_data_info, missing_data_percentage], axis=1, keys=['Total numbers', 'Percentage'])
        print("info about missing_data ---------------------------------------------------------")
        print(missing_data)
        

    # get missing attribute list
    @classmethod
    def get_missing_attribute_list(cls, data:pd.DataFrame) -> list:
        total_missing_data_info = data.isnull().sum().sort_values(ascending=False) # total_missing_data_info -> type: pandas.core.series
        
        # add missing attributes to a temp list
        missing_attribute_list = []

        # specify null value, usually it is equal to 0 -> 0 can be int/float/double
        # it should however be noted that, this threshold can be altered if users want to get rid of rows with low occurrences        
        NULL_VALUE_THRESHOLD = 0
        EPSILON = 1e-8 # if more accuracy is desired, for example 1e-15 can be used
        for Attri in total_missing_data_info.index:
            if(abs(total_missing_data_info[Attri] - NULL_VALUE_THRESHOLD) > EPSILON):
                missing_attribute_list.append(Attri)
        
        # now let's judge if the list is empty
        if not missing_attribute_list:
            print("no missing attributes found, will return an empty missing attribute list")
            return missing_attribute_list
        else:
            print("missing attribute list constructed, the following list will be obtained")
            print(missing_attribute_list) # print functions can slow down the efficiency a bit, now let's just use it to prompt some info
            return missing_attribute_list


    # WARNING:
    # this function is used for removing ALL rows which contain empty attributes
    # extra care needs to be taken -> some attributes are not really 'NaN', there can be intervals
    # i.e., an attribute can be recorded every for example 10 rows
    # process NaN values in the dataset (if any) according to the missing attributes
    # @return: a new dataset
    @classmethod
    def process_missing_data_removing(cls, data:pd.DataFrame) -> pd.DataFrame:

        Attri = 'OBS_VALUE' # specify the column here - this can be different for different dataset
        print("removing all rows with {0} == NULL".format(Attri))
        data_with_missing_removed = data.drop(data[data[Attri].isnull()].index)
        print("done")
        print()

        print("missing data info after NaN values removed --------------------------------------")
        missing_data_info_after = data_with_missing_removed.isnull().sum().sort_values(ascending=False)
        print(missing_data_info_after)


    @classmethod
    def print(cls) -> None:
        print("test preprocessing function")

    

def main():
    # entry point
    #Preprocessing.print()
    original_data = Preprocessing.load_data_csv("road_pa_mov_linear.csv")
    #Preprocessing.data_info(original_data)
    Preprocessing.get_missing_data_info(original_data)
    Preprocessing.get_missing_attribute_list(original_data)
    #data_without_nan_values = Preprocessing.process_nan_values(original_data)
    pass

if __name__ == "__main__":
    main()   
    pass
    