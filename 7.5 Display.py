
def print_result(principal, rate, years, ci, si):
    print("===== HASIL PERHITUNGAN TABUNGAN =====")
    print(f"Saldo Awal        : ¥{principal:,.0f}")
    print(f"Bunga Tahunan     : {rate*100:.1f}%")
    print(f"Lama Menabung     : {years} tahun")
    print("---------------------------------------")
    print(f"Nilai Akhir (CI)  : ¥{ci:,.0f}")
    print(f"Nilai Akhir (SI)  : ¥{si:,.0f}")
    print("=======================================")
