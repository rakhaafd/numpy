import numpy

array_1dimensi = numpy.array([4, 6, 7, 8, 9])
print(array_1dimensi)

#cek tipe data
print(type(array_1dimensi)) # <class 'numpy.ndarray'>

#cek ada berapa dimensi
print(f"{array_1dimensi.ndim} dimensi") #1 dimensi

# cek ada berapa elemen di dalam array
print(f"shape dari array 1 dimensi = {array_1dimensi.shape}") # shape dari array 1 dimensi = (5,)

array_2dimensi = numpy.array([[4,6,7], [8,9,10]]) # harus sama, tiap array harus tediri dari 3 elemen
print(array_2dimensi)
# [[ 4  6  7]
#  [ 8  9 10]]
print(f"{array_2dimensi.ndim} dimensi") # 2 dimensi
print(f"shape dari array 1 dimensi = {array_2dimensi.shape}") #(2, 3) 2 baris dan 3 kolom