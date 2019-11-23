i=0
name=[]
nim=[]
tugas=[]
uts=[]
uas=[]
tot=[]
while True:
    Nama=input ("Masukan Nama = ")
    name.append(Nama)
    aNim=input("Masukan Nim = ")
    nim.append(aNim)
    aTugas=float (input("Masukan Nilai Tugas = "))
    tugas.append(aTugas)
    aUts=float (input("Masukan Nilai UTS = "))
    uts.append(aUts)
    aUas=float (input("Masukan Nilai UAS = "))
    uas.append(aUas)
    Total=(0.3*aTugas)+(0.35*aUts)+(0.35*aUas)
    tot.append(Total)
    con = ' '
    while con!='y' and con!='t':
        con = input("tambah data [y/t]")
    i+=1
    if con=='t':
        break



print ('==========================================DAFTAR MAHASISWA==================================')
print ("============================================================================================ ")
print ("  NO  |\t  NAMA |    NIM       |       TUGAS     |     UTS      |       UAS    |       AKHIR     | ")
print ("============================================================================================= ")

for n in range (i):
    print (" ",n+1,"  |\t" ,name[n],"  |\t" ,nim[n],"  |\t" ,tugas[n],"  |\t" ,uts[n],"  |\t" ,uas[n], "  |\t",tot[n],"  |\t")
 
