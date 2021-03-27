# Entrada

- Dados separados por espaço.
- Linha 1: Quantidade de estados possiveis;
- Linha 2: Quantidade de símbolos no alfabeto seguido dos simbolos;
- Linha 3: Quantidade de estados de aceitação seguida dos estados;
- Linha 4: Quantidade x de transições possiveis;
- Linha 5 até 5+x-1: Estado de partida seguido do simbolo seguido do estado destino;
- Linha seguinte: Numero de cadeias a serem validadas;
- Enfim: cadeias uma por linha.
- Cadeia vazia: "-"

# Saída

Para cada cadeia fornecida:
- Se a cadeia de entrada pertencer à linguagem reconhecida pelo autômato, será retornado "aceita".
- Senão, caso a cadeia de entrada não pertença à linguagem reconhecida pelo autômato, retorna-se "rejeita".
