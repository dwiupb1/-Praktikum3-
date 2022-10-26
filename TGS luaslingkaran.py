print('Program Menghitung Luas & keliling lingkaran')
print('Nama  : Dwi heriyanto')
print('NIM   : 312210541')
print('Kelas : TI.22.B2')
print('Tugas : Pratikum3')



r = float(input('Masukkan nilai jari-jari : '))

phi = 3.14
diameter = 2*r

luas = phi*r*r
keliling = phi*diameter
print('\nLuasnya    =', str("%.2f" % luas))
print('kelilingnya =', str("%.2f" % keliling))
