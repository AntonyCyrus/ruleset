import requests

rawABC = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/ABC/ABC.yaml").text

result = rawABC.split("\n")

with open("./ABC.conf", "w") as f:
    f.write("\n".join(result))
