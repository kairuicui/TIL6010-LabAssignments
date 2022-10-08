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


    @classmethod
    def print(cls) -> None:
        print("test preprocessing function")

def main():
    # entry point
    Preprocessing.print()
    data = Preprocessing.load_data_csv("/owid-covid-data.csv")
    Preprocessing.data_info(data)
    pass

if __name__ == "__main__":
    main()   
    pass
    