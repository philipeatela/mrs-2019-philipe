from git import Repo
import git
import os
import collections

repo = Repo(os.getcwd() + '/EventBus')

def getAllCommits(repo):
  commitsList = list(repo.iter_commits('master'))
  print(commitsList[0].author)
  return len(list(repo.iter_commits('master')))

print("-- ITEM 01 --")
print(getAllCommits(repo))

# PASSO A PASSO
  # Buscar lista de todos os arquivos do sistema
  # Para cada arquivo da lista:
    # Salva nome do criador do arquivo
    # Busca todos os commits que o alteraram e salva essa lista
    # Separa lista com os devs que alteraram o arquivo em algum momento
    # Para cada dev que trabalhou no arquivo:
      # Chama o metodo getFileAuthor para cada arquivo
      # Printa o nome do arquivo atual com a lista de todos os devs e seu author factor

# def getFileAuthor(f, d):
#   c = 0
#   if (d === CreatorOf(f)):
#     c = 1
  
#   md = changesMadeBy(d, f) # calcula quantas mudanças o dev 'd' fez no arquivo 'f'
#   mo = changesNotMadeBy(d, f) # calcula qtas mudanças outros devs que nao 'd' fizeram em 'f'

#   return c + (0.5 * md) - (0.1 * mo) # formula da autoria de codigo