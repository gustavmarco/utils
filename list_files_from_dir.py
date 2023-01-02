# %%
import os
import pandas as pd

# user dialog for selection of directory
feature_dir = '/home/marcogustav/Documents/projects/geneva/data/geneva_features_xiyuewang/'
output_dir = '/home/marcogustav/Documents/projects/geneva/tables/'

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
clini_table.to_excel(output_dir+'GENEVA-CRC-DX_CLINI_blind.xlsx', index=False)
slide_table.to_csv(output_dir+'GENEVA-CRC-DX_SLIDE_blind.csv', index=False)

# %%
