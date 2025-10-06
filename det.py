from fileinput import close
from os import waitpid
from PIL import Image
import pygame
from pygame import KEYDOWN, MOUSEWHEEL
from pygame.draw_py import draw_line

from devices.AmperMetr import Amper_Metr
from devices.IstT import Istochnik_toka
from devices.VoltMetr import Volt_Metr
from devices.reostat import Reostat1
from devices.rezis import Rezis
from devices.provod import Node1, Node2
from devices.lampa import Lampa
from devices.key import Key
from lvls import lvl_choose,lvl_act

tasks=['источник тока', 'вольтметр', 'амперметр', 'ключ', 'реостат', 'соединительные провода', 'резистор R2']
# инициализируем библиотеку Pygame
pygame.init()

# определяем размеры окна
W,H = 1500, 1000

# задаем название окна
pygame.display.set_caption("Лабораторная работа")

# создаем окно
sc = pygame.display.set_mode((W, H))

# задаем цвет фона
background_color = (255, 255, 255)
# заполняем фон заданным цветом

clock = pygame.time.Clock()
# обновляем экран для отображения изменений
pygame.display.flip()
FPS=120
# показываем окно, пока пользователь не нажмет кнопку "Закрыть"
peremeshenie=False
# im = Image.open(A.obname)
# width, height = im.size
#print(im.size)


Ist =Istochnik_toka(400, 60, 'images/result_12q.jpg')
V=Volt_Metr(600, 60, 'images/result_result_VoltMetr.png')
A = Amper_Metr(700, 60, 'images/4(140).jpg')
Reos = Reostat1(800, 100, 'images/result_qw.png')
R1= Rezis(900,600,'images/rezis.png', 10)
R2=Rezis(900,900,'images/rezis.png', 20)
lamp=Lampa(600, 900, 'images/result_lamp.png')
K=Key(400,900, 'images/key_off.jpg')
# n=Node1(80,900)
# n2=Node2(200,900)

l4=lvl_choose(125*1,180,'images/lvl4.png',4)
l5=lvl_choose(125*3,180,'images/lvl5.png',5)
l6=lvl_choose(125*5,180,'images/lvl6.png',6)
l7=lvl_choose(125*1,340,'images/lvl7.png',7)
l8=lvl_choose(125*3,340,'images/lvl8.png',8)
l00=lvl_choose(125*5,340,'images/lvl00.png',999)
lvlv=pygame.sprite.Group()
lvlvs=[l4,l5,l6,l7,l8,l00]
for i in range(len(lvlvs)):
    lvlv.add(lvlvs[i])

ll4=lvl_act(1500-320,455, 'images/llvl4.png',4,[Ist,lamp,K,A])
ll5=lvl_act(1500-320,455, 'images/llvl5.png',5,[Ist,R1,R2,lamp,K,V])
ll6=lvl_act(1500-320,455, 'images/llvl6.png',6,[Ist,Reos,K,A])
ll7=lvl_act(1500-320,455, 'images/llvl7.png',7,[Ist,R1,K,A,Reos,V])
ll8=lvl_act(1500-320,455, 'images/llvl8.png',8,[Ist,lamp,K,A,V])
ll0=lvl_act(1500-320,455, 'images/lvl00.png',999,[Ist,A,V, Reos, R1,R2,lamp,K])


llvss=[ll4,ll5,ll6,ll7,ll8,ll0]
llvs=pygame.sprite.Group()
for i in range(len(llvss)):
    llvs.add(llvss[i])

masobj=[Ist,A,V, Reos, R1,R2,lamp,K]
ms=[Ist,A,V,  Reos, R1,R2,lamp,K]
pok=[R1,R2,A,V]
objects= pygame.sprite.Group()

obj=None

# def q():
#     global masobj
#     a=masobj[0]
#     a.con1
#     masobj[0]=a
# q()
# print(masobj[0].con1)





def on_per(obj):
    #im = Image.open(obj.obname)
    global peremeshenie
    pos = pygame.mouse.get_pos()
    width, height = obj.im.size
    if pos[0] >= obj.rect[0] + 0.25 * width and pos[0] <= obj.rect[0] + 0.75 * width and pos[1] <= obj.rect[1] + height and pos[1] >= obj.rect[1]:
        peremeshenie = True
    else:
        peremeshenie = False
    return peremeshenie
def per(obj):
    # im = Image.open(obj.obname)
    width, height = obj.im.size
    global peremeshenie

    if peremeshenie:
        pos = pygame.mouse.get_pos()
        if obj in maspr or pos[0] >= obj.rect[0] + 0.25 * width and pos[0] <= obj.rect[0] + 0.75 * width and pos[1] <= obj.rect[1] + height and pos[1] >= obj.rect[1]:
            obj.rect = (pos[0] - width//2, pos[1] - height//2)
        if obj.rect[0] < 0 or obj.rect[0] + width > W or obj.rect[1] < 0 or obj.rect[1] + height > H:
            peremeshenie = False

            if obj.rect[0] < 0:
                obj.rect = (0.25*width, obj.rect[1])
            elif obj.rect[0] + width > W:
                obj.rect = (W - 1.25*width, obj.rect[1])
            elif obj.rect[1] < 0:
                obj.rect = (obj.rect[0], 0.2*height)
            elif obj.rect[1] + height > H:
                obj.rect = (obj.rect[0], H - 1.2*height)





def opred(masobj):
    pos = pygame.mouse.get_pos()
    for i in range (len(masobj)):
        act=masobj[i]
        #im = Image.open(act.obname)
        width, height = act.im.size
        if pos[0]>=act.rect[0] and pos[0]<=act.rect[0]+width and pos[1]>=act.rect[1] and pos[1]<=act.rect[1]+height:
            global obj
            obj = act
            return obj
    return None
ka=[]

def con(pr):
    #pos = pygame.mouse.get_pos()
    global masobj
    global msn
    global maspr
    cn=True
    for i in range(len(masobj)-len(msn)):
        width, height = masobj[i].im.size
        if pr.rect[0]+40>=masobj[i].rect[0] and pr.rect[0]+40<=masobj[i].rect[0]+0.25*width and pr.rect[1]>=masobj[i].rect[1] and pr.rect[1]<=masobj[i].rect[1]+height:
            if pr!= None and not (pr in masobj[i].con1):
                if len(masobj[i].con1) == 0:
                    a = masobj[i]
                    a.con1.append(pr)
                    masobj[i] = a
                    pr.con = a
                    maspr[pr.id][pr.id2] = pr
                else:
                    for j in range(len(masobj[i].con1)):
                        if masobj[i].con1[j].id == pr.id:
                            cn = False
                    if cn:
                        a = masobj[i]
                        a.con1.append(pr)
                        masobj[i] = a
                        pr.con = a
                        maspr[pr.id][pr.id2] = pr
        elif pr.rect[0]-20<=masobj[i].rect[0]+width and pr.rect[0]-20>=masobj[i].rect[0]+0.75*width and pr.rect[1]>=masobj[i].rect[1] and pr.rect[1]<=masobj[i].rect[1]+height:
            if pr!= None and not (pr in masobj[i].con2):
                if len(masobj[i].con2)==0:
                    a=masobj[i]
                    a.con2.append(pr)
                    masobj[i] = a
                    pr.con = a
                    maspr[pr.id][pr.id2] = pr
                else:
                    for j in range(len(masobj[i].con2)):
                        if masobj[i].con2[j].id == pr.id:
                            cn=False
                    if cn:
                        a=masobj[i]
                        a.con2.append(pr)
                        masobj[i] = a
                        pr.con = a
                        maspr[pr.id][pr.id2] = pr

def discon(obj,maspr, mas):
    pos = pygame.mouse.get_pos()
    #if obj in mas:

    if obj!=None and obj in mas:
        width, height = obj.im.size
        if pos[0]>=obj.rect[0] and pos[0]<=obj.rect[0]+0.25*width and pos[1]>=obj.rect[1] and pos[1]<obj.rect[1]+height:
            pr=obj.con1
            for i in range(len(pr)):
                a=pr[i]
                a.con=None
                maspr[a.id][a.id2]=a
                a.rect=(a.rect[0]-40, a.rect[1]+a.im.size[1]/2)
            obj.con1=[]
        elif pos[0] <= obj.rect[0]+width and pos[0] >= obj.rect[0] + 0.75 * width and pos[1] >= obj.rect[1] and pos[1] < obj.rect[1] + height:
            pr = obj.con2
            for i in range(len(pr)):
                a = pr[i]
                a.con = None
                maspr[a.id][a.id2] = a
                a.rect=(a.rect[0]+50, a.rect[1]+a.im.size[1]/2)
            obj.con2 = []
    elif obj!=None and obj in maspr[obj.id]:
        width, height = obj.im.size
        ob=obj.con
        obj.con = None
        if obj.rect[0]<=ob.rect[0]:
            ob.con1=[]
            obj.rect = (obj.rect[0] - 40, obj.rect[1] + height / 2)
        else:
            ob.con2=[]
            obj.rect = (obj.rect[0] + 50, obj.rect[1]+height/2)




#
# def zamk():
#     global masobj
#     global maspr
#     global msn
#     act=masobj[0].con1
#     closelist=[]
#     erre = 1
#     while  act!=masobj[0]:
#         if act!=None and (act in msn):
#             print(1)
#             for i in range(len(maspr[act.id])):
#                 if act==maspr[i]:
#                     if i==1:
#                         act=maspr[act.id][0].con
#                     else:
#                         act=maspr[act.id][1].con
#         if type(act)== 'list':
#             print(121)
#             act=act[0].con2
#         else:
#             erre=1
#             break
#
#     if erre ==0:
#         print(0)
#         return True
#     else:
#
#         return False

def zamk(array_objects):
    for i in range(len(array_objects)):
        if len(array_objects[i].con1) == 0 and len(array_objects[i].con2) == 0 and array_objects[i] == Ist:
            return False
        elif (len(array_objects[i].con1) > 0 and len(array_objects[i].con2) == 0) or (len(array_objects[i].con1) == 0 and len(array_objects[i].con2) > 0):
            return False
        # elif masobj[i].con1[0].con==None or masobj[i].con2[0].con==None:
        #     return False
    return True




def schema(mas, prmas):
    wait=[]
    act=0
    b=0

    for i in range(len(mas)):
        if len(mas[i].con1) >0 and len(mas[i].con2)>0:
            wait.append(mas[i])
        if mas[i]==Ist:
            b=Ist
    shem=[]
    act = mas[0]
    a=0
    pred=0
    i=0
    while True:
        # if pred==0 or act.con2[0].id==pred.con1[0].id:
            #print(1)
        if len(act.con2)==1:
            if act.con2[0].id2==0:
                #print(10)
                if act.con2[0].id == prmas[act.con2[0].id][1].con.con1[0].id:
                    pr=prmas[act.con2[0].id][1]
                    act=pr.con
                    #print(11)
                else:
                    pr = prmas[act.con2[0].id][1].con.con1[0]
                    act = pr.con
                    #print(21)

            else:
                #print(20)
                if act.con2[0].id == prmas[act.con2[0].id][0].con.con1[0].id:
                    pr = prmas[act.con2[0].id][0]
                    act = pr.con
                    #print(12)
                else:
                    pr = prmas[act.con2[0].id][0].con.con1[0]
                    act = pr.con
        # elif len(act.con2)>1:
        #     for i in range(len(act.con2)):
        #         if act.con2[i].id2==1:
        #             if prmas[act.con2[i].id][0].con==Volt_Metr:
        #                 print(1)
        #                 if i ==1:
        #                     if act.con2[0].id2==0:
        #                         pr = prmas[act.con2[0].id][1].con.con1[0]
        #                         act=pr.con
        #                         break
        #                     else:
        #                         pr = prmas[act.con2[0].id][0].con.con1[0]
        #                         act = pr.con
        #                         break
        #                 else:
        #                     if act.con2[1].id2==0:
        #                         pr = prmas[act.con2[1].id][1].con.con1[0]
        #                         act=pr.con
        #                         break
        #                     else:
        #                         pr = prmas[act.con2[1].id][0].con.con1[0]
        #                         act = pr.con
        #                         break
        #             else:
        #                 if act.con2[i].id2==0:
        #                     pr = prmas[act.con2[i].id][1].con.con1[0]
        #                     act=pr.con
        #                     break
        #                 else:
        #                     pr = prmas[act.con2[i].id][0].con.con1[0]
        #                     act = pr.con
        #                     break
        #         else:
        #             if prmas[act.con2[i].id][1].con==Volt_Metr:
        #                 if i ==1:
        #                     if act.con2[0].id2==0:
        #                         pr = prmas[act.con2[0].id][1].con.con1[0]
        #                         act=pr.con
        #                         break
        #                     else:
        #                         pr = prmas[act.con2[0].id][0].con.con1[0]
        #                         act = pr.con
        #                         break
        #                 else:
        #                     if act.con2[1].id2==1:
        #                         pr = prmas[act.con2[1].id][0].con.con1[0]
        #                         act=pr.con
        #                         break
        #                     else:
        #                         pr = prmas[act.con2[1].id][1].con.con1[0]
        #                         act = pr.con
        #                         break
        #             else:
        #                 if act.con2[i].id2==1:
        #                     pr = prmas[act.con2[i].id][0].con.con1[0]
        #                     act=pr.con
        #                     break
        #                 else:
        #                     pr = prmas[act.con2[i].id][1].con.con1[0]
        #                     act = pr.con
        #                     break
        #     shem[-1].append(Volt_Metr)
            # print(1)
            # if act.con2[0].id2==0:
            #     print(2)
            #     if prmas[act.con2[0].id][1].con==Volt_Metr:
            #         print(3)
            #         if act.con2[1].id == prmas[act.con2[1].id][1].con.con1[0].id:
            #             pr = prmas[act.con2[1].id][1]
            #             act = pr.con
            #             print(31)
            #         else:
            #             pr = prmas[act.con2[1].id][1].con.con1[0]
            #             act = pr.con
            #             print(32)
            #     else:
            #         print(4)
            #         if act.con2[0].id == prmas[act.con2[0].id][1].con.con1[0].id:
            #             pr = prmas[act.con2[0].id][1]
            #             act = pr.con
            #             # print(11)
            #             print(41)
            #         else:
            #             pr = prmas[act.con2[0].id][1].con.con1[0]
            #             act = pr.con
            #             print(42)
            # else:
            #     print(5)
            #     if prmas[act.con2[0].id][0].con == Volt_Metr:
            #         print(6)
            #         if act.con2[1].id == prmas[act.con2[1].id][0].con.con1[0].id:
            #             pr = prmas[act.con2[1].id][0]
            #             act = pr.con
            #             print(61)
            #         else:
            #             pr = prmas[act.con2[1].id][0].con.con1[0]
            #             act = pr.con
            #             print(62)
            #     else:
            #         print(7)
            #         if act.con2[0].id == prmas[act.con2[0].id][0].con.con1[0].id:
            #             pr = prmas[act.con2[0].id][0]
            #             act = pr.con
            #             print(71)
            #             # print(11)
            #         else:
            #             print(72)
            #             pr = prmas[act.con2[0].id][0].con.con1[0]
            #             act = pr.con


                    #print(22)
        # elif act.con1[0].id==pred.con2[0].id:
        #     print(2)
        #     if len(act.con1) == 1:
        #         if act.con1[0].id2 == 0:
        #             print(10)
        #             if act.con1[0].id == prmas[act.con1[0].id][1].con.con2[0].id:
        #                 pr = prmas[act.con1[0].id][1]
        #                 act = pr.con
        #                 print(11)
        #             else:
        #                 pr = prmas[act.con1[0].id][1].con.con2[0]
        #                 act = pr.con
        #                 print(21)
        #
        #         else:
        #             print(20)
        #             if act.con1[0].id == prmas[act.con1[0].id][0].con.con2[0].id:
        #                 pr = prmas[act.con1[0].id][0]
        #                 act = pr.con
        #                 print(12)
        #             else:
        #                 pr = prmas[act.con1[0].id][0].con.con2[0]
        #                 act = pr.con
        #                 print(22)
        if act == mas[0]:
            break
        shem.append([act])
        #print(shem)
        #i=i+1
        #pred=wait[i-1]
        if act == mas[0]:
            break

        #print(pr)
    return shem


provoda= pygame.sprite.Group()
class provod():
    def __init__(self,n,n2):
        self.con1=n.con
        self.con2=n2.con


msn=[]
maspr=[]
for i in range(5):
    ni = Node1(80, 900-30*i, i,0)
    n2i = Node2(200, 900-30*i, i,1)
    maspr.append([ni,n2i])
    masobj.append(ni)
    masobj.append(n2i)
    msn.append(ni)
    msn.append(n2i)


lvl=None
wew=0
waw=1
wq=1
sh=[]
reos_r_prosh=Reos.R
R0=0
ot=True
kprz=False
for i in range(len(masobj)):
    objects.add(masobj[i])
#A.con1.append(maspr[4][1])
ak=0
while True:
    for event in pygame.event.get():
        pressed = pygame.mouse.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            obj = opred(masobj)
            pos = pygame.mouse.get_pos()
            #n2.rect = pos
            if obj != None:
                peremeshenie = on_per(obj)
            else:
                obj=opred(lvlvs)
                if obj!= None:
                    lvl=obj.nom
                    for i in range(len(llvss)):
                        if llvss[i].nom==lvl:
                            objects.empty()
                            llvl=llvss[i]
                            ms = llvl.objectsss
                            u=len(ms)
                            masobj=llvl.objectsss
                            #print(ms)
                            maspr=[]
                            msn=[]
                            for i in range(8):
                                ni = Node1(80, 900 - 30 * i, i, 0)
                                n2i = Node2(200, 900 - 30 * i, i, 1)
                                maspr.append([ni, n2i])
                                masobj.append(ni)
                                masobj.append(n2i)
                                msn.append(ni)
                                msn.append(n2i)
                            for i in range(len(masobj)):
                                objects.add(masobj[i])
                            k=[]
                            for i in range(u):
                                k.append(ms[i])
                            ms=k
                            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if opred(masobj)==K:
                if K.zaamk==True:
                    K.zaamk=False
                    K.image = pygame.image.load('images/key_off.jpg').convert_alpha()
                else:
                    K.zaamk=True
                    K.image = pygame.image.load('images/key_on.jpg').convert_alpha()
        elif event.type == pygame.MOUSEMOTION:
            obj = opred(masobj)
            if obj !=None:
                if obj in msn:
                    #print(1)
                    per(obj)
                    con(obj)
                else:
                    per(obj)
            pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            #print(A.rect)
            peremeshenie=False
            #print(peremeshenie)
        elif event.type == pygame.MOUSEWHEEL  and event.y == 1 and opred(masobj)==Reos:
            Reos.izmR(4)
        elif event.type == pygame.MOUSEWHEEL and event.y == -1 and opred(masobj)==Reos:
            Reos.izmR(5)
        elif pressed[0] and pressed[1] and pressed[2]:
            print('Обдурили!!!')
            pygame.quit()
            exit()
        elif event.type == KEYDOWN and event.key== pygame.K_q:
            discon(opred(masobj), maspr,ms)
        elif event.type == KEYDOWN and event.key == pygame.K_w:
            obj=opred(masobj)
            if obj!=None:
                obj.ot=True
        elif event.type == KEYDOWN and event.key == pygame.K_e:
            obj=opred(masobj)
            if obj!=None:
                obj.ot=False
    if lvl != None:
        sc.fill(background_color)


        objects.draw(sc)
        #pygame.draw.line(sc, (255, 255,0), (n.rect[0]+n.im.size[0]/2,n.rect[1]+n.im.size[1]/2),(n2.rect[0]+n2.im.size[0]/2,n2.rect[1]+n2.im.size[1]/2), 7)
        for i in range(len(maspr)):
            pygame.draw.line(sc, (255, 255, 0), (maspr[i][0].rect[0] + maspr[i][0].im.size[0] / 2, maspr[i][0].rect[1] + maspr[i][0].im.size[1] / 2),
                             (maspr[i][1].rect[0] + maspr[i][1].im.size[0] / 2, maspr[i][1].rect[1] + maspr[i][1].im.size[1] / 2), 7)
        for i in range(len(ms)):
            #print(len(ms[i].con1))
            if len(ms[i].con1)>0:
                for j in range(len(ms[i].con1)):
                    ms[i].con1[j].rect=(ms[i].rect[0]-20,ms[i].rect[1]+ms[i].im.size[1]/2-10)
            if len(ms[i].con2) > 0:
                for j in range(len(ms[i].con2)):

                    ms[i].con2[j].rect = (ms[i].rect[0]+ms[i].im.size[0], ms[i].rect[1] + ms[i].im.size[1] / 2 - 10)
        #R1.inf(sc)
        for i in range(len(pok)):
            pok[i].inf(sc)

        if peremeshenie==False:
            pr=None
        if zamk(ms)==False:
            wq=1
        if (zamk(ms) and wq==1) or (Reos.R != reos_r_prosh and zamk(ms)) or (zamk(ms) and kprz != K.zaamk):
            reos_r_prosh=Reos.R
            #print(1)
            wq=0
            sh=schema(ms,maspr)
            wew=0
            for i in range(len(sh)):
                if K == sh[i][0]:
                    wew=1
                    if K.zaamk==True:

                        for i in range(len(sh)):
                            R0=R0+sh[i][0].R
                        for i in range(len(sh)):
                            if len(sh[i])==1:
                                sh[i][0].I=Ist.U/R0
                                sh[i][0].U=sh[i][0].I*sh[i][0].R
                            else:
                                for j in range(len(sh[i])):
                                    if sh[i][j]!=0:
                                        R1=R1+1/sh[i][j]
                                for j in range(len(sh[i])):
                                    sh[i][0]=sh[i][1]=R1*Ist.U*R0
                            #print(Volt_Metr.U)
                        R0=0
                    else:
                        R0 = 0
                        for i in range(len(sh)):
                            for j in range(len(sh[i])):
                                sh[i][j].I = 0
                                sh[i][j].U = 0
                    kprz = K.zaamk
            if wew !=1:
                for i in range(len(sh)):
                    R0 = R0 + sh[i][0].R
                for i in range(len(sh)):
                    if len(sh[i]) == 1:
                        sh[i][0].I = Ist.U / R0
                        sh[i][0].U = sh[i][0].I * sh[i][0].R
                    else:
                        for j in range(len(sh[i])):
                            if sh[i][j] != 0:
                                R1 = R1 + 1 / sh[i][j]
                        for j in range(len(sh[i])):
                            sh[i][0] = sh[i][1] = R1 * Ist.U * R0
                    # print(Volt_Metr.U)
                R0 = 0
        else:
            for i in range(len(sh)):
                if K == sh[i][0]:
                    if K.zaamk==False or wq==1:
                        R0=0
                        for i in range(len(sh)):
                            for j in range(len(sh[i])):
                                sh[i][j].I = 0
                                sh[i][j].U = 0
        sc.blit(llvl.image, llvl.rect)
        if lamp.I>0:
            #print(1)
            ak=1
            lamp.imw='images/On_lamp.png'
            lamp.image = pygame.image.load('images/On_lamp.png').convert_alpha()
        # elif lamp.I==0 and lamp.imw=='images/On_lamp.png':
        else:
            #print(0)
            ak=0
            lamp.imw='images/result_lamp.png'
            lamp.image = pygame.image.load('images/result_lamp.png').convert_alpha()

    else:
        sc.fill(background_color)

        lvlv.draw(sc)
        f = pygame.font.Font(None, 44)
        sc_text = f.render('Выбор лабораторной работы', 1, (0, 0, 0))
        posi = sc_text.get_rect(center=(1000, 200))
        sc.blit(sc_text, posi)
        f = pygame.font.Font(None, 44)
        sc_text = f.render(' (нажмите на клетку с названием чтобы выбрать)', 1, (0, 0, 0))
        posi = sc_text.get_rect(center=(1110, 240))
        sc.blit(sc_text, posi)


    pygame.display.update()
    clock.tick(FPS)
