class CLanguage:
    def __init__ (self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    def say(self):
        print("我正在学Python")

clangs = CLanguage()
if hasattr(clangs,"name"):
    print(hasattr(clangs.name,"__call__"))
print("----------")
if hasattr(clangs,"say"):
    print(hasattr(clangs.say,"__call__"))