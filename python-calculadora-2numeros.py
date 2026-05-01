import os
from time import sleep
from colorama import Fore, Back, Style, init
init(autoreset=True)


def titulo():
    print(f"{Style.BRIGHT + Fore.WHITE + Back.BLUE}PYTHON CALCULADORA DE 2 NÚMEROS{Style.RESET_ALL} - Made by Paulo Fonseca\n")


def linha():
    print("-" * len("Digite 'Encerrar' ou 'Continuar':"), "\n")


def limpar():
    os.system("clear")
    os.system("clear")


def carregamento(texto, tempo):
    limpar()

    if texto == "":
        print(f"{texto}[...]\n")
    else:
        print(f"{texto} [...]\n")

    sleep(tempo)


def erro(texto_por_tipo_erro):
    limpar()
    carregamento("", 0.5)
    limpar()
    print(f"{Style.BRIGHT + Fore.RED}{texto_por_tipo_erro}\n")
    sleep(1.25)


def valor_formatado(valor):

    if valor == round(valor):
        return round(valor)
    else:
        return valor
    

def adicao(valor1, valor2):
    resultado = valor1 + valor2
    return valor_formatado(resultado)


def subtracao(valor1, valor2):
    resultado = valor1 - valor2  
    return valor_formatado(resultado)


def multiplicacao(valor1, valor2):
    resultado = valor1 * valor2
    return valor_formatado(resultado)


def divisao(valor1, valor2):
    resultado = valor1 / valor2
    return valor_formatado(resultado)


def potenciacao(valor1, valor2):
    resultado = valor1 ** valor2
    return valor_formatado(resultado)


def radiciacao(valor1, valor2):
    resultado = valor1 ** (1 / valor2)
    return valor_formatado(resultado)


def abertura():
    limpar()
    titulo()
    carregamento("", 0.5)
    limpar()
    titulo()
    input(f"Pressione{Style.BRIGHT + Fore.GREEN} 'Enter'{Style.RESET_ALL} para iniciar\n\n")
    carregamento(f"Iniciando {Style.BRIGHT + Fore.WHITE + Back.BLUE}'PYTHON CALCULADORA DE 2 NÚMEROS'{Style.RESET_ALL}", 0.75)


def escolher_operacao():
    nome_operacao = input(f"Digite o nome da operação desejada ou {Style.BRIGHT + Fore.RED}'Encerrar'\n\n{Style.BRIGHT + Fore.BLUE}Adição\nSubtração\nMultiplicação\nDivisão\nPotenciação\nRadiciação\n\n{Style.RESET_ALL}-> ").strip().capitalize()
    nome_operacao = nome_operacao.replace("cao", "ção").replace("çao", "ção").replace("cão", "ção").replace("sao", "são")
    return nome_operacao


def definicao_valores(texto_valor1, texto_valor2):
    valor1 = float(input(f"\n{texto_valor1}:\n\n->{Style.BRIGHT + Fore.BLUE} "))        
    valor2 = float(input(f"\n{Style.RESET_ALL}{texto_valor2}:\n\n->{Style.BRIGHT + Fore.BLUE} "))
    print()
    return valor_formatado(valor1), valor_formatado(valor2)


def conta(operacao, valor1, valor2, exibicao_resultado, simbolo_operacao):
    sleep(1)
    print(f"{Style.RESET_ALL}{exibicao_resultado} {Style.BRIGHT + Fore.BLUE}{valor1} {Style.RESET_ALL}{simbolo_operacao} {Style.BRIGHT + Fore.BLUE}{valor2} {Style.RESET_ALL}é {Style.BRIGHT + Fore.GREEN}{operacao(valor1, valor2)}\n")
    

def funcao_continuar_ou_encerrar():
    sleep(0.75)
    linha()
    while True:
        continuar_ou_encerrar = input(f"Digite{Style.BRIGHT + Fore.RED} 'Encerrar'{Style.RESET_ALL} ou{Style.BRIGHT + Fore.GREEN} 'Continuar'{Style.RESET_ALL}:\n\n").strip().capitalize()
        
        if continuar_ou_encerrar == "Encerrar":
            return False
        elif continuar_ou_encerrar == "Continuar":
            carregamento("Voltando ao menu", 1)
            break
        else:
            erro("Resposta inválida")
            limpar()
            

def encerramento():
    limpar()
    print(f"{Style.BRIGHT + Fore.RED}Programa encerrado.\n")
    sleep(0.75)
    os.system("clear")
    os.system("clear")
    

def calculadora():
    while True:
        try:
            limpar()
            nome_operacao = escolher_operacao()
            limpar()
            carregamento("", 0.5)
            limpar()
            
            if nome_operacao == "Encerrar":
                break
            elif nome_operacao not in ["Adição", "Subtração", "Multiplicação", "Divisão", "Potenciação", "Radiciação"]:
                erro("Resposta inválida")
                continue
            else:
                print(f"{Style.BRIGHT + Fore.BLUE}{nome_operacao.upper()}")
                  
                if nome_operacao == "Adição":
                    valor1, valor2 = definicao_valores("Digite o valor de uma parcela", "Digite o valor da outra parcela")
                    conta(adicao, valor1, valor2, "A soma de", "+")

                elif nome_operacao == "Subtração":
                    valor1, valor2 = definicao_valores("Digite o valor do minuendo", "Digite o valor do subtraendo")
                    conta(subtracao, valor1, valor2, "A diferença de", "-")

                elif nome_operacao == "Multiplicação":
                    valor1, valor2 = definicao_valores("Digite o valor de um fator", "Digite o valor do outro fator")
                    conta(multiplicacao, valor1, valor2, "O produto de", "x")

                elif nome_operacao == "Divisão":
                    valor1, valor2 = definicao_valores("Digite o valor do dividendo", "Digite o valor do divisor")
                    conta(divisao, valor1, valor2, "O quociente de", "÷")
                            
                elif nome_operacao == "Potenciação":
                    valor1, valor2 = definicao_valores("Digite o valor da base", "Digite o valor do expoente")
                    conta(potenciacao, valor1, valor2, "O resultado de", "^")
                            
                elif nome_operacao == "Radiciação":
                    valor1, valor2 = definicao_valores("Digite o valor do radicando", "Digite o valor do índice")
                    if valor1 >= 0  :
                        conta(radiciacao, valor1, valor2, "O resultado de", "√")
                    else:
                        erro("Conta inválida")
                        carregamento("Voltando ao menu", 1)
                        continue

            if funcao_continuar_ou_encerrar() == False:
                        break
            
        except ZeroDivisionError:
            erro("Conta inválida")
            carregamento("Voltando ao menu", 1)
            continue
                                                     
        except ValueError:
            erro("Resposta inválida")
            continue


def main():
    abertura()
    calculadora()
    encerramento()


if __name__ == "__main__":
    main()