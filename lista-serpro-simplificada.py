#Importando módulos necessários
import urllib.request
import os

#Definindo constantes
url = 'https://s3.i02.estaleiro.serpro.gov.br/blocklist/blocklist.txt'
arquivo = '/home/ticopan/blocklist.txt'
script1 = '/home/ticopan/Add_Address_SERPRO.txt'
script2 = '/home/ticopan/Add_Group_SERPRO.txt'

#Limpando arquivos
os.system( 'echo > ' + script1 )
os.system( 'echo > ' + script2 )

#Baixando o arquivo do link da internet
urllib.request.urlretrieve(url, arquivo)

#Abrindo arquivo baixado
f = open(arquivo, 'r')

#Abrindo e escrevendo linha inicial do arquivo
fs1 = open(script1, 'a')
fs1.write('config firewall address \n')

#Navegando por todas as linhas do arquivo
for line in f:
    conteudo = f.readline()
    fs1 = open(script1, 'a')
    fs1.write('edit SEPRO_' + conteudo)
    fs1.write('set subnet ' + conteudo.rstrip('\n') + '/32\n')
    fs1.write('next\n')
    #fs1.close()

#Escrevendo a linha final do arquivo
fs1 = open(script1, 'a')
fs1.write('end\n')

#Fechando arquivos
fs1.close()
f.close()

