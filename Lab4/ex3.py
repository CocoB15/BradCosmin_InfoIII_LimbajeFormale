class NFA:
    def __init__(self):
        self.states = {'S0', 'S1', 'S2', 'S3'}
        self.accept_state = {'S1'}
        self.transitions = {
            'S0': {'a': {'S2'}, 'b': {'S3'}},
            'S1': {},
            'S2': {'a': {'S2'}, 'b': {'S1'}},
            'S3': {'a': {'S1'}, 'b': {'S3'}}
        }

    def is_accepted(self, input_string):
        current_states = {'S0'}
        for symbol in input_string:
            next_states = set()
            for state in current_states:
                if symbol in self.transitions[state]:
                    next_states.update(self.transitions[state][symbol])
            current_states = next_states
        return bool(current_states.intersection(self.accept_state))


# Testăm implementarea
nfa = NFA()

# Testăm câteva șiruri
strings_to_test = ["ab", "aab", "bb", "bba"]
for string in strings_to_test:
    print(f"String '{string}' is accepted: {nfa.is_accepted(string)}")
