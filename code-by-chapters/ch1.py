import math

def check_prime(number):
    sqrt_number = math.sqrt(number)
    for i in range(2, int(sqrt_number) + 1):
        if (number / i).is_integer():
            return False
        
    return True

# def check_prime_vectorize(number):
#     sqrt_number = math.sqrt(number)
#     numbers = range(2, int(sqrt_number) + 1)
#     for i in range (0, len(numbers), 5):
#         # not valid python code
#         result = (number / numbers[i:(i + 5)]).is_integer()
#         if any(result):
#             return False
#     return True

print(f'check_prime(10,000,000) = {check_prime(10_000_000)}')

print(f'check_prime(10,000,019) = {check_prime(10_000_019)}')

# print(f'check_prime_vectorize(10,000,000) = {check_prime_vectorize(10_000_000)}')


def search_fast(haystack, needle):
    for item in haystack:
        if item in haystack:
            if item == needle:
                return True
        return False
    
def search_slow(haystack, needle):
    return_value=False
    for item in haystack:
        if item == needle:
            return_value= True
    return return_value

def search_unknown1(haystack, needle):
    return any((item == needle for item in haystack))

def search_unknown2(haystack, needle):
    return any([item == needle for item in haystack])

