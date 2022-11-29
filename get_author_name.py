import json
import requests
import os

pr_number = int(os.environ["PR_NUMBER"])

r = requests.get(f"https://api.github.com/repos/manishpjt/wysa-assesment/pulls/{pr_number}/commits")
result = json.loads(r.text)[0]
print(result["commit"]["author"]["name"])