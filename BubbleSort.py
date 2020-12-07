def BubbleSort(Lista):
    for numPasada in range(len(Lista)-1,0,-1):
        for i in range(numPasada):
            if Lista[i]>Lista[i+1]:
                temp = Lista[i]
                Lista[i] = Lista[i+1]
                Lista[i+1] = temp
    return Lista