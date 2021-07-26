########### imports #############
import os, sys, subprocess
import pandas as pd
import numpy as np
import xlrd, openpyxl

########### pre-work and declarations ##########
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$    DISCLAIMER    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$  This programs consolidates reports in a single file. $$$$$$$$$$$")
print("$$$$$$ Please place / extract the report files in a  $$$$$$$$$$$$$$$$$$")
print("$$$$$$$ single folder and make a note of it. $$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#Reports_loc = input("\n\nPlease mention the folder path of the report files: \n")
Reports_loc = "C:\\Users\\ddutta8\\Desktop\\Audit Report Collection\\Audit Report Collection\\"
#Cons_reprt_loc = input("\nPlease mention the folder path to save the consolidated report: \n")
Cons_reprt_loc = r'C:\Users\ddutta8\Desktop\temp data'
Cons_reprt_loc = Cons_reprt_loc + "\\Consolidated_Report"
print("\nFolder location for Consolidated Report is  :  " + Cons_reprt_loc + "\n")
if os.path.exists(Cons_reprt_loc) and not os.path.isfile(Cons_reprt_loc):
    if not os.listdir(Cons_reprt_loc):
        print(".. Target directory is EMPTY ..")
    else:
        print(".. Old report found ..\n")
        os.remove(Cons_reprt_loc+"\\Consolidated_Asset_Report.xlsx")
        print(".. Old report removed successfully ..\n")
else:
    os.makedirs(Cons_reprt_loc)

fileCount = 0
combined_report = pd.DataFrame({
    "CR #":[],
    "Product type" : [],
    "Serial number" : [],
    "Model" : [],
    "Customer asset tag" : [],
    "Disposition Code" : [],
    "Report File Name" : []}
)
log_store = pd.Series(["Report processing log"])
temp_log = pd.Series([""])

################### report folder iteration starts #############################
os.chdir(Reports_loc)
for report_file in os.listdir(Reports_loc):
    if report_file.endswith("xlsx"):
        #print("Reading file ... " + report_file, end = " ")
        temp_log = pd.Series(["Reading file ... " + report_file])
        log_store = log_store.append(temp_log)
        fileCount+=1
        report_read_buffer = pd.read_excel(report_file, skiprows=1, usecols=["CR #", "Product type", "Serial number", "Model", "Customer asset tag", "Disposition Code"])
        
        Report_File_Name = []
        for index_ in report_read_buffer["CR #"]:
            Report_File_Name.append(report_file)
        report_read_buffer["Report File Name"] = Report_File_Name

        combined_report = pd.concat([combined_report, report_read_buffer], axis=0)
        #print("->> ->> successfully read")
        temp_log = pd.Series(["successfully read"])
        log_store = log_store.append(temp_log)

#print("\n A total of " + str(fileCount) + " xlsx files read.\n")
temp_log = pd.Series(["A total of " + str(fileCount) + " xlsx files read."])
log_store = log_store.append(temp_log)

os.chdir(Cons_reprt_loc)
with pd.ExcelWriter('Consolidated_Asset_Report.xlsx') as writer:
    combined_report.to_excel(writer, sheet_name='ARSAuditReceiptReport.Report', index=False)
    log_store.to_excel(writer, sheet_name='ReportProcessing.Log', index=False)
print("... Processing complete ... Report generated ... ")
os.chdir(Cons_reprt_loc)
subprocess.Popen('explorer cwd')