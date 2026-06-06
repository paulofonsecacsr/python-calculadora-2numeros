# Calculadora Python de 2 números
Calculadora programada em __Python__ capaz de realizar __seis operações matemáticas__ (Adição, Subtração, Multiplicação, Divisão, Potenciação, Radiciação) entre dois números. Esse programa foi feito para ser executado no próprio Terminal da IDE de preferência do usuário.

## Instruções de instalação
Para executar o programa, primeiramente  instale ou tenha instalado o [__VSCode__](https://code.visualstudio.com/download) (ou outra IDE de sua preferência) em sua máquina.

Após isso, instale [__Python__](https://www.python.org/downloads/) em sua máquina.

Para a experiência visual plena desse programa, instale a biblioteca ___colorama___ em sua IDE. Para fazer o seu download, copie e cole no seu Terminal:<br>
* __Mac__: _pip3 install colorama_
* __Windows__: _pip install colorama_

## Instruções de uso
Para usar a "Calculadora Python de 2 Números", copie o código escrito no arquivo _python-calculadora-2numeros.py_ do repositório e cole na sua IDE.

## Processo de desenvolvimento e detalhes do código
No desenvolvimento desse programa, busquei aplicar os aprendizados recentes sobre __funções__ com parâmetros e _return_. 

Para o programa receber a operação matemática que deve ser executada, a fim de poder aplicar a função built-in _replace()_ com o intuito de fazer o programa __ler corretamente respostas mal-escritas__, optei por pedir que o usuário digite o nome da operação. Nesse sentido, tratei a ausência de primeira letra maiúscula e/ou de acento til e/ou de cedilha e/ou a presença de espaços antes e depois das palavras para que todas resultem numa resposta válida.

Trabalhei com afinco também no __tratamento de erros__, tanto no caso de respostas fora da gama de opções dada, como no caso do usuário digitar caracteres onde se pede um input do tipo _float_ (para esse caso, utilizei um bloco _try except_ com a exceção _ValueError_) e, não menos importante, no famoso caso da divisão por zero (incluindo a exceção _ZeroDivisionError_ no mesmo bloco _try except_). Tratei também o caso de radiciação com radicando negativo, que, apesar de possuir solução real no caso do expoente ser ímpar, em Python dá bug sem que haja a importação de alguma biblioteca matemática.

Para evitar a exibição de valores inteiros (recebidos como _float_) com um 0 decimal no final, criei também uma função responsável por __formatar valores__, removendo, quando desnecessária, essa casa decimal de um número.

Além disso, para dar a sensação de um Website real ao meu programa, fiz uso da função _sleep()_ da biblioteca nativa _time_ para criar funções responsáveis por __simular um carregamento__ no terminal. Ao final do projeto, decidi melhorar ainda mais a sua estética aplicando __cores estratégicas__ em alguns textos. Para isso, aprendi a usar as ferramentas da biblioteca importada _colorama_.
