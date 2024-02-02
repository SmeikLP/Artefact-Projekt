# Needed for some algorythms, ignore otherwise
def append_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content + '\n')
        file.close()

#Requires function append_to_file(), replace this function with print for simpler logging
        
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                append_to_file(file_path, str(my_list))
    
my_list = [-41, 24, 38, 13, -12, -28, 5, 49, -46, -23, 17, 8, -3, -33, 30, -16, 19, -35, 40, -26, 1, 11, 43, 29, 7, -5, 45, -31, 32, 2, -34, -2, -43, 10, -45, 31, 14, 26, -29, 15, -8, -14, -44, 22, -18, -49, 34, -48, -37, -30]
bubble_sort(my_list)