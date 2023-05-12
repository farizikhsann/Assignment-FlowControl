output=""
angka = int(input("Masukan angka: "))
for i in range(1,angka):
    

    if(i%3== 0 and i%5 == 0):
        output += "FizzBuzz "
    else:
        if(i%3==0):
            output += "Fizz "
        elif(i%5==0):
            output += "Buzz "
        else:
            output += str(i)+" "
print(output)
