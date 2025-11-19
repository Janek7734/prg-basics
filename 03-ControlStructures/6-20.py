number = int(input("Enter a decimal number: "))

remainders = []   # lista na reszty

# dopóki liczba jest większa od 0, dzielimy przez 2
while number > 0:
    remainder = number % 2         # reszta z dzielenia
    remainders.append(remainder)   # zapisujemy resztę
    number = number // 2           # dzielimy całkowicie przez 2

# odwracamy kolejność reszt, bo binary zapisuje się od dołu
remainders.reverse()

# zamieniamy cyfry na tekst i łączymy w jeden ciąg
binary = "".join(str(bit) for bit in remainders)

print("Binary number:", binary)