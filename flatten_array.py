import numpy

# numpy.flatten(): mengembalikan salinan dari array multidimensi menjadi 1 dimensi
# contoh_array = numpy.array([[1,2,3], [4,5,6]])
# array_flatten = contoh_array.flatten()

# print(f"array yang tidak di flatten {contoh_array}")
# print(f"array yang sudah di flatten {array_flatten}")
# array yang tidak di flatten [[1 2 3]
#  [4 5 6]]
# array yang sudah di flatten [1 2 3 4 5 6]

#ravel(): perubahan pada ravel() ini mempengaruhi nilai array asli
# contoh_array = numpy.array([[1,2,3], [4,5,6]])
# array_ravel = contoh_array.ravel()

# print(f"array yang belum di ravel {contoh_array}")
# print(f"array yang sudah di ravel {array_ravel}")

# array_ravel[0]=200
# print(f"contoh array = {contoh_array}")


#reshape(): mengatur bentuk ulang array, masih memungkinkan kita untuk mengubahnya ke bentuk semula
contoh_array = numpy.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
array_reshape = contoh_array.reshape(-1) #mengubah array yang semula 3 dimensi menjadi 1 dimensi
print(f"array asli {contoh_array}\n")
print(f"array yang di reshape {array_reshape}")