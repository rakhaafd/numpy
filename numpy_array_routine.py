import numpy

#numpy.zeros
my_arr = numpy.zeros((2, 4)) #membuat array berukuran 2 x 4 dengan elemen nya adalah 0
print(my_arr)

#numpy.ones
my_arr2 = numpy.ones((3, 5)) #membuat array berukuran 3 x 5 dengan elemen nya adalah 1
print(my_arr2)

#numpy.empty
my_arr3 = numpy.empty((3, 6)) #membuat array berukuran 3 x 6 dengan elemen nya adalah acak
print(my_arr3)

#numpy.arange
my_arr4 = numpy.arange(0, 10, 1) # 0: mulai, 10: end, 1: step
print(my_arr4)

#numpy.linspace
my_arr5 = numpy.linspace(0, 1, 5) #membuat interval
print(my_arr5)

#numpy.eye
my_arr6 = numpy.eye(12) #membuat matriks identitas berukuran 12x12
print(my_arr6)

#numpy.full
my_arr7 = numpy.full((4,5), 12) #membuat martriks dengan ukuran 4 x 5 dan elemennya adalah 12
print(my_arr7)

#numpy.random.rand
my_arr8 = numpy.random.rand(2, 3) # membuat matriks dengan ukuran 2x3 dengan nilai acak rentang 0-1
print(my_arr8)

#numpy.random.rand.
my_arr9 = numpy.random.randint(0, 20, (4, 5)) # membuat matriks dengan ukuran 4x5 dan nilai nya adalah 0-20
print(my_arr9)