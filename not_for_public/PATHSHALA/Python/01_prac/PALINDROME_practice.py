#####################################################################

### Test a string (single or multi word) for PALINDROME)

#####################################################################

str = input("Enter a single or a multi-word string :: ")
print("You have entered ::", str)

str_to_list = list(str)
# print(str, len(str))
# print(str_to_list, len(str_to_list))
l_str = len(str_to_list)

str_to_list_with_no_space = list()

for i in range(l_str):
    if str[i] != " ":
        str_to_list_with_no_space.append(str[i])
# print(str_to_list_with_no_space, len(str_to_list_with_no_space))

flag = 0
j = len(str_to_list_with_no_space) - 1

for i in range(len(str_to_list_with_no_space)):
    if str_to_list_with_no_space[i] == str_to_list_with_no_space[j]:
        flag = 1
    else:
        flag = 0
    j = j - 1

if flag == 1:
    print("It is a palindrome")
else:
    print("Not a palindrome")  


#####################	END 	################################################
