import numpy as np
import pandas as pd

nan_threshold = 0.1

def info(df):
    print("NaN values:")
    cols = df.columns
    for col in cols:
        nan = df[col].isna().sum()
        tot = df[col].size
        percentage = round(nan/tot, 2)
        if percentage > nan_threshold :
            print(col, tot, nan, percentage)

    count_duplicates(df)


def count_duplicates(df):
    print("\nDuplicated rows:")
    print(df[df.duplicated()].size)


if __name__ == '__main__':
    df = pd.read_csv("datasets/Big_Cities_Health_Data_Inventory.csv")

    info(df)