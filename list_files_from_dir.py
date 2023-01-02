# %%
import os
import pandas as pd

# user dialog for selection of directory
feature_dir = '/.../'
output_dir = '/.../'

# %%
file_list = []

# cut off string for each file after here 23 string elements
for file in os.listdir(feature_dir):
    filename = os.fsdecode(file)
    if filename.endswith(".h5"):
        file_list.append(str(filename).split('.')[0])

file_list.sort()
#%%   
clini_table = pd.DataFrame(columns=['PATIENT', 'isMSIH'])
slide_table = pd.DataFrame(columns=['PATIENT', 'FILENAME'])
clini_table['PATIENT'] = file_list
clini_table['isMSIH'] = 'MSIH'
slide_table['PATIENT'] = file_list
slide_table['FILENAME'] = file_list

# %%
clini_table.to_excel(output_dir+'clini.xlsx', index=False)
slide_table.to_csv(output_dir+'slide.csv', index=False)

# %%
