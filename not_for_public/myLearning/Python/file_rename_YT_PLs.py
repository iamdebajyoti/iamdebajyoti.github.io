import os

filelist = open(os.path.join(r"C:\Users\ddutta8\OneDrive - DXC Production\Desktop\pl_pl__Class_11_physics.txt"), "rt")

file_name_parts = dict()
single_file_parts = dict()

for i in list(filelist):
    # print(list(i))
    _ext_ = slice(-5) # 5 --> .mp4 and the \n (new line)
    i = i[_ext_] #strips the file extension part
    # print(i)
    i1 = i.split(sep="__")[0] #stores the playlist index number of the video file
    # print(i1)
    i2 = i.split(sep="__")[1] #stores the video file title
    # print(i2)
    '''
    The filename should not contain any of the following characters: 
    " (double quote), 
    * (asterisk), 
    < (less than), 
    > (greater than), 
    ? (question mark), 
    \ (backslash), 
    | (pipe), 
    / (forward slash), 
    : (colon)
    '''
    for c in list(i2):
        if c == "\"" or c == "*" or c == "<" or c == ">" or c == "?" or c == "\\" or c == "||" or c == "/" or c == ":" or c == "|":
            i2 = i2.replace(c, "-")
            
    _vid_ = slice(-11,len(i))
    i3 = i[_vid_] #strips the file video id part    
    # i3 = i.split(sep="__")[2] #stored the video id of the video file
    # print(i3)
    single_file_parts[i3] = (i1, i2)
    print(i1,i2,i3)

# print(single_file_parts)
# ii = 111
# ii = str(ii)
# print(single_file_parts.keys())
os.chdir('E:')
# _usb_folder_ = os.path.join(r'C:\DEB\New folder')
_usb_folder_ = r'E:\Physics\pl__Class 11 physics [ Physics wallah ]'
# print(type(_usb_folder_), _usb_folder_)
os.chdir(os.path.join(_usb_folder_))

_usb_folder_file_list = os.listdir(_usb_folder_)
# # print(type(_usb_folder_file_list))
print(_usb_folder_file_list)
c = 0
# print(os.getcwd())
for j in enumerate(_usb_folder_file_list):
    # print(type(j[1]), j[1])
    old_file_fullname = j[1]
    # print(type(old_file_fullname))
    print(old_file_fullname)
    # old_file_path = os.path.join(_usb_folder_,j[1])
    # old_file_path = os.path.abspath(old_file_path)
    # print(old_file_path)
    new_file_fullname = ""
    _ext_ = slice(-4) # 4 --> .mp4 and no (new line)
    old_file_name = old_file_fullname[_ext_] #strips the file extension part
    print(old_file_name)
    _vid_ = slice(-11,len(old_file_name))
    videoID = old_file_name[_vid_] #strips the file video id part
    print(videoID)
    if videoID in single_file_parts.keys(): 
        c = c + 1
        print(c)
        print(os.getcwd())
        new_file_fullname = single_file_parts[videoID][0] + "__" + single_file_parts[videoID][1] + "__" + videoID + ".mp4"
        # new_file_fullname = f'single_file_parts[j][0] + "__" + single_file_parts[j][1] + "__" + videoID + ".mp4"'
        # new_file_path = os.path.join(_usb_folder_,new_file_fullname)
        # new_file_path = os.path.abspath(new_file_path)
        # print(type(new_file_fullname))
        # print(j, single_file_parts[j])
        # print(old_file_path, '\n', new_file_path)
        print(old_file_fullname,'\n',new_file_fullname)
        # os.chdir(_usb_folder_)
        # os.replace(os.path.abspath(old_file_fullname), os.path.abspath(new_file_fullname))
        os.rename(os.path.join(_usb_folder_, old_file_fullname), os.path.join(_usb_folder_, new_file_fullname))
        # os.replace(old_file_path, new_file_path)
        
        
     
print(os.listdir(os.path.join(_usb_folder_)))
    
    
    