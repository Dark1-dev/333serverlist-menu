import requests
import json

queryurl = "https://master.333networks.com/json"
gamename = "deusex"
serverlist = requests.get(f"{queryurl}/{gamename}").json()

print("<openbox_pipe_menu>")
for i in serverlist[0]:
  print(f"<item label=\"{i['hostname'][:18]}\t{i['numplayers']}/{i['maxplayers']}\" />")
print("</openbox_pipe_menu>")
