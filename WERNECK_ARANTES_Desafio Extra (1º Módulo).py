# Função que converte um caractere ou string em binário.
def binario(x):
    vetor1, vetor2 = [], []          # Com o auxílio de duas listas, podemos transformar cada caractere da string
    for i in x:                      # em unicode, armazenando esses dados no vetor1. Depois, através da segunda
        vetor1.append(ord(i))        # lista, convertemos cada posição em binário, retornando o vetor2.
    for i in vetor1:
        vetor2.append(bin(i))
    return vetor2


# Função que converte um valor (ou valores) de binário para decimal.
def binario_dec(x):
    dec_x = 0                           # Convertemos cada byte binário do array em decimal (int, base2) e armaze-
    for i in range(len(x) // 8):        # namos na variável dec_x. A função retorna o valor final de dec_x.
        dec_x = int(x, 2)
    return dec_x


# Função que converte um valor (ou valores) de binário para string.
def binario_string(x):
    return ''.join(chr(int(x[i * 8:i * 8 + 8], 2)) for i in range(len(x) // 8))


# Função que converte um caractere ou string em hexadecimal.
def hexdecimal(z):
    vetor1, vetor2 = [], []             # Funcionalidade bem parecida com a função binario.
    for i in z:
        vetor1.append(ord(i))
    for i in vetor1:
        vetor2.append(hex(i))
    return vetor2


# Função que converte um caractere ou string em decimal.
def decimal(z):
    vetor1 = []                         # O mesmo princípio das funções binario e hexdecimal. Porém, agora com apenas
    for i in z:                         # uma lista.
        vetor1.append(ord(i))
    return vetor1


# Função principal, com opções. O desafio, em si e conforme anunciado na AVA, é resolvido na opção 2.

def main():
    print('\t\tCONVERSOR DE SISTEMAS DE NUMERAÇÃO (DECIMAL, BINÁRIO E HEXADECIMAL)')
    print()
    print('Opções Disponíveis:')
    print()
    print('1 - Converter um valor inteiro para Binário e Hexadecimal')
    print('2 - Converter uma String ou caractere para Decimal, Binário e Hexadecimal')
    print('3 - Converter um valor em Binário para Decimal')
    print('4 - Converter um valor em Binário para String')
    print('5 - Converter um valor em Hexadecimal para Decimal')
    print('6 - Converter um valor em Hexadecimal para String')
    print('7 - Encerrar o Programa')
    print()
    option = input('Digite a opção desejada: ')
    while option != '1' and option != '2' and option != '3' and option != '4' and option != '5' and option != '6' and \
            option != '7':
        print('\033[31mOpção Inválida!\033[m')
        option = (input('Digite a opção desejada: '))
    if option == '1':
        num = int(input('Digite um valor inteiro para convertê-lo em Binário e Hexadecimal: '))
        print()
        print('O número digitado foi: {}'.format(num))
        print('Seus valores em Binário e Hexadecimal são, respectivamente:')
        numbin = bin(num)
        numhex = hex(num)
        print('Binário: {}'.format(numbin))
        print('Hexadecimal: {}'.format(numhex))
        print()
        main()
    elif option == '2':
        msg = input('Digite uma string para convertê-la em Decimal, Binário e Hexadecimal: ')
        print()
        print('A string digitada foi: {}'.format(msg))
        print('Seus valores em Binário, Hexadecimal e Decimal são, respectivamente:')
        print('Binário:', binario(msg))
        print('Hexadecimal:', hexdecimal(msg))
        print('Decimal:', decimal(msg))
        print()
        main()
    elif option == '3':
        print('\033[31m Atenção! Os valores devem ser escritos sem o prefixo 0b!\033[m')
        bin_dec = input('Digite um valor em Binário para convertê-lo em Decimal: ')
        print()
        print('O valor digitado foi: {}'.format(bin_dec))
        print('O valor em Decimal é: {}'.format(binario_dec(bin_dec)))
        print()
        main()
    elif option == '4':
        print('\033[31m Atenção! Os valores devem ser escritos sem o prefixo 0b\033[m')
        bin_str = input('Digite um valor em Binário para convertê-lo em String: ')
        bin_strformat = bin_str.replace(" ", "")  # Retirando os espaços entre os bytes para que a função possa operar
        print()                                   # conforme a lógica esperada.
        print('O valor digitado foi: {}'.format(bin_str))
        print('O valor convertido em string é:', binario_string(bin_strformat))
        print()
        main()
    elif option == '5':
        hex_a = input('Digite um valor em Hexadecimal para convertê-lo em Decimal: ')
        hex_dec = int(hex_a, 16)
        print()
        print('O valor digitado foi: {}'.format(hex_a))
        print('O valor em Decimal é: {}'.format(hex_dec))
        print()
        main()
    elif option == '6':
        print('\033[31m Atenção! Os valores devem ser escritos sem o prefixo 0x\033[m')
        hex_b = str(input('Digite valores em Hexadecimal para convertê-los em uma string: '))
        print()
        print('O valor digitado foi: {}'.format(hex_b))
        hex_bformat = hex_b.replace(" ", "")  # Mesmo caso do elif == '4'.
        hexarray = bytearray.fromhex(hex_bformat)
        toascii = hexarray.decode('latin-1')              # Precisei usar latin-1 para ele converter os acentos.
        print('O valor convertido em string é: {}'.format(toascii))
        print()
        main()
    elif option == '7':
        print('Obrigado por usar o conversor!')
        quit()


main()
