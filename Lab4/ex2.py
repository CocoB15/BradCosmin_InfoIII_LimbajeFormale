class ParkingLot:
    def __init__(self, total_spaces):
        self.total_spaces = total_spaces
        self.available_spaces = total_spaces

    def park_car(self):
        if self.available_spaces > 0:
            self.available_spaces -= 1
            return True
        else:
            return False

    def leave_car(self):
        if self.available_spaces < self.total_spaces:
            self.available_spaces += 1
            return True
        else:
            return False

    def get_status(self):
        return f"Available Spaces: {self.available_spaces}/{self.total_spaces}"


class ParkingLotAutomaton:
    def __init__(self, total_spaces):
        self.parking_lot = ParkingLot(total_spaces)

    def process_request(self, request):
        if request == 'park':
            return self.parking_lot.park_car()
        elif request == 'leave':
            return self.parking_lot.leave_car()
        elif request == 'status':
            return self.parking_lot.get_status()
        else:
            return "Invalid request"


# Testăm implementarea
automaton = ParkingLotAutomaton(5)

print(automaton.process_request('status'))  # Afiseaza starea initiala a parcarii

print(automaton.process_request('park'))    # Șoferul parchează o mașină
print(automaton.process_request('park'))    # Șoferul parchează o altă mașină
print(automaton.process_request('park'))    # Șoferul încearcă să parcheze într-o parcare plină

print(automaton.process_request('status'))  # Afiseaza starea parcarii dupa ce au fost parcate doua masini

print(automaton.process_request('leave'))   # Șoferul pleacă cu o mașină
print(automaton.process_request('leave'))   # Șoferul pleacă cu o altă mașină
print(automaton.process_request('leave'))   # Șoferul încearcă să plece dintr-o parcare goală

print(automaton.process_request('status'))  # Afiseaza starea parcarii dupa ce au fost plecate doua masini
