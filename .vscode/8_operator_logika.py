# operator logika

# not, or, xor

# NOT
print('=====NOT====')
a = False
c = not a
print('data a = ',a)
print('--------- NOT')
print('data c = ',c)

# OR (Jika salah satu true maka hasilnya true)
print('=====OR====')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a= False
b= False
c= a or b
print(a,'OR',b,'=',c)


# and (Jika salah dua buah true maka hasilnya true)
print('=====and====')
a = False
b = False
c = a and b
print(a,'and',b,'=',c)
a= True
b= False
c= a and b
print(a,'and',b,'=',c)

# XOR (Akan true jika salahsatu true, sisanya false
print('=====XOR====')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a= True
b= False
c= a ^ b
print(a,'XOR',b,'=',c)



