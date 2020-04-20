from tkinter import *

root = Tk()
root.title('TFT Auto Roller')
var = IntVar()
var2 = IntVar()
root.iconphoto(False,PhotoImage(file='img/tft-icon.png'))


comps = ['Dark Stars\n(Jarvan IV,Ashe,Shaco,Lux,Karma,Jhin,Lulu,Xerath)',
        'Mech Infiltrators\n(Annie,KaiSa,Lux,Rumble,Shaco,Fizz,Kayle,Ekko)',
        'Star Guardian Sorcerers\n(Zoe,Ahri,Lux,Neeko,Syndra,Soraka,Velkoz,Xerath)',
        'Brawler Blasters\n(Malphite,Blitzcrank,Lucian,Ezreal,Vi,Chogat,Jinx,Miss Fortune)',
        'Chrono Bladermasters\n(Xayah,Shen,Ezreal,Kassadin,Kayle,Wukong,Miss Fortune,Thresh)',
        'Protector Mystics\n(Jarvan IV,Rakan,Sona,Xin Zhao,Karma,Neeko,Soraka,Lulu']

for i in range(len(comps)):
    R1 = Radiobutton(root, text=comps[i], variable=var, value=i,padx=20)
    R1.pack( anchor = W)

w = Label(root, text="Gold Limit",)
w.pack(padx=5, pady=10, side=LEFT)
w =Radiobutton(root, text="10", variable=var2, value=1,)
w.pack(padx=5, pady=20, side=LEFT)
w =Radiobutton(root, text="20", variable=var2, value=2,)
w.pack(padx=5, pady=20, side=LEFT)
w =Radiobutton(root, text="30", variable=var2, value=3,)
w.pack(padx=5, pady=20, side=LEFT)
w =Radiobutton(root, text="40", variable=var2, value=4,)
w.pack(padx=5, pady=20, side=LEFT)
w =Radiobutton(root, text="All", variable=var2, value=5,)
w.select()
w.pack(padx=5, pady=20, side=LEFT)

B = Button( text ="Start ROLL", command = None)
B.pack(padx=5, pady=20, side=LEFT)

label = Label(root)
label.pack()
root.mainloop()