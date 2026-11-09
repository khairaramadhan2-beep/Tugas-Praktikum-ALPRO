
def compound_interest(principal, rate, time):
    """hitung nilai akhir dengan bunga majemuk"""
    return principal * (1 + rate)**time

def simple_interest(principal, rate, time):
    """hitung nilai akhir dengan bunga sederhana"""
    return principal * (1 + rate * time)
