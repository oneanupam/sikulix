import re

Settings.OcrTextSearch = True
Settings.OcrTextRead = True

currentRegion = Screen(0)

resultObtained = currentRegion.text()
result = resultObtained.encode("utf-8")
#index = result.find("anupam")
print(result)

if(re.search("anupam", result, re.IGNORECASE)):
    print("Keyword found.")
else:
    print("Keyword not found")
