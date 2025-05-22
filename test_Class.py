class laptop:
    price = int()
    pro = int()
    ram = int() 
    print("\n", "Class name printed")

dell = laptop()
HP = laptop()
Len = laptop()

dell.price = "100000"
dell.pro = "i7"
dell.ram = "16gb"

HP.price = "200000"
HP.pro = "i8"
HP.ram = "14gb"

Len.price = "500000"
Len.pro = "i18"
Len.ram = "222gb"

print(dell.price)
print(HP.price)
print(Len.price)
print(laptop)