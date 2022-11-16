#menu selection
def menu():
    print('')
    print('Berikut adalah pilihan bilangan yang kami dapat hitung:')
    print("Bilangan Ganjil: 1")
    print('Bilangan Genap: 2')
    print("Bilangan Prima: 3")
    print("Bilangan Fibonacci: 4")
    print("Keluar: X")
    bil=input("PILIH BILANGAN YANG INGIN DICARI: ")
    if bil =='1':
        ganjil()
    elif bil=='2':
        genap()
    elif bil=='3':
        prima()
    elif bil=='4':
        fibonacci_deret()
    elif bil =='x' or 'X':
        print('Terimakasih telah menggunakan aplikasi kami :)')
    else:
        print('Kode bilangan tidak dikenal, mengulangi dari awal')
        menu()

def hitung_lagi():
    tanya = input("Apakah anda ingin menghitung lagi? [Y/N]: ")
    if tanya =='y' or 'Y':
        menu()
    else: 
        print('')
        print('Terimakasih telah menggunakan aplikasi kami :)')

#fungsi pencarian bilangan ganjil
def ganjil():
    print(" ")
    print('Bilangan Ganjil')
    x = int(input("Dari angka: "))
    y = int(input("Sampai angka: "))
    for i in range(x, y+1):
        if i % 2!=0:
            print(i,end=' ')
    print("")
    hitung_lagi()

#fungsi pencarian bilangan genap
def genap():
    print(" ")
    print('Bilangan Genap')
    x = int(input("Dari angka: "))
    y = int(input("Sampai angka: "))
    for i in range(x, y+1):
        if i % 2==0:
            print(i,end=' ')
    print("")
    hitung_lagi()

#fungsi pencarian bilangan prima
def prima():
    print(" ")
    print('Bilangan Prima')
    x = int(input("Dari angka: "))
    y = int(input("Sampai angka: ")) #range angka yang ingin dicari
    for angka in range (x, y+1): #setiap angka dalam interval x dan y, akan dicari bilangan prima
        if angka > 1: #bilangan prima selalu lebih besar dari 1
            for i in range(2, angka): #ngetes apakah angka memiliki faktor selain angka 1 dan angka itu sendiri
                if (angka % i)==0: #jika angka memiliki faktor selain angka 1 dan angka itu sendiri, maka angka akan dilewati
                    break
            else:
                print(angka,end=' ')
    print("") #jika angka tidak memiliki faktor lain, maka angka dicetak
    hitung_lagi()

#fungsi pencarian bilangan fibonacci
def fibonacci_deret():
    def fibonacci(n):
        if n == 0 or n == 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2) #kode rekursif
    print(" ")
    print('Bilangan Fibonacci')
    x = int(input("Dari angka: "))
    y = int(input("Sampai angka: ")) #range angka yang ingin dicari
    if x >= 0 and y >= 0: #memastikan agar interval tidak kurang dari 0
        for i in range (x,y+1):
            if y > 34: #untuk membatasi agar tidak ngelag
                break
            else:
                print(fibonacci(i),end=' ')
    print('')
    hitung_lagi()

#user interface

print("")
print('Selamat datang!')
print("MESIN PENGHITUNG BILANGAN")
print('version 1.0')

menu()