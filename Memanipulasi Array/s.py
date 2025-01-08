import numpy

my_arr = numpy.array([[1,2,3], [4,5,6], [7,8,9]])
print(my_arr[1, 2]) #angka pertama list keberapa, angka kedua index dari list tsb

# memotong array
my_arr2 = numpy.array([1, 2, 3, 4, 5, 6])
print(my_arr2[1:3]) #angka pertama dimulai, angka akhir batas -1
print(my_arr[2:, 1:])

#reshape
arr_yg_diubah = my_arr2.reshape(2, 3) #angka pertama baris, angka kedua kolom
print(arr_yg_diubah)

#concatination
my_arr3 = numpy.array([1,2,3])
my_arr4 = numpy.array([2, 4, 6])
gabung = numpy.concatenate((my_arr3, my_arr4)) #secara horizontal
print(gabung)

#vstack
my_arr5 = numpy.array([[1,2], [3,4]])
my_arr6 = numpy.array([[5,6], [7,8]])
gabungi = numpy.vstack((my_arr5, my_arr6)) #gabung array 2 dimensi secara vertikal ke bawah
print(gabungi)

#transpose
transpose = my_arr.T
print(transpose)

#flatten
array_flatten = my_arr.flatten() #mengubah array yang bersifat multidimensi menjadi 1 dimensi
print(array_flatten)