import cx_Freeze

programDosyasi = cx_Freeze.Executable("C://Users//asus//Desktop//Calisma//Python_Learn//Python_Kitap_Calismasi_06_Uygulamasi.py")

cx_Freeze.setup(
    name="Python Kitap Calismasi Uygulama-1-",
    version="0.1",
    description="Python Kitap Calismasi Uygulamasi-1-",
    executables=[programDosyasi]
)