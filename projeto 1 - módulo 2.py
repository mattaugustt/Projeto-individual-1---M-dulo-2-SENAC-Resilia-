#Projeto individual 1 - Módulo 2;
#SENAC/Resilia.
#Matheus Augusto de Souza.


import pandas as pd

#Função que imprime as listas em linhas
def imprime(lista):
  """Função criada para imprimir um indice da lista por linha"""
  for i in lista:
    print(i)



#Função que adiciona as notas do entrevistado e armazena em uma lista.
def compat():
    """Função que recebe as notas do usuário nas etapas do processo seletivo e 
    retorna as notas no formato: 'eX_tX_pX_sX'"""
    #devolve uma string no formato eX_tX_pX_sX - sendo que cada X 
    #é substituído pela avaliação da pessoa em uma das etapas do 
    #processo.
    #onde lista está no formato : [entrevista, testeTeo, testePra, softSkills]
    resultados = []
    #o resultado no fomato eX_tX_pX_sX vai ser adicionado na lista com 
    #resultados
    cont = 'sim'
    while cont == 'sim' or (cont == 'Sim') or (cont == 'SIM') or (cont == 's'):
      print('*'*50)
      nome = input('Diga qual o nome do entrevistado:\n')
      print('\n','*'*50) 
      lista = (input('Diga as notas da seguinte forma:\nEntrevista, Teste Teórico, Teste Prático, SoftSkills\n'))
      print('*'*50,'\n')
      dados = [] #lista vazia para adicionar o nome e as notas individuais;

      x = lista.split(',') #cria uma lista com as notas dadas pelo entrevistador
      resultado = ''
      resultado += 'e' + str(x[0]) + '_'  #primeira nota
      resultado += 't' + str(x[1]) + '_'  #segunda nota
      resultado += 'p' + str(x[2]) + '_'  #terceira nota
      resultado += 's' + str(x[3])  #quarta nota
      dados.append(nome)  #adiciona o nome na lista de dados individuais 
      dados.append(resultado)  #adiciona as notas no formato 'eX_tX_pX_sX'
      resultados.append(dados)
      print('*'*50,)
      cont = input('Deseja continuar?\n(digite sim ou não)\n')
      print('*'*50,'\n')
    print(resultados)
    
    return pd.DataFrame(resultados, columns=['Candidato', 'Resultado'])
    # Podemos usar a função: pd.DataFrame para imprimi uma tabela com as colunas 
    # Candidato e Resultado (após importar a biblioteca pandas)

    #return imprime(resultados)
    #caso não queiramos importar a biblioteca pandas, podemos usar essa função.
  


#Função que busca o entrevistado pelas notas minimas.
def busca(resultados, E,T,P,S):
    '''Função que recebe a lista de resultados e as notas minimas de cada parte 
    do processo seletivo e retorna uma lista com os usuários que correspondem as 
    exigencias. list, int, int, int, int -> '''
    selecionados = []  #lista com todos os candidatos que foram selecionados
    for entrevistas in resultados:
      sel = []  #lista com o selecionado (a cada loop)
      pessoa = entrevistas[0] #posição do nome na lista
      notas = entrevistas[1] #posição das nostas na lista
      total = []  #lista vazia para validação

      x = notas.split('_')
      for i in x:
        nota = i
        if 'e' in nota:
          valor = float(nota[1:])
          if valor >= E:
            total.append(nota)
        
        if 't' in nota:
          valor = float(nota[1:])
          if valor >= T:
            total.append(nota)
        
        if 'p' in nota:
          valor = float(nota[1:])
          if valor >= P:
            total.append(nota)
        
        if 's' in nota:
          valor = float(nota[1:])
          if valor >= S:
            total.append(nota)
        if len(total) == 4:
          sel.append(pessoa)
          sel.append(total)
      selecionados.append(sel)
      for i in selecionados:
        if i == []:
          selecionados.remove(i) #remove os espaços em vazios dos usuários que
          # não foram selecionados
    
    return pd.DataFrame(selecionados, columns=['Candidato', 'Notas']) #ou
    #return imprime(selecionados)

#teste:
#busca([['Matheus', 'e10_t10_p10_s7'], ['Luiz', 'e10_t9_p8_s7'], ['Larissa', 'e9_t8_p7_s6'], ['Barbara', 'e0_t0_p0_s0'], ['Bia', 'e8_t8_p9_s10']], 8,7,8,7)
