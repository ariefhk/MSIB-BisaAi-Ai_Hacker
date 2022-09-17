# Buatlah program yang menerima input nilai n siswa,
# kemudian tentukan rentang huruf nya jika rules nya adalah
# sebagai berikut:
# • A: Nilai >= 85 dan Nilai <= 100
# • B: Nilai >= 70 dan nilai <= 84
# • C: Nilai >= 60 dan nilai <= 69
# • D: Nilai < 60

grade = int(input('Masukkan nilai: '))
if grade >= 85 and grade <= 100:
    print('Nilai Anda A')
elif grade >= 70 and grade <= 84:
    print('Nilai Anda B')
elif grade >= 60 and grade <= 69:
    print('Nilai Anda C')
else:
    print('Nilai Anda D')
