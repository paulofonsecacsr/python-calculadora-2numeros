# python-calculadora-2numeros
Calculadora programada em Python capaz de realizar seis operações matemáticas (Adição, Subtração, Multiplicação, Divisão, Potenciação, Radiciação) entre dois números. Esse programa foi feito para ser executado no próprio Terminal.

No desenvolvimento desse programa, busquei aplicar os aprendizados recentes sobre Funcões com parâmetros e _return_. 

Para o programa receber a operação matemática que deve ser executada, a fim de poder aplicar a função _replace_ com o intuito de corrigir respostas mal-escritas, optei por pedir que o usuário escreva o nome da operação. Assim, a ausência de primeira letra maiúscula e/ou de acento til e/ou de cedilha e/ou a presença de espaços antes e depois das palavras foram todas tratadas para resultarem numa resposta válida.

Trabalhei com afinco também no Tratamento de Erros, tanto no caso de respostas fora da gama de opções dada, como no caso do usuário digitar caracteres onde se pede um input do tipo _float_ (para esse caso, utilizei um bloco _try except_) e, não menos importante, no famoso caso da divisão por zero (incluindo a exceção ZeroDivisionError no mesmo bloco _try except_). Tratei também o caso de radiciação com radicando negativo, que, apesar de possuir solução real no caso do expoente ser ímpar, dá bug na versão nativa do Python.

Para evitar a exibição de valores inteiros (recebidos como float) com um 0 decimal no final, criei também uma função responsável por formatar valores, removendo, quando desnecessária, essa casa decimal de um número. 

Além disso, para dar a sensação de um Website real ao meu programa, fiz uso da função _sleep_ da biblioteca nativa _time_ para criar funções responsáveis por simular um carregamento no Terminal. Ao final do projeto, decidi melhorar ainda mais a sua estética aplicando cores estratégicas em alguns textos. Para isso, aprendi a usar as ferramentas da biblioteca importada _colorama_*.

O desenvolvimento desse programa melhorou minhas habilidades principalmente no manejo de Funções, mas também na organização do código seguindo as recomendações do PEP8.

*Para a experiência visual plena desse programa, é necessário que se tenha instalada a biblioteca _colorama_. Para fazer o seu download, copie e cole no seu Terminal:
- Mac: pip3 install colorama
- Windows: pip install colorama
