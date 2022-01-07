#buatlah program python untuk menentukan sebuah bilangan
#termasuk bilangan prima atau tidak

data = int(input("masukkan bilangan :"))

if data > 1:
    for i in range(2,data):
        if(data %i) == 0:
            print(data,"bukan bilangan prima")
            break
        else:
            print(data,"adalah bilangan prima")
