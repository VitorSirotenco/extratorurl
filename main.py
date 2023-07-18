url = 'https://bytebank.com/cambio?moedaDestino=Dolar&moedaOrigem=real'

print('a url é: {} ' .format(url))

# Separa base e parâmetros
indice_interrogacao = url.find('?') #para buscar a posicao onde esta o ?
url_base = url[:indice_interrogacao] #quando n é passado o primeiro valor, vai puxar desde o primeiro caractere
print(url_base)

url_parametros = url[indice_interrogacao + 1:] #quando n é passado o ultimo valor, vai incluir até o final
print(url_parametros)


#Busca o valor de um parâmetro
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor) #para buscar entre o = e o &
if indice_e_comercial == -1: #quando o metodo find() nao encontra nada ele retorna -1
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]


print(valor)
