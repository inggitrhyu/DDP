nomor 2
#match case luas bangun 
ket ='''selamat datang di aplikasi menghitung luas bangun datar,masukan pilihan:
   pilihlah 1 untuk menghitung luas persegi
   pilihlah 2 untuk menghitung luas segitiga
   pilihlah 3 untuk menghitung luas lingkaran'''

pilihan=input(ket)

match pilihan:
        case"1" :
            print("pilihlah 1 untuk menghitung luas persegi")
            sisi= int(input("masukan sisi"))
            luasP= sisi*sisi
            print("luas persegi adalah", luasP)
        case"2" :
            print ("pilihlah 2 untuk memilih luas lingkaran")
            r= int(input("masukan jari-jari"))
            luaslingkaran= 3.14*r**2
            Print("Luas Lingkarang adalah", luaslingakaran)
        case"3" :
            print("pilihah 3 untuk menghitung lias segitiga")
            alas=int (input("masukan alas?"))
            tinggi=int (input("masukan tinggi?"))
            LuasSegitiga= 0.5*alas*tinggi
            print ("Luas Segitiga adalah", LuasSegitiga)
        case _:
                print ("anda salah memilih
