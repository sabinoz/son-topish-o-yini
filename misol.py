import random

def sontop(x=10):
    a = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
    c = 0
    while True:
        b = int(input(">>>"))
        c += 1
        if a > b:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:")         
        elif a < b:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:")    
        else:
            break
    print(f"Tabriklaymiz. {c} ta taxmin bilan topdingiz!")        
    return c


def sontop_pc(x = 10):
    input(f"Biror bir 1 dan {x} songacha sonni o'ylang, Men topishga harakat qilaman!\nO'ylagan bo'lsangiz biror bir tugmani bosing!")
    start = 1
    end = x
    c = 0
    while True:
        c += 1
        if start != end:
            taxmin = random.randint(start, end)
        else:
            taxmin = end
        javob = input(f"{taxmin} sonni o'yladingiz: to'g'ri (t),\nMen o'ylagan son bundan kattaroq bo'lsa (+), yoki kichikroq bo'lsa(-)".lower()) 
        if javob == "-":
            end -= 1
        elif javob == "+":
            start += 1
        else:
            break
    print(f"Men {c} ta taxmin bilan topdim!")
    return c     
            
def play(x = 10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user > taxminlar_pc:
            print("Men yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print("Siz yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaysizmi? Ha(1)/ Yo'q(0): "))    