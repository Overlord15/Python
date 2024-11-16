# Lists for conversion
ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]

amount = eval(input("Enter amount: "))

num = int(amount)  # Integer part of the amount
decimal_part = round((amount - int(amount)) * 100)  # Decimal part of the amount

# Conversion of integer part
integer_words = ""
if num == 0:
    integer_words = "Zero"
else:
    if num < 0:
        integer_words = "Negative "
        num = abs(num)

    words = ""
    if num // 1_000_000_000 > 0:
        billion_part = num // 1_000_000_000
        num = num % 1_000_000_000
        part_words = ""
        if billion_part // 100 > 0:
            part_words += ones[billion_part // 100] + " Hundred "
            billion_part %= 100
        if billion_part > 0:
            if billion_part < 10:
                part_words += ones[billion_part]
            elif billion_part < 20:
                part_words += teens[billion_part - 10]
            else:
                part_words += tens[billion_part // 10]
                if billion_part % 10 > 0:
                    part_words += "-" + ones[billion_part % 10]
        words += part_words.strip() + " Billion "
    if num // 1_000_000 > 0:
        million_part = num // 1_000_000
        num = num % 1_000_000
        part_words = ""
        if million_part // 100 > 0:
            part_words += ones[million_part // 100] + " Hundred "
            million_part %= 100
        if million_part > 0:
            if million_part < 10:
                part_words += ones[million_part]
            elif million_part < 20:
                part_words += teens[million_part - 10]
            else:
                part_words += tens[million_part // 10]
                if million_part % 10 > 0:
                    part_words += "-" + ones[million_part % 10]
        words += part_words.strip() + " Million "
    if num // 1_000 > 0:
        thousand_part = num // 1_000
        num = num % 1_000
        part_words = ""
        if thousand_part // 100 > 0:
            part_words += ones[thousand_part // 100] + " Hundred "
            thousand_part %= 100
        if thousand_part > 0:
            if thousand_part < 10:
                part_words += ones[thousand_part]
            elif thousand_part < 20:
                part_words += teens[thousand_part - 10]
            else:
                part_words += tens[thousand_part // 10]
                if thousand_part % 10 > 0:
                    part_words += "-" + ones[thousand_part % 10]
        words += part_words.strip() + " Thousand "
    if num // 100 > 0:
        words += ones[num // 100] + " Hundred "
        num %= 100
    if num > 0:
        if num < 10:
            words += ones[num]
        elif num < 20:
            words += teens[num - 10]
        else:
            words += tens[num // 10]
            if num % 10 > 0:
                words += "-" + ones[num % 10]
    integer_words = words.strip()

# Conversion of decimal part
decimal_words = ""
if decimal_part == 0:
    decimal_words = ""
else:
    words = ""
    if decimal_part < 10:
        words = ones[decimal_part]
    elif decimal_part < 20:
        words = teens[decimal_part - 10]
    else:
        words = tens[decimal_part // 10]
        if decimal_part % 10 > 0:
            words += "-" + ones[decimal_part % 10]
    decimal_words = words.strip()

# Construct the full words
if decimal_words == "":
    print(f"The amount in words is: {integer_words} Rupees")
else:
    print(f"The amount in words is: {integer_words} Rupees and {decimal_words} Paisa")
