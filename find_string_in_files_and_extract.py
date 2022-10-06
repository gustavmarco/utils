# %%
from distutils import filelist
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog

# %%
# user dialog for selection of directory
root = tk.Tk()
dir = filedialog.askdirectory(parent=root, initialdir=".", title='Please select feature directory:')
xlsx_file = filedialog.askopenfilename(parent=root, initialdir=".", title='Please select feature file (.xlsx):')
slide_table = 'slide_table.csv'
excluded_table = 'excluded_table.csv'
patient_xlsx_single_table = 'patient_xlsx_single.xlsx'

patient_xlsx = pd.read_excel(xlsx_file)
patient_xlsx_single = patient_xlsx.drop_duplicates()
patient_list = patient_xlsx_single['PATIENT']

# %%
filelist = []
for file in os.listdir(dir):
        filename = os.fsdecode(file)
        if filename.endswith(".h5"):
            filelist.append(filename)

# %%
pats = pd.DataFrame([], columns=['PATIENT', 'FILENAME'])
excs = pd.DataFrame([], columns=['PATIENT'])

for patient in patient_list:
    for element in filelist:
        if patient in element:
            pats.loc[len(pats)]=([patient, element.split('.')[0]])         

for patient in patient_list:
    if patient not in pats['PATIENT'].values:
        excs.loc[len(excs)]=([patient])

print(patient_xlsx_single)
# %%
patient_xlsx_single.to_excel(patient_xlsx_single_table, index=False)
pats.to_csv(slide_table, columns=['PATIENT', 'FILENAME'], index=False)
excs.to_csv(excluded_table, columns=['PATIENT'], index=False)
