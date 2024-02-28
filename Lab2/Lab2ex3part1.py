def generate_strings_gramatica1(S, A, B, length, current_string=""):
    if length == 0:
        print(current_string)
        return
    
    if S in current_string:
        generate_strings_gramatica1(A, A, B, length-1, current_string.replace(S, '', 1))
        generate_strings_gramatica1(B, A, B, length-1, current_string.replace(S, '', 1))
    else:
        generate_strings_gramatica1(A, A, B, length-1, current_string + A)
        generate_strings_gramatica1(B, A, B, length-1, current_string + B)


generate_strings_gramatica1('S', 'A', 'B', 4)