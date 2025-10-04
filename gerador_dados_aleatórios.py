#==================================================================================================================================================================================== FUNÇÕES ======================================================================

# Bibliotecas:
import random

# Gerar um CPF aleatório:

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


#=================================================================================================================================

# Gera uma data de nascimento aleatória:

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
    
    
#=================================================================================================================================

def nome():
    primeiro_nome = ["Rodolfo", "Marcelli", "Guilherme", "Kauan", "Davi", "Marina", "Joana", "Damião", "Sandra", "Solange", "Simone", "Silvia", "Alvaro", "Carlinhos", "Silvana", "Barbara", "Raphaelli", "Emerson", "Fabiana", "Nicole", "Nicolas", "Luan", "Thiago", "Jarlei", "Marcos", "Kaique", "Sthephanie", "Odila", "José", "João", "Irami"]
    p_n = random.choice(primeiro_nome)
    segundo_nome = ["Gonçalves", "Christine", "Maia", "Albuquerque", "Mendonça", "Borges", "Senna", "Santiago", "Benício", "Catarina"]
    s_n = random.choice(segundo_nome)
    sobrenome = ["Hermengildo", "Silva", "Camarotto", "Souza", "Lopes", "Lelis", "Costa", "Neto", "Filho", "Júnior", "Braga", "Plinio", "Fausto", "Liberatto", "Cechetto"]
    s = random.choice(sobrenome)

    return (f'{p_n} {s_n} {s}')




#=================================================================================================================================