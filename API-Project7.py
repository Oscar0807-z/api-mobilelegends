from OpenMLBB import OpenMLBB

client = OpenMLBB()

# same endpoint groups as API routers
academy_data = client.academy.roles(lang="en")
mlbb_data = client.mlbb.heroes(size=10, index=1, order="desc", lang="en")

print (mlbb_data)

