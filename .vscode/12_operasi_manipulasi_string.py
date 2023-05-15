# 1. Menyambung string

nama_pertama = "Gold"
nama_kedua ="D"
nama_ketiga="Roger"
nama_lengkap = nama_pertama +" "+ nama_kedua+" " + nama_ketiga
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# 3. Operator untuk string
# Mengecek apakah ada komponen char atau string

d = "d"
status = d in nama_lengkap
print(d+ " ada di "+ nama_lengkap + " = "+ str(status))

# Mengulang string
print("wk"*10)
print(15*"wk")

# Indexing

print("index ke-0 : "+ nama_lengkap[0])
print("index ke-6 : "+ nama_lengkap[6])
print("index ke-4 : "+ nama_lengkap[4])
print("index ke-11 : "+ nama_lengkap[11])
print("index ke-1 : "+ nama_lengkap[1])
print("index ke-1-4 : "+ nama_lengkap[0:3])

# item paling kecil
print("paling kecil : "+min(nama_lengkap))
# item paling besar
print("paling besar : "+max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + chr(ascii_code))
data = 117
print("char code untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah =data.count("o")
print("jumlah o pada "+data+" = "+ str(jumlah))

# 5. normal, upper, lower

data = "otong surotong pararotong"
print("normal = "+ data)

data = "surotong pararotong"
data=data.upper()
print("normal = "+ data)

data = "Otong Surotong Pararotong"
data=data.lower()
print("normal = "+ data)