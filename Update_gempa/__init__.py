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

        #result = soup.find('span', {'class': 'ic magnitude'})
        #magnitude = result.text
        #magnitudo = 0

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'}) #ini data yang diambil
        result = result.findChildren('li') #li adalah sub datanya, tanggal, waktu dll

        magnitude = None
        kedalaman = None
        ls = None
        bt = None
        koordinat = None
        lokasi = None
        dirasakan = None

        i = 0
        for res in result: #agar hasil diurutkan kebawahh
            print(i, res)
            if i == 1: #akan mengambil data magnitudo, yang merupakan data ke 1
                magnitudo = res.text #untuk mengambil nilainya saja
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = koordinat
        hasil['lokasi'] = lokasi
        hasil['keterangan'] = dirasakan
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
    print(f"koordinat : {hasil['koordinat']}")
    print(f"lokasi : {hasil['lokasi']}")
    print(f"keterangan : {hasil['keterangan']}")
