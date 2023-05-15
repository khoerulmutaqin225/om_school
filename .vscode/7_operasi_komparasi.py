# Operasi Komparasi

# setiap hasil dari operasi komparasi adalah boolean

# Lebih besar dari >
print('=================== Lebih besar dari (>)')
a = 4
b = 2
hasil = a > 3 
print(a,'>', 3,'=',hasil)
hasil= b > 3
print(b,'>', 3,'=',hasil)
hasil= b > 2
print(b,'>', 2,'=',hasil)

# kurang dari <
print('=================== Lebih kecil dari (<)')
a = 4
b = 2
hasil = a < 3 
print(a,'<', 3,'=',hasil)
hasil= b < 3
print(b,'<', 3,'=',hasil)
hasil= b < 2
print(b,'<', 2,'=',hasil)

# Lebih besar dari >
print('=================== Lebih besar dari sama dengan (>=)')
a = 4
b = 2
hasil = a >= 3 
print(a,'>=', 3,'=',hasil)
hasil= b >= 3
print(b,'>=', 3,'=',hasil)
hasil= b >= 2
print(b,'>=', 2,'=',hasil)

# kurang dari <
print('=================== Lebih kecil sama dengan dari (<=)')
a = 4
b = 2
hasil = a <= 3 
print(a,'<=', 3,'=',hasil)
hasil= b <= 3
print(b,'<=', 3,'=',hasil)
hasil= b <= 2
print(b,'<=', 2,'=',hasil)

# Lebih besar dari ==
print('=================== sama dengan (==)')
a = 4
b = 2
hasil = a == 3 
print(a,'==', 3,'=',hasil)
hasil= b == 3
print(b,'==', 3,'=',hasil)
hasil= b == 2
print(b,'==', 2,'=',hasil)

# tidak sama dengan !=
print('=================== Lebih kecil dari (!=)')
a = 4
b = 2
hasil = a != 3 
print(a,'!=', 3,'=',hasil)
hasil= b != 3
print(b,'!=', 3,'=',hasil)
hasil= b != 2
print(b,'<', 2,'=',hasil)


# 'is' sebagai komparasi object identity
print('=================== object identity is (is)')
x = 5
y = 5
print('nilai x =',x,',id',hex(id(x)))
print('nilai y =',y,',id',hex(id(y)))
hasil = x is 5
print('x is 5 =', hasil)


# 'is' sebagai komparasi object identity
print('=================== object identity is (is not)')
x = 5
y = 5
print('nilai x =',x,',id',hex(id(x)))
print('nilai y =',y,',id',hex(id(y)))
hasil = x is not 5
print('x is not 5 =', hasil)

