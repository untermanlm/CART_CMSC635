import json
import pandas as pd
import numpy as np

def cat_to_int(X: pd.DataFrame):
    cat_columns = X.select_dtypes(['category']).columns
    X[cat_columns] = X[cat_columns].apply(lambda x: x.cat.codes)
def cat_to_one_hot(X: pd.DataFrame) -> pd.DataFrame:
    cat_columns = X.select_dtypes(['category']).columns
    X = pd.get_dummies(X, cat_columns)
    return X
def mean_imputation():
    print("Not yet implemented!")
def set_categorical(X: pd.DataFrame, categorical_columns: list[str]):
    for cat_column in categorical_columns:
        X[cat_column] = X[cat_column].astype('category')

def main():
    settings_filename = 'src/settings.json'
    dataset_filename = 'src/adult.csv'
    clean_dataset_filename = 'src/clean_adult.csv'
    
    # Loading system settings
    with open(settings_filename, 'r') as file:
        settings = json.load(file)
    
    adult_income = pd.read_csv(dataset_filename, index_col=False, na_values='?')

    # Could also use X.select_dtypes(['object]).columns
    categorical_columns = ['workclass', 'education', 'marital-status', 'occupation', \
                           'relationship', 'race', 'gender', 'native-country', 'income']
    
    # Changes type of categorical data from 'object' to 'categorical' for future use
    set_categorical(adult_income, categorical_columns)
    
    if settings['mean_value_imputation']:
        mean_imputation()
    elif settings['drop_missing']:
        adult_income = adult_income.dropna(axis=0)

    if settings['replace_categorical']:
        if settings['cat_to_int']:
            cat_to_int(adult_income)

        elif settings['cat_to_one_hot']:
            adult_income = cat_to_one_hot(adult_income)
            print('Warning!!!\nOne-hot encoding of categorical variables not recommended!\n' \
                          'Dramatically increases dimensionality!')

    adult_income.to_csv(clean_dataset_filename, index=False)
    print('Preprocessing done!')


if __name__ == '__main__':
    main()




