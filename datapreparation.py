import numpy as np
import pandas as pd

nan_threshold = 0.1

def info(df):
    print("Dataset elements:", df.values.size)
    print("Dataset cols:", df.columns.size)

    print("\nNaN values:")
    cols = df.columns
    for col in cols:
        nan = df[col].isna().sum()
        tot = df[col].size
        percentage = round(nan/tot, 2)
        if percentage > nan_threshold :
            print(col, tot, nan, percentage)

    # remove duplicates
    df = remove_duplicates(df)


def remove_duplicates(df):
    old_size = df.values.size
    df = df.drop_duplicates()
    print("\nRemoved duplicates:", old_size - df.values.size)
    return df

if __name__ == '__main__':
    df = pd.read_csv("datasets/Big_Cities_Health_Data_Inventory.csv")

    info(df)