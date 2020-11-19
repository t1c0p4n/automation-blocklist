# automation-blocklist
# Script de automação de lista de ips maliciosos (blocklist) para regra de inserção em ACL de firewalls. 
# O presente modelo de regras é válido para sintaxes do FortiOS (Firewall Fortigate).
# O Script é válido para versões do FortiOS onde a lista externa automatizada (Fabric Connectors) não está funcional (versões < 6.4.x).
# A lista presente é disponibilizada pele CTIR Gov + SERPRO (Serviços Federais Brasileiros) e são atualizados por estes órgãos de forma automática.
# 
# Modo de usar:
# Execute o script sem nenhum parâmetro adicional:
# sudo python3 lista-serpro.py
# 
# Como saída, serão exibidas mensagens do andamento do script, bem como 2 arquivos de configuração.
# O arquivo 1. deve ser o primeiro arquivo a ser importado no seu fortigate, seguido do arquivo 2.
# O primeiro arquivo cria objetos do tipo endereço, enquanto que o segundo arquivo cria um grupo que aloca os endereços recém criados.
# Ressalto que o Fortigate possui limite de inserção de objetos em grupos, em algumas tentativas o FortiOS retornou erros que só puderam ser debugados na inserção do arquivo via CLI. Neste caso, divida a inserção do segundo arquivo em quantidade menores.
#
# Criado por Thiago Nogueira - ticopan@gmail.com
# Data de criação: 11.11..2020
