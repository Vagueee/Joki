class Mahasiswa:
    def __init__(self, nama: str, nim: int):
        self._nama = nama
        self._nim = nim
        self._nilai = {
            "tugas": 0,
            "quiz": 0,
            "ujian": 0,
        }
        self._nilai_akhir = 0

    def set_nilai(self, which: str, value: int):
        self._nilai[which] = value

    def count_nilai_akhir(self):
        self._nilai_akhir = self._nilai["tugas"] * 0.25 + self._nilai["quiz"] * 0.25 + self._nilai["ujian"] * 0.5
    
    def get_nilai(self, which:str) -> int:
        return self._nilai[which] if which != "akhir" else self._nilai_akhir
    def get_prop(self, which:str):
        match which:
            case "nama":
                return self._nama
            case "nim":
                return self._nim

list_of_mahasiswa = []

def sort_nilai():
    global list_of_mahasiswa
    n = len(list_of_mahasiswa)
    for i in range(1, n):
        current_mahasiswa = list_of_mahasiswa[i]
        j = i - 1
        while j >= 0 and current_mahasiswa.get_nilai("akhir") > list_of_mahasiswa[j].get_nilai("akhir"):
            list_of_mahasiswa[j + 1] = list_of_mahasiswa[j]
            j -= 1
        list_of_mahasiswa[j + 1] = current_mahasiswa


def input_mahasiswa():
    nama = str(input("Masukan nama mahasiswa: "))
    nim = str(input("Masukan NIM mahasiswa: "))
    tugas = float(input("Masukan nilai tugas: "))
    quiz = float(input("Masukan nilai quiz: "))
    ujian = float(input("Masukan nilai ujian: "))

    mahasiswa = Mahasiswa(nama, nim)
    mahasiswa.set_nilai("tugas", tugas)
    mahasiswa.set_nilai("quiz", quiz)
    mahasiswa.set_nilai("ujian", ujian)

    mahasiswa.count_nilai_akhir()

    global list_of_mahasiswa
    list_of_mahasiswa.append(mahasiswa)

def print_mahasiswa():
    global list_of_mahasiswa
    for index, mahasiswa in enumerate(list_of_mahasiswa):
        print(f"[{index}] {mahasiswa.get_prop("nim")} {mahasiswa.get_prop("nama")}")

def menu_utama():
    select_menu = str(input("Pilih menu: "))
    match select_menu:
        case "1":
            input_mahasiswa()
        case "2":
            print_mahasiswa()

while True:
    menu_utama()
    sort_nilai()