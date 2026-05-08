massage = input("Type your massage : ")
msg = massage.split()
Emoji = {
    ":)":"😍",
    ":()":"😞",
    ":*":"😒"
}
output = " "
for ch in msg :
    output += Emoji.get(ch,ch) + " "
print(output)