import requests

rawJOOX = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/JOOX/JOOX.yaml").text
rawMOOV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/MOOV/MOOV.yaml").text
rawmyTVSUPER = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/myTVSUPER/myTVSUPER.yaml").text
rawNowE = requests.get("https://raw.githubusercontent.com/AntonyCyrus/Rule/main/NowE.yaml").text
rawPCCW = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PCCW/PCCW.yaml").text
rawTVB = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TVB/TVB.yaml").text

result = ['payload:']
for rawresult in [rawJOOX, rawMOOV, rawmyTVSUPER, rawNowE, rawPCCW, rawTVB]:
    result.extend([item.rstrip() for item in rawresult.split('\n') if not (item.startswith('#') or item.startswith('payload:'))])
result_text = '\n'.join(result)

with open("./HKmedia.yaml", "w") as f:
    f.write("\n".join(result))
