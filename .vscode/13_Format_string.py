# Format string


# contoh generic
nama = "marlene"
format_str = f"hello {nama} "
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)


# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan ribuan
angka=2000
format_str =f"ribuan =  {angka:,}"
print(format_str)


# bilangan ribuan
angka=2000.23456
format_str =f"desimal =  {angka:.2f}"
print(format_str)



# bilangan desimal
angka=2000.23456
format_str =f"desimal =  {angka:.2f}"
print(format_str)


# menampilkan leading zero
angka=2005.23456
format_str = f"desimal =  {angka:010.3f}"
print(format_str)

# menampilkan tanda + atau -


angka_plus = 10
angka_minus = -8
format_minus = f"minus ={angka_minus:+d}"
format_plus = f"plus ={angka_plus:+d}"

print(format_plus)
print(format_minus)

