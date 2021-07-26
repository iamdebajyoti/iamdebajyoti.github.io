#%%
"""setting up the environment"""
import os, sys, stat 
import pandas as pd
import numpy as np
from pandas import ExcelWriter
import datetime
from datetime import datetime
from pprint import pprint

"""
### STEP 0 ###
setting file paths
Creating the initial dataFrames
Creating the Output File dataframe
"""
script_dir = os.path.dirname(os.path.abspath(__file__))
# print(type(script_dir), script_dir)

#%%
message = "Please enter the following input Filenames with file extensions AND the FULL PATH --"
print("\n\t" + "="*(len(message)+8) + "\n\t" + " "*4 + message + " "*4 + "\n\t" + "="*(len(message)+8) +"\n") 

print("\t", end="")
order_file = input(r'FILE  _Order_Tracking_Report-_DXC_-Queensland_Rail :: ')
order_file = os.path.abspath(order_file)
# order_file = r"C:\DEB\DXC_Automation\UCMS_31107\279577_Order_Tracking_Report-_DXC_-Queensland_Rail.xls"
print("\t", end="")
dashboard_file = input(r'FILE  Daily dashboard :: ')
dashboard_file = os.path.abspath(dashboard_file)
# dashboard_file = r"C:\DEB\DXC_Automation\UCMS_31107\Daily dashboard.xlsx"
print("\t", end="")
lease_supl_cons_file = input(r'FILE  DXC Lease Supplements Consolidated :: ')
lease_supl_cons_file = os.path.abspath(lease_supl_cons_file)
# lease_supl_cons_file = r"C:\DEB\DXC_Automation\UCMS_31107\DXC Lease Supplements Consolidated.xls"
print("\t", end="")
monthly_rental_file = input(r'FILE  Monthly rental prize :: ')
# monthly_rental_file = r"C:\DEB\DXC_Automation\UCMS_31107\Monthly rental prize.xlsx"
print("\t", end="")
qr_euc_models_file = input(r'FILE  QR EUC models :: ')
# qr_euc_models_file = r"C:\DEB\DXC_Automation\UCMS_31107\QR EUC models 20191001.xlsx"
#output_file = 


df_orders = pd.read_excel(order_file, sheet_name="Order Status Data", header=0, usecols=["Po Num", "Order Num", "Product Desc", "Brand Desc", "Combine svc tag", "Order Qty","Shipped Date"], encoding="ISO-8859-1", index_col=None, engine=None, na_values=None)
df_daily_dashboard = pd.read_excel(dashboard_file, sheet_name="Page 1", header=0, usecols=["Asset tag", "Serial number", "State", "Substate", "Assigned to", "Email", "Model", "Installed Date", "PO number"], encoding="ISO-8859-1", index_col=None, engine=None, na_values=None)
df_DXC_Lease_Supl_Cons= pd.read_excel(lease_supl_cons_file, sheet_name="Asset List", encoding="ISO-8859-1", index_col=None, engine=None, na_values=None)
df_monthly_rental_prize =  pd.read_excel(monthly_rental_file, sheet_name="Sheet1", header=0, encoding="ISO-8859-1", index_col=None, engine=None, na_values=None)
df_QR_EUC_models = pd.read_excel(qr_euc_models_file, sheet_name="Device models", header=0, encoding="ISO-8859-1", index_col=None, engine=None, na_values=None)
# df_Output_File = pd.DataFrame(columns=["Country","Customer","Contract Vendor","Contract Term","Billing Cycle","Lease Suppliment Term","Contract Lease Payment","Order Number","Serial Number","Serial Number Status","Asset Tag","Repository State","Repository Sub State","Assigned to","Email","Installation Date","Asset Description","Device Model Category", "PO Number","PO Match status","Order Qty","Order Qty Check","Shipped Date","Rental per Asset","Reconcilied", "Comments"], index=None)

# print(df_orders.shape,df_daily_dashboard.shape,df_DXC_Lease_Supl_Cons.shape,df_monthly_rental_prize.shape,df_QR_EUC_models.shape,df_Output_File.shape)


#%%
# ======================================== Processing Order Tracking report DF =====================================================

"""
- column H ("Combine svc tag") - split the serial numbers and count
- compare with count of column H and with column S ("Order Qty") and record any discrepancy inict_order_mismatch [ key will be column D ("Po Num"), value will be a comment]
- one serial number in each row - unpacking
- create a new DF - 'df_orders_unpacked' to hold the unpacked rows - this becomes the base DF for the orders file
- apply all the filters specified by requestor on the df_orders_unpacked in sequential manner 
- created df_orders_unpacked_PD_filters and 
- create a final filtered DF for Orders file - df_orders_unpacked_PD_filters and df_orders_unpacked_BD_filters to hold the filtered dataframes
- df_orders_unpacked_filtered becomes the final filtered dataframe
"""

message = "Processing Order Tracking report file started --"
print("\n\n\t" + "="*(len(message)+8) + "\n\t" + " "*4 + message + " "*4 + "\n\t" + "="*(len(message)+8) + "\n") 

row_start = 0
row_end = df_orders.shape[0]    
total_po_nums = total_order_numbers = total_serial_numbers = 0 ## needed for validation
po_nums_missing = order_nums_missing = serial_numbers_missing = 0 ## needed for validation
order_qty_check = list()
df_orders_unpacked = pd.DataFrame(columns=df_orders.columns)
for each_row in range(row_start,row_end):
    check1 = check2 = 0
    po_num = df_orders.iloc[each_row,0]
    order_num = df_orders.iloc[each_row,1]
    serial_numbers = df_orders.iloc[each_row,4]
    if (isinstance(po_num, np.int64)):
        total_po_nums += 1
    else:
        po_nums_missing += 1
    if (isinstance(order_num, np.int64)):
        total_order_numbers += 1
    else:
        order_nums_missing += 1
    if (isinstance(serial_numbers, str)):
        serial_numbers_count = len(serial_numbers.split(sep=","))
        total_serial_numbers = total_serial_numbers + serial_numbers_count
        if serial_numbers_count != df_orders.iloc[each_row,6]:
            check1 = 1
        else:
            check2 = 1
        serial_numbers_list = serial_numbers.split(sep=",") ## convert the serial number chunks to a list
        cnt = 0
        for unpacked_serials in range(0, len(serial_numbers_list)):
            new_list = list()
            new_list.append(df_orders.iloc[each_row,0])
            new_list.append(df_orders.iloc[each_row,1])
            new_list.append(df_orders.iloc[each_row,2])
            new_list.append(df_orders.iloc[each_row,3])
            new_list.append(serial_numbers_list[unpacked_serials])                            
            new_list.append(df_orders.iloc[each_row,5])
            new_list.append(df_orders.iloc[each_row,6])
            if (check1 == 1):
                order_qty_check.append("ORDER-SUPPLY MISMATCH for this PO")
            if (check2 == 1):
                order_qty_check.append("Supply as per Order")    
            cnt += 1
            ## converting the list to a Series
            temp_series = pd.Series(new_list, name="UnpackedSerials", index = df_orders.columns)
            df_orders_unpacked = df_orders_unpacked.append(temp_series, ignore_index=True)           
            # print("{} added".format(cnt))
    else:       
        serial_numbers_missing +=1
temp_series = pd.Series(order_qty_check, name="order_qty_check")
df_orders_unpacked["Order Qty Check"] = temp_series

print("\tOrder Tracking Report before unpacking has - {} - rows".format(df_orders.shape[0]))
"""
=========== Validation ==============
# print(check1,check2)
# print("Total number of Po numbers found - {}".format(total_po_nums))
# print("Total number of Po numbers missing - {}".format(po_nums_missing))
# print("Total number of Order numbers found - {}".format(total_order_numbers))
# print("Total number of Order numbers missing - {}".format(order_nums_missing))
# print("Total number of serial numbers found - {}".format(total_serial_numbers))
# print("Total number of serial numbers missing - {}".format(serial_numbers_missing))
"""
### Order Tracking file dataframe prepared
print("\tTotal rows after unpacking the Serial numbers - {}".format(df_orders_unpacked.shape[0]))

### Applying filters on Product Description as per the request
df_orders_unpacked_PD_filters = df_orders_unpacked[(df_orders_unpacked['Product Desc'] != "CLIENT PERIPHERALS")] 
df_orders_unpacked_PD_filters = df_orders_unpacked_PD_filters[(df_orders_unpacked_PD_filters['Product Desc'] != "SUPPORT SERVICES")]
df_orders_unpacked_PD_filters = df_orders_unpacked_PD_filters[(df_orders_unpacked_PD_filters['Product Desc'] != "Cloud Client")]
df_orders_unpacked_PD_filters = df_orders_unpacked_PD_filters[(df_orders_unpacked_PD_filters['Product Desc'] != "Other Electronics")]
df_orders_unpacked_PD_filters = df_orders_unpacked_PD_filters[(df_orders_unpacked_PD_filters['Product Desc'] != "UNKNOWN")]

print("\n\tFilter applied for Product Description as CLIENT PERIPHERALS, SUPPORT SERVICES, Cloud Client, Other Electronics, UNKNOWN.\n\t Removed {} rows".format(df_orders_unpacked.shape[0] - df_orders_unpacked_PD_filters.shape[0]))

### Applying filters on Brand Description as per the request
df_orders_unpacked_BD_filters = df_orders_unpacked_PD_filters[(df_orders_unpacked_PD_filters['Brand Desc'] != "PARTNER")]
df_orders_unpacked_BD_filters = df_orders_unpacked_BD_filters[(df_orders_unpacked_BD_filters['Brand Desc'] != "UNKNOWN")]

print("\n\tFilter applied for Brand Description as PARTNER and UNKNOWN.\n\t Removed {} rows".format(df_orders_unpacked_PD_filters.shape[0] - df_orders_unpacked_BD_filters.shape[0]))

df_orders_unpacked_filtered = df_orders_unpacked_BD_filters
print("\n\t\tValid rows after applying filters - {}".format(df_orders_unpacked_filtered.shape[0]))

df_orders_unpacked_filtered.rename(columns={"Po Num":"PO Number","Order Num":"Order Number","Combine svc tag":"Serial Number"}, inplace=True)
df_orders_unpacked_filtered = df_orders_unpacked_filtered.drop('Product Desc', axis=1)
df_orders_unpacked_filtered = df_orders_unpacked_filtered.drop('Brand Desc', axis=1)
df_orders_unpacked_filtered.insert(0,'Country', 'AUSTRALIA')
df_orders_unpacked_filtered.insert(1,'Customer', 'DXC TECHNOLOGY AUSTRALIA PTY LIMITED')
df_orders_unpacked_filtered.insert(2,'Contract Vendor', 'DELL')

# df_orders_unpacked_filtered.info()
message = "Processing Order Tracking report file completed --"
print("\t" + "="*(len(message)+8) + "\n\t" + " "*4 + message + " "*4 + "\n\t" + "="*(len(message)+8)) 

#%%
# ======================================= Processing Daily dashboard file DF  =========================================================
"""
 Processing the Daily Dashboard DF to create the required dataframe for vlookup/merge.
- Renaming the columns as per the final Ouput file and Order Tracking file
"""
message = "Processing Daily dashboard file started --"
print("\n\n\t" + "="*(len(message)+8) + "\n\t" + " "*4 + message + " "*4 + "\n\t" + "="*(len(message)+8) + "\n") 

def po_num_to_string(val):
    new_val = str(val)
    return new_val

df_daily_dashboard.rename(columns={"Asset tag":"Asset Tag","Serial number":"Serial Number","State":"Repository State",\
    "Substate":"Repository Sub State","Assigned to":"Assigned To",\
        "Model":"Asset Description","Installed Date":"Installation Date",\
            "PO number":"PO Number"},inplace=True)

df_daily_dashboard["PO Number"].apply(po_num_to_string)

df_daily_dashboard_slice = df_daily_dashboard.drop('PO Number', axis=1)
df_daily_dashboard_slice2 = df_daily_dashboard.filter(["PO Number","Serial Number"], axis=1)
df_daily_dashboard_slice3 = df_daily_dashboard.filter(["PO Number"], axis=1)
# print(df_daily_dashboard.shape)
# print(df_daily_dashboard_slice.shape)
# print(df_daily_dashboard_slice2.shape)

# >>>>>>>>>>>>>>>>> First Merge
dfmerged__order_dashbrd = pd.merge(df_orders_unpacked_filtered,df_daily_dashboard_slice, on="Serial Number", how='left')

dfmerged__order_dashbrd['PO Number'].apply(po_num_to_string)
# print(dfmerged__order_dashbrd.info())
df_po_match_status = dfmerged__order_dashbrd.filter(["PO Number"], axis=1)
df_po_match_status['PO Number'].apply(po_num_to_string)
df_po_match_status.insert(1, 'PO match status', 'PO match found')
# print(df_po_match_status.info())

df_PO = pd.merge(df_daily_dashboard_slice3,df_po_match_status, on="PO Number",how='right')
# df_PO.reset_index(drop=True, inplace=True)
# print(df_PO.info())
df_PO.drop('PO Number', axis=1, inplace=True)
# print(df_PO.info())
dfmerged__order_dashbrd["PO match status"] = df_PO["PO match status"]
# print(dfmerged__order_dashbrd.info()) 
print("\tPO numbers in Order Tracking Report cross verified with Daily Dashboard file...")

message = "Processing Daily dashboard file completed --"
print("\t" + "="*(len(message)+8) + "\n\t" + " "*4 + message + " "*4 + "\n\t" + "="*(len(message)+8)) 

#%%

"""
===== Validation =============
with pd.ExcelWriter("df_orders_unpacked.xlsx") as writer:
    df_orders_unpacked.to_excel(writer, sheet_name="df_orders_unpacked", engine='xlsxwriter', header=True, index=False)
    (max_row,max_col) = df_orders_unpacked.shape
    worksheet = writer.sheets["df_orders_unpacked"]
    worksheet.autofilter(0, 0, max_row, max_col-1)
    writer.save()
with pd.ExcelWriter("df_orders_unpacked_filtered.xlsx") as writer:
    df_orders_unpacked_filtered.to_excel(writer, sheet_name="df_orders_unpacked_filtered", engine='xlsxwriter', header=True, index=False)
    (max_row,max_col) = df_orders_unpacked_filtered.shape
    worksheet = writer.sheets["df_orders_unpacked_filtered"]
    worksheet.autofilter(0, 0, max_row, max_col-1)
    writer.save()
with pd.ExcelWriter("df_po_match_status.xlsx") as writer:
    df_po_match_status.to_excel(writer, sheet_name="df_po_match_status", engine='xlsxwriter', header=True, index=False)
    (max_row,max_col) = df_po_match_status.shape
    worksheet = writer.sheets["df_po_match_status"]
    worksheet.autofilter(0, 0, max_row, max_col-1)
    writer.save()
with pd.ExcelWriter("df_daily_dashboard_slice3.xlsx") as writer:
    df_daily_dashboard_slice3.to_excel(writer, sheet_name="df_daily_dashboard_slice3", engine='xlsxwriter', header=True, index=False)
    (max_row,max_col) = df_daily_dashboard_slice3.shape
    worksheet = writer.sheets["df_daily_dashboard_slice3"]
    worksheet.autofilter(0, 0, max_row, max_col-1)
    writer.save()
with pd.ExcelWriter("df_PO.xlsx") as writer:
    df_PO.to_excel(writer, sheet_name="df_PO", engine='xlsxwriter', header=True, index=False)
    (max_row,max_col) = df_PO.shape
    worksheet = writer.sheets["df_PO"]
    worksheet.autofilter(0, 0, max_row, max_col-1)
    writer.save()
with pd.ExcelWriter("dfmerged__order_dashbrd.xlsx") as writer:
    dfmerged__order_dashbrd.to_excel(writer, sheet_name="dfmerged__order_dashbrd", engine='xlsxwriter', header=True, index=False)
    (max_row,max_col) = dfmerged__order_dashbrd.shape
    worksheet = writer.sheets["dfmerged__order_dashbrd"]
    worksheet.autofilter(0, 0, max_row, max_col-1)
    writer.save()
with pd.ExcelWriter("dfmerged__order_dashbrd2.xlsx") as writer:
    dfmerged__order_dashbrd2.to_excel(writer, sheet_name="dfmerged__order_dashbrd2", engine='xlsxwriter', header=True, index=False)
    (max_row,max_col) = dfmerged__order_dashbrd2.shape
    worksheet = writer.sheets["dfmerged__order_dashbrd2"]
    worksheet.autofilter(0, 0, max_row, max_col-1)
    writer.save()
"""

#%%
# ================================ Processing Lease supplement file =============================================================
"""
removing blank rows from the top
set the column headings
setting the start row of the dataframe
drop all the blank rows - cells have NaN values
create a new DF - df_DXC_Lease_unpacked
unmerge and fill the last 3 columns using 'fillna'
split the "Lease Suppliment Term" column to two - Contract Term and Billing Cycle
fill the Output File DF with the columns "Lease Suppliment Term","Contract Lease Payment"
process the Output File for the columns "Contract Term","Billing Cycle", from column "Lease Suppliment Term"

"""
message = "Processing Lease supplement file started --"
print("\n\n\t" + "="*(len(message)+8) + "\n\t" + " "*4 + message + " "*4 + "\n\t" + "="*(len(message)+8)+ "\n") 

# with pd.ExcelWriter("LeaseFile__RAW.xlsx") as writer:
#     df_DXC_Lease_Supl_Cons.to_excel(writer, sheet_name="raw", engine='xlsxwriter', header=True, index=False)
#     (max_row,max_col) = df_DXC_Lease_Supl_Cons.shape
#     worksheet = writer.sheets["raw"]
#     worksheet.autofilter(0, 0, max_row, max_col-1)
#     writer.save()
df_DXC_Lease_Supl_Cons = df_DXC_Lease_Supl_Cons[9:]
# with pd.ExcelWriter("LeaseFile__TOPREMOVED.xlsx") as writer:
#     df_DXC_Lease_Supl_Cons.to_excel(writer, sheet_name="top_removed", engine='xlsxwriter', header=True, index=False)
#     (max_row,max_col) = df_DXC_Lease_Supl_Cons.shape
#     worksheet = writer.sheets["top_removed"]
#     worksheet.autofilter(0, 0, max_row, max_col-1)
#     writer.save()
df_DXC_Lease_Supl_Cons = df_DXC_Lease_Supl_Cons.reset_index(drop = True)
# with pd.ExcelWriter("LeaseFile__FIRSTRESETINDEX.xlsx") as writer:
#     df_DXC_Lease_Supl_Cons.to_excel(writer, sheet_name="first_reset_idx", engine='xlsxwriter', header=True, index=False)
#     (max_row,max_col) = df_DXC_Lease_Supl_Cons.shape
#     worksheet = writer.sheets["first_reset_idx"]
#     worksheet.autofilter(0, 0, max_row, max_col-1)
#     writer.save()
## resetting the start row
# df_DXC_Lease_Supl_Cons3 = df_DXC_Lease_Supl_Cons2.loc[:,:]
df_DXC_Lease_Supl_Cons.columns = df_DXC_Lease_Supl_Cons.iloc[0]
## resetting the start row of the data
df_DXC_Lease_Supl_Cons = df_DXC_Lease_Supl_Cons[1:]
# with pd.ExcelWriter("LeaseFile__FIRSTREPOSITON.xlsx") as writer:
#     df_DXC_Lease_Supl_Cons.to_excel(writer, sheet_name="first_reposition", engine='xlsxwriter', header=True, index=False)
#     (max_row,max_col) = df_DXC_Lease_Supl_Cons.shape
#     worksheet = writer.sheets["first_reposition"]
#     worksheet.autofilter(0, 0, max_row, max_col-1)
#     writer.save()

## dropping all completely blank rows and retain the same dataframe
df_DXC_Lease_Supl_Cons.dropna(how = 'all', inplace=True)
# with pd.ExcelWriter("LeaseFile__FIRSTCLEANUP.xlsx") as writer:
#     df_DXC_Lease_Supl_Cons.to_excel(writer, sheet_name="first_cleanup", engine='xlsxwriter', header=True, index=False)
#     (max_row,max_col) = df_DXC_Lease_Supl_Cons.shape
#     worksheet = writer.sheets["first_cleanup"]
#     worksheet.autofilter(0, 0, max_row, max_col-1)
#     writer.save()
## Unpacking the last 3 columns with merged cells accross column
df_DXC_Lease_Supl_Cons["Lease Suppliment Date"].fillna(method = 'ffill', inplace=True)
df_DXC_Lease_Supl_Cons["Lease Suppliment Term"].fillna(method = 'ffill', inplace=True)
df_DXC_Lease_Supl_Cons["Lease Suppliment Rental Amount"].fillna(method = 'ffill', inplace=True)
# with pd.ExcelWriter("LeaseFile__LAST3UNPACK.xlsx") as writer:
#     df_DXC_Lease_Supl_Cons.to_excel(writer, sheet_name="last3_unpck", engine='xlsxwriter', header=True, index=False)
#     (max_row,max_col) = df_DXC_Lease_Supl_Cons.shape
#     worksheet = writer.sheets["last3_unpck"]
#     worksheet.autofilter(0, 0, max_row, max_col-1)
#     writer.save()
## dropping more unnecessary rows having "EQUIPMENT DESCRIPTION"
df_DXC_Lease_Supl_Cons.dropna(how = 'any', inplace=True)
# with pd.ExcelWriter("LeaseFile__DROPPINGEQUIP.xlsx") as writer:
#     df_DXC_Lease_Supl_Cons.to_excel(writer, sheet_name="dropping_equip", engine='xlsxwriter', header=True, index=False)
#     (max_row,max_col) = df_DXC_Lease_Supl_Cons.shape
#     worksheet = writer.sheets["dropping_equip"]
#     worksheet.autofilter(0, 0, max_row, max_col-1)
#     writer.save()
print("\tTotal count of Invoice Number rows - {}".format(df_DXC_Lease_Supl_Cons.shape[0]))
# df_DXC_Lease_Supl_Cons= df_DXC_Lease_Supl_Cons.reset_index(drop = True)
# print(df_DXC_Lease_Supl_Cons.head(30))
print("\tOriginal DXC Lease Suppliment file has  {}  rows and  {}  columns".format(df_DXC_Lease_Supl_Cons.shape[0],df_DXC_Lease_Supl_Cons.shape[1]))
# df_DXC_Lease_Supl_Cons.iloc[80:]

### Iterating the dataframe for splitting the "Tag Number" column (Serial Number). 
### This column has seperator as 'space', 'new line', 'carriage return' and line endigs with 'new line'
start_row = 0
last_row = df_DXC_Lease_Supl_Cons.shape[0]
tag_nums_each_row  = tag_num_total_count = 0
df_DXC_Lease_unpacked = pd.DataFrame().reindex(columns=df_DXC_Lease_Supl_Cons.columns)
for rows_ in range(start_row, last_row):
    tags = df_DXC_Lease_Supl_Cons.iloc[rows_,6]
    # print(tags, type(tags))
    tags_1 =  tags.replace("\n"," ")  ## removing 'new line'
    # print(tags_1, type(tags_1))
    tags_2 = tags_1.replace("\r","")  ## removing 'carriage return'
    # print(tags_2, type(tags_2))
    tag_list = tags_2.split(sep = " ")  ## string to list -> delimiter = 'space' --> unpacking
    # print(tag_list, type(tag_list))
    tag_list = list(filter(None, tag_list)) ## removing empty list entries formed due to the previous processings --> clean up
    # print(tag_list, type(tag_list), len(tag_list))
    # print("-"*30)
    tag_nums_each_row = len(tag_list)  
    tag_num_total_count = tag_num_total_count + tag_nums_each_row
    # print("{} more tag/serial numbers found. A total of {} tag/serial numbers tracked so far..".format(tag_nums_each_row, tag_num_total_count))
    cnt = 0
    for expand_rows_ in range(0, len(tag_list)):
        new_list = list()
        new_list.append(df_DXC_Lease_Supl_Cons.iloc[rows_,0])
        new_list.append(df_DXC_Lease_Supl_Cons.iloc[rows_,1])
        new_list.append(df_DXC_Lease_Supl_Cons.iloc[rows_,2])
        new_list.append(df_DXC_Lease_Supl_Cons.iloc[rows_,3])
        new_list.append(df_DXC_Lease_Supl_Cons.iloc[rows_,4])
        new_list.append(df_DXC_Lease_Supl_Cons.iloc[rows_,5])
        new_list.append(tag_list[expand_rows_])
        new_list.append(df_DXC_Lease_Supl_Cons.iloc[rows_,7])
        new_list.append(df_DXC_Lease_Supl_Cons.iloc[rows_,8])
        new_list.append(df_DXC_Lease_Supl_Cons.iloc[rows_,9])
        temp_series = pd.Series(new_list, name="UnpackedTags", index = df_DXC_Lease_Supl_Cons.columns)
        df_DXC_Lease_unpacked = df_DXC_Lease_unpacked.append(temp_series, ignore_index=True)
        cnt += 1
#         print("{} more new rows added ... ".format(cnt))
#     print("{} total new rows added".format(df_new_rows.shape[0]))
print("\tA total of {} tag/serial numbers have been tracked.".format(tag_num_total_count))
print("\tFinal size of the Lease Supplement dataframe - {} rows...".format(df_DXC_Lease_unpacked.shape[0]))
    # df_DXC_Lease_unpacked.tail(30)
# with pd.ExcelWriter("LeaseFile__TAGUNPACK.xlsx") as writer:
#     df_DXC_Lease_unpacked.to_excel(writer, sheet_name="tag_unpck", engine='xlsxwriter', header=True, index=False)
#     (max_row,max_col) = df_DXC_Lease_unpacked.shape
#     worksheet = writer.sheets["tag_unpck"]
#     worksheet.autofilter(0, 0, max_row, max_col-1)
#     writer.save()
df_DXC_Lease_unpacked.rename(columns={"Tag Number":"Serial Number","Lease Suppliment Rental Amount":"Contract Lease Payment"},inplace=True)

df_DXC_Lease_unpacked_slice1 = df_DXC_Lease_unpacked.filter(["Serial Number","Lease Suppliment Term","Contract Lease Payment"], axis=1)
# with pd.ExcelWriter("LeaseFile__FIRSTSLICE.xlsx") as writer:
#     df_DXC_Lease_unpacked_slice1.to_excel(writer, sheet_name="first_slice", engine='xlsxwriter', header=True, index=False)
#     (max_row,max_col) = df_DXC_Lease_unpacked_slice1.shape
#     worksheet = writer.sheets["first_slice"]
#     worksheet.autofilter(0, 0, max_row, max_col-1)
#     writer.save()
_ii_ = 0
_jj_ = df_DXC_Lease_unpacked_slice1.shape[0]
Contract_Term = list()
Billing_Cycle = list()
for _ii_ in range(0, _jj_):
    term_billing = str(tuple(str(df_DXC_Lease_unpacked_slice1.iloc[_ii_,1]).split(sep=":"))[1]).split(sep=" ")
    term_billing = tuple(filter(None, term_billing))
    Contract_Term.append(term_billing[0])
    Billing_Cycle.append(term_billing[1])
# print(len(Contract_Term))
# print(len(Billing_Cycle))
temp_series = pd.Series(Contract_Term, name="Contract_Term")
df_DXC_Lease_unpacked_slice1["Contract Term"] = temp_series
temp_series = pd.Series(Billing_Cycle, name="Billing_Cycle")
df_DXC_Lease_unpacked_slice1["Billing Cycle"] = temp_series
# df_DXC_Lease_unpacked_slice1.info()
# print(df_DXC_Lease_unpacked_slice1.head(30))
# with pd.ExcelWriter("LeaseFile__FINAL.xlsx") as writer:
#     df_DXC_Lease_unpacked_slice1.to_excel(writer, sheet_name="final", engine='xlsxwriter', header=True, index=False)
#     (max_row,max_col) = df_DXC_Lease_unpacked_slice1.shape
#     worksheet = writer.sheets["final"]
#     worksheet.autofilter(0, 0, max_row, max_col-1)
#     writer.save()
print("\tThe Lease Supplement data processing completed with  {}  rows and  {}  columns".format(df_DXC_Lease_unpacked_slice1.shape[0],df_DXC_Lease_unpacked_slice1.shape[1]))

dfmerged__order_dashbrd_lease = pd.merge(dfmerged__order_dashbrd,df_DXC_Lease_unpacked_slice1, on="Serial Number",how='left')
# dfmerged__order_dashbrd_lease.info()

message = "Processing Lease supplement file completed --"
print("\t" + "="*(len(message)+8) + "\n\t" + " "*4 + message + " "*4 + "\n\t" + "="*(len(message)+8)) 

#%%
"""
Processing the models and their rentals
This uses Set Intersection method implemented on two sets generated from two lists and then the count of matches from the intersection was used to select the final Device Category
"""
message = "Processing QR EUC models file started --"
print("\n\n\t" + "="*(len(message)+8) + "\n\t" + " "*4 + message + " "*4 + "\n\t" + "="*(len(message)+8) + "\n") 

df_QR_EUC_models.dropna(how='all',inplace=True) # clean up of blank rows
df_QR_EUC_models_slice = df_QR_EUC_models.filter(["Model","Device model" ], axis=1)
df_QR_EUC_models_slice.rename(columns={"Model":"Asset Description","Device model":"Device Model Category"},inplace=True)
df_QR_EUC_models_slice['Device Model Category'] = df_QR_EUC_models_slice['Device Model Category'].str.rstrip()
# print(df_QR_EUC_models_slice.shape)
EUC_models_Kwds__CAT_list = list()
for _ii_ in range(0, df_QR_EUC_models_slice.shape[0]):
    model_tuple = tuple()
    model_tuple = (str(df_QR_EUC_models_slice.iloc[_ii_,0]).split(sep=" "),df_QR_EUC_models_slice.iloc[_ii_,1])
    # print(type(model_tuple[0]),type(model_tuple[1]))
    EUC_models_Kwds__CAT_list.append(model_tuple)
print("\tModel names and model category matrix generated...")
# asset_ctgrs = dfmerged__order_dashbrd.filter(["Serial Number","Asset Description"], axis=1)
# asset_ctgrs.insert(2, 'Device Model Category', '')
dfmerged__order_dashbrd_lease.insert(21, 'Device Model Category', '')
for _ii_ in range(0, dfmerged__order_dashbrd_lease.shape[0]):
    asset_kwds = str(dfmerged__order_dashbrd_lease.iloc[_ii_,14]).split(sep=" ")
    match_count_prev = match_count_new = 0
    for _zz_ in range(0, len(EUC_models_Kwds__CAT_list)):
      match_count_new = len(list(set(asset_kwds) & set(EUC_models_Kwds__CAT_list[_zz_][0])))
      if (match_count_new > match_count_prev):
          dfmerged__order_dashbrd_lease.iloc[_ii_,21] = EUC_models_Kwds__CAT_list[_zz_][1]
          flash = EUC_models_Kwds__CAT_list[_zz_][1]
          match_count_prev = match_count_new
print("\tCategorization of Assets completed...")
# print(dfmerged__order_dashbrd_lease.iloc[0:30,[14,21]])      
        
message = "Processing QR EUC models file completed --"
print("\t" + "="*(len(message)+8) + "\n\t" + " "*4 + message + " "*4 + "\n\t" + "="*(len(message)+8)) 
    
#%%   
"""
The Monthly Rental Price file has special characters in some rows in the Category column e.g. (Bundle)
This needs to be removed ==> df cell --> string-split --> tuple[0] --> replace the df cell with the cleansed value
"""
message = "Processing Monthly Rental Price file started --"
print("\n\n\t" + "="*(len(message)+8) + "\n\t" + " "*4 + message + " "*4 + "\n\t" + "="*(len(message)+8) + "\n") 
    
df_monthly_rental_prize_slice = df_monthly_rental_prize.filter(["Category","Final QR Monthly Fee"],axis=1)
df_monthly_rental_prize_slice.rename(columns={"Category":"Device Model Category","Final QR Monthly Fee":"Rental per Asset"},inplace=True)
_device_cat_name_ = ""
for _device_cats_ in range(0, df_monthly_rental_prize_slice.shape[0]):
    _device_cat_name_ = tuple(str(df_monthly_rental_prize_slice.iloc[_device_cats_,0]).split(sep=" ("))[0]
    _device_cat_name_ = _device_cat_name_.replace("- ","") #removing the '-' characters from the Device Category names
    df_monthly_rental_prize_slice.iloc[_device_cats_,0] = _device_cat_name_

# print(dfmerged__order_dashbrd_lease["Device Model Category"])
# print(df_monthly_rental_prize_slice)    
dfmerged__order_dashbrd_lease_rental = pd.merge(dfmerged__order_dashbrd_lease,df_monthly_rental_prize_slice,on="Device Model Category",how='left')
# dfmerged__order_dashbrd_lease_rental.head()

message = "Processing Monthly Rental Price file completed --"
print("\t" + "="*(len(message)+8) + "\n\t" + " "*4 + message + " "*4 + "\n\t" + "="*(len(message)+8)) 

#%%
"""
Adding the last 2 columns 'Serial Number Status' and  'Reconciled'
If Asset Tag columns entries are blank/null >> Serial number is missing from Daily Dashboard - Serial Number Status set to boolean values (from series generated by isnull())

"""
message = "Adding Reconcile status... --"
print("\n\n\t" + "="*(len(message)+8) + "\n\t" + " "*4 + message + " "*4 + "\n\t" + "="*(len(message)+8) + "\n") 

col_Reconcile = list()
check_for_null_assets_tags = dfmerged__order_dashbrd_lease_rental["Asset Tag"].isnull()
# print(check_for_null_assets_tags)
dfmerged__order_dashbrd_lease_rental["Serial Number Status"] = check_for_null_assets_tags
# print(dfmerged__order_dashbrd_lease_rental["Serial Number Status"])
# _true_ = _false_ = 0

start_row = 0
last_row = dfmerged__order_dashbrd_lease_rental.shape[0]
Serial_Number_Status_col_idx = dfmerged__order_dashbrd_lease_rental.columns.get_loc("Serial Number Status")
for rows_ in range(start_row, last_row):
    if (dfmerged__order_dashbrd_lease_rental.iloc[rows_,Serial_Number_Status_col_idx]):
        dfmerged__order_dashbrd_lease_rental.iloc[rows_,Serial_Number_Status_col_idx] = "Missing from Dashboard"
        col_Reconcile.append("Failed")
        # _true_ += 1
    else:
        dfmerged__order_dashbrd_lease_rental.iloc[rows_,Serial_Number_Status_col_idx] = "Matched with Dashboard"
        col_Reconcile.append("Check more")
        # _false_ += 1 
    
# print(_true_,_false_)
temp_series = pd.Series(col_Reconcile, name="col_Reconcile")
dfmerged__order_dashbrd_lease_rental["Reconcilied"] = temp_series


# dfmerged__order_dashbrd_lease_rental.info()
# dfmerged__order_dashbrd_lease_rental["Serial Number Status"]
# dfmerged__order_dashbrd_lease_rental["Reconcilied"]
# dfmerged__order_dashbrd_lease_rental.info()    

message = "Entire data procrssing completed .. All files processed ... "
print("\t" + "="*(len(message)+8) + "\n\t" + " "*4 + message + " "*4 + "\n\t" + "="*(len(message)+8)) 


with pd.ExcelWriter("Output_File.xlsx") as writer:
    # df_orders_unpacked_filtered.to_excel(writer, sheet_name="order_unpkd_fltrd", engine='xlsxwriter', header=True, index=False)
    # df_daily_dashboard.to_excel(writer, sheet_name="daily_db", engine='xlsxwriter', header=True, index=False)
    # df_daily_dashboard_slice.to_excel(writer, sheet_name="daily_db_slice", engine='xlsxwriter', header=True, index=False)
    # dfmerged__order_dashbrd.to_excel(writer, sheet_name="dfmerged__order_dashbrd", engine='xlsxwriter', header=True, index=False)
    # (max_row,max_col) = dfmerged__order_dashbrd.shape
    # worksheet = writer.sheets["dfmerged__order_dashbrd"]
    # worksheet.autofilter(0, 0, max_row, max_col - 1)
    # dfmerged__order_dashbrd_lease.to_excel(writer, sheet_name="dfmerged__order_dashbrd_lease", engine='xlsxwriter', header=True, index=False)
    # (max_row,max_col) = dfmerged__order_dashbrd_lease.shape
    # worksheet = writer.sheets["dfmerged__order_dashbrd_lease"]
    # worksheet.autofilter(0, 0, max_row, max_col - 1)
    dfmerged__order_dashbrd_lease_rental.to_excel(writer, sheet_name="__order_dashbrd_lease_rental", engine='xlswriter', header=True, index=False)
    (max_row,max_col) = dfmerged__order_dashbrd_lease_rental.shape
    worksheet = writer.sheets["__order_dashbrd_lease_rental"]
    worksheet.autofilter(0, 0, max_row, max_col - 1)
    writer.save()

message = "Final Output file generated at ... "
print("\n\n\t" + "="*((len(message) if len(message)>len(script_dir) else len(script_dir))+8) + "\n\t" + " "*4 + message + " "*4 + "\n\t" + " "*4 + script_dir + " "*4 + "\n\t" + "="*((len(message) if len(message)>len(script_dir) else len(script_dir))+8))

message = "Scroll Up to see the application messages at various stages or PRESS ENTER to QUIT to WINDOWS"
print("\n\n\t" + " "*4 + message + "."*4, end="")
input()


#%%

