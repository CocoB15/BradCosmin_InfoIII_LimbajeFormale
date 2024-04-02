Q = ["S1", "S2"]
E = ["A", "B"]
O = ["O1", "O2"]

trasitions = {
    ("S1", "A"): "S1",
    ("S1", "B"): "S2",
    ("S2", "A"): "S1",
    ("S2", "B"): "S2",
}


def return_output(state, input):
    if (state, input) in trasitions:
        state = trasitions[(state, input)]
        if state == Q[0]:
            return O[0]
        else:
            return O[1]
    else:
        print("Invalid state or input")


print("State " + Q[0] + " with input " + E[0] + ": " + return_output(Q[0], E[0]))
