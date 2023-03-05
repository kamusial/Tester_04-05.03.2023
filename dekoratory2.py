class KontoBankowe:
    def __init__(self):
        self.stan = 0
        self.plec = 'k'

    @property
    def stan_konta(self):
        return self.stan

    @stan_konta.getter
    def stan_konta(self):
        return 'stan konta: '+str(self.stan) + 'zl'

    @stan_konta.setter
    def stan_konta(self, o_ile):
        self.stan += o_ile

konto = KontoBankowe()
# print(konto.sprawdz_stan())
# konto.zmien_stan(50)
# print(konto.sprawdz_stan())
print(konto.stan_konta)
konto.stan_konta = 50
print(konto.stan_konta)