def format_cpf(cpf):
    # Remover caracteres não numéricos do CPF
    cpf_digits = ''.join(filter(str.isdigit, cpf))

    # Adicionar zeros à esquerda se necessário
    cpf_digits = cpf_digits.zfill(11)

    # Formatar o CPF
    formatted_cpf = f"{cpf_digits[:3]}.XXX.XXX-{cpf_digits[9:]}"
    print(f'cpf: {formatted_cpf}')

    return formatted_cpf
