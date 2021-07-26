"""
## 
## This script has been developed for 
## DXC UCMS Case Id - 32883
## Script file name - 32883_SCCM_SW_ADDL.py
## Last update date - 2021-04-09
## Script version - v1-0
## Developed by - debajyoti.dutta@dxc.com; dutta.debajyoti@gmail.com
## 
"""

import os, sys
import pandas as pd
import numpy as np
import csv
import tkinter as tk
from tkinter import *
from tkinter import ttk 
from tkinter import filedialog

root = tk.Tk()
root.title("32883_SCCM_SW_ADDL") 
root.iconbitmap()
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
root.geometry(f"{screenwidth}x{screenheight}")
screenwidth = int(screenwidth*.95)
screenheight = int(screenheight*.8)
root.geometry("{}x{}+10+10".format(screenwidth,screenheight))
left_offset = 10
top_offset = 10
root.geometry("{}x{}+{x}+{y}".format(screenwidth,screenheight,x=left_offset,y=top_offset))
root.update_idletasks()
# print(root.winfo_geometry())

# Create the primary frame
primary_frame = Frame(root )
# primary_frame.pack(fill="both", expand=1)
primary_frame.grid()

## Defining all functions. All functions will be under primary frame

### GUI close function    
def close_gui():
    root.destroy()

### File open function
def file_open():
    _filename = filedialog.askopenfilename(
        initialdir = "",
        title = "Select your file",
        filetype = (("all files","*.*"),("xlsx files","*.xlsx"),("xls files","*.xls"),("csv files","*.csv"))
    )
    _filename = r"{}".format(_filename)
    _filetype = os.path.splitext(_filename)[1]
    _filetype = _filetype[1]
    _label_1_.configure(text="You have seleted  {}  , which is a  {}  type of file".format(_filename, _filetype[1]))
            # df = pd.read_excel(_filename)
    # if _filename:
    #     try:
    #         _filename = r"{}".format(_filename)
    #         # _filename_txtbx_prd_.insert(1.0, _filename)   
    #         _filetype = os.path.splitext(_filename)[1]
    #         _filetype = _filetype[1]
    #         _label_1_.config(text="You have seleted  {}  , which is a  {}  type of file".format(_filename, _filetype[1]))
    #         # df = pd.read_excel(_filename)
    #     except ValueError:
    #         _filename_txtbx_prd_.text("File couldn't be opened..")
    #     # except FileNotFoundError:
    #         # my_label.config(text="File couldn't be found..")
    # # return(_filename,_filetype)

def close_session():
    my_notebook.forget()

def new_session():
    frame_2_ = ttk.Frame(my_notebook)
    my_notebook.add(frame_2_, text="New Tab")
    
    
    # tab_close_btn1 = Button(frame_1_, text="Kill Session").place(x=1,y=1)
    # tab_close_btn2 = Button(frame_2_, text="Kill Session", command=kill_session(my_notebook)).place(x=1,y=1)



# close_gui_button = Button(primary_frame, text="Close", command=close_gui).place(x=0, y=0)

## Add a menu object
my_menu = Menu(root)
root.config(menu=my_menu)

## Add a menu dropdown
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=close_gui)

gui_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="New Session", command=new_session)
my_menu.add_cascade(label="Close Session", command=close_session)
gui_menu.add_command(label="Close", command=close_gui)

my_menu.add_cascade(label="Close", command=close_gui),

##-------------------------Creating the Tabbed interface part
my_notebook = ttk.Notebook(primary_frame)
frame_1_ = LabelFrame(my_notebook, text="SCCM SW ADDL", padx=10)
my_notebook.add(frame_1_, text="Default")
# my_notebook.pack(fill = "both", expand=1)
my_notebook.grid()  

##------------------------- Creating treeview
my_tree = ttk.Treeview(frame_1_)

_label_1_ = Label(frame_1_, text='Browse for the PROD file', font=("Helvetica",9), justify=LEFT, wraplength=600, relief="flat", padx=10).grid(row=0, column=0,sticky=W)
_filename_txtbx_prd_ = tk.Text(frame_1_, padx=10, wrap=tk.WORD, width=100, height=5, font=("Helvetica",9)).grid(row=2,column=0)
_browse_btn_1_ = tk.Button(frame_1_, text="Browse", command=lambda:file_open()).grid(row=2,column=1)

_label_2_ = Label(frame_1_, text='Browse for the TEXT file', font=("Helvetica",9), justify=LEFT, wraplength=200, relief="flat", padx=10).grid(row=3, column=0, sticky=W)
_filename_txtbx_txt_ = tk.Text(frame_1_, padx=10, wrap=tk.WORD, width=100, height=5, font=("Helvetica",9)).grid(row=4,column=0)
_browse_btn_2_ = tk.Button(frame_1_, text="Browse", command=lambda:file_open()).grid(row=4,column=1)



def __df_creation__():
    _prd_filepath = r'C:\DEB\DXC_Automation\UCMS_32883_Software SCCM file enhancement\CBA_SCCM_SW_ADDL_COLS_Headers_23022020\CBA_CM_Sinv_PRD.SoftwareList.csv'
    _tst_filepath = r'C:\DEB\DXC_Automation\UCMS_32883_Software SCCM file enhancement\CBA_SCCM_SW_ADDL_COLS_Headers_23022020\CBA_CM_Sinv_TST.SoftwareList.csv\CBA_CM_Sinv_TST.SoftwareList.csv'

    with open(_prd_filepath) as _csvfile:
        _dialect = csv.Sniffer().sniff(_csvfile.read(14734))
    _prd_chunks = pd.read_csv(_prd_filepath, iterator=True, chunksize=10000, sep=',', quotechar='"', verbose=True, low_memory=True, encoding="ISO-8859-1", index_col=None, engine='python', error_bad_lines=False, dialect=_dialect)
    df_prd = pd.concat(_prd_chunks, ignore_index=True)

    with open(_tst_filepath) as _csvfile:
        _dialect = csv.Sniffer().sniff(_csvfile.read(14734))
    _tst_chunks = pd.read_csv(_tst_filepath, iterator=True, chunksize=10000, sep=',', quotechar='"', verbose=True, low_memory=True, encoding="ISO-8859-1", index_col=None, engine='python', error_bad_lines=False, dialect=_dialect)
    df_tst = pd.concat(_tst_chunks, ignore_index=True)

    print(df_prd.columns, df_prd.shape, df_prd.info())
    print(df_tst.columns, df_tst.shape, df_tst.info())




root.mainloop()