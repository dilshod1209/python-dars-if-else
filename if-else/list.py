# If ga oid masalalar ishlash
# 1
# a=int(input("Sonni kiriting! = "))
# if a >=0:
#     print(a+1)
# else:
#     print(a)
 #2
# a=int(input("Sonni kiritng! = "))
# if a >=1:
#     print(a+1)
# else:
#     print(a+2)
# 3
# a=int(input("sonni kiriting! = "))
# if a>0:
#     print(a+2)
# if a<0:
#     print(a-2)
# else:
#     print(10)
#4
# a=int(input("sonni kiriting"))
# b=int(input("sonni kiriting"))
# c=int(input("sonni kiriting"))
# musbat_sonlar_soni=0
# if a>0:
#     musbat_sonlar_soni+=1
# if b>0:
#     musbat_sonlar_soni+=1
# if c>0:
#     musbat_sonlar_soni+=1
# print(f"Musbat sonlar soni:{musbat_sonlar_soni}")
    #5
# son1=int(input("1-sonni kirititng! "))
# son2=int(input("1-sonni kirititng! "))
# son3=int(input("1-sonni kirititng! "))
# musbat_sonlar_soni=0
# manfiy_sonlar_soni=0
# if son1>0:
#     musbat_sonlar_soni+=1
# else:
#     manfiy_sonlar_soni+=1
# if son2>0:
#     musbat_sonlar_soni+=1
# else:
#     manfiy_sonlar_soni+=1
# if son3>0:
#     musbat_sonlar_soni+=1
# else:
#     manfiy_sonlar_soni+=1
# print(f"musbat sonlar soni: {musbat_sonlar_soni} ta")
# print(f"musbat sonlar soni: {manfiy_sonlar_soni} ta")
    #6
# son1=int(input("1-sonni kiriting"))
# son2=int(input("2-sonni kiriting"))
# if son1>son2:
#     print(f"eng kattasi:{son1}")
# if son2>son1:
#     print(f"eng kattasi:{son2}")
    #7
# son1=int(input("1-sonni kiriting"))
# son2=int(input("2-sonni kiriting"))
# kichik_sonni_tartib_raqami=0
# if son1<son2:
#     kichik_sonni_tartib_raqami=1
# elif son2<son1:
#     kichik_sonni_tartib_raqami=2
# else:
#     kichik_sonni_tartib_raqami="sonlar teng"
# print(f"kichik sonni tartib raqami:{kichik_sonni_tartib_raqami}")
    #8
# a=int(input("son-1:"))
# b=int(input("son-2:"))
# if a>b:
#     print(f"kattasi:{a}")
# else:
#     print(f"kichik son:{a}")
# if b>a:
#     print(f"katta son:{b}")
# else:
#     print(f"kichik son {b}")
    #9
# a=int(input("a="))
# b=int(input("b="))
# if a!=b:
#     print(a+b)
# else:
#     print(04)
    #10 float haqiqiy sonlarga ishlatiladi. bu yerda qiymat almashtirlidi
# a=float(input("a="))
# b=float(input("b="))
# if a>b:
#     a,b=b,a
# print(f"Almashtirligandan keyin:a={a},b={b}")
    #11
# A=float(input("A="))
# B=float(input("B="))
# if A==B:
#     print(A)
# else:
#     print(0)
    #12
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# if a>b:
#     print("kichigi b")
# if b>a:
#     print("kichigia a")
# if a>c:
#     print("kichigi c")
# if b>c:
#     print("kichigi c")
# if c>b:
#     print("eng kichigi b")
    #13
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# if a>b>c:
#     print("eng ortanchasi:{b}")
# if b>a>c:
#     print("eng ortanchasi: {a}")
# if b>c>a:
#     print("eng ortanchasi:{c}")
# if a>c>b:
#     print("eng ortanchasi:{c}")
# if c>a>b:
#     print("eng ortanchasi:{a}")
# if c>b>a:
#     print("eng ortanchasi:{b}")
    #14
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# if a>b>c:
#     print("kichigi c")
# if b>a>c:
#     print("eng kichigi c")
# if a>c>b:
#     print("eng kichigi b")
# if c>a>b:
#     print("eng kichigi b")
# if b>c>a:
#     print("kichigi a")
# if c>b>a:
#     print("kichigi a")
# if a>b>c:
#     print("kattasi a")
# if b>a>c:
#     print("kattasi b")
# if a>c>b:
#     print("kattasi a")
# if c>a>b:
#     print("kattsi c")
# if b>c>a:
#     print("kattasi b")
# if c>b>a:
#     print("kattasi c")
    #16
# A=int(input("A="))
# B=int(input("B="))
# C=int(input("C="))
# ikkilanish_son=2
# if A>B>C:
#     ikkilanish_son*=2
#     print(f"son:{ikkilanish_son}")
# else:
#    print("A={-B},B={-B}, C={-C}")
# hayvonot bog'i dasturini tuzish
# yosh= int(input("Yoshingizni kiriting!.>>>>"))
# narh=5000
# if yosh<=4:
#     print("sizga tekin")
# elif yosh>=12:
#     print(f"sizdan {narh} som")
# yosh=int(input("yoshingizni kiriting"))
# narh=500
# if yosh<=12:
#     narh=narh
# elif yosh>12:
#     narh=narh+20000
# print(f"sizdan:{narh} som boldi")
    #or opertaratoriga dastur tuzip koramz.
# kun=input("Bugun qaysi kun?")
# if kun== 'shanba' or kun == 'yakshanba':
#     print("Bugun dam olish kuni 😁")
# else:
#     print("Bugun ish kuni essiz kech qoldim 😒")

# sotuvchi=input("Sizga nima kerak")
# if sotuvchi=="cola" or sotuvchi=='flesh':
#     print("xa bu narslar bizda bor")
# else:
#     print("Kechirasz hurmatli mijoz bizda bunday narsalar yoq!")
    # and opertaroiga misollar korsak
# kun=input("Bugun qaysi kun")
# harorat=int(input("harorat qancha"))
# if kun=="yakshanba" and harorat>=30:
#     print("ketdik chomilgani boramiz")
# elif kun=='yakshanba'and harorat<=25:
#     print("Uyda dam olamiz")
# dorixonachi=input("Sizga qanday dori kerak?>>>")
# if dorixonachi=='parasitamol' or dorixonachi=='asperin':
#     print("xa bu dorilar bizda bor")
# else:
#     print("Kechirasz bu  doridan qolmapti")
# sotuvchi=input("keling hurmatli mijoz qanday kiyimlar kerak")
# menejer=input("kiyim oldingzmi hisoblayveraymi")
# if sotuvchi=='shim' or sotuvchi=='koylak' and menejer=="xa xisoblang":
#     print("etiboringz uchun raxmat")
# else:
#     print("kechirasz adashdingz bu boshqa dokon")
# Boolean tur bilan ishllash
# narh=5000
# choy=True
# salat=False
# if choy and salat:
#     narh=narh+500
# elif choy or salat:
#     narh+5000
# print("raxmat")
# menu=['manti','choy','osh']
# ovqat=input("nima ovqat yeysiz>>>")
# if ovqat in menu:
#     print("Buyurmangiz qabul qilindi>>>")
# else:
#     print("Bizda unday ovqat yoq")
# menu=['osh']
# print('osh' not in menu)
 # Buyurtmalr tizimini ishlab koramz?
menyu=['osh','norin','xalim','gumma','pirashki']
buyurtmalr=['osh','gumma','somsa']
if buyurtmalr:
    for taom in buyurtmalr:
        if taom in menyu:
            print(f"Menyuda {taom} bor")
else:
    print("savatchangiz bosh")
    