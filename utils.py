import pandas as pd

def load_datasets():
    datasets = {}

    datasets['dataset_1'] = pd.read_csv("C:\\Users\\arpitha_work\\Downloads\\arya\\datasets\\dataset 1.csv")
    datasets['dataset_2'] = pd.read_csv("C:\\Users\\arpitha_work\\Downloads\\arya\\datasets\\dataset 2.csv")
    datasets['dataset_3'] = pd.read_csv("C:\\Users\\arpitha_work\\Downloads\\arya\\datasets\\dataset 3.csv")
    datasets['dataset_4'] = pd.read_csv("C:\\Users\\arpitha_work\\Downloads\\arya\\datasets\\dataset 4.csv")
    datasets['dataset_5'] = pd.read_csv("C:\\Users\\arpitha_work\\Downloads\\arya\\datasets\\dataset 5.csv")

    return datasets


def basic_preprocess(df, target_column):
    df = df.dropna(subset=[target_column])
    df = df.dropna(axis=1, thresh=int(len(df) * 0.7))
    df = df.fillna(0)

    # Move target column to the end temporarily
    target = df[target_column]
    df = df.select_dtypes(include=['int64', 'float64'])
    
    # Put target back
    df[target_column] = target

    return df

