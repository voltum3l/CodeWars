# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
# 
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:
# 
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]


def snail(matriz):
    rows=len(matriz) -1
    columns=len(matriz) -1
    lista=[]

    if len(matriz[0]) == 0 or len(matriz) == 0:
        return lista
    cantidadElementos=len(matriz)*len(matriz[0])

    rumbo=0
    topes=[0,0,0]
    indiceRow = 0
    indiceColumn = 0

    while len(lista) != cantidadElementos:

        lista.append(matriz[indiceRow][indiceColumn])
        if rumbo==0:
            if indiceColumn < (columns - topes[0]):
                indiceColumn=indiceColumn+1
            else:
                rumbo=1
                topes[0]=topes[0]+1
        #abajo
        if rumbo==1:
            if indiceRow < (rows - topes[1]):
                indiceRow=indiceRow+1
            else:
                rumbo=2
                topes[1]=topes[1]+1
        #izquierda
        if rumbo==2:
            if indiceColumn > topes[2]:
                indiceColumn=indiceColumn-1
            else:
                rumbo=3
                topes[2]=topes[2]+1
        #arriba
        if rumbo==3:
            if indiceRow > topes[0]:
                indiceRow = indiceRow - 1
            else:
                rumbo=0
                indiceColumn=indiceColumn+1


        print(lista)
