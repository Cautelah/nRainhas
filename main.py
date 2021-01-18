import numpy
qtd_colunas = 8
qtd_linhas = 8
solucao = 0
tabuleiro = numpy.zeros((qtd_colunas,qtd_linhas))



def possivel(x,y):
  global tabuleiro
  for linha in range(qtd_linhas):
    if tabuleiro[x,linha] == 1: #mesma coluna
      return False
  for coluna in range(qtd_colunas):
    if tabuleiro[coluna,y] == 1: #mesma linha
      return False
  for coluna in range(qtd_colunas):
    for linha in range(qtd_linhas):
      if abs(x-coluna) == abs(y-linha):
        if tabuleiro[coluna,linha] == 1: #mesma diagonal
          return False
  return True


def resolver(coluna): #testa a coluna
  global tabuleiro
  global solucao
  for linha in range(qtd_linhas): #testa cada linha da atual coluna:
    if possivel(linha,coluna): #se puder ocupar, ocupe
      tabuleiro[linha,coluna] = 1
      if coluna +1 == qtd_colunas:  #se tentar preencher fora do tabuleiro, foi encontrado solução
        solucao += 1 
        print(f"Solução {solucao}:")
        print(tabuleiro) #mostrar solução encontrada
      else: #se não encontrou solução, preencha próxima coluna
        resolver(coluna+1)
      tabuleiro[linha,coluna] = 0 #recua independente de solução 


resolver(0)