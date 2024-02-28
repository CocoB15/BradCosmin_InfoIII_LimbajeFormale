from itertools import product

def generate_language(length):
    alphabet = ['0', '1', '2']
    palindromes = []
    //generam lombajul si verificam daca este palindrom
    for combo in product(alphabet, repeat=length // 2 + length % 2):
        palindrome = ''.join(combo) + ''.join(combo[-1 - length % 2::-1])
        palindromes.append(palindrome)

    return palindromes

def print_palindromes(max_length):
    scriem palindroamele
    for length in range(0, max_length):
        palindromes = generate_palindromes(length)
        print(f"Palindroame de lungime {length}: {palindromes}")


print_palindromes(5)