import numpy

#tipe data int
contoh_array = numpy.array([4,6,7,8], dtype=numpy.int8)
print(contoh_array)
print(contoh_array.dtype)

#tipe data desimal
contoh_array_desimal = numpy.array([3.1, 3.2, 3.3, 3.4], dtype=numpy.float16)
print(contoh_array_desimal)
print(contoh_array_desimal.dtype)

#tipe data bool
contoh_array_logika = numpy.array([True, False, True, False], dtype=numpy.bool_)
print(contoh_array_logika)

#tipe data kompleks
contoh_array_kompleks = numpy.array([4j + 1 - 2 + 5], dtype=numpy.complex64)
print(contoh_array_kompleks.dtype)
print(contoh_array_kompleks)

#tipe data positif
contoh_array_positif = numpy.array([1, 2, 3, 4, 5], dtype=numpy.uint32)
print(contoh_array_positif.dtype)
print(contoh_array_positif)

#tipe data unsigned
contoh_array_unsigned = numpy.array(['hello', 'world'], dtype="<U5")
print(contoh_array_unsigned)
print(contoh_array_unsigned.dtype)

# menangani dalam array banyak tipe data
contoh_array_beragam = numpy.array([{"nilai" : 1,}, ["abc",3], 20, "gyu young", True], dtype=object)
print(contoh_array_beragam)
print(contoh_array_beragam.dtype)