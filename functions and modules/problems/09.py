def sum_of_digits(n):
    if n==0:
        return 0
    return n%10 + sum_of_digits(n//10)

print(sum_of_digits(12345))
print(sum_of_digits(6789))

# sum of digits of 12345 is 15
# 5(last digit)+sum_of_digits(1234)