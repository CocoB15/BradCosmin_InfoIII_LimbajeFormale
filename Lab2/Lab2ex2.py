def generate_string(iterations, counter, choices_list):
    if iterations <= 0:
        return ""
    case_result = choices_list[counter]
    if case_result == 0:
        return "a" + generate_string(iterations - 1, counter + 1, choices_list) + "a"
    elif case_result == 1:
        return "b" + generate_string(iterations - 1, counter + 1, choices_list) + "b"
    elif case_result == 2:
        return "a"
    elif case_result == 3:
        return "b"
    else:
        return ""


def main():
    strings_list = []
    choices_list = [0, 0, 0]
    stop_generation = False

    print("Options from production line: ")
    print("1: aSa")
    print("2: bSb")
    print("3: a")
    print("4: b")
    print("")

    while not stop_generation:
        print(f"Case: {choices_list[0] + 1},{choices_list[1] + 1},{choices_list[2] + 1}")

        for i in range(1, 4):
            strings_list.append(generate_string(i, 0, choices_list))
            print(f"Iteration {i}: {strings_list[-1]}")

        print("")

        if choices_list[2] < 3:
            choices_list[2] += 1
        elif choices_list[1] < 3:
            choices_list[1] += 1
            choices_list[2] = 0
        elif choices_list[0] < 3:
            choices_list[0] += 1
            choices_list[1] = 0
            choices_list[2] = 0
        else:
            stop_generation = True


if __name__ == "__main__":
    main()
