import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_Valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.format_cep()

    def cep_eh_Valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return "{}-{}".format(self.cep[:5],self.cep[5:])

    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )


cep = 49037475
objeto_cep = BuscaEndereco(cep)

print(objeto_cep.format_cep())
cep_request = objeto_cep.acessa_via_cep()
# print(dir(cep_request))
print(cep_request)
