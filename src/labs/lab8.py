from github import Github

# First create a Github instance:

# using username and password
g = Github("f8fc3b056882e15b6c24923b33f1b2371c376156")

r = g.get_repo("torvalds/linux")
# print("Pergunta 1:")
# languages = r.get_languages()
# for key, value in languages.iteritems():
#   print(key)

# print("Pergunta 2:")
# for rel in r.get_tags()[:10]:
#   print(rel.name)

# print("Pergunta 3:")
# u = g.get_user("torvalds")
# for repo in u.get_repos():
#   print(repo.name)

# print("Pergunta 4:")
# for repo in g.search_repositories(query='language:C')[:10]:
#   print(repo.name)
#   print(repo.stargazers_count)

# print("Pergunta 5:")
# most_forked_repos = g.search_repositories(query='language:C', sort='forks', order='desc')[:10]
# for repo in most_forked_repos:
#   print(repo.name)
#   print(repo.forks_count)

# print("Pergunta 6:")
# ms_repos = g.search_repositories(query='topic:microservices', sort='stars')[:10]
# for repo in ms_repos:
#   print(repo.name)
#   print(repo.stargazers_count)

# print("Pergunta 7:")
# html5_repos = g.search_repositories(query='topic:html5 and language:javascript', sort='stars')[:10]
# for repo in html5_repos:
#   print(repo.name)
#   print(repo.stargazers_count)

# print("Pergunta 8:")
# fn_repos = g.search_repositories(query='topic:fakenews', sort='stars')
# for repo in fn_repos:
#   print(repo.name)
#   print(repo.stargazers_count)

print("Pergunta 9:")
android_repos = g.search_repositories(query='name:android', sort='stars')[:10]
for repo in android_repos:
  print(repo.name)
  print(repo.stargazers_count)

print("Pergunta 10:")
a_repos = g.search_repositories(query='description:android+description:client', sort='stars')[:10]
for repo in a_repos:
  print(repo.name)
  print(repo.stargazers_count)

print("Pergunta 11:")
circle_repos = g.search_repositories(query='documentation:circleCI', sort='stars')[:10]
for repo in circle_repos:
  print(repo.name)
  print(repo.stargazers_count)

print("Pergunta 12:")
critical_issues_js = g.search_repositories(query='language:javascript', sort='stars')[:10]
for repo in critical_issues_js:
  label = repo.get_label("critical")
  print(repo.name)
  print(repo.stargazers_count)
  for i in repo.get_issues(labels=label):
    print(i.title)

