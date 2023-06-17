#Compute the sum of digits in all numbers from 1 to n

def compute_sum_of_digits(n):
    sumOfDigits = 0

    for number in range(1, n + 1):
        for digit in str(number):
            sumOfDigits += int(digit)

    return sumOfDigits


# Example usage
n = 100
result = compute_sum_of_digits(n)
print("Sum of digits from 1 to", n, "is:", result)




#Find the max number

def find_max_number(a, b, c):
    max_number = max(a, b, c)
    return max_number


# Example usage
num1 = 178
num2 = 61
num3 = 75

maximum = find_max_number(num1, num2, num3)
print("The maximum number is:", maximum)


#Count odd and even numbers

def count_odd_even_digits(number):
    evenDigitCount = 0
    oddDigitCount = 0

    numberStr = str(number)
    for digit in numberStr:
        digit = int(digit)
        if digit % 2 == 0:
            evenDigitCount += 1
        else:
            oddDigitCount += 1

    return evenDigitCount, oddDigitCount


# Example usage
number = 67890
evenDigitCount, oddDigitCount = count_odd_even_digits(number)
print("Number of even digits:", evenDigitCount)
print("Number of odd digits:", oddDigitCount)

