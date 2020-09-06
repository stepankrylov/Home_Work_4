list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

list_2 = [list_1[i+1] for i in range(len(list_1)-1) if list_1[i] < list_1[i+1]]
print(list_2)
