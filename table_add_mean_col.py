import pandas as pd

# path of table folder
path = '/home/.../'
# path of table
tabular_data = pd.read_csv(path + 'table.csv', encoding='latin1')

# find columns with numerical entries and loop through all of them
numeric_cols_orig = tabular_data.select_dtypes(include=['int', 'float'])
for name in numeric_cols_orig.columns:
    # choose columns with values that are not only 0, 1, NaN
    if tabular_data[name].dropna().nunique() > 2:
        mean = tabular_data[name].mean()
        # rename old cols so that given targets are taken from newly created columns (which include mean)
        tabular_data.rename(columns={name: name+'_num'}, inplace=True)
        # create new columns with classification (higher/lower than mean) with column names from original columns
        tabular_data[name] = ['high' if x > mean else 'low' if x < mean else 'NaN' for x in tabular_data[name+'_num']]

# reorder dataframe
tabular_data.sort_index(axis=1, inplace=True)

# define first three columns for better readability
first_col= tabular_data.pop('PATIENT')
tabular_data.insert(0, 'PATIENT', first_col)

# export df to csv
tabular_data.to_csv(path + 'GECCO_EPIC_CORSA_WHI_CLINI_num.csv', index=False)



