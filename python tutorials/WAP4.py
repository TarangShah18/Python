a = "Tarang123"

letter_count = 0
digit_count = 0

for char in a:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print(f"Number of Letters: {letter_count}")
print(f"Number of digits: {digit_count}")

