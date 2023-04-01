#字串運算
s ="Hell\"o" #跳脫
print(s)

s = "Hello" "World"  #"Hello"+"World"
print(s)

s="Hello\n World" #換行
s="""Hello
World""" #換行 一定要有三個雙引號
print(s)

#字串會對內部的字元編號(索引)，從0開始算起
s="Hello"
print(s[1:]) #從開頭算起取得後面的所有字
print(s[:4]) #不要結尾取得前面所有的字