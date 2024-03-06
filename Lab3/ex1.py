class AutomatCafea:
    def __init__(self):
        self.stare_curenta = 'q0'

    def tranzitie(self, input_symbol):
        tranzitii = {
            ('q0', 'C'): 'q1',
            ('q0', 'T'): 'q2',
            ('q0', 'A'): 'q3',
            ('q0', 'H'): 'q4',
            ('q1', 'OK'): 'q4',
            ('q2', 'OK'): 'q4',
            ('q3', 'OK'): 'q4',
            ('q4', 'OK'): 'q0',
        }

        cheie_tranzitie = (self.stare_curenta, input_symbol)

        if cheie_tranzitie in tranzitii:
            self.stare_curenta = tranzitii[cheie_tranzitie]

    def comanda_bautura(self, bautura):
        self.tranzitie(bautura)
        if self.stare_curenta == 'q4':
            print(f"Bautura {bautura} pregatita! Comanda finalizata.")
        else:
            print(f"Bautura {bautura} selectata. Asteptati confirmarea.")

# Exemplu de utilizare
automat = AutomatCafea()
automat.comanda_bautura('C')  # Selecteaza cafeaua
automat.comanda_bautura('OK')  # Confirma comanda
