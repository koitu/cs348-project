import requests
from random import randint

# number of accounts to generate
n = 25

accounts = []
users = []

url = f"https://randomuser.me/api/?results={n}&password=upper,lower,number,12-24"
response = requests.get(url)
assert(response.status_code == 200)

body = response.json()
results = body.get("results")
assert(results is not None)

for r in results:
    id = randint(1, 100000)
    accounts.append((
        id,
        r["login"]["username"],
        r["email"],
        r["login"]["password"],
    ))
    users.append((
        id,
        r["name"]["first"] + " " + r["name"]["last"],
        r["picture"]["thumbnail"],
    ))

with open("account.sql", "w") as f:
    f.write("INSERT INTO Account VALUES\n\t")
    f.write(",\n\t".join(str(a) for a in accounts))
    f.write("\n")

with open("user.sql", "w") as f:
    f.write("INSERT INTO User VALUES\n\t")
    f.write(",\n\t".join(str(a) for a in users))
    f.write("\n")
