import re
import sys

print("############# Code starts #############")
input1 = sys.argv[1]
print("Input1: " + input1)

# shepherd = "Martha"
# age = 34
# # Note f before first quote of string
# stuff_in_string = f"Shepherd {shepherd} is {age} years old."
# print(stuff_in_string)


# Open python file > save to string > find all instances of email > replace with *
with open(f'/Users/sajadrahmdel/Desktop/Sajad-NLP-Course/2_Text_Hider_Website/uploaded_files/{input1}') as f:
    # save file to string
    linesList = f.readlines()
    # convert list to string
    linesStr = ''.join(linesList)
    # find all instances of email
    matchEmail = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', linesStr)
    # replace with *
    for email in matchEmail:
        print('i is:', email)
        # find string before @ sign
        beforeAt = email.split('@')[0]
        linesStr = linesStr.replace(beforeAt, '*'*len(beforeAt))
    # find all instances of phone numbers: 010-2508-1486
    matchPhone = re.findall(r'\d{3}-\d{4}-\d{4}', linesStr)
    # replace with *
    for phone in matchPhone:
        # find string after - sign
        afterDash = phone.split('-')[2]
        linesStr = linesStr.replace(afterDash, '*'*len(afterDash))
    # print(linesStr)
    # save string to file
    text_file = open(f"edited_files/{input1}", "w")
    n = text_file.write(linesStr)
    text_file.close()
