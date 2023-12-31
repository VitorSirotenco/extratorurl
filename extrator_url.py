import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()


    def sanitiza_url(self, url): #para tirar os espaços em branco da url e corrigir caso for passado um None
        if type(url) == str:
            return url.strip()
        else:
            return ""


    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia") #raise quando a mensagem a ser mostrada vem de um erro

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)  # metodo match pra conferir se o padrao bate exatamente com oq foi passado
        if not match:
            raise ValueError('Url invalida')


    def get_url_base(self):
        indice_interrogacao = self.url.find('?')  # para buscar a posicao onde esta o ?
        url_base = self.url[:indice_interrogacao]  # quando n é passado o primeiro valor, vai puxar desde o primeiro caractere
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]  # quando n é passado o ultimo valor, vai incluir até o final
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)  # para buscar entre o = e o &
        if indice_e_comercial == -1:  # quando o metodo find() nao encontra nada ele retorna -1
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self): #str é o metodo chamado quando usamos o print
        return "A URL é: " + self.url + "\n" + "Url Base: " + self.get_url_base() + "\n" + "Parâmetros: " + self.get_url_parametros()


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL("https://bytebank.com/cambio?moedaDestino=Dolar&moedaOrigem=real")
valor_quantidade = extrator_url.get_valor_parametro("moedaOrigem")
print(extrator_url)
print(valor_quantidade)








