
import interest
import display

print("=== Program Kalkulator Bunga Tabungan ===")

principal = float(input("Masukkan Saldo Awal       : ¥"))
rate = float(input("Masukkan Bunga Tahunan (%) : ")) / 100
years = int(input("Masukkan Lama Menabung (tahun): "))

ci = interest.compound_interest(principal, rate, years)
si = interest.simple_interest(principal, rate, years)

display.print_result(principal, rate, years, ci, si)
