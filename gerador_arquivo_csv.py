# Biblioteca 
from datetime import datetime
import gerador_dados_aleatórios as gda

# Dados a serem usados no arquivo:

data_atual = datetime.now().strftime('%d%m%Y')
nome = gda.nome()
data_nascimento = gda.data_nasc()
cpf = gda.gerar_cpf()
nome_mae = gda.nome()
nome_pai = gda.nome()
endereco = ""
cel = gda.cel()
email = ''
endereco = ''



info_csv = (f'{data_atual}, {nome}, {data_nascimento}, {cpf}, {nome_mae}, {nome_pai}, {endereco},{cel}''\n')

with open('csv_massa_dados.csv', 'a', encoding= 'utf-8') as arquivo:
    arquivo.write(info_csv)


    