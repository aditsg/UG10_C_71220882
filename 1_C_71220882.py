print ("========Pilih Menu========")
print ("1.Tambah")
print ("2.Kurang")
print ("3.Kali")
print ("4.Bagi")
angka1=int(input("Masukan angka pertama :"))
angka2=int(input("Masukan angka kedua :" ))
menu= input ("Masukan pilihan :")
if menu=="1" :
    Tambah= angka1+angka2
    print (Tambah)
elif menu=="2" :
    Kurang= angka1-angka2
    print (Kurang)
elif menu=="3" :
    Kali= angka1*angka2
    print (Kali)
elif menu=="4" : 
    Bagi= angka1/angka2
    print (Bagi)
    
       
