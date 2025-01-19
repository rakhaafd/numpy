import numpy
# contoh_array = numpy.array([2, 4, 6, 8, 10])

# for elemen in contoh_array:
#     print(elemen)


# contoh_array1 = numpy.array([[1,2,3], [4,5,6], [7,8,9]])
# for baris in contoh_array1:
#     for elemen in baris:
#         print(elemen, end=' ')
#     print()


# contoh_array2 = numpy.array([[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]])
# for matrix in contoh_array2:
#     for baris in matrix:
#         for elemen in baris:
#             print(elemen, end=' ')
#         print()
#     print()


#nditer(): mempermudah nested loop
# contoh_array3 = numpy.array([[1,2,3], [4,5,6], [7,8,9]])
# for elemeen in numpy.nditer(contoh_array3, order='F'): #membuat iterasi dari kolom
#     print(elemeen, end=' ')

array_modulus = numpy.array([10, 20, 30, 40, 50])
for elemen in numpy.nditer(array_modulus, op_flags=["readwrite"]):
    elemen[...] = elemen * 2
print(array_modulus)