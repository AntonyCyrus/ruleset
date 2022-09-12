import requests

rawBBC = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/BBC/BBC.yaml").text
rawBritboxUK = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/BritboxUK/BritboxUK.yaml").text
rawDailymail = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Dailymail/Dailymail.yaml").text
rawMy5 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/My5/My5.yaml").text

result = ['payload:']
for rawresult in [rawBBC, rawBritboxUK, rawDailymail, rawMy5]:
    result.extend([item.rstrip() for item in rawresult.split('\n') if not (item.startswith('#') or item.startswith('payload:'))])
result_text = '\n'.join(result)

with open("./KRmedia.yaml", "w") as f:
    f.write("\n".join(result))
