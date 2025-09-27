text = """
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
print(text)
text=text.strip()
print(text)
text=text.lower()
print(text)
text=text.replace("!",".")
print(text)
text=text.strip().lower()
# print(text)
text =text.replace('!','.')
# print(text)
f = text.split('.')
for i in range(len(f)):
    f[i] = f[i].strip()
    if f[i]=='': f.remove(f[i])
print(f)
first = f[0].split()
print(first)
print(text.count('python'))
start = f[0].startswith("python")
end = f[0].endswith("language")
print(start, end)
print(len(text), text.count('f'), text.find("data"))
words = text.replace('.','').replace(',','').split()
print(words)
newText = ''
for i in words:
    newText += i + '-'
newText=newText[:-1]
d = {}
for i in newText.split('-'):
    if i not in d:
        d[i] = newText.count(i)
print(d)

def clean(text):
    return text.replace('.','').replace(',','').replace('!','').replace('?','').lower().strip()
print(clean('   Hi, Misha      '))
