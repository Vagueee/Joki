mahasiswa = {
    "nama": [],
    "nim": [],
    "nilai_tugas": [],
    "nilai_quiz": [],
    "nilai_ujian": [],
    "nilai_akhir": []
}
nilai_akhir_sorted = sorted(mahasiswa["nilai_akhir"])

def input_mahasiswa():
    nama = str(input("Masukan nama mahasiswa: "))
    nim = str(input("Masukan NIM mahasiswa: "))
    tugas = float(input("Masukan nilai tugas: "))
    quiz = float(input("Masukan nilai quiz: "))
    ujian = float(input("Masukan nilai ujian: "))
    data = [nama, nim, tugas, quiz, ujian, (tugas*0.25 + quiz*0.25 + ujian*0.5)]
    for i, j in zip(mahasiswa, data):
        mahasiswa[i].append(j)

def sorted():
    for i in nilai_akhir_sorted:
        sorted = mahasiswa["nilai_akhir"].index(i)
        print(mahasiswa["nama"][sorted])
        print(mahasiswa["nilai_akhir"][sorted])

def menu_utama():
    select_menu = str(input("Pilih menu: "))
    match select_menu:
        case "1":
            input_mahasiswa()
        case "2":
            print(nilai_akhir_sorted)

while True:
    menu_utama()