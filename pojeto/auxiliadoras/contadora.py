class Contadora:

    def __init__(self, texto):
        self.texto = texto

    def countL(self):
        with open(self.texto) as linha:
            i = 0
            for line in linha:
                i += 1

        return i