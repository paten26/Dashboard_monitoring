"""
FOLDER Update_Gempa adalah PACKAGE, yang didalamnya berisi modul __init__.py
modul ini yang dipanggil di main.py menggunakan perintah if __name__ == "__main__":
"""
import requests
from bs4 import BeautifulSoup


def ekstraksi_data():  #mendefinisikan fungsi ekstraksi data

    """
    Gempabumi Terkini
    Tanggal 28 Juli 2024,
    Waktu 18:20:31 WIB
    Magnitudo 5.6 SR
    Kedalaman 144 km
    Lokasi 6.31 LS - 130.20 BT
    Pusat gempa : 221 km BaratLaut TANIMBAR
    Keterangan : tidak berpotensi TSUNAMI
    :return:
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('span', {'class': 'ic magnitude'})
        magnitude = result.text

        hasil = dict()
        hasil['tanggal'] = '28 Juli 2024'
        hasil['waktu'] = '18:20:31 WIB'
        hasil['magnitudo'] = 5.6
        hasil['kedalaman'] = 144
        hasil['lokasi'] = {'ls': 6.31, 'bt': 130.20}
        hasil['pusat'] = '221 km BaratLaut TANIMBAR'
        hasil['keterangan'] = 'tidak berpotensi TSUNAMI'
        return hasil
    else:
        return None

def tampilkan_data(hasil):  #mendefinisikan fungsi tampilkan data
    if hasil is None:
        print("Tidak bisa menemukan data gempa terkini")
        return

    print("GEMPABUMI TERKINI")
    print(f"tanggal : {hasil['tanggal']}")
    print(f"waktu : {hasil['waktu']}")
    print(f"magnitudo : {hasil['magnitudo']}")
    print(f"kedalaman : {hasil['kedalaman']}")
    print(f"lokasi : {hasil['lokasi']}")
    print(f"pusat : {hasil['pusat']}")
    print(f"keterangan : {hasil['keterangan']}")
