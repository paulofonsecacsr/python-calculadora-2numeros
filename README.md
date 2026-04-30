# python-calculadora-2numeros
Calculadora programada em Python capaz de realizar seis operações matemáticas (Adição, Subtração, Multiplicação, Divisão, Potenciação, Radiciação) entre dois números. Esse programa foi feito para ser executado no próprio Terminal.

No desenvolvimento desse programa, busquei aplicar os conhecimento recém obtidos sobre Funcões com parâmetros e _return_. Trabalhei com afinco também no Tratamento de Erros, tanto no caso de respostas fora da gama de opções dada, como no caso do usuário digitar caracteres onde se pede um input do tipo _float_ (nesse caso, utilizando um bloco _try except_). Para evitar a exibição de valores inteiros (recebidos como float) com um 0 decimal no final, criei também uma função responsável por formatar valores, removendo, quando desnecessária, essa casa decimal de um número. Para não poluir o terminal, criei uma função responsável por limpá-lo a partir da funcão _clear_ da biblioteca nativa _os_.

Além disso, para dar a sensação de um Website real ao meu programa, fiz uso da função _sleep_ da biblioteca nativa _time_ para criar funções responsáveis por simular um carregamento no Terminal. Ao final do projeto, decidi melhorar ainda mais a sua estética aplicando cores estratégicas em alguns textos. Para isso, aprendi a usar as ferramentas da biblioteca importada _colorama_*.

O desenvolvimento desse programa melhorou minhas habilidades principalmente no manejo de Funções, mas também na organização do código seguindo as recomendações do PEP8.

*Para a execução plena desse programa, é importante que se tenha instalada a biblioteca _colorama_. Para fazer o seu download, copie e cole no seu Terminal:
- Mac: pip3 install colorama
- Windows: pip install colorama
