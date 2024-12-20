import re
word="Simple regular expression pushpa example regular spushpatatement regular expression module"
result=re.findall("pushpa",word)
print(result,len(result))

space=re.search('\s',word)
print("\n The first space is at",space.start())
