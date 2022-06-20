def isprime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def prime_list(number):
    my_prime_list = []
    for i in range(2, number + 1):
        if isprime:
            my_prime_list.append(i)
    return my_prime_list

number = int(input("Up to which number do you want to get the prime list for: "))
print(prime_list(number))