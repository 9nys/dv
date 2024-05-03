def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'
    elif decimal == 1:
        return '1'
    else:
        return decimal_to_binary(decimal // 2) + str(decimal % 2)


decimal_number = 10
binary_number = decimal_to_binary(decimal_number)
print(f"Двійкове представлення числа {decimal_number}: {binary_number}")
