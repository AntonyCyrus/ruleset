import requests

rawNaver = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Naver/Naver.yaml").text
rawNaverTV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/NaverTV/NaverTV.yaml").text
rawPandoraTV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PandoraTV/PandoraTV.yaml").text

result = ['payload:']
for rawresult in [rawNaver, rawNaverTV, rawPandoraTV]:
    result.extend([item.rstrip() for item in rawresult.split('\n') if not (item.startswith('#') or item.startswith('payload:'))])
result_text = '\n'.join(result)

with open("./KRmedia.yaml", "w") as f:
    f.write("\n".join(result))
