import re


print("############# Code starts #############")

# fave_language = "Python"
# print(fave_language)

# Open python file > save to string > find all instances of email > replace with *
with open('/Users/sajadrahmdel/Desktop/Sajad-NLP-Course/2_Text_Hider_Website/text_12345.txt') as f:
    # save file to string
    linesList = f.readlines()
    # convert list to string
    linesStr = ''.join(linesList)
    # find all instances of email
    matchEmail = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', linesStr)
    # replace with *
    for i in matchEmail:
        linesStr = linesStr.replace(i, '*'*len(i))
    # find all instances of phone numbers: 010-2508-1486
    matchPhone = re.findall(r'\d{3}-\d{4}-\d{4}', linesStr)
    # replace with *
    for i in matchPhone:
        linesStr = linesStr.replace(i, '*'*len(i))

    print(linesStr)
