Busca e Otimização: Viaje mais rápido com A-Estrela

O caso 

Imagine este trecho do metrô de Paris
![image](https://user-images.githubusercontent.com/62081666/131940344-75f54f96-d428-4fcc-8eb4-6d31eb89931b.png)

como achar qual o caminho mais rápido de uma dada estação até um dado destino, respeitando toda as constraints, como baldeações?

Os desafios do caso:

* a complexidade da linha metroviária - estamos usando um recorte apenas para facilitar a implementação
* A-estrela é um algoritmo de busca heurística e combina dois tipos de busca, a gulosa (rápida, porém imperfeita) e a de custo uniforme (otimizada, porém lenta) e o desafio se dá em como escrever o algoritmo de modo a garantir que o comportamento está sendo cumprido e sem ser muito custoso.
* modelar constraints do sistema e exceções. O que fazer se escolher um "fim da linha"? Por onde deveria voltar? Qual novo caminho deveria escolher?

Documentação 

O projeto foi feito em Python, versão 3.7.0

Foram usadas as bibliotecas:

* math

O projeto foi feito no pycharm, então, clonar este repositório e abrir como um novo projeto na referida IDE deve ser o bastante para sua reprodução

Próximos passos

* Por mais que esteja comentado, reconheço que o código precisa de uma refatoração, seja para reescrever alguns métodos de forma mais sucinta, seja para ajudar na legibilidade do código

* Muitas funções foram implementadas do zero e não busquei bibliotecas para o problema, deixando o código em baixo nível. Enquanto considero que há notáveis vantagens em implementar seu código, também reconheço que o uso de bibliotecas e funções pode facilitar a resolução do problema.
