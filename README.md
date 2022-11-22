# financas-pessoais
Durante minha transição para morar sozinho percebi que precisaria controlar minhas contas, apelei pra uma agenda, excel, ábaco, mas nada satisfez minha criatividade, então decidi criar meu próprio software de finanças pessoais.
A ideia era criar um banco de dados próprio, o resultado foi um arquivo CSV pirateado, ou como gosto de chamar, o VSV.
Algo que tentei evitar constantemente foi carregar todos os dados violentamente em uma variavel, por isso, criei metodos que liam linha por linha, e processavam elas individualmente.
Usei este software durante 6 meses, carreguei quase 300 registros, e, apesar de um tanto tosco, me ajudou a gerir minha vida financeira.
Hoje, analisando ele, vejo que errei em muitas coisas: 
-Os lançamentos são muito mecânicos, muitas vezes tornando um registro simples algo complexo;
-As classes são mal organizadas, e a orientação a objetos não foi nada respeitada;
-Usar um arquivo de texto ao invés de um banco de dados SQL é inviável.
Mesmo com estes e muitos defeitos, pude treinar conceitos como: organização básica de uma interface gráfica com tkinter, leitura e edição de arquivos, programação procedural, programação orientada a objetos.
