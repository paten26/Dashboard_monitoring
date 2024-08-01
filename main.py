"""
APLIKASI UPDATE GEMPA BMKG
"""
from Update_gempa import ekstraksi_data, tampilkan_data

if __name__ == "__main__":
    print('Aplikasi Utama')
    result = ekstraksi_data()  #fungsi untuk mengekstraksi data
    tampilkan_data(result)  #fungsi untuk menampilkan data
