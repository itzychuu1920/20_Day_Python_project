sum_even_digit = 0
sum_odd_digit = 0
total = 0
card_num = input("Enter the credit card number: ")
card_num = card_num.replace("-","")
card_num = card_num.replace(" ","")
card_num = card_num[::-1]
for x in card_num[::2]:
    sum_odd_digit += int(x)
for x in card_num[1::2]:
    x = int(x) * 2
    if x >= 10:
        x = (1 + (x % 10))
        sum_even_digit += x
    else:
        sum_even_digit += x
total = sum_odd_digit + sum_even_digit
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")