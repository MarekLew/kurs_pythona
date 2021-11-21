print(float('12'))
print(float('1123.456789'))
# Od wersji 🐍 3.6:
print(float('1_123.456_789'))
# Dziwne przykłady:
print(float(False))  # dziwne ale możliwe
print(float(bool([1])))  # w połączeniu z bool(też liczba)
