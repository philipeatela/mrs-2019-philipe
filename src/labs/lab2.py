from git import Repo
import git
import os
import collections

def getCommitNumOfFiles(repo, arg):
  commits = list(repo.iter_commits('master'))
  commit = commits[arg]
  return len(commit.stats.files)

def getCommitNumOfJavaFiles(repo, arg):
  commits = list(repo.iter_commits('master'))
  commit = commits[arg]
  count = 0
  for f in list(commit.stats.files):
    if ('.java' in f):
      count = count + 1
  return count

def getCommitsFileCount(repo):
  commits = list(repo.iter_commits('master'))
  for c in commits:
    print('Commit ' + c.message)
    print(str(len(c.stats.files)) + ' arquivos modificados')

def getCommitsJavaFileCount(repo):
  commits = list(repo.iter_commits('master'))
  for c in commits:
    print('Commit ' + c.message)
    files = c.stats.files
    count = 0
    for f in files:
      if ('.java' in f):
        count = count + 1
    print(str(count) + ' arquivos java modificados')

  commits = list(repo.iter_commits('master', since=dateSince, until=dateUntil))
  fileChanges = []
  for c in commits:
    for d in c.diff():
      fileName = d.a_path
      if ('.java' in fileName):
        fileChanges.append(fileName)
  print(collections.Counter(fileChanges).most_common(5))

def getCommitsJavaLinesCount(repo):
  commits = list(repo.iter_commits('master'))
  for c in commits:
    print('Commit ' + c.message)
    count = 0
    for d in c.diff(git.NULL_TREE, create_patch=True):
      if ('.java' in str(d.a_path)):
        for line in d.diff.splitlines():
          print(line)
          if (line[0] == '+'):
            count = count + 1
        print(str(count) + ' linhas java modificadas')

def getAddedFilesByYear(repo, dateSince, dateUntil):
  commits = repo.iter_commits('master', since=dateSince, until=dateUntil)
  for c in commits:
    d = c.diff(git.NULL_TREE, create_patch=True)
    print(d)

def getAllCommits(repo):
  return len(list(repo.iter_commits('master')))

def getCommitsByYear(repo, dateSince, dateUntil):
  return len(list(repo.iter_commits('master', since=dateSince, until=dateUntil)))

def getCommitsByMsg(repo, msg):
  return len(list(repo.iter_commits('master', grep=msg)))

def getMostModifiedFiles(repo, dateSince='2000-01-01', dateUntil='2050-01-01'):
  commits = list(repo.iter_commits('master', since=dateSince, until=dateUntil))
  fileChanges = []
  for c in commits:
    for d in c.diff():
      fileName = d.a_path
      if ('.java' in fileName):
        fileChanges.append(fileName)
  print(collections.Counter(fileChanges).most_common(5))

def getMostActiveAuthorsByDate(repo, dateSince='2000-01-01', dateUntil='2050-01-01'):
  commits = list(repo.iter_commits('master', since=dateSince, until=dateUntil))

  authors = []
  for c in commits:
    authors.append(c.author.name)

  mostActive = collections.Counter(authors).most_common(3)
  for author, count in mostActive:
    print(author)

#type='+'-> added
#type='-' -> removed
def getAlteredCodeCountByText(repo, text, type='+'):
  commits = list(repo.iter_commits('master'))
  lines = []
  count = 0
  for c in commits:
    for d in c.diff(git.NULL_TREE, create_patch=True, S=text):
      for line in d.diff.splitlines():
        if(line[0] == type and text in line):
          count = count + 1

  print (count)

repo = Repo(os.getcwd() + '/EventBus')

# print("-- ITEM 01 --")
# print(getCommitNumOfFiles(repo, 0))
# print(getCommitNumOfFiles(repo, -1))

# print("-- ITEM 02 --")
# print(getCommitNumOfJavaFiles(repo, 0))
# print(getCommitNumOfJavaFiles(repo, -1))

# print("-- ITEM 03 --")
# getCommitsFileCount(repo)

# print("-- ITEM 04 --")
# getCommitsJavaFileCount(repo)

# print("-- ITEM 05 --")
# getCommitsJavaLinesCount(repo)

print("-- ITEM 06 --")
getAddedFilesByYear(repo, '2016-01-01', '2016-12-31')