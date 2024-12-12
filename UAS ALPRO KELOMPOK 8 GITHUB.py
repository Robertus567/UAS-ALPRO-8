from collections import deque
from datetime import datetime


antrean_konsultasi_langsung = deque()
antrean_jadwal_konsultasi = deque()
jadwal_konsultasi = []


def login():
    """Fungsi untuk proses login pengguna"""
    credentials = {
        "pasien": {"username": "pasien", "password": "12345"},
        "admin": {"username": "admin", "password": "admin123"},
        "dokter": {"username": "dokter", "password": "dokter123"}
    }

    print("=== Login Sistem ===")

    print("Pilih peran:")
    print("1. Pasien")
    print("2. Admin")
    print("3. Dokter")

    role_choice = input("Masukkan pilihan (1/2/3): ")

    roles = {"1": "pasien", "2": "admin", "3": "dokter"}
    role = roles.get(role_choice)

    if not role:
        print("Pilihan tidak valid. Silakan coba lagi!")
        return None

    if role == "pasien":
        print("Login berhasil sebagai Pasien.")
        return role

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    cred = credentials.get(role)
    if username == cred["username"] and password == cred["password"]:
        print(f"Login berhasil sebagai {role.capitalize()}.")
        return role

    print("Username atau password salah. Silakan coba lagi!")
    return None



# Menu Pasien
def menu_pasien():
    while True:
        print("\n=== Menu Pasien ===")
        print("1. Ambil nomor antrean konsultasi langsung dengan dokter")
        print("2. Ambil nomor antrean mengatur jadwal konsultasi")
        print("3. Kembali ke menu login")

        choice = input("Masukkan pilihan (1/2/3): ")

        if choice == "1":
            nomor_antrean = len(antrean_konsultasi_langsung) + 1
            antrean_konsultasi_langsung.append(nomor_antrean)
            print(f"Nomor antrean konsultasi langsung Anda: {nomor_antrean}")
        elif choice == "2":
            nomor_antrean = len(antrean_jadwal_konsultasi) + 1
            antrean_jadwal_konsultasi.append(nomor_antrean)
            print(f"Nomor antrean janji konsultasi Anda: {nomor_antrean}")
        elif choice == "3":
            return
        else:
            print("Pilihan tidak valid. Silakan coba lagi!")
            
            
            
if __name__ == "__main__":
    while True:
        user = login()
        if user == "pasien":
            menu_pasien()
        elif user == "admin":
            menu_admin()
        elif user == "dokter":
            menu_dokter()
        else:
            print("Gagal login. Program akan diulang.")
