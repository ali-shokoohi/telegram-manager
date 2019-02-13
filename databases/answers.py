#!/usr/bin/python3

#-----------Read-answers-from-md-files-------------
ask = open("../databases/answers/ask.md", "r").read()
bitcoin = open("../databases/answers/bitcoin.md", "r").read()
botinfo = open("../databases/answers/botinfo.md", "r").read()
farsi = open("../databases/answers/farsi.md", "r").read()
flood = open("../databases/answers/flood.md", "r").read()
free = open("../databases/answers/free.md", "r").read()
grub = open("../databases/answers/grub.md", "r").read()
hacker = open("../databases/answers/hacker.md", "r").read()
help = open("../databases/answers/help.md", "r").read()
kali = open("../databases/answers/kali.md", "r").read()
lamp = open("../databases/answers/lamp.md", "r").read()
link = open("../databases/answers/link.md", "r").read()
mahak = open("../databases/answers/mahak.md", "r").read()
searx= open("../databases/answers/searx.md", "r").read()
smart = open("../databases/answers/smart.md", "r").read()
start = open("../databases/answers/start.md", "r").read()
tor = open("../databases/answers/tor.md", "r").read()
xampp = open("../databases/answers/xampp.md", "r").read()
#--------------------------------------------------

answers = {
    "ask": ask,
    "bitcoin": bitcoin,
    "botinfo": botinfo,
    "farsi": farsi,
    "flood": flood,
    "free": free,
    "grub": grub,
    "hacker": hacker,
    "help": help,
    "kali": kali,
    "lamp": lamp,
    "link": link,
    "mahak": mahak,
    "searx": searx,
    "smart": smart,
    "start": start,
    "tor": tor,
    "xampp": xampp,
}