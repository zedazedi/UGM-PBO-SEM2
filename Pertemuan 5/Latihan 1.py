class Yunani:
    def ibukota(self):
        print("Ibukota Yunani adalah Athena")

    def mata_uang(self):
        print("Mata uang Yunani adalah Euro (EUR)")

class Korea_selatan:
    def ibukota(self):
        print("Ibukota Korea Selatan adalah Seoul")

    def mata_uang(self):
        print("Mata uang Korea Selatan adalah Won Korea Selatan (KRW)")

yunani = Yunani()
korsel = Korea_selatan()

for negara in (yunani, korsel):
    negara.ibukota()
    negara.mata_uang()
