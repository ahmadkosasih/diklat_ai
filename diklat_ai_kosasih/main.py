import click

"""Konstanta Planck"""
h = 6.626 * 10**-34

"""Function Energi Foton"""
def energi_foton(f):
    """Rumus Energi Foton"""
    """Energi = Konstanta Planck * Frekuensi Gelombang"""
    E = h * f
    return E

def welcome():
    """Aplikasi sederhana untuk menghitung Energi Foton"""
    click.echo('Welcome to Diklat AI Kosasih package. My Name is Ahmad Kosasih!')
    print("Aplikasi untuk menghitung Energi Foton")
    while(True):
        konfirmasi = input("Apakah Anda ingin menghitung Energi Foton? [Ya]/[Tidak] : ").lower()
        try:
            if konfirmasi[0] == 't' or konfirmasi == 'tidak':
                print("Terima kasih telah menggunakan aplikasi ini :)")
                break
            elif konfirmasi[0] == 'y' or konfirmasi == 'ya':
                print("Rumus Energi Foton")
                print("E = h * f")
                print("Keterangan")
                print("E : Energi Foton (Joule)")
                print("h : Konstanta Planck ({:e})".format(h))
                print("f : Frekuensi Gelombang (Hz)")
                frekuensi = float(input("Masukkan Nilai Frekuensi Gelombang (Hz) : "))
                energi = energi_foton(frekuensi)
                print("Energi Foton (Joule) : {:e}".format(energi))
            else:
                print("Jawab dengan pilihan [Ya]/[Tidak]")
        except IndexError:
            print("Jawab dengan pilihan [Ya]/[Tidak]")
            continue

if __name__ == '__main__':
    welcome()