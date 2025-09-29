# Biblioteca 
from datetime import datetime
import random

# Funções

def gerar_cpf():
    # Gera os 9 primeiros dígitos do CPF
    cpf = [random.randint(0, 9) for _ in range(9)]

    # Calcula o primeiro dígito verificador
    soma = sum((10 - i) * cpf[i] for i in range(9))
    primeiro_digito = (soma * 10 % 11) % 10
    cpf.append(primeiro_digito)

    # Calcula o segundo dígito verificador
    soma = sum((11 - i) * cpf[i] for i in range(10))
    segundo_digito = (soma * 10 % 11) % 10
    cpf.append(segundo_digito)

    # Retorna o CPF formatado
    return "{}{}{}{}{}{}{}{}{}{}{}".format(*cpf)

def data_nasc():
    dia = random.randint(1, 31)
    mes = random.randint(1, 12)
    ano = random.randint(1960, 2000)

    if dia <= 9:
        dia = (f'0{dia}')
    if mes <= 9:
        mes = (f'0{mes}')
        return (f'{dia}{mes}{ano}')
    else:
        return (f'{dia}{mes}{ano}')


# Dados a serem usados no arquivo

data_atual = datetime.now().strftime('%d%m%Y')
nome = 'Rodolfo'
data_nascimento = data_nasc()
cpf = gerar_cpf()
nome_mãe = ''
endereço = ''
cel = ''



info_csv = (f'{data_atual},{nome},{data_nascimento},{cpf},{nome_mãe},{endereço},{cel}')





