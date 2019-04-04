from git import Repo
import os
import git

def normalizeFile(filename, old_string="\t", new_string=" "):
  # Safely read the input filename using 'with'
  with open(filename) as f:
      s = f.read()
      if old_string not in s:
        print('"{old_string}" not found in {filename}.'.format(**locals()))
        return

  # Safely write the changed content, if found in the file
  with open(filename, 'w') as f:
    print('Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
    s = s.replace(old_string, new_string)
    f.write(s)

def getFileMetrics(path):
  normalizeFile(path)
  f = open(path)
  lines = f.readlines()
  cta = 0
  lineCount = 0
  mca = 0
  for l in lines:
    # print(l)
    lineCount = lineCount + 1
    tabsCount = 0
    for index, c in enumerate(l):
      if (c != ' '):
        tabsCount = index
        cta = cta + tabsCount
        if (tabsCount > mca):
          mca = tabsCount
        break
    # print(str(tabsCount) + " espacos encontrados")
  cra = float(cta) / float(lineCount)
  return cta, cra, mca

def getLastCommit(repo):
  commits = list(repo.iter_commits('master'))
  commit = commits[0]
  return commit

def getFileCountByCommit(repo, commit, type=None):
  index = repo.index
  index.reset(commit)
  co = index.checkout(force=True)

  count = 0
  for file in co:
    if(type is None or type in file):
      count += 1

  return count

def getCommitMetrics(commit):
  index = repo.index
  index.reset(commit)
  co = index.checkout(force=True)

  maxCta = 0
  maxCra = 0
  maxMca = 0

  for file in co:
    print(file)
    cta, cra, mca = getFileMetrics("EventBus/" + file)
    if (cta > maxCta):
      maxCta = cta
      ctaFile = file
    if (cra > maxCra):
      maxCra = cra
      craFile = file
    if (mca > maxMca):
      maxMca = mca
      mcaFile = file

  print('O arquivo ' + ctaFile + ' possui o maior CTA neste commit (' + str(maxCta) + ')')
  print('O arquivo ' + craFile + ' possui o maior CRA neste commit (' + str(maxCra) + ')')
  print('O arquivo ' + mcaFile + ' possui o maior MCA neste commit (' + str(maxMca) + ')')

repo = Repo(os.getcwd() + '/EventBus')

lastCommit = getLastCommit(repo)
getCommitMetrics(lastCommit)

# inplace_change(os.getcwd() + "/teste.py",  '\t', ' ')
