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

def __source_file_path__():
    pass

def __df_creation__():
    print("Enter the FULL path of the Prod file ... ")
    _prd_filepath = input(r':: ')
    _prd_filepath = r'C:\DEB\DXC_Automation\UCMS_32883_Software SCCM file enhancement\CBA_SCCM_SW_ADDL_COLS_Headers_23022020\CBA_CM_Sinv_PRD.SoftwareList.csv'
    print("Processing ... Prod file ...")
    with open(_prd_filepath) as _csvfile:
        _dialect = csv.Sniffer().sniff(_csvfile.read(14734))
    _prd_chunks = pd.read_csv(_prd_filepath, iterator=True, chunksize=100000, verbose=False, low_memory=True, encoding="ISO-8859-1", index_col=False, engine='python', error_bad_lines=False, dialect=_dialect)
    df_prd = pd.concat(_prd_chunks, ignore_index=True)
    # print(df_prd.columns, df_prd.shape, df_prd.info())
    print("Prod file has  {}  rows and  {}  columns".format(df_prd.shape[0],df_prd.shape[1]))

    print("Enter the FULL path of the Test file ... ")
    _tst_filepath = input(r':: ')
    _tst_filepath = r'C:\DEB\DXC_Automation\UCMS_32883_Software SCCM file enhancement\CBA_SCCM_SW_ADDL_COLS_Headers_23022020\CBA_CM_Sinv_TST.SoftwareList.csv\CBA_CM_Sinv_TST.SoftwareList.csv'
    print("Processing ... Test file ...")
    with open(_tst_filepath) as _csvfile:
        _dialect = csv.Sniffer().sniff(_csvfile.read(14734))
    _tst_chunks = pd.read_csv(_tst_filepath, iterator=True, chunksize=10000, verbose=False, low_memory=True, encoding="ISO-8859-1", index_col=False, engine='python', error_bad_lines=False, dialect=_dialect)
    df_tst = pd.concat(_tst_chunks, ignore_index=True)
    # print(df_tst.columns, df_tst.shape, df_tst.info())
    print("Test file has  {}  rows and  {}  columns".format(df_tst.shape[0],df_tst.shape[1]))

    print("Merging Prod and Test file ...")
    dfmerged = df_prd.append(df_tst, ignore_index=True)
    # print(dfmerged.columns, dfmerged.shape, dfmerged.info())
    print("Combined raw data dump has  {}  rows and  {}  columns".format(dfmerged.shape[0],dfmerged.shape[1]))
    return dfmerged
#----------------------------------------------------------------------------------------------------    
def __capture_columns_to_search_(_col_list_):
    _full_list_ = _col_list_
    print("\nThe available columns are ...\n")
    for _f_ in range(len(_full_list_)):
        print("{}. {}".format((_f_+1),_full_list_[_f_]))
    print("Please select the column number / s to search for" + "\n\t(For multiple column selection," + "\n\tUse comma OR semicolon OR space in between)... :: ", end="")
    _selection_ = input()
    _selection_ = _selection_.replace(" ",",")
    _selection_ = _selection_.replace(";",",")
    _selection_ = _selection_.replace(",,",",")
    while (_selection_.count(",,",1) >=1):
        _selection_ = _selection_.replace(",,",",")
    # print(_selection_, type(_selection_))
    _selection_ = _selection_.split(sep=",")
    # print(_selection_, type(_selection_))
    for _i_ in range(len(_selection_)):
        # print(_selection_[_i_], type(_selection_[_i_]))
        if _selection_[_i_] == '':
            _selection_.pop(_i_)
    print(_selection_)
# TODO add invalid selection logic like 0 etc - upper bound etc
    print("You have selected the following columns ... :")
    _selected_cols_ = list()
    for _f_ in _selection_:
        print("{}. {}".format(_f_,_full_list_[int(_f_)-1]))
        # print(_f_,type(_f_))
        # print(int(_f_),type(_f_))
        _selected_cols_.append(_full_list_[int(_f_)-1])

    return _selected_cols_
    # pass

#------------------------------------------------- M A I N  S E C T I O N -------------------------------------------------- 

print("Started...")

_dfmerged_ = __df_creation__()
print("Ended...")
# print(type(_dfmerged_))
# print(type(_dfmerged_.columns))
_col_list = list(_dfmerged_.columns)
# print(col_list)
_selected_columns = __capture_columns_to_search_(_col_list)
# Brand detail is available in Column I(Publisher) and if OSType is XP/8.1/10 then it should be a EUC device remaining other OS belongs to Servers.
# SoftwareDescription
_sw_desc_PIVOT_ = pd.pivot_table(_dfmerged_, values="ComputerName", index=["SoftwareDescription"], columns=["OSType"])
print(_sw_desc_PIVOT_)

