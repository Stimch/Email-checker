mail = input("Write down your e-mail...")
a = input("Are you sure, that all is right?(Y/N)")
base = ["a", 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
if a == "Y":
    print("OK")
elif a == "N":
    mail = input("Write your e-mail again..")
else:
    print("Error!")
    print("Reset this program")
def ss(word, n):
    found = False
    for i in word:
        if i == n:
            found = True
            break
    return found
s1 = ss(mail, "@")
print(s1)

def prev(word):
    list = []
    for i in word:
        list.append(i)
    if (list[list.index('@') - 1]) in base:
        return("True")
    else:
        return('Error!')
print(prev(mail))

def end(word):
    s = []
    ends = ['mail.ru', 'inbox.ru', 'gmail.com', 'yandex.ru', 'bk.ru', 'hotmail.com', 'live.com']
    for i in word:
        s.append(i)
    if word[(s.index('@') + 1):] in ends: #не доделано! доделай!
        return("True, your e-mail is right!")
    else:
        return('Error!')
        return(word[(s.index('@')):]) #додумай насчет этого
print(end(mail))
