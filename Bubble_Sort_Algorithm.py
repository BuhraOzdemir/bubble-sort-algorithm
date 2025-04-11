def BubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if(array[j]>array[j+1]):
                array[j],array[j+1]=array[j+1],array[j]


array1=[3,10,8,-9,5,-7,200,-420]
BubbleSort(array1)
print(array1)
