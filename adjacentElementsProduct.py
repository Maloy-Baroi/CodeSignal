def adjacentElementsProduct(inputArray):


    l=inputArray
    list1=[]
    lenof_array=len(l)
    x=l[0]
    
    for i in range(1,lenof_array):
        y=x*l[i]
        x=l[i]
        list1.append(y)
    m=max(list1)
    print(m)

Array = [3, 6, -2, -5, 7, 3]
adjacentElementsProduct(Array)
