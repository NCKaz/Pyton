volume = 1.44
pages = 100
lines = 50
kol_symbols = 25
ves_symbol = 4

pamyt_b = volume * 1024 * 1024
ves_knigi = pages * lines * kol_symbols * ves_symbol
vsego_knig = int(pamyt_b // ves_knigi)

print("Количество книг, помещающихся на дискету:", vsego_knig)
