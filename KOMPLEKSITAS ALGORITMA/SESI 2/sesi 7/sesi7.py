amount = int(input("Masukkan jumlah uang: "))

coins = list(map(int, input("Masukkan nilai koin (pisahkan dengan spasi): ").split()))

coins.sort(reverse=True)

print("\nKombinasi koin yang digunakan:")

remaining = amount
coin_count = 0

for coin in coins:
    count = remaining // coin
    if count > 0:
        print(f"{coin} x {count}")
        coin_count += count
        remaining -= coin * count

print(f"\nJumlah total koin: {coin_count}")
if remaining > 0:
    print(f"Sisa uang yang tidak bisa ditukar: {remaining}")