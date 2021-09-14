def get_even(numbers):
    get_even = [num for num in numbers if not num % 2]
    return get_even
print (get_even([1, 2, 3, 4, 5, 6]))