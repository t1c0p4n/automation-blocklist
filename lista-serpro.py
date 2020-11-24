#Importando módulos necessários
import urllib.request
import os

#Definindo constantes
url = 'https://s3.i02.estaleiro.serpro.gov.br/blocklist/blocklist.txt'
arquivo = '/<seu_diretório>/blocklist.txt'
script1 = '/<seu_diretório>/1.Add_Address_SERPRO.txt'
script2 = '/<seu_diretório>/2.Add_Group_SERPRO.txt'
c = 0

#Limpando arquivos
print('--> Limpando os arquivos de config antigos')
os.system( 'echo > ' + script1 )
os.system( 'echo > ' + script2 )

#Baixando o arquivo do link da internet
urllib.request.urlretrieve(url, arquivo)

#Abrindo arquivo baixado
f = open(arquivo, 'r')

#Abrindo e escrevendo linha inicial do arquivo
fs1 = open(script1, 'a')
fs1.write('config firewall address \n')
fs2 = open(script2, 'a')
fs2.write('config firewall addrgrp \n')
fs2.write('edit "SEPRO_IPs" \n')
fs2.write('set member ')


#Navegando por todas as linhas do arquivo
for line in f:
    conteudo = f.readline()
    fs1 = open(script1, 'a')
    fs1.write('edit SEPRO_' + conteudo)
    fs1.write('set subnet ' + conteudo.rstrip('\n') + '/32\n')
    fs1.write('next\n')
    fs2.write('SEPRO_' + conteudo.rstrip('\n') + ' ')
    c = c + 1

#Escrevendo a linha final do arquivo
fs1 = open(script1, 'a')
fs1.write('end\n')

fs2 = open(script2, 'a')
fs2.write('next \n')
fs2.write('end \n')

#Fechando arquivos
fs1.close()
fs2.close()
f.close()
print('--> Arquivos escritos com sucesso! Total de ' + str(c) + ' IPs na lista.' )

#Copiando arquivos para a pasta documentos no Windows
os.system('cp *Add_* /<seu_diretório>/')
print('--> Arquivos de config copiados para pasta "/<seu_diretório>/"')
