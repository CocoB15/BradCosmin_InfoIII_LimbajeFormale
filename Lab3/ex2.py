class AutomatLimbaj:
    def __init__(self):
        self.stare_curenta = 'q0'
        self.stari_finale = {'q3'}

    def tranzitie(self, simbol):
        tranzitii = {
            ('q0', 'a'): 'q1',
            ('q0', 'b'): 'q0',
            ('q0', 'c'): 'q0',
            ('q0', 'd'): 'q0',
            ('q1', 'a'): 'q1',
            ('q1', 'b'): 'q2',
            ('q1', 'c'): 'q1',
            ('q1', 'd'): 'q1',
            ('q2', 'a'): 'q2',
            ('q2', 'b'): 'q2',
            ('q2', 'c'): 'q2',
            ('q2', 'd'): 'q2',
            ('q3', 'a'): 'q3',
            ('q3', 'b'): 'q3',
            ('q3', 'c'): 'q3',
            ('q3', 'd'): 'q3',
        }

        cheie_tranzitie = (self.stare_curenta, simbol)

        if cheie_tranzitie in tranzitii:
            self.stare_curenta = tranzitii[cheie_tranzitie]

    def este_cuvant_valid(self, cuvant):
        for simbol in cuvant:
            self.tranzitie(simbol)

        return self.stare_curenta in self.stari_finale

# Exemplu de utilizare
automat = AutomatLimbaj()

# Verificare aleatoare a 3 cuvinte
cuvant1 = 'aabbcc'
cuvant2 = 'aaa'
cuvant3 = 'bbbaac'

print(f"{cuvant1} este valid: {automat.este_cuvant_valid(cuvant1)}")
print(f"{cuvant2} este valid: {automat.este_cuvant_valid(cuvant2)}")
print(f"{cuvant3} este valid: {automat.este_cuvant_valid(cuvant3)}")
