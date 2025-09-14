import multiprocessing
import os
import string

print('The current processs id is : ' + str(os.getpid()) + '.')
print('The current parent processs id is : ' + str(os.getppid()) + '.')

process_pool = multiprocessing.cpu_count()
print(f'The number of CPU cores : {process_pool}')
print(f'The number of CPU cores : {os.cpu_count()}')
print()


a = [1,2,3,4,5]
alphabets = list(string.ascii_lowercase)
b = [26]
i = 1
for items in alphabets:
    #print(items)
    b[i] = items
    print(b[i])

#print(alphabets)
#print(b)




