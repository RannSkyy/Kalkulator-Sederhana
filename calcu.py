what_type = input ("Mau memakai operasi apa? [+] [-] [*] [/] ")
num1 = input ("Masukkan angka pertama: ")
num2 = input ("Masukkan angka kedua: ")

if what_type == "+":
    print (int(num1) + int(num2))

elif what_type == "-":
    print (int(num1) - int(num2))

elif what_type == "*":
    print (int(num1) * int(num2))
    
elif what_type == "/":
    print (int(num1) / int(num2))
    
else:
    print ("Aku tidak paham")