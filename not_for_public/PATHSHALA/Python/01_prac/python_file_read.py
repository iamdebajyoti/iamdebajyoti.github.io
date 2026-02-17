import os

# print("\n\n 1. example of read\n\n")
# with open("INC4030182_Prepare_message.txt", 'r') as f1:
#     line = f1.read()
#     print(type(line))
#     print(line)
# with open("INC4030182_Prepare_message.txt", 'r') as f11:
#     line2 = f11.read(5)
#     print(type(line2),line2)



# print("\n\n 2. example of readline\n\n")
# with open("INC4030182_Prepare_message.txt", 'r') as f2:
#     line21 = f2.readline()
#     print(type(line21))  
#     x = 1
#     while line21:
#         print(x, " -- ", line21.strip())
#         line21 = f2.readline()
#         x = x + 1
    
# with open("INC4030182_Prepare_message.txt", 'r') as f22:
#     line22 = f22.readline(10)
#     print(type(line22),line22)


print("\n\n 3. example of readlines\n\n")
with open("INC4030182_Prepare_message.txt", 'r') as f3:
    lines31 = f3.readlines()
print(type(lines31))
print(lines31)

print("\n==================\n")
i = 0
j = 1
for ll in lines31:
    print(i,",",j,">> ",ll.strip())
    i = i + 1
    j = j + 1

print("\n==================\n")
x = 14
print("Read line number", x , lines31[x])

with open("INC4030182_Prepare_message.txt", 'r') as f32:
    line32 = f32.readlines(30)
print(type(line32), line32)




# print("\n\n 4. example of other methods\n\n")
# with open("INC4030182_Prepare_message.txt", 'r') as f4:
#     for l in f4:
#         print(l.strip())


