import os

if not os.path.exists("/tmp/prs"):
    os.mkdir("/tmp/prs")

with open("/tmp/prs/abc.json", "w") as file:
    file.write("{'a':1}")
    file.close()

print("Done")