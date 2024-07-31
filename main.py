"""
APLIKASI UPDATE GEMPA BMKG
"""

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

    hasil = dict()
    hasil['tanggal'] = '28 Juli 2024'
    hasil['waktu'] = '18:20:31 WIB'
    hasil['magnitudo'] = 5.6
    hasil['kedalaman'] = 144
    hasil['lokasi'] = {'ls': 6.31, 'bt': 130.20}
    hasil['pusat'] = '221 km BaratLaut TANIMBAR'
    hasil['keterangan'] = 'tidak berpotensi TSUNAMI'

    return hasil


def tampilkan_data(hasil):  #mendefinisikan fungsi tampilkan data
    print("GEMPABUMI TERKINI")
    print(f"result {hasil['tanggal']}")
    print(f"result {hasil['waktu']}")
    print(f"result {hasil['magnitudo']}")
    print(f"result {hasil['kedalaman']}")
    print(f"result {hasil['lokasi']}")
    print(f"result {hasil['pusat']}")
    print(f"result {hasil['keterangan']}")


if __name__ == "__main__":
    print('Aplikasi Utama')
    result = ekstraksi_data()  #fungsi untuk mengekstraksi data
    tampilkan_data(result)  #fungsi untuk menampilkan data
