from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
import sqlite3 as sql
def WA():
    global xplace,yplace,spawnmap,xp,energy,cuteness,skinpos,health
    if spawnmap[yplace-1][xplace-1] != "barrier" and skinlist[len(skinlist)-1][1]!= 2:
        if energy > 0 and health > 0:
            xplace = xplace - 1
            yplace = yplace - 1
            xp = xp + 1 * cuteness
            energy = energy - 1
        else:
            xplace = xplace - 1
            yplace = yplace - 1
            xp = xp + 1 * cuteness
            health = health - 2
    else:
        if skinlist[skinpos][1]== 2 and spawnmap[yplace-1][xplace-1] != "barrier":
            xplace = xplace - 1
            yplace = yplace - 1
    timeadd()
    mapupdate()
    statsupdate()
def W():
    global xplace,yplace,xp,energy,cuteness,skinpos,health
    if spawnmap[yplace-1][xplace] != "barrier" and skinlist[len(skinlist)-1][1]!= 2:
        if energy > 0 and health > 0:
            yplace = yplace - 1
            xp = xp + 1 * cuteness
            energy = energy - 1
        else:
            yplace = yplace - 1
            xp = xp + 1 * cuteness
            health = health - 2
    else:
        if skinlist[skinpos][1]== 2 and spawnmap[yplace-1][xplace] != "barrier":
            yplace = yplace - 1
    timeadd()
    mapupdate()
    statsupdate()
def WD():
    global xplace,yplace,xp,energy,cuteness,skinpos,health
    if spawnmap[yplace-1][xplace+1] != "barrier" and skinlist[len(skinlist)-1][1]!= 2:
        if energy > 0 and health > 0:
            xplace = xplace + 1
            yplace = yplace - 1
            xp = xp + 1 * cuteness
            energy = energy - 1
        else:
            xplace = xplace + 1
            yplace = yplace - 1
            xp = xp + 1 * cuteness
            health = health - 2
    else:
        if skinlist[skinpos][1]== 2 and spawnmap[yplace-1][xplace+1] != "barrier":
            xplace = xplace + 1
            yplace = yplace - 1
    timeadd()
    mapupdate()
    statsupdate()
def A():
    global xplace,yplace,xp,energy,cuteness,skinpos,health
    if spawnmap[yplace][xplace-1] != "barrier" and skinlist[len(skinlist)-1][1]!= 2:
        if energy > 0 and health > 0:
            xplace = xplace - 1
            xp = xp + 1 * cuteness
            energy = energy - 1
        else:
            xplace = xplace - 1
            xp = xp + 1 * cuteness
            health = health - 2
    else:
        if skinlist[skinpos][1]== 2 and spawnmap[yplace][xplace-1] != "barrier":
            xplace = xplace - 1
    timeadd()
    mapupdate()
    statsupdate()
def D():
    global xplace,yplace,xp,energy,cuteness,skinpos,health
    if spawnmap[yplace][xplace+1] != "barrier" and skinlist[len(skinlist)-1][1]!= 2:
        if energy > 0 and health > 0:
            xplace = xplace + 1
            xp = xp + 1 * cuteness
            energy = energy - 1
        else:
            xplace = xplace + 1
            xp = xp + 1 * cuteness
            health = health - 2
    else:
        if skinlist[skinpos][1]== 2 and spawnmap[yplace][xplace+1] != "barrier":
            xplace = xplace + 1
    timeadd()
    mapupdate()
    statsupdate()
def NYA():
    timeadd()
    statsupdate()
def SA():
    global xplace,yplace,xp,energy,cuteness,skinpos,health
    if spawnmap[yplace+1][xplace-1] != "barrier" and skinlist[len(skinlist)-1][1]!= 2:
        if energy > 0 and health > 0:
            xplace = xplace - 1
            yplace = yplace + 1
            xp = xp + 1 * cuteness
            energy = energy - 1
        else:
            xplace = xplace - 1
            yplace = yplace + 1
            xp = xp + 1 * cuteness
            health = health - 2
    else:
        if skinlist[skinpos][1]== 2 and spawnmap[yplace+1][xplace-1] != "barrier":
            xplace = xplace - 1
            yplace = yplace + 1
    timeadd()
    mapupdate()
    statsupdate()
def S():
    global xplace,yplace,xp,energy,cuteness,skinpos,health
    if spawnmap[yplace+1][xplace] != "barrier" and skinlist[len(skinlist)-1][1]!= 2:
        if energy > 0 and health > 0:
            yplace = yplace + 1
            xp = xp + 1 * cuteness
            energy = energy - 1
        else:
            yplace = yplace + 1
            xp = xp + 1 * cuteness
            health = health - 2
    else:
        if skinlist[skinpos][1]== 2 and spawnmap[yplace+1][xplace] != "barrier":
            yplace = yplace + 1
    timeadd()
    mapupdate()
    statsupdate()
def SD():
    global xplace,yplace,xp,energy,cuteness,skinpos,health
    if spawnmap[yplace+1][xplace+1] != "barrier" and skinlist[len(skinlist)-1][1]!= 2:
        if energy > 0 and health > 0:
            xplace = xplace + 1
            yplace = yplace + 1
            xp = xp + 1 * cuteness
            energy = energy - 1
        else:
            xplace = xplace + 1
            yplace = yplace + 1
            xp = xp + 1 * cuteness
            health = health - 2
    else:
        if skinlist[skinpos][1]== 2 and spawnmap[yplace+1][xplace+1] != "barrier":
            xplace = xplace + 1
            yplace = yplace + 1
    timeadd()
    mapupdate()
    statsupdate()
def mapupdate():
    global xplace,yplace
    screen6.config(command = D)
    for i in range(len(indexlist)):
        if spawnmap[yplace-1][xplace-1] == indexlist[i-1]:
            screen1.config (image = imagelist[i-1])
    for i in range(len(indexlist)):
        if spawnmap[yplace-1][xplace] == indexlist[i-1]:
            screen2.config (image = imagelist[i-1])    
    for i in range(len(indexlist)):
        if spawnmap[yplace-1][xplace+1] == indexlist[i-1]:
            screen3.config (image = imagelist[i-1])    
    for i in range(len(indexlist)):
        if spawnmap[yplace][xplace-1] == indexlist[i-1]:
            screen4.config (image = imagelist[i-1])
    for i in range(0,len(skinlist)-1):
        if skinlist[i][1] == 2:   
            screen5.config (image = skinlist[i][0])
    if skinlist[len(skinlist)-1][1] == 2:
        screen5.config (image = scooter,command = carexit)
    for i in range(len(indexlist)):
        if spawnmap[yplace][xplace+1] == indexlist[i-1]:
            screen6.config (image = imagelist[i-1])   
    for i in range(len(indexlist)):
        if spawnmap[yplace+1][xplace-1] == indexlist[i-1]:
            screen7.config (image = imagelist[i-1])        
    for i in range(len(indexlist)):
        if spawnmap[yplace+1][xplace] == indexlist[i-1]:
            screen8.config (image = imagelist[i-1])        
    for i in range(len(indexlist)):
        if spawnmap[yplace+1][xplace+1] == indexlist[i-1]:
            screen9.config (image = imagelist[i-1])    
    if skinlist[len(skinlist)-1][1] != 2:
        if hours > 6 and hours < 21:
            if xplace == 9 and yplace == 8:
                marketshop()
            if xplace == 11 and yplace == 10:
                petstore()    
            if xplace == 11 and yplace == 8:
                workstore()
            if xplace == 12 and yplace == 8:
                NPC1()
            if xplace == 9 and yplace == 10:
                clothesstore()
            if xplace == 12 and yplace == 10:
                casinoenter()
            if xplace == 20 and yplace == 6:
                examboard()
            if xplace == 19 and yplace == 6:
                NPC2()
            if xplace == 8 and yplace == 10:
                storageenter()
            if xplace == 10 and yplace == 8:
                yplace = 9
                xplace = 20
                mapupdate()
        if spawnmap[yplace][xplace] == "parking":
            parkingenter()
        if xplace == 11 and yplace == 12 and spawnmap[12][11] == ho:
            yplace = 3
            xplace = 21
            mapupdate()
        if xplace == 11 and yplace == 12 and spawnmap[12][11] == "forsale":
            A()
            screen6.config(text = "Build a house for 150000 $?",image = "",command = housebuild)
        if xplace == 21 and yplace == 4:
            yplace = 12
            xplace = 10
            mapupdate()
        if xplace == 20 and yplace == 10:
            yplace = 9
            xplace = 10
            mapupdate()
def housebuild():
    global catollars
    if catollars >=150000:
        spawnmap[12][11] = ho
        catollars = catollars - 150000
        statsupdate()
        mapupdate()
    timeadd()
def carexit():
    global currentskin,skinpos
    if spawnmap[yplace][xplace] == "parking":
        skinpos = currentskin
        skinlist[len(skinlist)-1][1] = 1    
        skinlist[currentskin][1] = 2
        close()
    mapupdate()
def xproadopen():
    global lvl,xproadpos,nickname2,xpinfo
    screen1.config (image = exitbtn,command = close)
    screen2.config (image = "",bg = "blue",text = xproadpos+1,command = nothing)
    screen3.config (image = "",text = nickname2,bg = "blue",command = nothing)
    screen4.config (image = leftbtn,command = xproadleft)
    if xproadrewards[xproadpos][1] > 0:
        screen5.config (image = moneybox,command = xproadredeem)
    if xproadrewards[xproadpos][2] > 0:
        screen5.config (image = diamondbox,command = xproadredeem)
    screen6.config (image = rightbtn,command = xproadright)
    screen7.config (image = "",bg = "blue",text = lvl ,command = nothing)
    screen8.config (image = "",bg = "blue",text = xpinfo,command = nothing)
    screen9.config (image = "",bg = "blue",text = lvl + 1,command = nothing)
def xproadleft():
    global xproadpos
    if xproadpos > 0:
        xproadpos = xproadpos - 1
        xproadopen()
def xproadright():
    global xproadpos
    if xproadpos < 14:
        xproadpos = xproadpos + 1
        xproadopen()
def xproadredeem():
    global lvl,xproadpos,catollars,health,cuteness,gems,moneyboxes,diamondboxes
    if lvl >= xproadpos+1 and xproadrewards[xproadpos][0] == 0:
        if xproadrewards[xproadpos][1] > 0:
            moneyboxes = moneyboxes + 1
            screen3.config(text = "REDEEMED REWARD")
        else:
            diamondboxes = diamondboxes + 1
            screen3.config(text = "REDEEMED REWARD")
        xproadrewards[xproadpos][0] = 1
        statsupdate()
def parkingenter():
    global currentskin,catollars,skinpos
    if skinlist[len(skinlist)-1][1] == 1 or skinlist[len(skinlist)-1][1] == 2:
        for i in range(len(skinlist)-1):
            if skinlist[i][1] ==2:
                print(catollars)
                skinlist[i][1] = 1
                currentskin  = skinpos
                screen5.config (image = scooter,command = carexit)
                skinpos = len(skinlist)-1  
                skinlist[len(skinlist)-1][1] = 2
    else:
        S()
        screen2.config(image = "",bg = "white",text = "BUY SCOOTERPASS FOR 2500 CATOLLARS?",command = scooterbuy)
def scooterbuy():
    global catollars,skinlist
    if catollars > 2499:
        catollars = catollars - 2500
        W()
        skinlist[len(skinlist)-1][1] = 2
        mapupdate()
        statsupdate()
        close()
        timeadd()
def backpackopen():
    screen1.config (image = exitbtn,command = close)
    screen2.config (image = wall,command = nothing)
    screen3.config (image = wall,command = nothing)
    screen4.config (image = leftbtn,command = inventoryleft)
    screen6.config (image = rightbtn,command = inventoryright)
    screen5.config (command = backpackactivate)
    screen7.config (image = wall,command = nothing)
    screen8.config (image = wall,command = nothing)
    screen9.config (image = wall,command = nothing)
    backpackupdate()
def backpackupdate():
    global subtextinfo
    for i in range(len(inventory)):
        if inventory[inventorypos][0] == inventory[i-1][0]:
            screen5.config (image = foodimagelist[i-1])  
    subtext.config (text = inventory[inventorypos][1])
def backpackactivate():
    global energy,health,xp,cuteness,hunger
    if inventory[inventorypos][1] > 0 and hunger > 0:
        if energy + inventory[inventorypos][2] <= 100:
            energy = energy + inventory[inventorypos][2]
        else:
            energy = 100
        if health + inventory[inventorypos][3] <= 100:
            health = health + inventory[inventorypos][3]
        else:
            health = 100
        if inventorypos == 13:
            health = health +100
        inventory[inventorypos][1] = inventory[inventorypos][1] - 1
        hunger = hunger - 1
        xp = xp + (3 * cuteness)
        backpackupdate()
        timeadd()
    statsupdate()
def inventoryleft():
    global inventorypos
    if inventorypos != 0 :
        inventorypos = inventorypos - 1
        backpackupdate()
def inventoryright():
    global inventorypos
    if inventorypos != len(inventory)-1:
        inventorypos = inventorypos + 1
        backpackupdate()
def codevaultopen():
    screen1.config (image = road,command = nothing)
    screen2.config (image = road,command = nothing)
    screen3.config (image = road,command = nothing)
    screen4.config (image = exitbtn,command = close)
    screen5.config (image = lookingcat)
    screen6.config (image = "",text = "use 0 and 1 to get codes",bg = "grey",command = nothing)
    screen7.config (image = zerobtn,command=addzero)
    screen8.config (image = onebtn,command=addone)
    screen9.config (image = okbtn,command=redeem)
def addzero():
    currentcode.append("0")
def addone():
    currentcode.append("1")
def redeem():
    global currentcode,currentcode2,catollars,xp,cpxp
    for i in range(len(currentcode)):
        currentcode2 = currentcode2 + currentcode[i]
    if currentcode2 == "01100011110000011111" and codes[0] == 0:
        screen2.config (image = "",text="CODE REDEEMED SUCCESEFULLY",command = nothing)
        catollars = catollars + 1000
        codes[0] = 1
    if currentcode2 == "10100110100000110111" and codes[1] == 0:
        screen2.config (image = "",text="CODE REDEEMED SUCCESEFULLY",command = nothing)
        skinlist[1][1] = 2
        codes[1] = 1
    if currentcode2 == "11111111111111111111" and codes[2] == 0:
        screen2.config (image = "",text="CODE REDEEMED SUCCESEFULLY",command = nothing)
        gems = gems + 5
        codes[2] = 1
    if currentcode2 == "00000000000000000000" and codes[3] == 0:
        xp = xp + 1000
        screen2.config (image = "",text="CODE REDEEMED SUCCESEFULLY",command = nothing)
        codes[3] = 1
    if currentcode2 == "0100001001110010011000010110100101101110" and codes[4] == 0:
        skinlist[9][1] = 1
        screen2.config (image = "",text="CODE REDEEMED SUCCESEFULLY",command = nothing)
        codes[4] = 1
    currentcode = []
    currentcode2 = ""
    statsupdate()
def marketshop():
    screen1.config (image = exitbtn,command = close)
    screen2.config (image = lookingcat)
    screen3.config (image = wall,command = nothing)
    screen4.config (image = leftbtn,command = marketleft)
    screen5.config (image = foodimagelist[marketpos],command = marketpurchase)
    screen6.config (image = rightbtn,command = marketright)
    screen7.config (image = wall,command=nothing)
    screen8.config (image = wall,command=nothing)
    screen9.config (image = wall,command=nothing)
def marketleft():
    global marketpos
    if marketpos > 0:
        marketpos = marketpos -1
        marketshop()
def marketright():
    global marketpos
    if marketpos < len(inventory)-1:
        marketpos = marketpos + 1
        marketshop()
def marketpurchase():
    global marketpos,inventory,gems,catollars
    if inventory[marketpos][4] > 0:
        if catollars >= inventory[marketpos][4]:
            inventory[marketpos][1] = inventory[marketpos][1] + 1
            catollars = catollars - inventory[marketpos][4]
            timeadd()
    else:
        if gems >= inventory[marketpos][5]:
            inventory[marketpos][1] = inventory[marketpos][1] + 1
            gems = gems - inventory[marketpos][5]
            timeadd()
    statsupdate()
def workstore():
    global workbuttoninfo
    workbuttoninfo = workbutton[random.randint(0, 25)]
    screen1.config (text = "match this button to earn money --->",image = "",command = nothing)
    screen2.config (text = workbuttoninfo ,image = "",command = nothing)
    screen3.config (image = "",command = nothing)
    screen4.config (image = exitbtn,command = close)
    screen5.config (image = workcat)
    screen6.config (image = wall,command = nothing)
    screen7.config (image = leftbtn,command = workbuttonleft)
    screen8.config (text = workbuttoninfo,image = '',command = nothing)
    screen9.config (image = rightbtn,command = workbuttonright)
    workbuttonupdate()
def workbuttonleft():
    global workbuttonpos
    if workbuttonpos > 0:
        workbuttonpos = workbuttonpos - 1
    if workbuttonpos == 0:
        workbuttonpos = 26
    workbuttonupdate()   
def workbuttonright():
    global workbuttonpos
    if workbuttonpos < 26:
        workbuttonpos = workbuttonpos + 1
    if workbuttonpos == 26:
        workbuttonpos = 1
    workbuttonupdate()
def workbuttonupdate():
    global workbuttonpos
    screen8.config (text = workbutton[workbuttonpos],image = '',command = workbuttonactivate)
    screen2.config(text = workbuttoninfo)
def workbuttonactivate():
    global workbuttoninfo,catollars,energy,health,xp    
    if workbutton[workbuttonpos] == workbuttoninfo:
        catollars = catollars + 50
        energy = energy - 5
        health = health - 1
        xp = xp + 5
        workbuttonchange()
    statsupdate()
    timeadd()
def workbuttonchange():
    global workbuttoninfo
    workbuttoninfo = workbutton[random.randint(0, 25)]
    workbuttonupdate()
def storageenter():
    screen1.config (image = "",bg = "brown",text = "Your reward is:",command = nothing)
    screen2.config (image = "",bg = "brown",command = nothing) 
    screen3.config (image = wall,command = nothing)
    screen4.config (image = leftbtn,command = storageleft)
    if storagepos == 0:
        screen5.config (image = foodbox,command = box1)
    if storagepos == 1:
        screen5.config (image = capsule,command = box2)
    if storagepos == 2:
        screen5.config (image = moneybox,command = box3)
    if storagepos == 3:
        screen5.config (image = diamondbox,command = box4)
    storagelist = [foodboxes,capsules,moneyboxes,diamondboxes]
    subtext.config (text = storagelist[storagepos])
    screen6.config (image = rightbtn,command = storageright)
    screen7.config (image = exitbtn,command = close)
    screen8.config (image = wall,command = nothing)
    screen9.config (image = wall,command = nothing)
def storageleft():
    global storagepos
    if storagepos > 0:
        storagepos = storagepos - 1
        storageenter()
def storageright():
    global storagepos
    if storagepos < 3:
        storagepos = storagepos + 1
        storageenter()
def box1():
    global reward,rewardtext,foodboxes,catollars,storagelist,moneyboxes
    if foodboxes > 0:
        foodboxes = foodboxes - 1
        storagelist = [foodboxes,capsules,moneyboxes,diamondboxes]
        subtext.config (text = storagelist[storagepos])
        reward = random.randint(0,len(inventory)-1)
        screen2.config (image = foodimagelist[reward])
        inventory[reward][1] = inventory[reward][1] + 10
        statsupdate()
        timeadd()
def box2():
    global reward,rewardtext,capsules,catollars,storagelist,condition,skinlist,i,storagepos
    if capsules > 0:
        capsules = capsules - 1
        storagelist = [foodboxes,capsules,moneyboxes,diamondboxes]
        subtext.config (text = storagelist[storagepos])
        reward = random.randint(0,32)
        if reward < 16:
            condition = 0
            while condition == 0:
                for i in range(0,len(skinlist)-2):
                    print(skinlist[i][5])
                    if skinlist[i][5] == "common":
                        reward = random.randint(1,100)
                        if reward == 1:
                            skinlist[i][1] = 1
                            screen2.config (image = skinlist[i][0])
                            condition = 1
        if reward > 15 and reward < 25:
            condition = 0
            while condition == 0:
                for i in range(0,len(skinlist)-2):
                    print(skinlist[i][5])
                    if skinlist[i][5] == "rare":
                        reward = random.randint(1,100)
                        if reward == 1:
                            skinlist[i][1] = 1
                            screen2.config (image = skinlist[i][0])
                            condition = 1
        if reward > 24 and reward < 30:
            condition = 0
            while condition == 0:   
                for i in range(0,len(skinlist)-2):
                    print(skinlist[i][5])
                    if skinlist[i][5] == "superrare":
                        reward = random.randint(1,100)
                        if reward == 1:
                            skinlist[i][1] = 1
                            screen2.config (image = skinlist[i][0])
                            condition = 1
        if reward > 29 and reward < 32:
            condition = 0
            while condition == 0:
                for i in range(0,len(skinlist)-2):
                    print(skinlist[i][5])
                    if skinlist[i][5] == "epic":
                        reward = random.randint(1,100)
                        if reward == 1:
                            skinlist[i][1] = 1
                            screen2.config (image = skinlist[i][0])
                            condition = 1
        if reward == 32:
            condition = 0
            while condition == 0:
                for i in range(0,len(skinlist)-2):
                    print(skinlist[i][5])
                    if skinlist[i][5] == "legendary":
                        reward = random.randint(1,100)
                        if reward == 1:
                            skinlist[i][1] = 1
                            screen2.config (image = skinlist[i][0])
                            condition = 1
        statsupdate()
        timeadd()
def box3():
    global reward,rewardtext,moneyboxes,catollars,storagelist
    if moneyboxes > 0:
        moneyboxes = moneyboxes - 1
        storagelist = [foodboxes,capsules,moneyboxes,diamondboxes]
        subtext.config (text = storagelist[storagepos])
        reward = random.randint(100,5000)
        rewardtext = "you won" + reward + "catollars!"
        screen2.config (image = "",text = rewardtext)
        catollars = catollars + reward
        statsupdate()
        timeadd()
def box4():
    global reward,rewardtext,diamondboxes,diamonds,storagelist
    if diamondboxes > 0:
        diamondboxes = diamondboxes - 1
        storagelist = [foodboxes,capsules,moneyboxes,diamondboxes]
        subtext.config (text = storagelist[storagepos])
        reward = random.randint(10,100)
        rewardtext = "you won" + reward + "diamonds!"
        screen2.config (image = "",text = rewardtext)
        diamonds = diamonds + reward
        statsupdate()
        timeadd()
def clothesstore():
    screen4.config (image = leftbtn,command = skinposleft)
    screen5.config (image = skinlist[skinpos][0],command = skinredeem)
    if skinlist[skinpos][1] == 1 or 2:
            subtext.config (text = "✓")
    if skinlist[skinpos][1] == 0: 
        subtext.config (text = skinlist[skinpos][2])
    screen6.config (image = rightbtn,command = skinposright)
    screen7.config (image = exitbtn,command = close)
    if skinlist[skinpos][5] == "common":
        screen1.config (image = "",command = nothing,bg = "white")
        screen2.config (image = "",command = nothing,bg = "white") 
        screen3.config (image = "",command = nothing,bg = "white")
        screen8.config (image = "",bg = "white",text = str(skinlist[skinpos][4]),command = nothing)
        screen9.config (image = "",command = nothing,text = skinlist[skinpos][5],bg = "white")
    if skinlist[skinpos][5] == "rare":
        screen1.config (image = "",command = nothing,bg = "green")
        screen2.config (image = "",command = nothing,bg = "green") 
        screen3.config (image = "",command = nothing,bg = "green")
        screen8.config (image = "",bg = "green",text = str(skinlist[skinpos][4]),command = nothing)
        screen9.config (image = "",command = nothing,text = skinlist[skinpos][5],bg = "green")
    if skinlist[skinpos][5] == "superrare":
        screen1.config (image = "",command = nothing,bg = "blue")
        screen2.config (image = "",command = nothing,bg = "blue") 
        screen3.config (image = "",command = nothing,bg = "blue")
        screen8.config (image = "",bg = "blue",text = str(skinlist[skinpos][4]),command = nothing)
        screen9.config (image = "",command = nothing,text = skinlist[skinpos][5],bg = "blue")
    if skinlist[skinpos][5] == "epic":
        screen1.config (image = "",command = nothing,bg = "purple")
        screen2.config (image = "",command = nothing,bg = "purple") 
        screen3.config (image = "",command = nothing,bg = "purple")
        screen8.config (image = "",bg = "purple",text = str(skinlist[skinpos][4]),command = nothing)
        screen9.config (image = "",command = nothing,text = skinlist[skinpos][5],bg = "purple")
    if skinlist[skinpos][5] == "legendary":
        screen1.config (image = "",command = nothing,bg = "yellow")
        screen2.config (image = "",command = nothing,bg = "yellow") 
        screen3.config (image = "",command = nothing,bg = "yellow")
        screen8.config (image = "",bg = "yellow",text = str(skinlist[skinpos][4]),command = nothing)
        screen9.config (image = "",command = nothing,text = skinlist[skinpos][5],bg = "yellow")
    if skinlist[skinpos][5] == "special" and skinlist[skinpos][1] == 1 or skinlist[skinpos][1] == 2 and skinlist[skinpos][5] == "special":
        screen1.config (image = "",command = nothing,bg = "orange")
        screen2.config (image = "",command = nothing,bg = "orange") 
        screen3.config (image = "",command = nothing,bg = "orange")
        screen8.config (image = "",bg = "orange",text = str(skinlist[skinpos][4]),command = nothing)
        screen9.config (image = "",command = nothing,text = skinlist[skinpos][5],bg = "orange")
    if skinlist[skinpos][5] == "special" and skinlist[skinpos][1] == 0:
        screen1.config (image = "",command = nothing,bg = "orange")
        screen5.config (image = "",bg = "white",text = "???",command = skinredeem)
        screen2.config (image = "",command = nothing,bg = "orange") 
        screen3.config (image = "",command = nothing,bg = "orange")
        screen8.config (image = "",bg = "orange",text = "???",command = nothing)
        screen9.config (image = "",command = nothing,text = skinlist[skinpos][5],bg = "orange")
def skinposleft():
    global skinpos
    if skinpos > 0:
        skinpos = skinpos - 1
        clothesstore()
def skinposright():
    global skinpos,skinlist
    if skinpos < len(skinlist)-2:
        skinpos = skinpos + 1
        clothesstore()
def skinredeem():
    global catollars
    if skinlist[skinpos][1] == 1 or skinlist[skinpos][1] == 2:
        for i in range(0,len(skinlist)):
            if skinlist[i][1] == 2:
                skinlist[i][1] = 1
        skinlist[skinpos][1] = 2
        clothesstore()  
    if catollars >= skinlist[skinpos][2] and skinlist[skinpos][1] == 0:
        for i in range(0,len(skinlist)):
            if skinlist[i][1] == 2:
                skinlist[i][1] = 1
        skinlist[skinpos][1] = 2
        catollars = catollars - skinlist[skinpos][2]
        statsupdate()
        clothesstore()
        timeadd()
def petstore():
    screen1.config (image = "",command = nothing,bg = "white")
    screen2.config (image = "",command = nothing,bg = "white") 
    screen3.config (image = "",command = nothing,bg = "white")
    screen4.config (image = leftbtn,command = petposleft)
    subtext.config (image = petlist[petpos][0],command = nothing)
    screen6.config (image = rightbtn,command = petposright)
    screen7.config (image = exitbtn,command = close)
    screen8.config (image = "",text = "ANY PET 10000",bg = "brown",command = nothing)
    screen9.config (image = "",command = nothing,text = petlist[petpos][2],bg = "white")
def petposleft():
    global petpos
    if petpos > 0:
        petpos = petpos - 1
        petstore()
def petposright():
    global petpos,petlist
    if petpos < len(petlist)-1:
        petpos = petpos + 1
        petstore()
def examboard():
    screen1.config (image = "",text = "study cat math",bg = "green",command = nothing)
    screen2.config (image = exitbtn,command = close)
    screen3.config (image = "",text = "cat math exam",bg = "green",command = nothing)
    screen4.config (image = "",text = "study cat language",bg = "green",command = nothing)
    screen5.config (image = "",text = "",bg = "brown",command = nothing)   
    screen6.config (image = "",text = "cat language exam",bg = "green",command = nothing)
    screen7.config (image = "",text = "study cat science",bg = "green",command = nothing)
    screen8.config (image = "",text = "rating",bg = "brown",command = nothing)
    screen9.config (image = "",text = "cat science exam",bg = "green",command = nothing)
def cattlepassopen():
    global cpinfo,cpinfo2,cppos,task1,cpxp,cplvl,taskinfo
    if cpxp > 99:
        cplvl = cplvl + 1
        cpxp = cpxp - 100
    if cppos % 2 == 1:
        cpinfo2 = "premium reward"
    else:
        cpinfo2 = "free reward"
    taskinfo = ("Task -",task1)
    cpinfo = (cppos,cpinfo2,",",cplvl,"(",cpxp,"/100)")
    screen1.config (image = exitbtn,command = close)
    screen2.config (image = "",bg = "purple",text = cpinfo,command = nothing)
    screen3.config (image = "",text = taskinfo,bg = "purple",command = nothing)
    screen4.config (image = leftbtn,command = cpleft)
    if cprewards[cppos][2] > 0:
        screen5.config (image = catollarsimage2,command = cpredeem)
        subtext.config (text = cprewards[cppos][2])
    if cprewards[cppos][3] > 0:
        screen5.config (image = healthimage2,command = cpredeem)
        subtext.config (text = cprewards[cppos][3])
    if cprewards[cppos][4] > 0:
        screen5.config (image = cutenessimage2,command = cpredeem)
        subtext.config (text = cprewards[cppos][4])
    if cprewards[cppos][5] > 0:
        screen5.config (image = xpimage,command = cpredeem)
        subtext.config (text = cprewards[cppos][5])        
    screen6.config (image = rightbtn,command = cpright)
    screen7.config (image = "",text = "",bg = "purple",command = nothing)
    screen8.config (image = "",text = "",bg = "purple",command = nothing)
    screen9.config (image = "",bg = "yellow",text = "BUY CATTLEPASS (100 gems)",command = cppremium)  
def cpleft():
    global cppos
    if cppos > 0:
        cppos = cppos - 1
        cattlepassopen()
def cpright():
    global cppos
    if cppos < 5:
        cppos = cppos + 1
        cattlepassopen()
def cpredeem():
    global cplvl,cppos,catollars,health,cuteness,xp,cattlepass
    if cplvl >= cppos and cprewards[cppos][0] == 0:
        if cattlepass >= cprewards[cppos][1]:
            catollars = catollars+ cprewards[cppos][2]
            health = health+ cprewards[cppos][3]
            cuteness = cuteness + cprewards[cppos][4]
            xp = xp + cprewards[cppos][5]
            cprewards[cppos][0] = 1
            statsupdate()
def cppremium():
    if cattlepass == 0 and gems >= 100:
        screen7.config (image = summercat,command = nothing)
        screen8.config (image = "",text = "extra rewards free skin and more!",command = nothing,bg = "purple")
        screen9.config (image = "",bg="yellow",text = "BUY CATTLEPASS(-100 gems)",command = cattleplus)  
def cattleplus():
    global gems,cattlepass
    cattlepass = 1
    gems = gems - 100
    statsupdate()
def casinoenter():
    global play4money
    screen1.config (image = zerologo,command = zerostart)
    screen2.config (image = TTT,command = nothing)
    screen3.config (image = donimg,command = DON)
    screen4.config (image = exitbtn,command = close)
    screen5.config (image = wall,command = nothing)
    if play4money == 0:
        screen6.config (image = "",bg = "red",text = "Safe playing(no winning/losing money)",command = P4M1)
    if play4money == 1:
        screen6.config (image = "",bg = "green",text = "Playing for money",command = P4M2)
    screen7.config (image = wall,command = nothing)
    screen8.config (image = wall,command = nothing)
    screen9.config (image = wall,command = nothing)
def P4M1():
    global play4money
    play4money = 1
    casinoenter()
def P4M2():
    global play4money
    play4money = 0
    casinoenter()
def DON():
    global donpos
    screen1.config (image = "",bg = "brown",command = nothing)
    screen2.config (image = "",bg = "brown",command = nothing)
    screen3.config (image = "",bg = "brown",command = nothing)
    screen4.config (image = exitbtn,bg = "brown",command = close)
    screen5.config (image = "",bg = "white",text = "",command = donstart)
    screen6.config (text = "",image = "",bg = "brown",command = nothing)
    screen7.config (image = leftbtn,command = donleft)
    screen8.config (image = "",bg = "brown",command = nothing)
    screen9.config (image = rightbtn,command = donright)
    subtext.config (text = donlist[donpos])
    timeadd()
def donleft():
    global donpos
    if donpos > 0:
        donpos = donpos - 1
        DON()
def donright():
    global donpos
    if donpos < 5:
        donpos = donpos + 1
        DON()
def donstart():
    global donpos,donlist,catollars,donstatus,play4money
    if catollars >= donlist[donpos]:        
        for i in range(0,10):
            for n in range(i*i):
                donstatus = random.randint(0,1)
        if donstatus == 0:
            screen5.config (bg = "red")
            if play4money == 1:
                catollars = catollars - donlist[donpos]
            statsupdate()
            timeadd()
        if donstatus == 1:
            screen5.config (bg = "green")
            if play4money == 1:
                catollars = catollars + donlist[donpos]
            statsupdate()
            timeadd()
def zerostart():
    global currentcards1,currentcards2
    for i in range(0,5):
        currentcards1 = 5
        currentcards2 = 5
        zerocards1[i].append(zerocolors[random.randint(0,4)])
        zerocards2[i].append(zerocolors[random.randint(0,4)])
        zerocards1[i].append(zeronumber[random.randint(0,10)])
        zerocards2[i].append(zeronumber[random.randint(0,10)])
    screen1.config (image = takecard,command = zerocardstake)
    screen2.config (image = workcat,command = nothing)
    screen3.config (image = "",bg = "brown",command = nothing)
    screen4.config (image = "",bg = "brown",command = nothing)
    screen5.config (image = wall,command = nothing)
    screen6.config (text = "",image = "",bg = "brown",command = nothing)
    screen7.config (image = leftbtn,command = zeroleft)
    screen8.config (image = wall,command = cardactivate)
    screen9.config (image = rightbtn,command = zeroright)
    zeroupdate()
    timeadd()
def cardactivate():
    global currentcolor,currentnumber,currentcards1
    if (zerocards1[zerocardspos][0] == currentcolor)or (zerocards1[zerocardspos][0] == "grey") or (str(zerocards1[zerocardspos][1]) == str(currentnumber)):
        currentcolor = zerocards1[zerocardspos][0]
        currentnumber = zerocards1[zerocardspos][1]
        zerocards1[zerocardspos][0] = "-"
        zerocards1[zerocardspos][1] = "-1"
        currentcards1 = currentcards1 - 1
        zeroupdate()
def zerocardstake():
    global currentcards1,catollars
    for i in range(0,10):
        if zerocards1[i][0] == "-":
            zerocards1[i][0] = (zerocolors[random.randint(0,4)])
            zerocards1[i][1] = (zeronumber[random.randint(0,10)])
            currentcards1 = currentcards1 + 1
            break
    zeroupdate()
    print(zerocards1)
def zeroupdate():
    global zerocardspos,currentcards1,currentcards2,catollars,play4money
    if zerocards1[zerocardspos][0] != "-":
        screen8.config (bg = zerocards1[zerocardspos][0],image = "",text = zerocards1[zerocardspos][1])
    else:
        screen8.config (bg = "black",image = "")
    screen5.config (bg = currentcolor,image = "",text = currentnumber)
    if currentcards1 >= 10 or currentcards2 <= 0:
        if play4money == 1:
            catollars = catollars - 1000
        screen5.config (text = "you lost",bg = "red")
        timeadd()
        close()
    if currentcards2 >= 10 or currentcards1 <= 0:
        if play4money == 1:
            catollars = catollars + 1000
        screen5.config (text = "you win",bg = "green")
        timeadd()
        close()
def zeroleft():
    global zerocardspos
    if zerocardspos > 0:
        zerocardspos = zerocardspos - 1
    else:
        zerocardspos = 9
    zeroupdate()
def zeroright():
    global zerocardspos
    if zerocardspos < 9:
        zerocardspos = zerocardspos + 1
    else:
        zerocardspos = 0
    zeroupdate()
def saveopen():
    global logincheck
    screen1.config (image = "",bg = "green",text = "Log in",command = login)
    screen6.config (image = wall,text = "",command = nothing)
    if logincheck == 0:
        screen3.config (image = "",bg = "blue",text = "Create Account",command = savecreate)
    else:
        screen3.config (image = "",bg = "blue",text = "Save",command = save)
    screen4.config (image = exitbtn,bg = "brown",command = close)
    screen5.config (image = wall,command = nothing)
    screen2.config (image = wall,text = "",command = nothing)
    screen7.config (image = wall,text = "Logged in as:",command = nothing)
    screen8.config (image = wall,text = nickname2,command = nothing)
    screen9.config (image = Credits,command = nothing)
def savecreate():
    global password,database,xplace,yplace,xp,lvl,nickname,catollars,user_password_entry_area,user_name_input_area,rut
    rut = Toplevel()
    rut.geometry("300x200")
    user_name = Label(rut,text = "Username(unchangable)")
    user_name.place(x = 10,y = 60)    
    user_password = Label(rut,text = "Password")
    user_password.place(x = 40,y = 100)
    user_name_input_area = Entry(rut, textvariable = nickname,width = 30).place(x = 150,y = 60)
    user_password_entry_area = Entry(rut, textvariable = password,width = 30).place(x = 150,y = 100)
    sub_btn= Button(rut,text = 'Submit', command = submit).place(x=200,y=150)
def save():
    global nickname2,xplace,yplace,catollars
    database.execute("UPDATE catlife SET catollars = '{catollars}' WHERE nickname = '{nickname2}'")
    print(catollars)
    screen2.config (image = "",text = "Data is saved",bg = "green",command = nothing)
    databasee.commit()
def submit():
    global user_password_entry_area,user_name_input_area,rut,nicknamecheck,logincheck
    nickname2 = nickname.get()
    password2 = password.get()
    database.execute("SELECT * FROM catlife")
    rows = database.fetchall()
    for row in rows:
        if row[0] == nickname2:
            nicknamecheck = 1
    if nicknamecheck ==1:
        screen2.config (image = "",text = "Error: This nickname already exists!",bg = "red",command = nothing)
    else:
        database.execute(f"INSERT INTO `catlife` VALUES ('{nickname2}', '{password2}','{xplace}', '{yplace}','{xp}','{lvl}','{catollars}')")
        databasee.commit()
        screen2.config (image = "",text = "Account created!",bg = "green",command = nothing)
        logincheck = 1
    rut.destroy()
def login():
    global password,database,xplace,yplace,xp,lvl,nickname,catollars,user_password_entry_area,user_name_input_area,rut
    rut = Toplevel()
    rut.geometry("300x200")
    user_name = Label(rut,text = "Username(unchangable)")
    user_name.place(x = 10,y = 60)    
    user_password = Label(rut,text = "Password")
    user_password.place(x = 40,y = 100)
    user_name_input_area = Entry(rut, textvariable = nickname,width = 30).place(x = 150,y = 60)
    user_password_entry_area = Entry(rut, textvariable = password,width = 30).place(x = 150,y = 100)
    sub_btn= Button(rut,text = 'Submit', command = submit2).place(x=200,y=150)
def submit2():
    global user_password_entry_area,user_name_input_area,rut,nicknamecheck,nickname,password,nickname2,password2,logincheck
    nickname2 = nickname.get()
    password2 = password.get()
    database.execute(f"SELECT * FROM catlife WHERE (nickname = '{nickname2}')")
    rows = database.fetchall()
    for row in rows:
        if password2 == row[1]:
            xplace = row[2]
            xplace = row[3]
            xp = row[4]
            lvl = row[5]
            catollars = row[6]
            nickname2 = row[0]
            logincheck = 1
            print(row)
            print(catollars)
            screen2.config (image = "",text = "Successfully logged in!",bg = "green",command = nothing)
        else:
            screen2.config (image = "",text = "Error: Incorrect password!",bg = "red",command = nothing)
    rut.destroy()
    statsupdate()
def timeadd():
    global minutes,hours,days,hunger
    timeinfo = (str(hours) + ":" + str(minutes) + "0")
    dayinfo = ( "Day " + str(days))
    minutes = minutes + 1
    if minutes == 6:
        minutes = 0
        hours = hours + 1
    if hours == 24:
        hours = 0
        days= days + 1
        hunger = 3
    timestat1.config(text = timeinfo)
    timestat2.config(text = dayinfo)
    statsupdate()
def statsupdate():
    global cplvl,xp,catollars,lvlinfo,nickname2,lvl,xpinfo,cuteness,gems,energy,health,hunger,timeinfo,dayinfo
    lvlinfo = (nickname2,"|","lvl",lvl,"*",cuteness)
    xpinfo = (xp,"xp"," from ","1000")
    lvlstat.config(text = lvlinfo)
    lvlstat2['value'] = int(xp/10)
    healthstat2['value'] = health
    energystat2['value'] = energy
    catollarsstat2.config(text = catollars)
    gemsstat2.config(text = gems)
    if xp > 999:
        lvl = lvl + 1
        xp = xp - 1000
        statsupdate()
    if hunger == 3:
        foodstat.config (text = "⚫⚫⚫",command = nothing)
    if hunger == 2:
        foodstat.config (text = "⚫⚫",command = nothing)
    if hunger == 1:
        foodstat.config (text = "⚫",command = nothing)
    if hunger == 0:
        foodstat.config (text = "",command = nothing)
def NPC1():
    screen1.config (image = misskitty,command = close)
    screen2.config (bg="red",text = "Hi! I cant find my roses,can you find them for me?",image = "",command = nothing)
    screen3.config (bg="red",text = "",image = "",command = nothing)
    screen4.config (image = cat,command = nothing)
    screen5.config (bg="blue",text = "O O O",image = "",command = nothing)
    screen6.config (bg="blue",text = "",image = "",command = nothing)
    screen7.config (bg="white",image = "",text = "32",command = nothing)
    screen8.config (bg="white",image = "",text = "Yes,sure(quest)",command = nothing)
    screen9.config (bg="white",image = "",text = "I need to go.",command = close)
    timeadd()
def NPC2():
    screen1.config (image = teacher,command = close)
    screen2.config (bg="red",text = "Hi! studying hard? ",image = "",command = nothing)
    screen3.config (bg="red",text = "",image = "",command = nothing)
    screen4.config (image = cat,command = nothing)
    screen5.config (bg="blue",text = "O O O",image = "",command = nothing)
    screen6.config (bg="blue",text = "",image = "",command = nothing)
    screen7.config (bg="white",image = "",text = "Can i do something for you(quest)?",command = nothing)
    screen8.config (bg="white",image = "",text = "I need to improve my grades(-50 catollars,+ 10 rating)",command = nothing)
    screen9.config (bg="white",image = "",text = "I need to go.",command = close)
    timeadd()
def close():
    screen1.config (command = WA, bg = "white")
    screen2.config (command = W, bg = "white")
    screen3.config (command = WD, bg = "white")
    screen4.config (command = A, bg = "white")
    screen5.config (command = NYA, bg = "white")
    screen6.config (command = D, bg = "white")
    screen7.config (command = SA, bg = "white")
    screen8.config (command = S, bg = "white")
    screen9.config (command = SD, bg = "white")
    subtext.config (text = "")
    if spawnmap[yplace][xplace] != "road":
        S()
    mapupdate()
def menu1():
    global menupos
    if menupos > 0:
        menupos = menupos - 1
    else:
        menupos = 5
    menuupdate()
def menu2():
    global menupos
    if menupos < 5:
        menupos = menupos + 1
    else:
        menupos = 0
    menuupdate()
def menuupdate():
    global menupos
    if menupos == 0:
        backpackbtn.config(image = backpackbutton,command = backpackopen)
    if menupos == 1:
        backpackbtn.config(image = dtbutton,command = backpackopen)
    if menupos == 2:
        backpackbtn.config(image = cattlepassbutton,command = cattlepassopen)
    if menupos == 3:
        backpackbtn.config(image = achbutton,command = cattlepassopen)
    if menupos == 4:
        backpackbtn.config(image = codevaultbutton,command = codevaultopen)
    if menupos == 5:
        backpackbtn.config(image = savebutton,command = saveopen)
def nothing():
    print("")

nickchangestatus = 0
health = 100
healthlimit = 100
catollars = 160000
gems = 5
cuteness = 1
xplace = 10
yplace = 10
energy = 100
energylimit = 100
hunger = 3
xp = 0
lvl = 1
xpinfo = (xp,"/",1000)
days = 1
hours = 0
minutes = 0
timeinfo = (str(hours) + ":" + str(minutes) + "0")
dayinfo = ( "Day " + str(days))
workbutton = ["","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
workbuttoninfo = ""
workbuttonpos = 0
inventory = [["milk",10,30,0,5,0],["coffee",0,100,0,15,0],["banana",0,15,5,8,0],["burger",10,100,-5,5,0],["salad",0,75,15,20,0],["watermelon",0,100,25,0,0,30,0],["potion1",0,0,100,0,0,5],["potion2",0,75,75,0,5]]
inventorypos = 0
marketpos = 0
currentcode = []
currentcode2 = ""
skinpos = 0
currentskin = 0
xproadrewards = [[0,500,0],[0,500,0],[0,500,0],[0,500,0],[0,0,5],[0,500,0],[0,500,0],[0,500,0],[0,500,0],[0,0,5],[0,500,0],[0,500,0],[0,500,0],[0,500,0],[0,0,5]]
xproadpos = 0
cattlepass = 0
cprewards = [[0,0,100,0,0,0],[0,1,0,50,0,0],[0,0,500,0,0,0],[0,1,2500,0,0,0],[0,0,0,0,0.1,0],[0,1,0,0,0,1000]]
cptasks = ["buy water","buy milk","buy juice","buy cola","buy coffee","buy tea","buy banana","buy fries","buy burger","buy chocolate","buy watermelon","buy salad","buy rose","talk to miskitty","talk to teacher","go to watershop","go to foodshop","go to healshop","go to school","go to clothesshopshop"]
task1 = cptasks[random.randint(0,len(cptasks)-1)]
taskinfo = ("Task -",task1)
cppos = 0
cpxp = 0
cplvl = 0
cpinfo = (cppos,cpxp,"/100")
cpinfo2 = 0
play4money = 0
zerocolors=["red","yellow","green","blue","grey"]
zeronumber=["0","1","2","3","4","5","6","7","8","9","+2"]
zerocards1 = [[],[],[],[],[],["-","-1"],["-","-1"],["-","-1"],["-","-1"],["-","-1"]]
zerocardspos = 0
zerocards2 = [[],[],[],[],[],["-","-1"],["-","-1"],["-","-1"],["-","-1"],["-","-1"]]
currentcolor = zerocolors[random.randint(0,4)]
currentnumber = random.randint(0,9)
botcard = 0
currentcards1 = 5
currentcards2 = 5
TTTA = [0,0,0,0,0,0,0,0,0]
TTTB = 0
donpos = 0
donlist = [10,100,1000,10000,100000,1000000]
donstatus = 0
saveorload = 0
savelist = [catollars,xplace,yplace]
storagepos = 0
foodboxes = 1
capsules = 5
moneyboxes = 0
diamondboxes = 0
condition = 0
storagelist = [foodboxes,capsules,moneyboxes,diamondboxes]
reward = random.randint(0,3)
rewardtext = ""
dabloons = 0
codes = [0,0,0,0,0]
schoollist = [["you",0],["maria",random.randint(0,99)],["katrina",random.randint(0,99)],["max",random.randint(0,99)],["alex",random.randint(0,99)],["john",random.randint(0,99)],["daniel",random.randint(0,99)],["natalia",random.randint(0,99)],["mary",random.randint(0,99)],["lucy",random.randint(0,99)],["matt",random.randint(0,99)]]
for i in range(len(schoollist)):
    cursor = schoollist[i][1]
    pos = i        
    while pos > 0 and schoollist[pos - 1][1] > cursor:
        schoollist[pos][1] = schoollist[pos - 1][1]
        pos = pos - 1
    schoollist[pos][1] = cursor
schoolpos = 0
petpos = 0
print(schoollist)
menupos = 0
nicknamecheck = 0
nickname2 = ""
password2 = ""
logincheck = 0
r = "road"
m = "market"
b = "barrier"
w = "work"
c = "clothesshop"
k = "carshop"
p = "parking"
s = "forsale"
ho = "home"
n1 = "NPC1"
n2 = "NPC2"
n3 = "NPC3"
n4 = "NPC4"
ca = "casino"
st = "storage"
sc = "school"
re = "roomexit"
bo = "board"
ch = "chair"
d = "dabloonshop"
pe = "petshop"
sb = "susbarrier"
spawnmap = [[b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b],
            [b,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,b,r,r,r,r,r,r,b],
            [b,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,b,r,r,r,r,r,r,b],
            [b,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,b,r,r,r,r,r,r,b],
            [b,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,b,r,r,re,r,r,r,b],
            [b,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b],
            [b,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,b,n2,bo,r,b],
            [b,r,r,r,r,r,n4,r,r,r,r,r,r,r,r,r,r,r,b,r,r,r,b],
            [b,r,r,r,r,r,r,r,p,m,sc,w,n1,r,r,r,r,r,b,ch,r,ch,b],
            [b,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,b,ch,r,ch,b],
            [b,r,r,r,r,r,r,r,st,c,r,pe,ca,r,r,r,r,r,b,ch,re,ch,b],
            [b,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,b,b,b,b,b],
            [b,r,r,r,r,r,r,r,r,d,r,s,r,r,r,r,r,r,sb,r,r,n3,b],
            [b,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,b,b,b,b,b],
            [b,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,b],
            [b,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,b],
            [b,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,b],
            [b,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,b],
            [b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b]]

root = Tk()
root.geometry("1200x900")
password = StringVar()
nickname = StringVar()
lvlinfo = (nickname2,"|","lvl",lvl,"*",cuteness)
road = ImageTk.PhotoImage(Image.open("road.png"))
wall = ImageTk.PhotoImage(Image.open("wall.png"))
market = ImageTk.PhotoImage(Image.open("market.png"))
clothesshop = ImageTk.PhotoImage(Image.open("clothesshop.png"))
casino = ImageTk.PhotoImage(Image.open("casino.png"))
zerologo = ImageTk.PhotoImage(Image.open("zerologo.png"))
takecard = ImageTk.PhotoImage(Image.open("zerocards.png"))
workcat = ImageTk.PhotoImage(Image.open("workcat.png"))
work = ImageTk.PhotoImage(Image.open("work.png"))
parking = ImageTk.PhotoImage(Image.open("parking.png"))
barrier = ImageTk.PhotoImage(Image.open("barrier.png"))
susbarrier = ImageTk.PhotoImage(Image.open("susbarrier.png"))
forsale = ImageTk.PhotoImage(Image.open("forsalesign.png"))
home = ImageTk.PhotoImage(Image.open("home.png"))
storage = ImageTk.PhotoImage(Image.open("storage.png"))
petshop = ImageTk.PhotoImage(Image.open("petshop.png"))
misskitty = ImageTk.PhotoImage(Image.open("misskitty.png"))
teacher = ImageTk.PhotoImage(Image.open("teacher.png"))
torgi = ImageTk.PhotoImage(Image.open("torskin.png"))
cybercat = ImageTk.PhotoImage(Image.open("cybercat.png"))
school = ImageTk.PhotoImage(Image.open("school.png"))
roomexit = ImageTk.PhotoImage(Image.open("roomexit.png"))
board = ImageTk.PhotoImage(Image.open("board.png"))
chair = ImageTk.PhotoImage(Image.open("chair.png"))
dabloonshop = ImageTk.PhotoImage(Image.open("dabloonshop.png"))
indexlist = ["road","market","barrier","work","clothesshop","parking","forsale","NPC1","casino","storage","school","roomexit","home","NPC2","board","chair","dabloonshop","petshop","susbarrier","NPC3","NPC4"]
imagelist = [road,market,barrier,work,clothesshop,parking,forsale,misskitty,casino,storage,school,roomexit,home,teacher,board,chair,dabloonshop,petshop,susbarrier,torgi,cybercat]
catollarsimage2 = ImageTk.PhotoImage(Image.open("catollarsimage2.png"))
healthimage = ImageTk.PhotoImage(Image.open("healthimage.png"))
healthimage2 = ImageTk.PhotoImage(Image.open("healthimage2.png"))
cutenessimage = ImageTk.PhotoImage(Image.open("cutenessimage.png"))
cutenessimage2 = ImageTk.PhotoImage(Image.open("cutenessimage2.png"))
Credits = ImageTk.PhotoImage(Image.open("Credits.png"))
xpimage = ImageTk.PhotoImage(Image.open("xpimage.png"))
milk = ImageTk.PhotoImage(Image.open("milk.png"))
coffee = ImageTk.PhotoImage(Image.open("coffee.png"))
banana = ImageTk.PhotoImage(Image.open("banana.png"))
burger = ImageTk.PhotoImage(Image.open("burger.png"))
salad = ImageTk.PhotoImage(Image.open("salad.png"))
watermelon = ImageTk.PhotoImage(Image.open("watermelon.png"))
potion1 = ImageTk.PhotoImage(Image.open("potion1.png"))
potion2 = ImageTk.PhotoImage(Image.open("potion2.png"))
potion3 = ImageTk.PhotoImage(Image.open("potion3.png"))
foodimagelist = [milk,coffee,banana,burger,salad,watermelon,potion1,potion2]
scooter = ImageTk.PhotoImage(Image.open("car0skin.png"))
lookingcat = ImageTk.PhotoImage(Image.open("lookingcat.png"))
foodbox = ImageTk.PhotoImage(Image.open("foodbox.png"))
capsule = ImageTk.PhotoImage(Image.open("capsule.png"))
moneybox = ImageTk.PhotoImage(Image.open("moneybox.png"))
diamondbox = ImageTk.PhotoImage(Image.open("diamondbox.png"))
exitbtn = ImageTk.PhotoImage(Image.open("exit.png"))
leftbtn = ImageTk.PhotoImage(Image.open("left.png"))
rightbtn = ImageTk.PhotoImage(Image.open("right.png"))
onebtn = ImageTk.PhotoImage(Image.open("oneicon.png"))
zerobtn = ImageTk.PhotoImage(Image.open("zeroicon.png"))
okbtn = ImageTk.PhotoImage(Image.open("okicon.png"))
TTT= ImageTk.PhotoImage(Image.open("TTT.png"))
TTTX = ImageTk.PhotoImage(Image.open("tttX.png"))
TTTO = ImageTk.PhotoImage(Image.open("tttO.png"))
screen1 = Button ( root, text =  "", command =  WA )
screen1.place ( x = 0, y = 0, width = 300, height = 300)
screen2 = Button ( root, text =  "", command =  W )
screen2.place ( x = 300, y = 0, width = 300, height = 300)
screen3 = Button ( root, text =  "", command =  WD )
screen3.place ( x = 600, y = 0, width = 300, height = 300)
screen4 = Button ( root, text =  "", command =  A )
screen4.place ( x = 0, y = 300, width = 300, height = 300)
cat = ImageTk.PhotoImage(Image.open("Catlifecat.png"))
braincat = ImageTk.PhotoImage(Image.open("braincatskin.png"))
yoda = ImageTk.PhotoImage(Image.open("skinyoda.png"))
duckitty = ImageTk.PhotoImage(Image.open("duckittyskin.png"))
human = ImageTk.PhotoImage(Image.open("human.png"))
dbcat = ImageTk.PhotoImage(Image.open("dablooncat.png"))
summercat = ImageTk.PhotoImage(Image.open("Summercat.png"))
maxwell = ImageTk.PhotoImage(Image.open("maxwell.png"))
burgerocat = ImageTk.PhotoImage(Image.open("burgerocat.png"))
ghostcat = ImageTk.PhotoImage(Image.open("Ghostcat.png"))
starcat = ImageTk.PhotoImage(Image.open("starcat.png"))
scooter = ImageTk.PhotoImage(Image.open("car0skin.png"))
skinlist = [[cat,2,0,0,"Looks kinda odd...","common"],[duckitty,0,1000,0,"Will come for your bread","rare"],[summercat,0,5000,0,"Summer enjoyer","superrare"],[misskitty,0,5000,0,"Came straight from 50s","superrare"],[teacher,0,6500,0,"80% Useless","epic"],[human,0,6666,0,"He broke the 4th wall","epic"],[cybercat,0,10101,0,"I will come back(he wont)","legendary"],[yoda,0,11111,0,"GREEEEEEEEEEEEN","legendary"],[torgi,0,12345,0,"What the dog is doin?","legendary"],[braincat,0,9999999,0,"Definetly CAN play chess","special"],[ghostcat,0,9999999,0,"Main hero in all horrors","special"],[dbcat,0,9999999,0,"4 Dabloons,last offer","special"],[starcat,0,9999999,0,"Be proud about your achievments","special"],[maxwell,0,9999999,0,"Rotates when happy","special"],[burgerocat,0,9999999,0,"Double with cheese and bacon","special"],[scooter,0,1000,0.2]]
brainpet = ImageTk.PhotoImage(Image.open("brainpet.png"))
yodapet = ImageTk.PhotoImage(Image.open("yodapet.png"))
phonepet = ImageTk.PhotoImage(Image.open("phonepet.png"))
kittenpet = ImageTk.PhotoImage(Image.open("kittenpet.png"))
ghostpet = ImageTk.PhotoImage(Image.open("ghostpet.png"))
smilepet = ImageTk.PhotoImage(Image.open("smilepet.png"))
petlist = [[brainpet,0,"in case yours dont work"],[yodapet,0,"he protecc"],[phonepet,0,"yeah i got friends"],[kittenpet,0,"its you!"],[ghostpet,0,"BOO!"],[smilepet,0,"welcome to glaggleland"]]
screen5 = Button ( root, text =  "",image = cat, command =  NYA )
screen5.place ( x = 300, y = 300, width = 300, height = 300)
screen6 = Button ( root, text =  "", command =  D)
screen6.place ( x = 600, y = 300, width = 300, height = 300)
screen7 = Button ( root, text =  "", command =  SA )
screen7.place ( x = 0, y = 600, width = 300, height = 300)
screen8 = Button ( root, text =  "", command =  S )
screen8.place ( x = 300, y = 600, width = 300, height = 300)
screen9 = Button ( root, text =  "", command =  SD)
screen9.place ( x = 600, y = 600, width = 300, height = 300)
subtext = Button ( root,bg = "grey", text =  "")
subtext.place ( x = 550, y = 550, width = 50, height = 50)
s = ttk.Style()
s.theme_use('clam')
s.configure("blue.Horizontal.TProgressbar", foreground='blue', background='blue')
lvlstat2 = ttk.Progressbar(root,orient='horizontal', style="blue.Horizontal.TProgressbar",mode='determinate',length=200)
lvlstat2.place(x=0, y=20)
lvlstat2['value'] = xp/10
lvlstat = Button ( root, text =  lvlinfo,command = xproadopen)
lvlstat.place ( x = 0, y = 0, width = 200, height = 20)
s = ttk.Style()
s.theme_use('clam')
s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
healthstat2 = ttk.Progressbar(root,orient='horizontal', style="green.Horizontal.TProgressbar",mode='determinate',length=100)
healthstat2.place(x=200, y = 20)
healthstat2['value'] = health
healthstat = Button ( root, text =  "Health")
healthstat.place ( x = 200, y = 0, width = 100, height = 20)
s = ttk.Style()
s.theme_use('clam')
s.configure("yellow.Horizontal.TProgressbar", foreground='yellow', background='yellow')
energystat2 = ttk.Progressbar(root,orient='horizontal', style="yellow.Horizontal.TProgressbar",mode='determinate',length=100)
energystat2.place(x=300, y=20)
energystat2['value'] = energy
energystat = Button ( root, text =  "Energy")
energystat.place ( x = 300, y = 0, width = 100, height = 20)
foodstat = Button ( root, text =  "⚫⚫⚫")
foodstat.place ( x = 400, y = 0, width = 50, height = 40)
timestat1 = Button ( root, text =  timeinfo)
timestat1.place ( x = 450, y = 0, width = 50, height = 20)
timestat2 = Button ( root, text =  dayinfo)
timestat2.place ( x = 450, y = 20, width = 50, height = 20)
catollarsicon = ImageTk.PhotoImage(Image.open("catollarsicon.png"))
catollarsstat = Button ( root, text =  "",image = catollarsicon)
catollarsstat.place ( x = 600, y = 0, width = 50, height = 40)
catollarsstat2 = Button ( root, text =  catollars)
catollarsstat2.place ( x = 650, y = 0, width = 100, height = 40)
gemsicon = ImageTk.PhotoImage(Image.open("gemsicon.png"))
gemsstat = Button ( root, text =  "",image = gemsicon)
gemsstat.place ( x = 750, y = 0, width = 50, height = 40)
gemsstat2 = Button ( root, text =  gems)
gemsstat2.place ( x = 800, y = 0, width = 100, height = 40)
donimg = ImageTk.PhotoImage(Image.open("DON.png"))
menuup = ImageTk.PhotoImage(Image.open("menuup.png"))
menuupbtn = Button ( root, text =  "",image = menuup, command =  menu1 )
menuupbtn.place ( x = 900, y = 0, width = 300, height = 150)
menudown = ImageTk.PhotoImage(Image.open("menudown.png"))
menudownbtn = Button ( root, text =  "",image = menudown, command =  menu2 )
menudownbtn.place ( x = 900, y = 300, width = 300, height = 150)
backpackbutton = ImageTk.PhotoImage(Image.open("backpackbtn.png"))
backpackbtn = Button ( root, text =  "",image = backpackbutton, command =  backpackopen )
backpackbtn.place ( x = 900, y = 150, width = 300, height = 150)
dtbutton  = ImageTk.PhotoImage(Image.open("dtbtn.png"))
codevaultbutton  = ImageTk.PhotoImage(Image.open("codevaultbtn.png"))
cattlepassbutton  = ImageTk.PhotoImage(Image.open("cattlepassbtn.png"))
achbutton  = ImageTk.PhotoImage(Image.open("achbtn.png"))
savebutton  = ImageTk.PhotoImage(Image.open("savebtn.png"))
databasee = sql.connect('catlife.db')
database = databasee.cursor()
database.execute("CREATE TABLE IF NOT EXISTS `catlife` (`nickname` STRING, `password` STRING, `xplace` STRING, `yplace` STRING, `xp` STRING, `lvl` STRING, `catollars` STRING)")
mapupdate()
