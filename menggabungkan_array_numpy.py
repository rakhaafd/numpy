import numpy

#1 dimensi
# contoh_array1 = numpy.array([1,2,3])
# contoh_array2 = numpy.array([4,5,6])
# gabung_array = numpy.concatenate((contoh_array1, contoh_array2))
# print(gabung_array)

#2 dimensi
# contoh_array1 = numpy.array([[1,2], [3,4]])
# contoh_array2 = numpy.array([[5,6], [7,8]])
# gabung_array = numpy.concatenate((contoh_array1, contoh_array2), axis=1)
# print(gabung_array)

#3 dimensi
contoh_array1 = numpy.array([[[1, 2], [3,4]], [[5,6], [7,8]]])
contoh_array2 = numpy.array([[[9, 10], [11,12]], [[13,14], [15,16]]])
gabung = numpy.concatenate((contoh_array1, contoh_array2), axis=0)
print(gabung)