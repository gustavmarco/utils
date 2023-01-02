import os
#import tkinter as tk
#from tkinter import filedialog

# user dialog for selection of directory
dir = ''
# root = tk.Tk()
# dir = filedialog.askdirectory(parent=root, initialdir=".", title='Please select directory:')

# cut off string for each file after here 23 string elements
for file in os.listdir(dir):
    filename = os.fsdecode(file)
    if filename.endswith("ome.h5"):
        filename_p1 = filename.split('_')
        # adjust to other string length
        filename_new = filename_p1[0] + ".h5"
        os.rename(dir + "/" + filename, dir + "/" + filename_new)
        

