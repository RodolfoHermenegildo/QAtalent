# Biblioteca 
from datetime import datetime
import gerador_dados_aleatórios as gda

# Dados a serem usados no arquivo:

data_atual = datetime.now().strftime('%d%m%Y')
data_atual_posicional = f'{data_atual:<15}'
nome = gda.nome()
data_nascimento = gda.data_nasc()
cpf = gda.gerar_cpf()
nome_mae = gda.nome()
nome_pai = gda.nome()
endereco = ""
cel = gda.cel()
email = (nome.lower().replace(' ',''))
endereco = gda.endereco()



info_posicional = (f'{data_atual_posicional}{nome}{data_nascimento}{cpf}{nome_mae}{nome_pai}{endereco}{cel}{f'{email}@main.com'}{endereco}''\n')


#{'São Paulo':<15}



with open('posicional_massa_dados.txt', 'a', encoding= 'utf-8') as arquivo:
    arquivo.write(info_posicional)

