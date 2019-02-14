#!/usr/bin/python3
# -*- coding: utf-8 -*-

#-----------Read-answers-from-md-files-------------
ask = open("../databases/answers/ask.md", "r", encoding="utf8").read()
bitcoin = open("../databases/answers/bitcoin.md", "r", encoding="utf8").read()
botinfo = open("../databases/answers/botinfo.md", "r", encoding="utf8").read()
farsi = open("../databases/answers/farsi.md", "r", encoding="utf8").read()
flood = open("../databases/answers/flood.md", "r", encoding="utf8").read()
free = open("../databases/answers/free.md", "r", encoding="utf8").read()
grub = open("../databases/answers/grub.md", "r", encoding="utf8").read()
hacker = open("../databases/answers/hacker.md", "r", encoding="utf8").read()
help_pv = open("../databases/answers/help_pv.md", "r", encoding="utf8").read()
help_pub = open("../databases/answers/help_pub.md", "r", encoding="utf8").read()
kali = open("../databases/answers/kali.md", "r", encoding="utf8").read()
lamp = open("../databases/answers/lamp.md", "r", encoding="utf8").read()
link = open("../databases/answers/link.md", "r", encoding="utf8").read()
mahak = open("../databases/answers/mahak.md", "r", encoding="utf8").read()
searx= open("../databases/answers/searx.md", "r", encoding="utf8").read()
smart = open("../databases/answers/smart.md", "r", encoding="utf8").read()
start = open("../databases/answers/start.md", "r", encoding="utf8").read()
tor = open("../databases/answers/tor.md", "r", encoding="utf8").read()
xampp = open("../databases/answers/xampp.md", "r", encoding="utf8").read()
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
    "help_pv": help_pv,
    "help_pub": help_pub,
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
