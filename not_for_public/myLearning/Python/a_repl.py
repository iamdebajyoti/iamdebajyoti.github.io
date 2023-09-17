from arepl_dump import dump


# def count_to_ten_generator():
#   for number in range(10):
#     yield number
# my_generator = count_to_ten_generator()
# print(my_generator)
# list_or_the_rest = list(my_generator)
# print(list_or_the_rest)

# # first_number = next(my_generator)
# # print(first_number)
# # first_number = next(my_generator)
# # print(first_number)
# # first_number = next(my_generator)
# # print(first_number)
# # first_number = next(my_generator)
# # print(first_number)





# def inorder(t):
#     if t:
#         for x in inorder(t.left):
#             yield x

#         yield t.label

#         for x in inorder(t.right):
#             yield x


# next(inorder(my_generator))



import datetime
import dateutil
from dateutil.relativedelta import relativedelta

old = datetime.date(2005,12,1)
today1 = datetime.datetime.today()
cur = datetime.date(today1.year, today1.month, today1.day)
datediff = relativedelta(cur, old)
print(f"{datediff.years} years, {datediff.months} months and {datediff.days} days")

# if datediff.months > 1 : print("months"), print("month")