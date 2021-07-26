import pandas as pd
import numpy as np
import os

#print("Enter the folder location for the ESL report  :  ")
#esl_report_location = input()
esl_report_location = r'C:\Users\ddutta8\Documents'
#print("Enter the ESL report file name  :  ")
#esl_file_name = input()
esl_file_name = "Copy of esl_report.8257298.xlsx"
target_file_path = os.path.join(esl_report_location, esl_file_name)
#print("Enter the sheet name to scan  :  ")
#target_sheet_name = input()
target_sheet_name = "Results"
print(target_file_path + "[" + target_sheet_name + "]")
esl_report_dataframe = pd.read_excel(target_file_path, header=0, sheet_name=target_sheet_name )
#esl_report_sorted_dataframe = esl_report_dataframe.sort_values(by=["System Name", 'Contract Name'])
#print(esl_report_sorted_dataframe)
sanitized_report_dataframe = pd.DataFrame({
    "System Name" : [],
    "Contract Name 1" : [],
    "Contract Name 2" : [],
})
##### processing starts here
pivot_table_of_raw_data = pd.pivot_table(esl_report_dataframe, index=["System Name"], values=["System Name"], aggfunc=['count'])

i = 0
#dup = 0
#nodup= 0
print(len(pivot_table_of_raw_data))
for idx, rows in pivot_table_of_raw_data.iterrows():
    if i < len(pivot_table_of_raw_data):
        check_system_count = pivot_table_of_raw_data.iloc[i,0]
        if check_system_count <= 1:
            #nodup += 1
            filter = esl_report_dataframe.["System Name"].str.Contains(idx, case=False, na=False)
            selected_sysnames = esl_report_dataframe[filter]
            print(selected_sysnames)
        elif check_system_count == 2:
            #dup += 1
        else:
            print("special case " + idx + " has " + str(check_system_count) + " entries")
    i +=1
print(i)
# print("total number of single server {}".format(nodup))
# print("total number of duplicate server {}".format(dup))
# print(dup+nodup)


# pd.pivot_table()
