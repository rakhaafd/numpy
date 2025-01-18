import numpy

my_list: list = [1, 2, 3, 4, 5]
my_arr = numpy.array(my_list)
print(my_arr)
print(type(my_arr)) #<class 'numpy.ndarray'>

my_new_arr = numpy.asarray(my_list) #numpy.asarray cocok untuk menangani data data yang besar, karena bersifat efisien
print(my_new_arr)

arr_copy = numpy.copy(my_list) #membuat copy an dari my_list untuk dimodifikasi
arr_copy[0] = 10
print(arr_copy)

#fromfunction: membuat array dari matematika dari konsep yang ada pada function
# def nilai (a: int, b: int) -> int:
#     return a + b

# arr_math = numpy.fromfunction(nilai, (3, 3), dtype=int)
# print(arr_math)

#fromiter: membuat array dari hasil iterasi looping
my_arr2 = [nilai for nilai in range(5)]
arr_result = numpy.array(my_arr2, dtype=int)
print(arr_result)