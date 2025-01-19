import numpy

#vstack: vertical stack
# contoh_array1 = numpy.array([[1,2], [3,4]])
# contoh_array2 = numpy.array([[5,6], [7,8]])
# gabung = numpy.vstack((contoh_array1, contoh_array2))
# print(gabung)

# hstack: horizontal stack
# contoh_array1 = numpy.array([[1,2], [3,4]])
# contoh_array2 = numpy.array([[5,6], [7,8]])
# gabung = numpy.hstack((contoh_array1, contoh_array2))
# print(gabung)

#dstack: untuk array 3d
# contoh_array1 = numpy.array([[1,2], [3,4]])
# contoh_array2 = numpy.array([[5,6], [7,8]])
# gabung = numpy.dstack((contoh_array1, contoh_array2))
# print(gabung)

#stack dengan axis 0
contoh_array1 = numpy.array([[1,2], [3,4]])
contoh_array2 = numpy.array([[5,6], [7,8]])
gabung = numpy.stack((contoh_array1, contoh_array2), axis=0)
print(gabung)