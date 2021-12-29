array=[1, 'dog', 'cat', 5, 6, 'sky']
def insert(index, value):
    # First, we will have to create space for a new element.
    array.append(0)
    # then shift all the elements to the right from the index location
    for i in range(index,len(array)-1,-1):
        array[i+1]=array[i]
    # Finally assign the value of index
    array[index]=value
insert(0,'hi')
print(array)
