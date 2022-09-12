import requests

rawAbemaTV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/AbemaTV/AbemaTV.yaml").text
rawHuluJP = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/HuluJP/HuluJP.yaml").text
rawNiconico = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Niconico/Niconico.yaml").text
rawNikkei = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Nikkei/Nikkei.yaml").text
rawNintendo = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Nintendo/Nintendo.yaml").text
rawParavi = requests.get("https://raw.githubusercontent.com/HotKids/Rules/master/Clash/RuleSet/Paravi.yaml").text
rawPixiv = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Pixiv/Pixiv.yaml").text
rawPixnet = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Pixnet/Pixnet.yaml").text
rawTver = requests.get("https://raw.githubusercontent.com/HotKids/Rules/master/Clash/RuleSet/TVer.yaml").text
rawU_NEXT = requests.get("https://raw.githubusercontent.com/HotKids/Rules/master/Clash/RuleSet/U-NEXT.yaml").text

result = ['payload:']
for rawresult in [rawAbemaTV, rawHuluJP, rawNiconico, rawNikkei, rawNintendo, rawParavi, rawPixiv, rawPixnet, rawTver, rawU_NEXT]:
    result.extend([item.rstrip() for item in rawresult.split('\n') if not (item.startswith('#') or item.startswith('payload:'))])
result_text = '\n'.join(result)

with open("./JPmedia.yaml", "w") as f:
    f.write("\n".join(result))
