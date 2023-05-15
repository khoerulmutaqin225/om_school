# Tipe data
# tipe data integer
data_integer = 11
print('data : ', data_integer)
print('-bertipe : ', type(data_integer))

# tipe data float
data_float = 1.5
print('data : ',data_float)
print('-bertipe : ', type(data_float))


# Tipe data string
data_string = "Khoerul Mutaqin"
print('data : ', data_string)
print('-bertipe : ', type(data_string))

# tipe data bool
data_bool = False
print('data : ',data_bool)
print('-bertipe : ', type(data_bool))

# tipe data khusus

# bilangan kompleks
data_komplex = complex(5,6)
print('data : ',data_komplex)
print('-bertipe : ', type(data_komplex))

# tipe data dari bahasa C
from ctypes import c_double,c_bool,c_float,c_int

data_c_double = c_double(10.5)
print('data : ',data_c_double)
print('-bertipe : ', type(data_c_double))
