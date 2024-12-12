# class mhsw :
#      def __init__(self):
#         self.nama    = ""
#         self.nobp    = ""
#         self.gender  = ""
#         self.jurusan = ""
#         print('\tData Mahasiswa ')
    
# hanif = mhsw ()
# hanif.nama = 'Hanif Wahyudi'
# hanif.nobp = 23101152630140
# hanif.gender = 'Laki-Laki'
# hanif.jurusan = 'Teknik Informatika'
# print(f'Nama Lengkap :{hanif.nama}')
# print(f'Nobp :{hanif.nobp}')
# print(f'Gender :{hanif.gender}')
# print(f'Jurusan :{hanif.jurusan}\n')
# print()

# jevin= mhsw ()
# jevin.nama = 'Jevin Trihatmotno'
# jevin.nobp = 23101152630140
# jevin.gender = 'Laki-Laki'
# jevin.jurusan = 'Teknik Informatika'
# print(f'Nama Lengkap :{jevin.nama}')
# print(f'Nobp :{jevin.nobp}')
# print(f'Gender :{jevin.gender}')
# print(f'Jurusan :{jevin.jurusan}\n')
# print()

# raihan= mhsw ()
# raihan.nama = 'Raihan Trihamotno'
# raihan.nobp = 23101152630140
# raihan.gender = 'Laki-Laki'
# raihan.jurusan = 'Teknik Informatika'
# print(f'Nama Lengkap :{raihan.nama}')
# print(f'Nobp :{raihan.nobp}')
# print(f'Gender :{raihan.gender}')
# print(f'Jurusan :{raihan.jurusan}\t')
# print()

# luthfi= mhsw ()
# luthfi.nama = 'Luthfi Trihamotno'
# luthfi.nobp = 23101152630140
# luthfi.gender = 'Laki-Laki'
# luthfi.jurusan = 'Teknik Informatika'
# print(f'Nama Lengkap :{luthfi.nama}')
# print(f'Nobp :{luthfi.nobp}')
# print(f'Gender :{luthfi.gender}')
# print(f'Jurusan :{luthfi.jurusan}\t')
# print()

# farli= mhsw ()
# farli.nama = 'Farli Trihamotno'
# farli.nobp = 23101152630140
# farli.gender = 'Laki-Laki'
# farli.jurusan = 'Teknik Informatika'
# print(f'Nama Lengkap :{farli.nama}')
# print(f'Nobp :{farli.nobp}')
# print(f'Gender :{farli.gender}')
# print(f'Jurusan :{farli.jurusan}\t')
# print()

#menggunakan instance method
class mhsw :
     def __init__(self,nama,nobp,gender,jurusan):
        self.nama    = nama
        self.nobp    = nobp
        self.gender  = gender
        self.jurusan = jurusan
        print('\tData Mahasiswa ')

     def info_mhs(self):
        print(f'Nama Lengkap :{self.nama}')
        print(f'Nobp :{self.nobp}')
        print(f'Gender :{self.gender}')
        print(f'Jurusan :{self.jurusan}')
        print()

hanif = mhsw  ('Hanif Wahyudi"','23101152630140','Laki-Laki','Teknik Informatika')
hanif.info_mhs()
jevin = mhsw  ('Jevin Trihatmono','23101152630142','Laki-Laki','Teknik Informatika')
jevin.info_mhs()
zaki= mhsw ('Zaki Trihatmono"','23101152630140','Laki-Laki','Teknik Informatika')
zaki.info_mhs()
dika= mhsw  ('Dika Trihatmono','23101152630140','Laki-Laki','Teknik Informatika')
dika.info_mhs()
raihan= mhsw('Raihan Trihatmono','23101152630140','Laki-Laki','Teknik Informatika')
raihan.info_mhs()



