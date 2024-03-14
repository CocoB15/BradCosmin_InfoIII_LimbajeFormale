class DFA:
    def __init__(self):
        self.current_state = 'A'
        self.final_states = {'A'}

    def transition(self, input_symbol):
        if self.current_state == 'A' and input_symbol == '0':
            self.current_state = 'B'
        elif self.current_state == 'B' and input_symbol == '0':
            self.current_state = 'A'
        # No need to handle transitions for input '1' explicitly,
        # as specified transitions keep the state unchanged.
    
    def process_input(self, input_string):
        for symbol in input_string:
            self.transition(symbol)
        return self.current_state

# Implementation testing
automaton = DFA()

# Sequence "010"
print("For the '010' sequence, we have the final state:", automaton.process_input('010'))

# Sequence "110"
automaton = DFA()  # reset automaton for a new sequence
print("For the '110' sequence, we have the final state:", automaton.process_input('110'))

# Sequence "1001"
automaton = DFA()  # reset automaton for a new sequence
print("For the '1001' sequence, we have the final state:", automaton.process_input('1001'))
