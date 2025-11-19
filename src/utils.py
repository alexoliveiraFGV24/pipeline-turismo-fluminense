import pandas as pd
import os


def DATA_FOLDER():
    return os.path.join(os.getcwd(), "data")


def dir_files(dir_path:str):
    onlyfiles = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    return onlyfiles


def column_strip(df:pd.DataFrame, column:str):
    df[column] = df[column].str.strip()


def remove_lines(df:pd.DataFrame, lines:list[int]):
    df.drop(lines)


def concat_dfs(dfs:list[pd.DataFrame]):
    pd.concat(dfs, ignore_index=True)


def read_excel(file:str, sheet:int=1):
    df = pd.read_excel(file, sheet_name=sheet)
    return df


def read_csv(file:str, sep:str=","):
    df = pd.read_csv(file, sep=sep)
    return df