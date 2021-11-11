class People:
    def __init__(self, vezetek, kereszt, nem, szam, munkahely, munkahely_cim, bme_tanulo, ):
        self.vezetek = vezetek
        self.kereszt = kereszt
        self.nem = nem
        self.szam = szam
        self.munkahely = munkahely
        self.munkahely_cim = munkahely_cim
        self.bme_tanulo = bme_tanulo
        self.nev = vezetek + kereszt

    def __str__(self):
        return f"====================================\n" \
               f"Név: {self.vezetek} {self.kereszt}\tNeme: {self.nem}\tTelefonszám: {self.szam}\nMunka:{self.munkahely}\t" \
               f"Munkahely címe:{self.munkahely_cim}\nBME-n tanul: {self.bme_tanulo}"

    def save(self):
        return [str(self.vezetek), str(self.kereszt), str(self.nem), int(self.szam), ]
