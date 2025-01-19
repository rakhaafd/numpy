import numpy

#split: memecah array menjadi bagian yg lebih kecil
# contoh_array1 = numpy.array([1,2,3,4,5,6])
# bagi = numpy.split(contoh_array1, 3) #hanya bisa sama persis dengan ukurannya
# print(bagi) #[array([1, 2]), array([3, 4]), array([5, 6])

#array_split(): jika ingin bisa otomatis
# contoh_array = numpy.array([1,2,3,4,5,6,8,9])
# bagi_array = numpy.array_split(contoh_array, 3)
# print(bagi_array)

#hsplit(): membagi array sepanjang sumbu horizontal. default axisnya 1
#vsplit(): membagi array sepanjang sumbu vertikal. default axisnya 0
# contoh_array = numpy.array([[1,2,3,4], [6,7,8,9]])
# bagi = numpy.hsplit(contoh_array, 2)
# print(bagi)
contoh_array = numpy.array([[1,2,3,4], [6,7,8,9]])
bagi = numpy.vsplit(contoh_array, 2)
print(bagi)