import requests

rawDiscord = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/DiscoveryPlus/DiscoveryPlus.yaml").text
rawFacebook = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Facebook/Facebook.yaml").text
rawInstagram = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Instagram/Instagram.yaml").text
rawKakaoTalk = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/KakaoTalk/KakaoTalk.yaml").text
rawLine = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Line/Line.yaml").text
rawPinterest = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Pinterest/Pinterest.yaml").text
rawPotatoChat = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PotatoChat/PotatoChat.yaml").text
rawReddit = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Reddit/Reddit.yaml").text
rawSnap = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Snap/Snap.yaml").text
rawStackexchange = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Stackexchange/Stackexchange.yaml").text
rawTumblr = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Tumblr/Tumblr.yaml").text
rawTwitter = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Twitter/Twitter.yaml").text
rawVK = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/VK/VK.yaml").text
rawWhatsapp = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Whatsapp/Whatsapp.yaml").text

result = ['payload:']
for rawresult in [rawDiscord, rawFacebook, rawInstagram, rawKakaoTalk, rawLine, rawPinterest, rawPotatoChat, rawReddit, rawSnap, rawStackexchange, rawTumblr, rawTwitter, rawVK, rawWhatsapp]:
    result.extend([item.rstrip() for item in rawresult.split('\n') if not (item.startswith('#') or item.startswith('payload:'))])
result_text = '\n'.join(result)

with open("./Socialmedia.yaml", "w") as f:
    f.write("\n".join(result))
