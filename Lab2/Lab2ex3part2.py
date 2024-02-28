def generate_strings_gramatica2(S, X, Y, Z, length, current_string=""):
    if length == 0:
        print(current_string)
        return
    
    if S in current_string:
        generate_strings_gramatica2(X, X, Y, Z, length-1, current_string.replace(S, 'X', 1))
    else:
        generate_strings_gramatica2(X, X, Y, Z, length-1, current_string + X)

    if Y in current_string:
        generate_strings_gramatica2(Y, X, Y, Z, length-1, current_string.replace(Y, '2', 1))
        generate_strings_gramatica2(Y, X, Y, Z, length-1, current_string.replace(Y, 'X', 1))
    else:
        generate_strings_gramatica2(Y, X, Y, Z, length-1, current_string + '2')
        generate_strings_gramatica2(Y, X, Y, Z, length-1, current_string + Y)

    if Z in current_string:
        generate_strings_gramatica2(Z, X, Y, Z, length-1, current_string.replace(Z, '3', 1))
        generate_strings_gramatica2(Z, X, Y, Z, length-1, current_string.replace(Z, '4', 1))
        generate_strings_gramatica2(Z, X, Y, Z, length-1, current_string.replace(Z, 'X', 1))
    else:
        generate_strings_gramatica2(Z, X, Y, Z, length-1, current_string + '3')
        generate_strings_gramatica2(Z, X, Y, Z, length-1, current_string + '4')
        generate_strings_gramatica2(Z, X, Y, Z, length-1, current_string + Z)


generate_strings_gramatica2('S', 'X', 'Y', 'Z', 4)
