"""
APLIKASI UPDATE GEMPA BMKG
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE
"""
import Update_gempa #ini modul yang di import dari package

if __name__ == "__main__": #Fungsi utama untuk memanggil modul pada package
    result = Update_gempa.ekstraksi_data()  #fungsi untuk mengekstraksi data
    Update_gempa.tampilkan_data(result)  #fungsi untuk menampilkan data
