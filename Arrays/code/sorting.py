import time


def bubble_sort(my_list):
    for i in reversed(range(len(my_list))):
        for j in range(i):
            if my_list[j+1] < my_list[j]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

def select_sort(myList):
    lenght = len(myList)
    for i in range(lenght-1):
        min_index = i
        for j in range(i+1, lenght):
            if myList[j] < myList[min_index]:
                min_index = j
        if min_index!=i:
            temp = myList[i]
            myList[i]=myList[min_index]
            myList[min_index]=temp


    return myList







myList = list(reversed(range(1000)))
start_time = time.time()
bubble_sort(myList)
print('Exectution time bubble sort in ms:', (time.time() - start_time)*1000)


myList = list(reversed(range(1000)))
start_time = time.time()
select_sort(myList)
print('Exectution time insertion sort in ms:', (time.time() - start_time)*1000)