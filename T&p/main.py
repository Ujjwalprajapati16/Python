input1 = "Fi_er"
input2 = "Fever:filer:Filter:Fixer:Fiber:tailor:offer"

index = input1.find("_")
words = input2.upper().split(":")
res = ""

for word in words:
    temp = input1.upper()
    ch = word[index]
    temp = temp.replace("_", ch)
    if temp == word:
        if res == "":
            res = word
        else :
            res = res + ":" + word

print(res)
