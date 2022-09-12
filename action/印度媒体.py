import requests

rawHotstar = requests.get("https://raw.githubusercontent.com/HotKids/Rules/master/Clash/RuleSet/Hotstar.yaml").text
rawZeeTV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/ZeeTV/ZeeTV.yaml").text

result = ['payload:']
for rawresult in [rawHotstar, rawZeeTV]:
    result.extend([item.rstrip() for item in rawresult.split('\n') if not (item.startswith('#') or item.startswith('payload:'))])
result_text = '\n'.join(result)

with open("./INmedia.yaml", "w") as f:
    f.write("\n".join(result))
