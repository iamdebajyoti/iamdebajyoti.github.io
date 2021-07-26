"""
## 
## This script was developed for 
## DXC UCMS Case Id - 29864
## Script file name - 29864_Stranded_Assets.py
## Last update date - 2021-04-29
## Script version - v1-2
## Developed by - debajyoti.dutta@dxc.com; dutta.debajyoti@gmail.com
## 
"""

#%%
import os, psutil
import pandas as pd
import numpy as np
import datetime
from pandas import ExcelWriter
import datetime
# from datetime import datetime
#%%
def phase1():
    #----------common part
    _message_ = " INITIAL SETUP "
    print("\n\t" + "="*(len(_message_)+8) + "\n\t" + "~"*4 + _message_ + "~"*4 + "\n\t" + "="*(len(_message_)+8) +"\n")


    _script_dir = os.path.dirname(os.path.abspath(__file__))
    # print(_script_dir) #..//CodeCheck
    _source_file_path = r"C:\DEB\DXC_Automation\UCMS_29864__Stranded Assets - Automation\_input_"

    _message_ = "SET File / Folder paths and Filenames with file extensions --"
    print("\n\t" + "="*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "="*(len(_message_)+8) +"\n")

    # Phase 1 file/s
    ###########################################################################
    # AD files
    _message_ = "FOLDER  -->>  Source folder for AD files"
    print("\n\t"+_message_+"\n\t", end="")
    _ad_files_path = input(r' :: ')
    # _ad_files_path = r"C:\DEB\DXC_Automation\UCMS_29864__Stranded Assets - Automation\_input_\AD_files"
    _ad_files_path = os.path.abspath(_ad_files_path)
    print("\n\t" + ">->->  " + _ad_files_path)

    # 772 file
    _message_ = "FILE  -->>  Full PATH and File name with extension of \"772\" file "
    print("\n\t"+_message_+"\n\t", end="")
    _file_772 = input(r' :: ')
    # _file_772 = r"C:\DEB\DXC_Automation\UCMS_29864__Stranded Assets - Automation\_input_\EXTNMSC_AP_AM772.csv"
    _file_772 = os.path.abspath(_file_772)
    print("\n\t" + ">->->  " + _file_772)

    # Redeployment file
    _message_ = "FILE  -->>  Full PATH and File name with extension of \"REDEPLOYMENT\" file "
    print("\n\t"+_message_+"\n\t", end="")
    _file_redeploy_list = input(r' :: ')
    # _file_redeploy_list = r"C:\DEB\DXC_Automation\UCMS_29864__Stranded Assets - Automation\_input_\CBA Hardware Redeployment Report - 290121.xlsb"
    _file_redeploy_list = os.path.abspath(_file_redeploy_list)
    print("\n\t" + ">->->  " + _file_redeploy_list)

    # Cancelled file
    _message_ = "FILE  -->>  Full PATH and File name with extension of \"CANCELLED\" file "
    print("\n\t"+_message_+"\n\t", end="")
    _file_Cancelled = input(r' :: ')
    # _file_Cancelled = r"C:\DEB\DXC_Automation\UCMS_29864__Stranded Assets - Automation\_input_\Cancelled Tickets (1).xlsx"
    _file_Cancelled = os.path.abspath(_file_Cancelled)
    print("\n\t" + ">->->  " + _file_Cancelled)

    # Sanoja's file
    _message_ = "FILE  -->>  Full PATH and File name with extension of \"SANOJA'S\" file "
    print("\n\t"+_message_+"\n\t", end="")
    _file_Sanoja = input(r' :: ')
    # _file_Sanoja = r"C:\DEB\DXC_Automation\UCMS_29864__Stranded Assets - Automation\_input_\Sanoja's file.xlsx"
    _file_Sanoja = os.path.abspath(_file_Sanoja)
    print("\n\t" + ">->->  " + _file_Sanoja)

    # #Sweep Asset file #--------------------- removed from end-user's requirement
    # _message_ = "FILE  -->>  Full PATH and File name with extension of \"SWEEP ASSET\" file "
    # print("\n\t"+_message_+"\n\t", end="")
    # _file_SweepAsset = input(r' :: ')
    # # _file_SweepAsset = r"C:\DEB\DXC_Automation\UCMS_29864__Stranded Assets - Automation\_input_\Sweep Asset_HPAM upto 17th Nov2020.xlsb"
    # _file_SweepAsset = os.path.abspath(_file_SweepAsset)
    # print("\n\t" + ">->->  " + _file_SweepAsset)

        #%%
    _message_ = "PHASE 1 Started..."
    print("\n\t" + "="*(len(_message_)+16) + "\n\t" + " "*4 + "="*(len(_message_)+8) + "\n\t" + " "*8 + _message_ + " "*8  + "\n\t" + "="*(len(_message_)+16) +"\n")

    #%%
    ##### STEP 0 #####
    ##### AD REPORT COMPILATION #####

    # os.chdir(_ad_files_path)  
    df_Compiled_AD_files = pd.DataFrame()
    _message_ = "Compilation of AD files started ..."
    print("\t" + "="*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "="*(len(_message_)+8))

    file_name = ""
    for files_ in (os.listdir(_ad_files_path)):
        file_name = os.path.join(_ad_files_path,files_)
        df_Temp = pd.DataFrame()
    #     print(files_)
        Temp = pd.read_csv(file_name, iterator=True, low_memory=False)
        df_Temp = pd.concat(Temp, ignore_index=True)
        df_Compiled_AD_files = pd.concat([df_Compiled_AD_files, df_Temp], ignore_index=True)
        print("\tThe file  {}  has  {}  rows and  {}  columns and the compiled file has  {}  rows.".\
            format(files_,df_Temp.shape[0], df_Temp.shape[1], df_Compiled_AD_files.shape[0]))
    print("\n\tVerify: The compiled AD files contains  {}  rows and  {}  columns.".format(df_Compiled_AD_files.shape[0],df_Compiled_AD_files.shape[1]))
    # print("df_Compiled_AD_files INFO")

    ## formatting Scan Dates to sort by Serial Number and then by formatted Scan Dates in DESCENDING order - this will push the row with older scan date to the bottom if there are multiple scan dates for the same serial number
    df_Compiled_AD_files['ScanDateFormated'] = pd.to_datetime(pd.to_datetime(df_Compiled_AD_files["ScanDate"]).dt.strftime('%d-%m-%Y'))
    df_Compiled_AD_files.sort_values(by=['SerialNumber','ScanDateFormated'],inplace=True, ascending=False)
    print("\t" +"Formatted the scan dates..... and sorted in Descending order")

    ## and then remove duplicate rows
    df_Compiled_AD_files = df_Compiled_AD_files.drop_duplicates(subset=['SerialNumber'], keep='first')
    print("\t" +"Removed duplicate rows having old scan dates.\n\n\tRectified AD Compilation dump has  {}  rows and  {}  columns...".format(df_Compiled_AD_files.shape[0],df_Compiled_AD_files.shape[1]))

    with pd.ExcelWriter("Rectified_AD_Compilation_dump.xlsx") as writer:
        df_Compiled_AD_files.to_excel(writer, sheet_name="AD_Compilation_dump_NODUPS", engine="xlsxwriter", header=True, index=False)
        (max_row,max_col) = df_Compiled_AD_files.shape
        worksheet = writer.sheets["AD_Compilation_dump_NODUPS"]
        worksheet.autofilter(0, 0, max_row, max_col-1)
        writer.save()

    _message_ = "Writing Rectified AD Compilation dump file COMPLETED ...\n\tYou can find the file\n\t  \"Rectified_AD_Compilation_dump.xlsx\"  at\n\t  {}"
    print("\t" + "~"*(len(_message_)+8) + "\n\t" + " "*4 + _message_.format(os.getcwd()) + " "*4 + "\n\t" + "="*(len(_message_)))


    ## slicing down to relevant columns only for next level processing 
    df_Compiled_AD_files_slice1 = df_Compiled_AD_files.filter(['SerialNumber','UserEmployeeID','UserID','OSName','Location','ScanDate','ScanDateFormated'])
    print("\t" + "Extracted the relevant columns --")
    # print("\t" + str(df_Compiled_AD_files_slice1.columns)) #..//CodeCheck

    ## setting column names as per the request template from end user
    df_Compiled_AD_files_slice1.rename(columns={"UserEmployeeID":"AD USEREMPID","UserID":"AD USERID","OSName":"AD OS","Location":"AD Location","ScanDateFormated":"AD Scandate"}, inplace=True)
    ## dropping the unformatted scan date column
    df_Compiled_AD_files_slice1 = df_Compiled_AD_files_slice1.drop(columns=['ScanDate'])
    print("\t" + "Renamed the relevant columns as per Stranded Report file  and \n\tdropped unformatted scan date column.")
    # print("\t" + str(df_Compiled_AD_files_slice1.columns)) #..//CodeCheck

    print("\tAD Compilation dump sliced down to  {}  rows and  {}  columns for susequent levels of processing.".format(df_Compiled_AD_files_slice1.shape[0],df_Compiled_AD_files_slice1.shape[1]))


    _message_ = "Compilation of AD files ended ..."
    print("\t" + "~"*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "~"*(len(_message_)+8))

    print("\n"*3)
    # #%%
    """
    772 file is the base file for all processing.
    Create a slice with the followig columns
    SERIALNO
    CLIENTNAME
    LOCATIONNAME
    ASSETTAG
    ASSETNAME
    VENDORNAME
    MODELNAME
    UNSPSCDESCRIPTION
    COSTCENTERID
    COSTCENTERNAME
    STATUS
    ASSIGNMENT
    EMPLASTNAME
    EMPFIRSTNAME
    CREATEDBY
    DATECREATED
    ADDR1
    ADDR2
    SUB_Location
    STATE
    ZIP
    COUNTRY
    EMPNO
    EMPNO_1
    OPERATINGSYSTEM
    Billing_Start_Date
    Status_Change_Date
    EXTERNALASSETID
    TEXT10

    Change dtype for DATECREATED, Status_Change_Date, Billing_Start_Date to 'datetime' with a format %Y-%m-%d
    Apply all the filters in the sequence given in the Requirement document

    Below filters are used to identity stranded assets:
    •	Include Laptop, Desktop and Tablet Computers assets in column “UNSPSCDESCRIPTION”.
    •	Exclude Chrome books in column “MODELNAME”.
    •	Exclude PAT LAB Devices in column “TEXT10”.
    •	Exclude CFS assets in column “TEXT10”.
    •	Exclude Fastrack location assets in column “LOCATIONNAME”.
    •	Exclude all Vendor cost centers in column “COSTCENTERNAME”.
    •	Exclude assets which are created less than 15 days [HPAM  create date < 15 days] in column “DATECREATED”.
    •	Exclude assets which has latest status change date [HPAM Status change date < 15 days] in column “Status_Change_Date”.
    •	Exclude all International assets from column “TEXT10”


    772 file --> Stranded Assets Report
    Serial Number is the main key for lookup.

    Filter only the Deployed assets in “STATUS” column that goes into the category “No AD Scan” and “91+AD Scan” in “AD Remarks” column.
    """
    _message_ = "Processing for File 772 started ..."
    print("\t" + "="*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "="*(len(_message_)+8))

    df_772 = pd.DataFrame()
    df_772 = pd.read_csv(_file_772, low_memory=False)
    print("\n\tFile 772 has  {}  rows and  {}  columns.".format(df_772.shape[0], df_772.shape[1]))

    # print("df_772_slice1 INFO")

    ## First slice of relevant columns
    df_772_slice1 = df_772.filter(\
        ['SERIALNO','CLIENTNAME','LOCATIONNAME','ASSETTAG','ASSETNAME','VENDORNAME','MODELNAME','UNSPSCDESCRIPTION','NATURE','COSTCENTERID','COSTCENTERNAME','STATUS','ASSIGNMENT','EMPLASTNAME','EMPFIRSTNAME','CREATEDBY','DATECREATED','ADDR1','ADDR2','SUB_Location','STATE','ZIP','COUNTRY','EMPNO','EMPNO_1','OPERATINGSYSTEM','Billing_Start_Date','Status_Change_Date','EXTERNALASSETID','TEXT10',])
    print("\tExtracted the relevant columns  --", end="  ")
    # print(str(df_772_slice1.columns)) #..//CodeCheck

    ## Date format correction for all date/datetime columns
    df_772_slice1['DATECREATED'] = pd.to_datetime(pd.to_datetime(df_772_slice1['DATECREATED']).dt.strftime('%d-%m-%Y'))
    df_772_slice1['Billing_Start_Date'] = pd.to_datetime(pd.to_datetime(df_772_slice1['Billing_Start_Date']).dt.strftime('%d-%m-%Y'))
    df_772_slice1['Status_Change_Date'] = pd.to_datetime(pd.to_datetime(df_772_slice1['Status_Change_Date']).dt.strftime('%d-%m-%Y'))
    print("\n\tNow working with  {}  rows and  {}  columns".format(df_772_slice1.shape[0],df_772_slice1.shape[1]))

    # print(df_772_slice1.filter(['DATECREATED','Billing_Start_Date','Status_Change_Date']).head(30)) #..//CodeCheck

    ## Filters applied
    df_772_slice1 = df_772_slice1[(df_772_slice1['UNSPSCDESCRIPTION'] == "Desktop") | \
        (df_772_slice1['UNSPSCDESCRIPTION'] == "Laptop") | (df_772_slice1['UNSPSCDESCRIPTION'] == "Tablet Computers")]
    df_772_slice1 = df_772_slice1[df_772_slice1['NATURE'].str.contains("Computer", na=False, case=False, regex=False)]
    df_772_slice1 = df_772_slice1[~df_772_slice1['MODELNAME'].str.contains("CHROMEBOOK", na=False, case=False, regex=False)]    
    df_772_slice1 = df_772_slice1[~df_772_slice1['TEXT10'].str.contains("International", na=False, case=False, regex=False)]
    df_772_slice1 = df_772_slice1[~df_772_slice1['TEXT10'].str.contains("PAT LAB", na=False, case=False, regex=False)]
    df_772_slice1 = df_772_slice1[~df_772_slice1['TEXT10'].str.contains("CFS", na=False, case=False, regex=False)]
    df_772_slice1 = df_772_slice1[~df_772_slice1['LOCATIONNAME'].str.contains("FAST", na=False, case=False, regex=False)]
    df_772_slice1 = df_772_slice1[~df_772_slice1['COSTCENTERNAME'].str.contains("Vendor", na=False, case=False, regex=False)]

    print("\tApplied filters on UNSPSCDESCRIPTION, MODELNAME, TEXT10, LOCATIONNAME, COSTCENTERNAME" + "\n\tNow working with  {}  rows and  {}  columns".format(df_772_slice1.shape[0],df_772_slice1.shape[1]))

    df_772_slice1 = df_772_slice1[df_772_slice1['STATUS'].str.contains("Deployed", na=False, case=False, regex=False)]

    print("\tApplied filters on STATUS" + "\n\tNow working with  {}  rows and  {}  columns".format(df_772_slice1.shape[0],df_772_slice1.shape[1]))

    # now applying the Date type filters for column DATECREATED and Status_Change_Date
    DATECREATED_exclusion_period = 15
    offset = datetime.timedelta(days=DATECREATED_exclusion_period)
    # print(type(offset),offset) #..//CodeCheck 
    cut_off_date = ((datetime.datetime.strptime(datetime.date.today().strftime('%d-%m-%Y'), "%d-%m-%Y")) - offset)
    # print(type(cut_off_date),cut_off_date) #..//CodeCheck
    mask_DATECREATED = (df_772_slice1['DATECREATED'] < cut_off_date)
    # print(type(mask_DATECREATED),mask_DATECREATED) #..//CodeCheck
    df_772_slice1 = df_772_slice1.loc[mask_DATECREATED]
    print("\tFilter applied on DATECREATED. \n\t Exclusion period is  {}  days. \n\tDates older than  {}  will be considered.".format(DATECREATED_exclusion_period, cut_off_date))
    mask_Status_Change_Date = (df_772_slice1['Status_Change_Date'] < cut_off_date)
    df_772_slice1 = df_772_slice1.loc[mask_Status_Change_Date]
    print("\tFilter applied on Status_Change_Date. \n\t Exclusion period is  {}  days. \n\tDates older than  {}  will be considered.".format(DATECREATED_exclusion_period,cut_off_date))

    df_772_slice1.rename(columns={"SERIALNO":"SerialNumber"}, inplace=True)

    # print(df_772_slice1.filter(['DATECREATED','Billing_Start_Date','Status_Change_Date']).head(20))
    print("\tNow working with  {}  rows and  {}  columns".format(df_772_slice1.shape[0],df_772_slice1.shape[1]))

    _message_ = "Processing for File 772 ended."
    print("\t" + "~"*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "~"*(len(_message_)+8))
    print("\n"*3)

    #%%
    _message_ = "Initiating Step 1 of data processing..."
    print("\t" + "="*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "="*(len(_message_)+8))

    _message_ = "Comparing / Looking up the Serial Numbers from 772 file with those in the Compiled and Revised AD file"
    # print("\n\t" + _message_ + " "*4 + "\n\t" + "~"*(len(_message_)+8))

    dfmerge_772_AD = pd.merge(df_772_slice1, df_Compiled_AD_files_slice1, on=['SerialNumber'], how='left')
    print("\t" + "Rows remaining after the comparison / lookup ....  {}  ".format(dfmerge_772_AD.shape[0]))
    print("\t" + "The resultant working dataset has  {}  rows and  {}  columns".format(dfmerge_772_AD.shape[0],dfmerge_772_AD.shape[1]))
    # print("\n\t" + "~"*(len(_message_)+8))

    _message_ = "Adding 4 columns for date processing - 'scd<AD', 'AD date diff', 'AD Remarks' and '_Report_Analysis_Date_' "
    print("\n\t" + _message_ + "\n\t")

    dfmerge_772_AD.insert(dfmerge_772_AD.shape[1], 'scd<AD', '')
    #..//HACK
    mask_SCD_lt_AD = (dfmerge_772_AD['Status_Change_Date'] < dfmerge_772_AD['AD Scandate'])
    # print(type(mask_SCD_lt_AD),mask_SCD_lt_AD) #..//CodeCheck
    dfmerge_772_AD["scd<AD"] = mask_SCD_lt_AD

    dfmerge_772_AD.insert(dfmerge_772_AD.shape[1], 'AD date diff', '')
    #..//HACK
    # dfmerge_772_AD["_Report_Analysis_Date_"] = datetime.date.today()
    print("\t\t"+ "Setting the Report Analysis Date - format(yyyy-mm-dd)")

    print("\t\t\t", end="")
    yyyy = int(input('yyyy :: '))
    print("\t\t\t", end="")
    mm = int(input('mm :: '))
    print("\t\t\t", end="")
    dd = int(input('dd :: '))

    dfmerge_772_AD["_Report_Analysis_Date_"] = datetime.date(yyyy, mm, dd)
    dfmerge_772_AD["_Report_Analysis_Date_"] = pd.to_datetime(dfmerge_772_AD["_Report_Analysis_Date_"])
    dfmerge_772_AD["AD date diff"] = dfmerge_772_AD["_Report_Analysis_Date_"] - dfmerge_772_AD["AD Scandate"]
    #%%



    #%%
    dfmerge_772_AD.insert(dfmerge_772_AD.shape[1], 'AD Remarks', '')

    #%%
    #..//TODO
    _bins_ = [ pd.Timedelta(days = -30), pd.Timedelta(days = 0), pd.Timedelta(days = 30), pd.Timedelta(days = 60), pd.Timedelta(days = 90), pd.Timedelta(days = 150) ]
    # _labels_ = ["{0} - {1} AD Scan".format(i, i+30) for i in range(0, 150, 30)]
    _labels_ = ['No AD Scan', '1 - 30 AD Scan', '31 - 60 AD Scan', '61 - 90 AD Scan', '91+AD Scan', ]
    # print(_labels_) #..//CodeCheck
    dfmerge_772_AD["AD Remarks"] = pd.cut(dfmerge_772_AD["AD date diff"], _bins_, labels=_labels_)
    # print(dfmerge_772_AD[["AD date diff","AD Remarks"]].head(50)) #..//CodeCheck

    dfmerge_772_AD = dfmerge_772_AD[(dfmerge_772_AD["AD date diff"] < pd.Timedelta(days = 1)) | (dfmerge_772_AD["AD date diff"] > pd.Timedelta(days = 90))]
    # print(dfmerge_772_AD.info()) #..//CodeCheck

    print("\t" + "The resultant working dataset has  {}  rows and  {}  columns\n".format(dfmerge_772_AD.shape[0],dfmerge_772_AD.shape[1]))

    #%%
    # print(dfmerge_772_AD.info()) #..//CodeCheck


    _message_ = "Step 1 of data processing completed..."
    print("\t" + "~"*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "~"*(len(_message_)+8))
    print("\n"*3)


    #%%
    """
    Redeployment list
    """
    # os.chdir(_source_file_path)
    _message_ = "Processing for - File Hardware Redeployment started ..."
    print("\t" + "="*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "="*(len(_message_)+8))

    df_redeploy_1 = pd.read_excel(_file_redeploy_list, sheet_name="Main Data", engine="pyxlsb", encoding="ISO-8859-1", index_col=None, na_values=None, skiprows=15, usecols=["Product Types","Serial#"])
    df_redeploy_1 = df_redeploy_1[(df_redeploy_1["Product Types"] == "Desktop") | (df_redeploy_1["Product Types"] == "Media Tablet") | (df_redeploy_1["Product Types"] == "Notebook")]
    df_redeploy_1.rename(columns={"Serial#":"SerialNumber"}, inplace=True)
    print("\tExtracted  {}  rows from worksheet  \"Main Data\"".format(df_redeploy_1.shape[0]))
    # print(df_redeploy_1.info()) #..//CodeCheck

    df_redeploy_2 = pd.read_excel(_file_redeploy_list, sheet_name="Main Data File - Fujitsu Tablet", engine="pyxlsb", encoding="ISO-8859-1", index_col=None, na_values=None, skiprows=18, usecols=["Product Types","Serial#"])
    df_redeploy_2 = df_redeploy_2[df_redeploy_2["Product Types"] == "Media Tablet"]
    df_redeploy_2.rename(columns={"Serial#":"SerialNumber"}, inplace=True)
    print("\tExtracted  {}  rows from worksheet  \"Main Data File - Fujitsu Tablet\"".format(df_redeploy_2.shape[0]))
    # print(df_redeploy_2.info()) #..//CodeCheck

    df_redeploy_3 = pd.read_excel(_file_redeploy_list, sheet_name="Main Data File - Desktop", engine="pyxlsb", encoding="ISO-8859-1", index_col=None, na_values=None, skiprows=12, usecols=["Product Types","Serial#"])
    df_redeploy_3 = df_redeploy_3[df_redeploy_3["Product Types"] == "Desktop"]
    df_redeploy_3.rename(columns={"Serial#":"SerialNumber"}, inplace=True)
    print("\tExtracted  {}  rows from worksheet  \"Main Data File - Desktop\"".format(df_redeploy_3.shape[0]))
    # print(df_redeploy_3.info()) #..//CodeCheck

    df_redeploy_4 = pd.read_excel(_file_redeploy_list, sheet_name="Redeployed Assets", engine="pyxlsb", encoding="ISO-8859-1", index_col=None, na_values=None, skiprows=3, usecols=["Product Types","Serial#","Status"])
    df_redeploy_4 = df_redeploy_4[df_redeploy_4["Status"].str.contains("Redeployed", na=False, case=False, regex=False)]
    df_redeploy_4 = df_redeploy_4.filter(["Product Types","Serial#"], axis=1)
    df_redeploy_4 = df_redeploy_4[(df_redeploy_4["Product Types"] == "Desktop") | (df_redeploy_4["Product Types"] == "Media Tablet") | (df_redeploy_4["Product Types"] == "Notebook")]
    df_redeploy_4.rename(columns={"Serial#":"SerialNumber"}, inplace=True)
    print("\tExtracted  {}  rows from worksheet  \"Redeployed Assets\"".format(df_redeploy_4.shape[0]))
    # print(df_redeploy_4.info()) #..//CodeCheck

    df_redeploy_all = pd.concat([df_redeploy_1,df_redeploy_2,df_redeploy_3,df_redeploy_4])
    df_redeploy_all.rename(columns={"Product Types":"Redeployment List"}, inplace=True)
    # print(df_redeploy_all.info()) #..//CodeCheck

    _message_ = "Final data volume in the Redeployment file  {}  rows  and  {}  columns."
    print("\n\t" + _message_.format(df_redeploy_all.shape[0],df_redeploy_all.shape[1]) + "\n\t")

    _message_ = "Processing for File - Hardware Redeployment completed ..."
    print("\t" + "~"*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "~"*(len(_message_)+8))
    print("\n"*3)
    #%%
    """
    Cancelled File
    """
    _message_ = "Processing for - Cancelled file started ..."
    print("\t" + "="*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "="*(len(_message_)+8))

    df_Cancelled = pd.read_excel(_file_Cancelled, sheet_name="Sheet1", encoding="ISO-8859-1", index_col=None, engine=None, usecols=["Serial Numbers","Status"])
    df_Cancelled.rename(columns={"Serial Numbers":"SerialNumber"}, inplace=True)
    _SrNum_col_idx = df_Cancelled.columns.get_loc("SerialNumber")
    _SrStatus_col_idx = df_Cancelled.columns.get_loc("Status")
    # print(_SrNum_col_idx,_SrStatus_col_idx) #..//CodeCheck
    df_Temp = pd.DataFrame(columns=df_Cancelled.columns)
    # print(df_Cancelled.shape, df_Temp.shape) #..//CodeCheck
    _extra = 0
    for _sr_nums in range(0, df_Cancelled.shape[0]):
        _SrNum_LIST = str(df_Cancelled.iloc[_sr_nums,_SrNum_col_idx]).split(sep=",")
        # print(_SrNum_LIST,type(_SrNum_LIST),len(_SrNum_LIST)) #..//CodeCheck
        if len(_SrNum_LIST) > 1:
            _extra += (len(_SrNum_LIST) - 1) 
            for _ii_ in range(1, len(_SrNum_LIST)):
                new_list = list()
                new_list.append(str(_SrNum_LIST[_ii_].replace(" ","")))
                new_list.append("Cancelled")
                temp_series = pd.Series(new_list, name="Cancelled SrNums", index=df_Cancelled.columns)
                df_Temp = df_Temp.append(temp_series, ignore_index=True)
    # print(_extra) #..//CodeCheck
    df_Cancelled = df_Cancelled.append(df_Temp, ignore_index=True)
    # print(df_Cancelled.shape, df_Temp.shape) #..//CodeCheck
    df_Cancelled.rename(columns={"Status":"Cancelled"}, inplace=True)

    _message_ = "Final data volume in the Cancelled file  {}  rows  and  {}  columns."
    print("\n\t" + _message_.format(df_Cancelled.shape[0],df_Cancelled.shape[1]) + "\n\t")

    _message_ = "Processing for File - Cancelled's file completed ..."
    print("\t" + "~"*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "~"*(len(_message_)+8))
    print("\n"*3)

    #%%
    """
    Sanoja's File
    """
    _message_ = "Processing for - Sanoja's file started ..."
    print("\t" + "="*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "="*(len(_message_)+8))

    df_Sanoja = pd.read_excel(_file_Sanoja, sheet_name="Sheet1", encoding="ISO-8859-1", index_col=None, engine=None, usecols=["Serial Number"])
    df_Sanoja.rename(columns={"Serial Number":"SerialNumber"}, inplace=True)
    df_Sanoja["Sanoja's file"] = "Present in Sanoja's file"

    _message_ = "Final data volume in the Sanoja's file  {}  rows  and  {}  columns."
    print("\n\t" + _message_.format(df_Sanoja.shape[0],df_Sanoja.shape[1]) + "\n\t")

    _message_ = "Processing for - Sanoja's file completed ..."
    print("\t" + "~"*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "~"*(len(_message_)+8))
    print("\n"*3)
    #%%
    #--------------------- removed from end-user's requirement
    # """
    # Sweep Asset file
    # """
    # _message_ = "Processing for - Sweep Asset file started ..."
    # print("\t" + "="*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "="*(len(_message_)+8))

    # df_Sweep = pd.read_excel(_file_SweepAsset, sheet_name="Sweep Assets", encoding="ISO-8859-1", index_col=None, engine="pyxlsb", usecols=["SerialNumber"])
    # df_Sweep["Sweep list"] = "Present in Sweep list"

    # _message_ = "Final data volume in the Sweep Asset file  {}  rows  and  {}  columns."
    # print("\n\t" + _message_.format(df_Sweep.shape[0],df_Sweep.shape[1]) + "\n\t")

    # _message_ = "Processing for File - Sweep Asset file completed ..."
    # print("\t" + "~"*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "~"*(len(_message_)+8))
    # print("\n"*3)

    # %%
    _message_ = "Initiating Step 2 of data processing..."
    print("\t" + "="*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "="*(len(_message_)+8))

    _message_ = "Comparing / Looking up the Serial Numbers from the last lookup results with those in the Redeployment file"
    print("\n\t" + _message_ + "\n\t")
    dfmerge_772_AD_Redeploy = pd.merge(dfmerge_772_AD,df_redeploy_all, on=['SerialNumber'], how='left')
    # print(dfmerge_772_AD_Redeploy.columns) #..//CodeCheck
    print("\t" + "Rows remaining after the comparison / lookup ....  {}  ".format(dfmerge_772_AD_Redeploy.shape[0]))
    print("\t" + "The resultant working dataset has  {}  rows and  {}  columns\n".format(dfmerge_772_AD_Redeploy.shape[0],dfmerge_772_AD_Redeploy.shape[1]))

    _message_ = "Comparing / Looking up the Serial Numbers from the last lookup results with those in the Cancelled file"
    print("\n\t" + _message_ + "\n\t")
    dfmerge_772_AD_Redeploy_Cancelled = pd.merge(dfmerge_772_AD_Redeploy, df_Cancelled,on=['SerialNumber'], how='left')
    print("\t" + "Rows remaining after the comparison / lookup ....  {}  ".format(dfmerge_772_AD_Redeploy_Cancelled.shape[0]))
    print("\t" + "The resultant working dataset has  {}  rows and  {}  columns\n".format(dfmerge_772_AD_Redeploy_Cancelled.shape[0],dfmerge_772_AD_Redeploy_Cancelled.shape[1]))

    _message_ = "Comparing / Looking up the Serial Numbers from the last lookup results with those in the Sanoja's file"
    print("\n\t" + _message_ + "\n\t")
    dfmerge_772_AD_Redeploy_Cancelled_Sanoja = pd.merge(dfmerge_772_AD_Redeploy_Cancelled, df_Sanoja,on=['SerialNumber'], how='left')
    print("\t" + "Rows remaining after the comparison / lookup ....  {}  ".format(dfmerge_772_AD_Redeploy_Cancelled_Sanoja.shape[0]))
    print("\t" + "The resultant working dataset has  {}  rows and  {}  columns\n".format(dfmerge_772_AD_Redeploy_Cancelled_Sanoja.shape[0],dfmerge_772_AD_Redeploy_Cancelled_Sanoja.shape[1]))

    # _message_ = "Comparing / Looking up the Serial Numbers from the last lookup results with those in the Sweep Asset file"
    # print("\n\t" + _message_ + "\n\t")
    # dfmerge_772_AD_Redeploy_Cancelled_Sanoja_Sweep = pd.merge(dfmerge_772_AD_Redeploy_Cancelled_Sanoja, df_Sweep,on=['SerialNumber'], how='left')
    # print("\t" + "Rows remaining after the comparison / lookup ....  {}  ".format(dfmerge_772_AD_Redeploy_Cancelled_Sanoja_Sweep.shape[0]))
    # print("\t" + "The resultant working dataset has  {}  rows and  {}  columns\n".format(dfmerge_772_AD_Redeploy_Cancelled_Sanoja_Sweep.shape[0],dfmerge_772_AD_Redeploy_Cancelled_Sanoja_Sweep.shape[1]))

    _message_ = "Step 2 of data processing completed..."
    print("\t" + "~"*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "~"*(len(_message_)+8))
    print("\n"*3)
    # %%

    _message_ = "Now writing Phase 1 output file ..."
    print("\t" + "="*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "~"*(len(_message_)))

    os.chdir(_script_dir)

    # with pd.ExcelWriter("Intermediate_Report_for_Validation.xlsx") as writer:

    #     df_Compiled_AD_files.to_excel(writer, sheet_name="df_Compiled_AD_files", engine='xlsxwriter', header=True, index=False)
    #     (max_row,max_col) = df_Compiled_AD_files.shape
    #     worksheet = writer.sheets["df_Compiled_AD_files"]
    #     worksheet.autofilter(0, 0, max_row, max_col-1)

    #     df_Compiled_AD_files_slice1.to_excel(writer, sheet_name="df_Compiled_AD_files_slice1", engine='xlsxwriter', header=True, index=False)
    #     (max_row,max_col) = df_Compiled_AD_files_slice1.shape
    #     worksheet = writer.sheets["df_Compiled_AD_files_slice1"]
    #     worksheet.autofilter(0, 0, max_row, max_col-1)
        
    #     dfmerge_772_AD.to_excel(writer, sheet_name="dfmerge_772_AD", engine='xlsxwriter', header=True, index=False)
    #     (max_row,max_col) = dfmerge_772_AD.shape
    #     worksheet = writer.sheets["dfmerge_772_AD"]
    #     worksheet.autofilter(0, 0, max_row, max_col-1)
        
    #     df_redeploy_all.to_excel(writer, sheet_name="df_redeploy_all", engine="xlsxwriter", header=True, index=False)
    #     (max_row,max_col) = df_redeploy_all.shape
    #     worksheet = writer.sheets["df_redeploy_all"]
    #     worksheet.autofilter(0, 0, max_row, max_col-1)
        
    #     dfmerge_772_AD_Redeploy.to_excel(writer, sheet_name="dfmerge_772_AD_Redeploy", engine="xlsxwriter", header=True, index=False)
    #     (max_row,max_col) = dfmerge_772_AD_Redeploy.shape
    #     worksheet = writer.sheets["dfmerge_772_AD_Redeploy"]
    #     worksheet.autofilter(0, 0, max_row, max_col-1)
        
    #     df_Cancelled.to_excel(writer, sheet_name="df_Cancelled", engine="xlsxwriter", header=True, index=False)
    #     (max_row,max_col) = df_Cancelled.shape
    #     worksheet = writer.sheets["df_Cancelled"]
    #     worksheet.autofilter(0, 0, max_row, max_col-1)

    #     df_Sanoja.to_excel(writer, sheet_name="df_Sanoja", engine="xlsxwriter", header=True, index=False)
    #     (max_row,max_col) = df_Sanoja.shape
    #     worksheet = writer.sheets["df_Sanoja"]
    #     worksheet.autofilter(0, 0, max_row, max_col-1)

    #     df_Sweep.to_excel(writer, sheet_name="df_Sweep", engine="xlsxwriter", header=True, index=False)
    #     (max_row,max_col) = df_Sweep.shape
    #     worksheet = writer.sheets["df_Sweep"]
    #     worksheet.autofilter(0, 0, max_row, max_col-1)

    #     dfmerge_772_AD_Redeploy_Cancelled.to_excel(writer, sheet_name="dfmerge_772_AD_Redep_Can", engine="xlsxwriter", header=True, index=False)
    #     (max_row,max_col) = dfmerge_772_AD_Redeploy_Cancelled.shape
    #     worksheet = writer.sheets["dfmerge_772_AD_Redep_Can"]
    #     worksheet.autofilter(0, 0, max_row, max_col-1)

    #     dfmerge_772_AD_Redeploy_Cancelled_Sanoja.to_excel(writer, sheet_name="dfmerge_772_AD_Redep_Can_San", engine="xlsxwriter", header=True, index=False)
    #     (max_row,max_col) = dfmerge_772_AD_Redeploy_Cancelled_Sanoja.shape
    #     worksheet = writer.sheets["dfmerge_772_AD_Redep_Can_San"]
    #     worksheet.autofilter(0, 0, max_row, max_col-1)

    #     dfmerge_772_AD_Redeploy_Cancelled_Sanoja_Sweep.to_excel(writer, sheet_name="dfmerge_772_AD_Redep_Can_San_Sw", engine="xlsxwriter", header=True, index=False)
    #     (max_row,max_col) = dfmerge_772_AD_Redeploy_Cancelled_Sanoja_Sweep.shape
    #     worksheet = writer.sheets["dfmerge_772_AD_Redep_Can_San_Sw"]
    #     worksheet.autofilter(0, 0, max_row, max_col-1)

    #     writer.save()


    with pd.ExcelWriter("Stranded_Assets_Report.xlsx") as writer:
        dfmerge_772_AD_Redeploy_Cancelled_Sanoja.to_excel(writer, sheet_name="Stranded_Assets_Report", engine="xlsxwriter", header=True, index=False)
        (max_row,max_col) = dfmerge_772_AD_Redeploy_Cancelled_Sanoja.shape
        worksheet = writer.sheets["Stranded_Assets_Report"]
        worksheet.autofilter(0, 0, max_row, max_col-1)
        writer.save()

    _message_ = "Writing Phase 1 output file COMPLETED ...\n\tYou can find the file\n\t  \"Stranded_Assets_Report.xlsx\"  at\n\t  {}"
    print("\t" + "~"*(len(_message_)+8) + "\n\t" + " "*4 + _message_.format(os.getcwd()) + " "*4 + "\n\t" + "="*(len(_message_)))

    _message_ = "PHASE 1 Ended..."
    print("\n\t" + "~"*(len(_message_)+16) + "\n\t" + " "*4 + "~"*(len(_message_)+8) + "\n\t" + " "*8 + _message_ + " "*8  + "\n\t" + "~"*(len(_message_)+16) +"\n")

"""
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
"""

def phase2():
    #----------common part
    _message_ = " INITIAL SETUP "
    print("\n\t" + "="*(len(_message_)+8) + "\n\t" + "~"*4 + _message_ + "~"*4 + "\n\t" + "="*(len(_message_)+8) +"\n")


    _script_dir = os.path.dirname(os.path.abspath(__file__))
    # print(_script_dir) #..//CodeCheck
    _source_file_path = r"C:\DEB\DXC_Automation\UCMS_29864__Stranded Assets - Automation\_input_"

    _message_ = "SET File / Folder paths and Filenames with file extensions --"
    print("\n\t" + "="*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "="*(len(_message_)+8) +"\n")

    # Phase 2 file/s
    _message_ = "FILE  -->>  Full PATH and File name with extension of \"PHASE 2 HPAM EXTRACT\" file "
    print("\n\n\t"+_message_+"\n\t", end="")
    _file_Phase2_HPAMextract = input(r' :: ')
    # _file_Phase2_HPAMextract = r"C:\DEB\DXC_Automation\UCMS_29864__Stranded Assets - Automation\Input files H\Input files\Phase 2\Phase 2 - HPAM Extract - Input file.xlsx"
    _file_Phase2_HPAMextract = os.path.abspath(_file_Phase2_HPAMextract)
    print("\t"+_file_Phase2_HPAMextract)
    
    _message_ = "PHASE 2 Started..."
    print("\n\t" + "="*(len(_message_)+16) + "\n\t" + " "*4 + "="*(len(_message_)+8) + "\n\t" + " "*8 + _message_ + " "*8  + "\n\t" + "="*(len(_message_)+16) +"\n")

    df_Phase2 = pd.read_excel(_file_Phase2_HPAMextract, sheet_name="Sheet1", encoding="ISO-8859-1", index_col=None, engine=None)
    df_Phase2_EOLife = df_Phase2[df_Phase2["Status (Asset)"].str.contains("End of life", case=False, na=False, regex=False)]
    df_Phase2_EOLease = df_Phase2[df_Phase2["Status (Asset)"].str.contains("End of lease", case=False, na=False, regex=False)]
    df_Phase2_EO = pd.DataFrame()
    df_Phase2_EO = df_Phase2_EOLife.append(df_Phase2_EOLease)

    df_Phase2_EO = df_Phase2_EOLife[df_Phase2_EOLife["Text 6 (Batch)"].str.contains("STRANDED", case=False, na=False, regex=False)]
    # print(df_Phase2_EOL.shape) #..//CodeCheck
    print("\t" + "End Of Life and End Of Lease dataset has  {}  rows and  {}  columns\n".format(df_Phase2_EO.shape[0],df_Phase2_EO.shape[1]))

    df_Phase2_Missing = df_Phase2[df_Phase2["Status (Asset)"].str.contains("Missing", case=False, na=False, regex=False)]
    # print(df_Phase2_Missing.shape)#..//CodeCheck
    print("\t" + "Missing dataset has  {}  rows and  {}  columns\n".format(df_Phase2_Missing.shape[0],df_Phase2_Missing.shape[1]))

    _message_ = "Now writing Phase 2 output file ..."
    print("\t" + "="*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "~"*(len(_message_)+8))

    os.chdir(_script_dir)
    with pd.ExcelWriter("Consolidated_Stranded_list_Output_file.xlsx") as writer:

        df_Phase2_EO.to_excel(writer, sheet_name="EOL via Michelle File", engine="xlsxwriter", header=True, index=False)
        (max_row,max_col) = df_Phase2_EO.shape
        worksheet = writer.sheets["EOL via Michelle File"]
        worksheet.autofilter(0, 0, max_row, max_col-1)

        df_Phase2_Missing.to_excel(writer, sheet_name="Missing via Stranded", engine="xlsxwriter", header=True, index=False)
        (max_row,max_col) = df_Phase2_Missing.shape
        worksheet = writer.sheets["Missing via Stranded"]
        worksheet.autofilter(0, 0, max_row, max_col-1)

        writer.save()

    _message_ = "Writing Phase 2 output file COMPLETED ...\n\tYou can find the file\n\t  \"Consolidated_Stranded_list_Output_file.xlsx\"  at\n\t  {}"
    print("\t" + "~"*(len(_message_)) + "\n\t" + " "*4 + _message_.format(os.getcwd()) + " "*4 + "\n\t" + "="*(len(_message_)))

    _message_ = "PHASE 2 Ended..."
    print("\n\t" + "~"*(len(_message_)+16) + "\n\t" + " "*4 + "~"*(len(_message_)+8) + "\n\t" + " "*8 + _message_ + " "*8  + "\n\t" + "~"*(len(_message_)+16) +"\n")









"""
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
"""

_message_ = "SELECT YOUR OPERATION - PHASE 1 OR PHASE2 2"
print("\t" + "="*(len(_message_)+8) + "\n\t" + " "*4 + _message_ + " "*4 + "\n\t" + "="*(len(_message_)+8))
print("\t\t", end="")
_choice_ = int(input())
# print(_choice_, type(_choice_))
if _choice_ == 1:
    phase1()
    print("\n"*5 + "\t"+ "Script completed .. Press any key to close the script / window")
elif _choice_ == 2:
    #phase2()
    #print("\n"*5 + "\t"+ "Script completed .. Press any key to close the script / window")
    print("\n"*5 + "\t"+ "Phase 2 operations have been moved to a different script .. Press any key to close the script / window")
else:
    print("\n"*5 + "\t"+ "Invalid Choce .. Press any key to Exit the script / window")

#%%
input(r'')


