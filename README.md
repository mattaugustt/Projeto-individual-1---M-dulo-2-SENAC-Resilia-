#Projeto individual 1 - Módulo 2; <br>
#Matheus Augusto de Souza.


* Desenvolver um código capaz de ajudar uma startup na verificação de compatibilidade de um candidato com a vaga, de acordo com o desempenho obtido no processo seletivo.

- Propostas do projeto: <b><br>
1°) Criar uma função que devolve/retorna uma string do tipo: 'eX_tX_pX_sX', onde cada X é substituído pela nota obtida pela pessoa em cada uma das etapas do processo - entrevista, teste teórico, teste prático e avaliação de soft skills. <br>
2°) Criar uma função que faça a busca dos usuários, com as notas minimas (de 'e', 't', 'p' e 's') dadas como entrada na função, e retorne uma listagem com os entrevistados que possuem notas maior ou igual as dadas na busca.

A primeira função vai ser chamada sem paramâmetros, e os dados vão ser inseridos em listas através de inputs. <br>
A segunda função vai ser chamada com 5 parâmetros, sendo eles: a lista com todos os usuários entrevistados e as notas de 'e', 't', 'p' e 's'. <br>

Se quisermos uma apresentação mais bonita dos usuários e resultados obtidos, podemos utilizar a função pd.DataFrame da biblioteca 'pandas'. Esta irá apresentar os dados em uma tabela.
