
angka = int(input("Masukan jumlah deret angkanya: "))
var1, var2 = 0, 1
count = 0
if(angka ==1):
    print(angka)
elif(angka == 100):
    print("angka terlalu banyak")
else:
    while count < angka:
        print(var1)
        var = var1 + var2
        var1 = var2
        var2 = var
        count += 1
