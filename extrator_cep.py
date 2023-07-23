endereco = "rua Teodoro Xavier, 63A, Cidade Lider, São Paulo, 08260-180"

import re #Regular Expression, regEx

# 5 digitos + hifen (opcional) + 3 digitos padrao CEP

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
#para passar o padrao para o programa, o ? significa opcional e {} a qtd de vezes que ele vai se repetir
busca = padrao.search(endereco) #para buscar o padrao dentro da string, match
if busca:
    cep = busca.group() #para retornar a string encontrada naquele padrão
    print(cep)
