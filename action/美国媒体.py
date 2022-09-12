import requests

rawAmericasvoice = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Americasvoice/Americasvoice.yaml").text
rawBestbuy = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Bestbuy/Bestbuy.yaml").text
rawCNN = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/CNN/CNN.yaml").text
rawCrunchyroll = requests.get("https://raw.githubusercontent.com/HotKids/Rules/master/Clash/RuleSet/Crunchyroll.yaml").text
rawEspn = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Espn/Espn.yaml").text
rawFuboTV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/FuboTV/FuboTV.yaml").text
rawHBO = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/HBOUSA/HBOUSA.yaml").text
rawHuffpost = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Huffpost/Huffpost.yaml").text
rawHuluUSA = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/HuluUSA/HuluUSA.yaml").text
rawStarPlus = requests.get("https://raw.githubusercontent.com/HotKids/Rules/master/Clash/RuleSet/Star%2B%2B.yaml").text
rawSling = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Sling/Sling.yaml").text
rawNBC = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/NBC/NBC.yaml").text
rawNYPost = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/NYPost/NYPost.yaml").text
rawNYTimes = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/NYTimes/NYTimes.yaml").text
rawOreilly = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Oreilly/Oreilly.yaml").text
rawPBS = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PBS/PBS.yaml").text
rawPeacock = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Peacock/Peacock.yaml").text
rawViki = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Viki/Viki.yaml").text


result = ['payload:']
for rawresult in [rawAmericasvoice, rawBestbuy, rawCNN, rawCrunchyroll, rawEspn, rawFuboTV, rawHBO, rawHuffpost, rawHuluUSA, rawStarPlus, rawSling, rawNBC, rawNYPost, rawNYTimes, rawOreilly, rawPBS, rawPeacock, rawViki]:
    result.extend([item.rstrip() for item in rawresult.split('\n') if not (item.startswith('#') or item.startswith('payload:'))])
result_text = '\n'.join(result)

with open("./USmedia.yaml", "w") as f:
    f.write("\n".join(result))
