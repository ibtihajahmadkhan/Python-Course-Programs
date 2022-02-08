## Example

# Write a program, which makes the following list,
# [1, 8.0, 'N', 2, 0.5, 'A', 3, 0.5, 'M', 4, 0.5, 'E']
# the code will check the list item one by one, if,
# it is int, add it to the previous int, 
# it is float, multiply it to the previous float answer,
# it is str, combine with the previous str,
# The output should look like a list[10, 1.0, 'Name']


My_lst = [1, 8.0, 'N', 2, 0.5, 'A', 3, 0.5, 'M', 4, 0.5, 'E']
temp_Ans_int = 0
temp_Ans_float = 1.0
temp_Ans_string = ''
for i in range(0,len(My_lst)):
    if type(My_lst[i])==int:
        temp_Ans_int = temp_Ans_int + My_lst[i]
    elif type(My_lst[i])==float:
        temp_Ans_float = temp_Ans_float * My_lst[i]
    else:
        temp_Ans_string = temp_Ans_string + My_lst[i]

New_List = [temp_Ans_int, temp_Ans_float , temp_Ans_string ]
print("The Answer list is ", New_List)
