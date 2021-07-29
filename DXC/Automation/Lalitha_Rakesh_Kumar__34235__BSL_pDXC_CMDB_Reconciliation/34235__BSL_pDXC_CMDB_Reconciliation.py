#%%
from numpy.core.fromnumeric import shape
import pandas as pd
import numpy as np
import os
import openpyxl

'''
~~~~~~~~~~~~~~~~
- Path setting
~~~~~~~~~~~~~~~~
'''
# print("\n\n")
# path1 = input(r"Enter the full path for the DXC dump file  ::  ")
# path2 = input(r"Enter the full path for the BSL dump file  ::  ")
# path3 = input(r"Enter the full path for the Status Mapping file  ::  ")

path0 = os.curdir
path1 = r"C:\Users\ddutta8\OneDrive - DXC Production\Documents\DXC_Automation\Lalitha_Rakesh_Kumar__34235__BSL_pDXC_CMDB_Reconciliation\input files\DXC CMDB - BSL (June 30).xlsx"
path2 = r"C:\Users\ddutta8\OneDrive - DXC Production\Documents\DXC_Automation\Lalitha_Rakesh_Kumar__34235__BSL_pDXC_CMDB_Reconciliation\input files\BSL CMDB - June 26th.xlsx"
path3 = r"C:\Users\ddutta8\OneDrive - DXC Production\Documents\DXC_Automation\Lalitha_Rakesh_Kumar__34235__BSL_pDXC_CMDB_Reconciliation\input files\Status Mapping.xlsx"
path4 = r"C:\Users\ddutta8\OneDrive - DXC Production\Documents\DXC_Automation\Lalitha_Rakesh_Kumar__34235__BSL_pDXC_CMDB_Reconciliation\output files\DXC CMDB - BSL (June 30-1).xlsx"
path5 = r"C:\Users\ddutta8\OneDrive - DXC Production\Documents\DXC_Automation\Lalitha_Rakesh_Kumar__34235__BSL_pDXC_CMDB_Reconciliation\output files\BSL CMDB - June 30000.xlsx"


path1 = os.path.abspath(path1)
path2 = os.path.abspath(path2)
path3 = os.path.abspath(path3)
path4 = os.path.abspath(path4)
path5= os.path.abspath(path5)
message = ""
line = "~"*80

########################################################################
## Procceing the DXC dump file with BSL lookups ( primary referrencing)....
########################################################################

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Preparing the DXC dataframe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
message = "\nProcessing DXC dump file .."
print(message)

dxc_cmdb_df = pd.DataFrame()
# dxc_cmdb_df = pd.read_excel(path1, index_col=None, engine="openpyxl", usecols="B,D,F,G,I,M,N,O,R,S,T,V", header=0) 
dxc_cmdb_df = pd.read_excel(path1, index_col=None, engine="openpyxl", header=0) 
dxc_cmdb_df.rename(columns=lambda x:  'dxc_'+x, inplace=True)
# print(dxc_cmdb_df.shape)#, dxc_cmdb_df.columns, dxc_cmdb_df.info())

dxc_cmdb_df["dxc_name"] = dxc_cmdb_df["dxc_name"].astype('str')
dxc_cmdb_df = dxc_cmdb_df[dxc_cmdb_df["dxc_name"].notnull()]
dxc_cmdb_df["dxc_name"] = dxc_cmdb_df["dxc_name"].str.strip(" "
)
dxc_cmdb_df["dxc_install_status"] = dxc_cmdb_df["dxc_install_status"].astype('str')
dxc_cmdb_df["dxc_install_status"] = dxc_cmdb_df["dxc_install_status"].str.strip(" ")

dxc_cmdb_df["dxc_serial_number"].fillna(value='missing', inplace=True)
dxc_cmdb_df["dxc_serial_number"] = dxc_cmdb_df["dxc_serial_number"].astype('str')
dxc_cmdb_df["dxc_serial_number"] = dxc_cmdb_df["dxc_serial_number"].str.strip(" ")

# print(dxc_cmdb_df["dxc_name"].shape)
# print(dxc_cmdb_df["dxc_serial_number"].shape)
# print(dxc_cmdb_df["dxc_install_status"].shape)

dxc_cmdb_df["dxc_sys_class_name"] = dxc_cmdb_df["dxc_sys_class_name"].str.strip(" ")
dxc_cmdb_df["dxc_ip_address"] = dxc_cmdb_df["dxc_ip_address"].str.strip(" ")
dxc_cmdb_df["dxc_model_id"] = dxc_cmdb_df["dxc_model_id"].str.strip(" ")
dxc_cmdb_df["dxc_location"] = dxc_cmdb_df["dxc_location"].str.strip(" ")
dxc_cmdb_df["dxc_manufacturer"] = dxc_cmdb_df["dxc_manufacturer"].str.strip(" ")
dxc_cmdb_df["dxc_ref_cmdb_ci_computer.os_version"] = dxc_cmdb_df["dxc_ref_cmdb_ci_computer.os_version"].str.strip(" ")
# dxc_cmdb_df["dxc_ref_cmdb_ci_computer.cpu_count"] = dxc_cmdb_df["dxc_ref_cmdb_ci_computer.cpu_count"].str.strip(" ")
# dxc_cmdb_df["dxc_ref_cmdb_ci_computer.ram"] = dxc_cmdb_df["dxc_ref_cmdb_ci_computer.ram"].str.strip(" ")

# dxc_cmdb_df.sort_values(by=["dxc_name"], inplace=True, ascending=True)
# dxc_cmdb_df.drop_duplicates(subset=['dxc_name'], inplace=True, keep='first')
message = "DXC dump status ..."
print(message, dxc_cmdb_df.shape)
# print(dxc_cmdb_df.shape, dxc_cmdb_df.columns, dxc_cmdb_df.info())
# print(dxc_cmdb_df.info())
# print(dxc_cmdb_df.columns.tolist())


'''
~~~~~~~~~~~~~~~~~~~~~~~~~~
Preparing the BSL dataframe
~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
# print("\n\n")
message = "\nProcessing BSL dump file .."
print(message)
# bsl_cmdb_df = pd.DataFrame()
# bsl_cmdb_df = pd.read_excel(path2, index_col=None, engine="openpyxl", usecols="A,B,D,F,G,J,K,O,P,Q,S", header=0)
bsl_cmdb_df = pd.read_excel(path2, index_col=None, engine="openpyxl",header=0)
bsl_cmdb_df.rename(columns=lambda x:  'bsl_'+x, inplace=True)
# print(bsl_cmdb_df.columns, bsl_cmdb_df.shape, bsl_cmdb_df.info())
bsl_cmdb_df["bsl_name"] = bsl_cmdb_df["bsl_name"].astype('str')
bsl_cmdb_df["bsl_name"] = bsl_cmdb_df["bsl_name"].str.strip(" ")

bsl_cmdb_df["bsl_install_status"] = bsl_cmdb_df["bsl_install_status"].astype('str')
bsl_cmdb_df["bsl_install_status"] = bsl_cmdb_df["bsl_install_status"].str.strip(" ")

bsl_cmdb_df["bsl_serial_number"] = bsl_cmdb_df["bsl_serial_number"].astype('str')
bsl_cmdb_df["bsl_serial_number"] = bsl_cmdb_df["bsl_serial_number"].str.strip(" ")

# print(bsl_cmdb_df["bsl_name"].shape)
# print(bsl_cmdb_df["bsl_serial_number"].shape)
# print(bsl_cmdb_df["bsl_install_status"].shape)

bsl_cmdb_df["bsl_sys_class_name"] = bsl_cmdb_df["bsl_sys_class_name"].str.strip(" ")
bsl_cmdb_df["bsl_ip_address"] = bsl_cmdb_df["bsl_ip_address"].str.strip(" ")
bsl_cmdb_df["bsl_model_id"] = bsl_cmdb_df["bsl_model_id"].str.strip(" ")
bsl_cmdb_df["bsl_location"] = bsl_cmdb_df["bsl_location"].str.strip(" ")
bsl_cmdb_df["bsl_manufacturer"] = bsl_cmdb_df["bsl_manufacturer"].str.strip(" ")
bsl_cmdb_df["bsl_manufacturer"] = bsl_cmdb_df["bsl_manufacturer"].str.strip(" ")
bsl_cmdb_df["bsl_ref_cmdb_ci_computer.os_version"] = bsl_cmdb_df["bsl_ref_cmdb_ci_computer.os_version"].str.strip(" ")
bsl_cmdb_df["bsl_ref_cmdb_ci_computer.cpu_count"] = bsl_cmdb_df["bsl_ref_cmdb_ci_computer.cpu_count"].str.strip(" ")
bsl_cmdb_df["bsl_ref_cmdb_ci_computer.ram"] = bsl_cmdb_df["bsl_ref_cmdb_ci_computer.ram"].str.strip(" ")

bsl_cmdb_df.sort_values(by=["bsl_name"], inplace=True, ascending=True)
bsl_cmdb_df.drop_duplicates(subset=['bsl_name'],inplace=True, keep='first')
message = "BSL dump after cleaning duplicates from CI names ..."
print(message, bsl_cmdb_df.shape)
bsl_cmdb_df.sort_values(by=["bsl_serial_number"], inplace=True, ascending=True)
# bsl_cmdb_df.drop_duplicates(subset=['bsl_serial_number'],inplace=True, keep='first')
# message = "BSL dump after cleaning duplicates from Serial numbers ..."
# print(message, bsl_cmdb_df.shape)
# print(bsl_cmdb_df.columns, bsl_cmdb_df.shape, bsl_cmdb_df.info())

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~
Preparing the status dataframe
~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
message = "\nProcessing Status Mapper file .."
print(message)
df_status = pd.DataFrame()
df_status = pd.read_excel(os.path.join(path3), index_col=None, engine="openpyxl", skiprows=1, header=0)
df_status.rename(columns={"DXC  Status":"DXC_Status_mapper","BSL  Status":"BSL_Status_mapper"}, inplace=True)
# df_status.sort_values(by=["BSL_Status_mapper"], ascending=True)
df_status.drop(columns="Unnamed: 0",inplace=True)
df_status["DXC_Status_mapper"].astype('str')
df_status["DXC_Status_mapper"].str.strip(" "
)
df_status["BSL_Status_mapper"].astype('str')
df_status["BSL_Status_mapper"].str.strip(" ")

df_status.fillna(value='undefined', inplace=True)
# print(df_status["DXC_Status_mapper"])
# print(df_status["BSL_Status_mapper"])
# print(df_status)
message = "Status file read and processed ..."
print(message)


'''
~~~~~~~~~~~~~~~~~~~~~~~~~
- VLOOKUP from DXC on BSL 
- Using dxc_name as base column
~~~~~~~~~~~~~~~~~~~~~~~~~
'''
# print("\n\n")
df_out_DXC = pd.DataFrame()
df_out_DXC = pd.merge(dxc_cmdb_df,bsl_cmdb_df[['bsl_name','bsl_serial_number','bsl_install_status','bsl_sys_class_name','bsl_ip_address','bsl_model_id','bsl_location','bsl_manufacturer','bsl_lease_id','bsl_ref_cmdb_ci_computer.os_version','bsl_ref_cmdb_ci_computer.cpu_count','bsl_ref_cmdb_ci_computer.ram']], how='left', left_on='dxc_name', right_on='bsl_name')
##,'bsl_serial_number'
message = "\nAfter looking up with dxc_name  ..."

#%%
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- VLOOKUP of BSL status on Status map to retrieve the DXC status
- Match the DXC status with the retrieved status and compare
- Store the comparison results
- Extract City name from DXC location and BSL location
- Match the City name and store the comparison results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
df_out_DXC = pd.merge(df_out_DXC,df_status, how='left', left_on='bsl_install_status', right_on='BSL_Status_mapper')
message = "\nAfter looking up BSL Install Status with Status Mapping table  ..."
print(message, df_out_DXC.shape)
df_out_DXC.drop(columns="BSL_Status_mapper",inplace=True)
# print(df_out_DXC.shape)
df_out_DXC["Status_Matching_for_CI_Name"] = (df_out_DXC["dxc_install_status"] == df_out_DXC["DXC_Status_mapper"])
df_out_DXC.drop(columns="DXC_Status_mapper",inplace=True)
# print(df_out_DXC.columns.tolist)
# print(df_out_DXC["Status_Matched_via_Mapping_Table"])
message = "\nAfter comparing with Status Mapper table and capturing match status ..."
print(message, df_out_DXC.shape)
#%%
message = "\nComparing CITY name between DXC and BSL ..."
print(message)
DXC_loc_CITY = df_out_DXC["dxc_location"].str.split(",", n = -1, expand = True)
df_out_DXC["DXC_loc_CITY"] = DXC_loc_CITY[1]
df_out_DXC["DXC_loc_CITY"] = df_out_DXC["DXC_loc_CITY"].str.strip(" ")
# print(df_out_DXC["DXC_loc_CITY"])

BSL_loc_CITY =  df_out_DXC["bsl_location"].str.split(" ", n = -1, expand = True)
df_out_DXC["BSL_loc_CITY"] = BSL_loc_CITY[0]
df_out_DXC["BSL_loc_CITY"] = df_out_DXC["BSL_loc_CITY"].str.strip(" ")
# print(df_out_DXC["BSL_loc_CITY"])

df_out_DXC["location_match"] = (df_out_DXC["DXC_loc_CITY"] == df_out_DXC["BSL_loc_CITY"])
# print(df_out_DXC["location_match"])
message = "After comparing CITY name between DXC and BSL ..."
print(message, df_out_DXC.shape)

# print(df_out_DXC.columns.tolist())



#%%
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Rearranging the columns in the DXC output file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
message = "\nRearranging the columns in the DXC output file ..."
print(message)
df_out_DXC.insert(2,'bsl_name_',df_out_DXC['bsl_name'])
df_out_DXC.insert(7,'bsl_serial_number_via_CI-name_lookup',df_out_DXC['bsl_serial_number'])
df_out_DXC.insert(10,'bsl_install_status_via_CI-name',df_out_DXC['bsl_install_status'])
df_out_DXC.insert(11,'Install_Status_Match_for_CI_Name',df_out_DXC['Status_Matching_for_CI_Name'])
df_out_DXC.insert(14,'bsl_sys_class_name_',df_out_DXC['bsl_sys_class_name'])
df_out_DXC.insert(19,'bsl_ip_address_',df_out_DXC['bsl_ip_address'])
df_out_DXC.insert(21,'bsl_model_id_',df_out_DXC['bsl_model_id'])
df_out_DXC.insert(25,'bsl_lease_id_',df_out_DXC['bsl_lease_id'])
df_out_DXC.insert(27,'bsl_location_',df_out_DXC['bsl_location'])
df_out_DXC.insert(28,'DXC_loc_CITY_',df_out_DXC['DXC_loc_CITY'])
df_out_DXC.insert(29,'BSL_loc_CITY_',df_out_DXC['BSL_loc_CITY'])
df_out_DXC.insert(30,'location_match_',df_out_DXC['location_match'])
df_out_DXC.insert(33,'bsl_ref_cmdb_ci_computer.os_version_',df_out_DXC['bsl_ref_cmdb_ci_computer.os_version'])
df_out_DXC.insert(36,'bsl_ref_cmdb_ci_computer.cpu_count_',df_out_DXC['bsl_ref_cmdb_ci_computer.cpu_count'])
df_out_DXC.insert(38,'bsl_ref_cmdb_ci_computer.ram_',df_out_DXC['bsl_ref_cmdb_ci_computer.ram'])
df_out_DXC.insert(40,'bsl_manufacturer_',df_out_DXC['bsl_manufacturer'])


df_out_DXC.drop(columns=['bsl_name','bsl_serial_number','bsl_install_status','Status_Matching_for_CI_Name','bsl_sys_class_name','bsl_ip_address','bsl_model_id','bsl_lease_id','bsl_ref_cmdb_ci_computer.os_version','bsl_ref_cmdb_ci_computer.cpu_count','bsl_ref_cmdb_ci_computer.ram','bsl_manufacturer','bsl_location','DXC_loc_CITY','BSL_loc_CITY','location_match'],inplace=True)
# print(df_out_DXC.info())
message = "Done ..."
print(message, df_out_DXC.shape)
# print(message, df_out_DXC.shape, df_out_DXC.columns, df_out_DXC.info())

#%%
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- VLOOKUP of Serial number from DXC to BSL
- Compare the Install status again
    - VLOOKUP of BSL status on Status map to retrieve the DXC status
    - Match the DXC status with the retrieved status and compare
    - Store the comparison results in a sepearte column
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
# dxc_serialnum_df = 

message = "\nNow looking up BSL dump using Serial Numbers from DXC dump  ..."
print(message, df_out_DXC.shape)
df_out_DXC = pd.merge(df_out_DXC,bsl_cmdb_df[['bsl_serial_number','bsl_install_status']], how='left', left_on='dxc_serial_number', right_on='bsl_serial_number')
# df_out_DXC.rename(columns={'bsl_serial_number':'bsl_serial_number_via_Serial-Num_lookup'}, inplace=True)
df_out_DXC.insert(8,'bsl_serial_number_via_Serial-Num_lookup',df_out_DXC['bsl_serial_number'])
df_out_DXC.drop(columns="bsl_serial_number", inplace=True)

message = "\nRecomparing BSL Install Status with Status Mapping table   ..."
print(message)
df_out_DXC = pd.merge(df_out_DXC,df_status, how='left', left_on='bsl_install_status', right_on='BSL_Status_mapper')
df_out_DXC.drop(columns="BSL_Status_mapper", inplace=True)
# print(df_out_DXC.shape)
df_out_DXC["_Install_Status_Match_for_Serial-Num_"] = (df_out_DXC["dxc_install_status"] == df_out_DXC["DXC_Status_mapper"])
df_out_DXC.drop(columns="DXC_Status_mapper", inplace=True)
df_out_DXC.insert(13,'bsl_install_status_via_Serial-Num', df_out_DXC['bsl_install_status'])
df_out_DXC.insert(14,'Install_Status_Match_for_Serial-Num', df_out_DXC['_Install_Status_Match_for_Serial-Num_'])
df_out_DXC.drop(columns=["bsl_install_status","_Install_Status_Match_for_Serial-Num_"], inplace=True)

message = "\nAfter comparing with Status Mapper table and capturing match status ..."
print(message)
message = "Post lookup status ..."
print(message, df_out_DXC.shape)#, df_out_DXC.info())
#%%
#%%
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Splitting the class names in the DXC dump
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
class_names = list(df_out_DXC.groupby(["dxc_sys_class_name"]).groups.keys())
message = "\nDXC dump class names extracted ..."
print(message)
print("{} {} -- are the class names found.\n".format(" "*len(message),', '.join(class_names)))
# print(', '.join(class_names))

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Writing the DXC output file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

print(line)

with pd.ExcelWriter(os.path.join(path0,"DXC_CMDB_with_BSL.xlsx")) as writer:
    df_out_DXC.to_excel(writer, sheet_name="DXC_CMDB_mapped_BSL", engine="xlswriter", header=True, index=None)
    (max_row, max_col) = df_out_DXC.shape
    worksheet = writer.sheets["DXC_CMDB_mapped_BSL"]
    worksheet.autofilter(0, 0, max_row, max_col-1)
    
    message = "\nCreated DXC output file ....\n"
    print(message)
    
    count = 0
    for classes in class_names:
        df_out_DXC_class_cat = df_out_DXC[df_out_DXC["dxc_sys_class_name"].str.contains(classes)]
        count += df_out_DXC_class_cat.shape[0]
        # print(classes, df_out_DXC_class_cat.shape[0])
    # print(count)
        df_out_DXC_class_cat.to_excel(writer,sheet_name=classes, engine="xlswriter", header=True, index=None)
        (max_row, max_col) = df_out_DXC_class_cat.shape
        worksheet = writer.sheets[classes]
        worksheet.autofilter(0, 0, max_row, max_col-1)

        message = "Filtered class --> {} ,  in a seperate sheet in the DXC output file ...  {}  entries..."
        print(message.format(classes, df_out_DXC_class_cat.shape[0]))






###########################################################
# Procceing the BSL dump file with DXC lookups ( cross referrencing)....
###########################################################
# df_out_BSL_check = pd.DataFrame()
# df_out_BSL_check = pd.read_excel(path5)
# # df_out_BSL_check.info()
# # print(df_out_BSL_check.columns)
print(line)
message = "\nProcessing BSL dump ...\n"
print(message)

df_out_BSL = pd.merge(bsl_cmdb_df,dxc_cmdb_df[['dxc_name','dxc_serial_number','dxc_install_status','dxc_sys_class_name']], how='left', left_on=('bsl_name','bsl_serial_number'),  right_on= ('dxc_name','dxc_serial_number'))
# df_out_BSL.info()
message = "After looking up with bsl_name  ... "
print(message,df_out_BSL.shape)
df_out_BSL.insert(1,'dxc_name_',df_out_BSL['dxc_name'])
df_out_BSL.insert(5,'dxc_serial_number_',df_out_BSL['dxc_serial_number'])
df_out_BSL.insert(8,'dxc_install_status_',df_out_BSL['dxc_install_status'])
df_out_BSL.insert(10,'dxc_sys_class_name_',df_out_BSL['dxc_sys_class_name'])
# print(df_out_BSL.info())
# print(df_out_BSL.columns.tolist())
df_out_BSL.drop(columns=['dxc_name','dxc_serial_number','dxc_install_status','dxc_sys_class_name'], inplace=True)
print()
# print(df_out_BSL.columns.tolist())
with pd.ExcelWriter(os.path.join(path0,"BSL_CMDB_with_DXC.xlsx") ) as writer:
    df_out_BSL.to_excel(writer,  sheet_name="cmdb_ci_bsl_dxc",  engine="xlswriter", header=True, index=False)
    (max_row,max_col) = df_out_BSL.shape
    worksheet = writer.sheets["cmdb_ci_bsl_dxc"]
    worksheet.autofilter(0, 0, max_row, max_col-1)
    
    message = "Created BSL output file ...."
    print(message)




message = "\n\n...  E N D  ...\n\n"
print(message)

# %%
