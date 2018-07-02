# -*- coding: utf-8 -*-

#  「 From Helloworldd / Edited by Puy 」 "
# ID : yapuy

from PUY.linepy import *
from PUY.akad.ttypes import Message
from PUY.akad.ttypes import ContentType as Type
from time import sleep
from datetime import datetime, timedelta
from googletrans import Translator
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, subprocess, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit

#puy = LINE() 
#puy = LINE("Eu3uZTYkIRM2fSpwaDw4.hv+9sZ7pkk5jYglvNr+V1a.VhhW/7dJnrAmDhL7sIZ/jQC64HM9Uz84BTnpLcHVcHQ=")    # UNTUK LOGIN TOKEN #
puy = LINE("EutMtZ9ix0jmdz8VyI3c.NNBWxvmEnnLSJ4NTVieR3a.myMZxpliibs+u/r/pGl6ClnktOWq5L+M+gwh6BVodMY=")
#puy = LINE('','')      # UNTUK LOGIN MAIL LINE #
puyMid = puy.profile.mid
puyProfile = puy.getProfile()
puySettings = puy.getSettings()
puyPoll = OEPoll(puy)

#pi = LINE()
#pi = LINE("EumLwjR7X3GGXQXoaBmc.NNBWxvmEnnLSJ4NTVieR3a.eGR/JaDeSKbGfXG8pBVL4CgcSDrV+WojdxKKXf3xJaU=")
#piMid = pi.profile.mid
#piProfile = pi.getProfile()
#piSettings = pi.getSettings()
#piPoll = OEPoll(pi)
botStart = time.time()

msg_dict = {}

qrprotect = []
inviteprotect = []
protect = []
cancelprotect = []

Bots = [puy]
Creator = ["uac8e3eaf1eb2a55770bf10c3b2357c33"]
Owner = ["uac8e3eaf1eb2a55770bf10c3b2357c33"]
Admin = ["uac8e3eaf1eb2a55770bf10c3b2357c33"]

#unsendOpen = codecs.open("unsend.json","r","utf-8")

settings = {
    "autoJoin": True,
    "autoLeave": False,
    "autoRead": False,
    "Inroom": True,
    "autoAdd": False,
    "Outroom": True,
    "detectMention": True,
    "autoJoinTicket": True,
    "detectUnsend": False,
    "autoAddMessage": "@!, Thx for add",
    "autoJoinMessage": "@!, makasih sudah invite saya",
    "autoResponMessage": "Hey @!, Don't Tag.",
    "reread": True,
    "responMention": True,
    "addSticker": {
        "name": "",
        "status": False
    },
    "blacklist": {},
    "timeRestart": "18000",
    "changeGroupPicture": [],
    "limit": 50,
    "limits": 50,
    "wordban": [],
    "crashMention": True,
    "autoRespon": True,
    "keyCommand": "",
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "setKey": False,
    "unsendMessage": True
}

message = {
    "replyPesan": "Don't tag me,It's annoying."
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.unsend())
    with open("sticker.json","r") as f:
        stickers = json.loads(f)
        for sticker in stickers:
            if text.lower() == sticker:
                sid = stickers[sticker]["STKID"]
                spkg = stickers[sticker]["STKPKGID"]
                sver = stickers[sticker]["STKVER"]
                puy.sendSticker(to, sver, spkg, sid)
except:
    print("PUY")

settings["myProfile"]["displayName"] = puyProfile.displayName
settings["myProfile"]["statusMessage"] = puyProfile.statusMessage
settings["myProfile"]["pictureStatus"] = puyProfile.pictureStatus
coverId = puy.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)

def autoRestart():
    if time.time() - botStart > int(settings["timeRestart"]):
        time.sleep(5)
        restartBot()

def getRecentMessages(self, messageBox, count):
      return self.Talk.puy.getRecentMessages(messageBox.id, count)

def unsendMessage(self, messageId):
    self._unsendMessageReq += 1
    return self.talk.unsendMessage(self._unsendMessageReq, messageId)

def sendMentionFooter(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Meka Finee "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    puy.sendMessage(to, textx, {'AGENT_NAME':'@Muh.khadaffy on Instagram', 'AGENT_LINK': 'https://www.instagram.com/muh.khadaffy', 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + puy.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)    
    #'AGENT_LINK': 'line://ti/p/~{}'.format(puy.getProfile().userid),

def backupData():
    try:
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = unsend
        f = codecs.open('unsend.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    puy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)    

def unsMes(id):
    puy.unsendMessage(id)
    for i in Mid:
        thread1 = threading.Thread(target=unsMes, args=(i,))
        thread1.start()
        thread1.join()
    puy.sendMessage(to, '「 Unsend {} message 」'.format(len(Mid)))

def siderMembers(to, mid):
    arrData = ""
    textx = "Sider User\nHii ".format(str(len(mid)))
    arr = []
    no = 1
    num = 2
    for i in mid:
        mention = "@x\n"
        slen = str(len(textx))
        elen = str(len(textx) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':i}
        arr.append(arrData)
        textx += mention+settings["mention"]
        if no < len(mid):
            no += 1
            textx += "%i. " % (num)
            num=(num+1)
        else:
            try:
                no = "\nâ•šâ•â•[ {} ]".format(str(puy.getGroup(to).name))
            except:
                no = "\nâ•šâ•â•[ Success ]"
    puy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def sendMessageWithFooter(to, text, name, url, iconlink):
        contentMetadata = {
            'AGENT_NAME': name,
            'AGENT_LINK': url,
            'AGENT_ICON': iconlink
        }
        return puy.sendMessage(to, text, contentMetadata, 0)
    
def sendMessageWithFooter(to, text):
 puy.reissueUserTicket()
 dap = puy.getProfile()
 ticket = "http://line.me/ti/p/"+puy.getUserTicket().id
 pict = "http://dl.profile.line-cdn.net/"+dap.pictureStatus
 name = dap.displayName
 dapi = {"AGENT_ICON": pict,
     "AGENT_NAME": name,
     "AGENT_LINK": ticket
 }
 puy.sendMessage(to, text, contentMetadata=dapi)
    
def sendMessageWithContent(to, name, link, url, iconlink):
        contentMetadata = {
            'AGENT_NAME': name,
            'AGENT_LINK': url,
            'AGENT_ICON': iconlink
            }
        return self.sendMessage(to, text, contentMetadata, 0)    
    
def logError(text):
    puy.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                puy.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    puy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def helpmessage():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpMessage =   "\n  「 PUY  」     " + "\n" + \
                    " " + key + "1) About puy " + "\n" + \
                    " " + key + "2) Token" + "\n" + \
                    " " + key + "3) Keluar" + "\n" + \
                    " " + key + "4) helpMedia" + "\n" + \
                    "   - Setautoadd: " + "\n" + \
                    "   - Setautojoin: " + "\n" + \
                    "   - Setautoreply: " + "\n\n" + \
                    " " + key + " 「 CEKSIDER & MENTION  」" + "\n" + \
                    " " + key + "5) Ceksider On/Off - [For SetRead]" + "\n" + \
                    " " + key + "6) Ceksider reset - [For Reset reader point]" + "\n" + \
                    " " + key + "7) Ceksider - [For Ceksider]" + "\n\n" + \
                    " Creator : @!" + "\n" + \
                    "   「 Use " + key + " For the Prefix 」" + "\n" + \
                    " 「 From Helloworld / Edited by Puy 」"
    return helpMessage

def helpmedia():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpMedia =   "\n  「 MEDIA  」     " + "\n" + \
                    " " + key + "8)  InstaInfo (Username)" + "\n" + \
                    " " + key + "9)  InstaStory (Username*number)" + "\nExam :" + key +"Instastory muh.khadaffy*1\n" + \
                    " " + key + "10) Quotes" + "\n" + \
                    " " + key + "11) Carigambar (text)" + "\n" + \
                    " " + key + "12) CariMusik (text)" + "\n" + \
                    " " + key + "13) CariLirik (text)" + "\n" + \
                    " " + key + "14) DoujinSearch (text)" + "\n" + \
                    " " + key + "15) YoutubeSearch (text)" + "\n\n" + \
                    " Creator : @!" + "\n" + \
                    "  「 Use" + key + "For the Prefix 」" + "\n" + \
                    " 「 From Helloworld / Edited by Puy 」"
    return helpMedia
	
def puyBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return

        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                puy.findAndAddContactsByMid(op.param1)
            puy.sendMention(op.param1, settings["autoAddMessage"], [op.param1])
                
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            if settings["autoJoin"] and puyMid in op.param3:
                puy.acceptGroupInvitation(op.param1)
                puy.sendMention(op.param1, settings["autoJoinMessage"], [op.param2])

        if op.type == 19:
            print ("[ 19 ] NOTIFIED KICKOUT FROM GROUP")
            group = puy.getGroup(op.param1)
            contact = puy.getContact(op.param2)
            victim = puy.getContact(op.param3)
            dap = "   Group Name : {}".format(str(group.name))
            dapp = "\n   Executor : {}".format(str(contact.displayName))
            dappp = "\n   Victim : {}".format(str(victim.displayName))
            puy.sendMessage(op.param1, "「 Notify Kickout From Group 」\n\nPelaku Kick : {}\nK{}".format(str(contact.displayName),"orban Kick : {}".format(str(victim.displayName))))
            puy.sendContact(op.param1, op.param2)
            puy.sendContact(op.param1, op.param3)
            print (dap)
                
        if op.type in [22, 24]:
            print ("[ 22 And 24 ] NOTIFIED INVITE INTO ROOM & NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                dan = puy.getContact(op.param2)
                tgb = puy.getGroup(op.param1)
                sendMention(op.param2, "@! hmm?", [sender])
                puy.leaveRoom(op.param1)
                                
        if op.type == 26:
            try:
                print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != puy.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if cmd == "help":
                                helpMessage = helpmessage()
                                poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                creator = puy.getContact(poey)
                                #puy.sendMessage(to, str(helpMessage),{'AGENT_ICON':'http://dl.profile.line-cdn.net/0h-uTmd0A5clppFF8EVusNDVVRfDceOnQSEXppOktDLW4RIDcMAXA4aUQTfmMTLT1YACFvNUwXfz8W','AGENT_LINK':'https://line.me/ti/p/~yapuy','AGENT_NAME':'Help Message'})
                                sendMention(to, str(helpMessage), [poey])
                                #sendMention(to, str(helpMessage), "@!", [mid])
                                #sendMention(sender, "Creator\n@!", (str(helpMessage), [sender]))
                                #sendMention(sender, mid, [sender])
                                #sendMention(to, 'Creator : '+ac+'puy', (str(helpMessage), [sender]))

                            if cmd == "helpmedia":
                                helpMedia = helpmedia()
                                poeyy = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                creator = puy.getContact(poeyy)
                                sendMention(to, str(helpMedia), [poeyy])
                            
                            elif cmd == "token generator":
                                sendMentionFooter(to, "「 TOKEN TIPE  」\n1* DESKTOPWIN\n2* WIN10\n3* DESKTOPMAC\n4* IOSPAD\n5* CHROME\n\n*Usage : Type #login with Token Type\n\n*Example : #login chrome\n\n[ From BotEater / Edited by Puy ]\n@! - Selamat Mencoba.", [sender])
                            elif cmd == "#token":
                                sendMentionFooter(to, "「 TOKEN TIPE  」\n1* DESKTOPWIN\n2* WIN10\n3* DESKTOPMAC\n4* IOSPAD\n5* CHROME\n\n*Usage : Type #login with Token Type\n\n*Example : #login chrome\n\n[ From BotEater / Edited by Puy ]\n@! - Selamat Mencoba.", [sender])
                                
                            elif cmd == "speed":
                              if sender in Owner:
                                start = time.time()
                                puy.sendMessage(to, "...")
                                elapsed_time = time.time() - start
                                puy.sendMessage(to, "[ Speed ]\nKecepatan mengirim pesan {} detik puy".format(str(elapsed_time)))

                            elif cmd == "logout":
                              if sender in Owner:
                                puy.sendMessage(to, "PUY telah dimatikan")
                                sys.exit("[ INFO ] BOT SHUTDOWN")
                                return

                            elif cmd == "perbarui":
                              if sender in Owner:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                Timed = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                #if msg.to not in read['readPoint']:
                                    #dap.sendMessage(msg.to, "「 NOTIFIED BOT SPEED 」\n\n" + Timed)
                                #sendMention(to, "@! \nPUY berhasil diperbarui.\n\nPada :\n" + Timed, [sender])
                                puy.sendMessage(to, "PUY berhasil diperbarui.\n\nPada :\n" + Timed)
                                restartBot()
                              else:
                                  puy.sendMessage("Permission Denied")

                            elif cmd.startswith("spamcall"):
                              if sender in Owner:
                                if msg.toType == 2:
                                   group = puy.getGroup(to)
                                   members = [mem.mid for mem in group.members]
                                   jmlh = int(settings["limit"])
                                   puy.sendMessage(msg.to, "Invitation Call Groups {} In Progress ".format(str(settings["limit"])))
                                   if jmlh <= 9999:
                                    for x in range(jmlh):
                                     try:
                                        puy.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        puy.sendMessage(msg.to,str(e))
                                    else:
                                        puy.sendMessage(msg.to,"Invitation Call Groups Successed")                                  
                                  
                            elif cmd[:15] == "pengagumrahasia":
                                name = cmd[16:]
                                r = requests.get("http://planetbiru.com/ramalan/ramalan-pengagum/?nama="+name).content
                                data =BeautifulSoup(r, 'html5lib');tgb="[ Pengagum Rahasia {} ]\n\n".format(name);numz=[0, 1,2,3,4]
                                num = [dan for dan in data.findAll('div', {'class':'pmeter'})]
                                jdl = [wil for wil in data.findAll('div', {'class':'plabel'})]
                                for numm in numz:
                                 tgb += "{} [ {} ]\n".format(jdl[numm].text, num[numm].text.replace("\n",""))
                                tgb+="\n[ Finish ]"
                                sendMessageWithFooter(to, str(tgb))                                  
                                  
                            elif cmd == "me":
                                contact = puy.getContact(sender)
                                sendMentionFooter(to, "At here @!", [sender])
                                puy.sendContact(to, sender)
                                puy.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))                                                        
                                  
                            elif cmd == "autojoin on":
                              if msg._from in Owner:
                                settings["autoJoin"] = True
                                sendMention(to, "[ Notified Auto Join ]\nBerhasil mengaktifkan Auto Join @!", [sender])
                            elif cmd == "autojoin off":
                              if msg._from in Owner:
                                settings["autoJoin"] = False
                                sendMention(to, "[ Notified Auto Join ]\nBerhasil menonaktifkan Auto Join @!", [sender])
                            elif cmd == "autoread on":
                              if msg._from in Owner:
                                settings["autoRead"] = True
                                sendMention(to, "[ Notified Auto Join ]\nBerhasil mengaktifkan Auto Read @!", [sender])
                            elif cmd == "autoread off":
                              if msg._from in Owner:
                                settings["autoRead"] = False
                                sendMention(to, "[ Notified Auto Join ]\nBerhasil menonaktifkan Auto Read @!", [sender])                                
                            elif cmd == "replymention on":
                                settings["responMention"] = True
                                sendMention(to, "[ Notified Auto Leave ]\nBerhasil mengaktifkan responMention @!", [sender])
                            elif cmd == "replymention off":
                              if msg._from in Owner:
                                settings["responMention"] = False
                                sendMention(to, "[ Notified Auto Leave ]\nBerhasil menonaktifkan responMention @!", [sender])
                            elif cmd == "detectunsend on":
                              if msg._from in Owner:
                                settings["detectUnsend"] = True
                                sendMention(to, "[ Notified Detect Unsend ]\nBerhasil mengaktifkan Detect Unsend\n@!", [sender])
                            elif cmd == "detectunsend off":
                              if msg._from in Owner:
                                settings["detectUnsend"] = False
                                sendMention(to, "[ Notified Detect Unsend ]\nBerhasil menonaktifkan Detect Unsend\n@!", [sender])
                            elif cmd == "autoleave on":
                              if msg._from in Owner:
                                settings["autoLeave"] = True
                                sendMention(to, "[ Notified Auto Leave ]\nBerhasil mengaktifkan Auto leave @!", [sender])
                            elif cmd == "autoleave off":
                              if msg._from in Owner:
                                settings["autoLeave"] = False
                                sendMention(to, "[ Notified Auto Leave ]\nBerhasil menonaktifkan Auto leave @!", [sender])
                            elif cmd == "status":
                                try:
                                    ret_ = "\n   PUY STATUS"
                                    if settings["autoJoin"] == True: ret_ += "\n   [ ON ] Auto Join"
                                    else: ret_ += "\n   [ OFF ] Auto Join"
                                    if settings["autoRead"] == True: ret_ += "\n   [ ON ] Auto Read"
                                    else: ret_ += "\n   [ OFF ] Auto Read"
                                    if settings["detectUnsend"] == True: ret_ += "\n   [ ON ] Detect Unsend"
                                    else: ret_ += "\n   [ OFF ] Detect Unsend"
                                    if settings["detectUnsend"] == True: ret_ += "\n   [ ON ] Detect Unsend"
                                    else: ret_ += "\n   [ OFF ] Detect Unsend"
                                    if settings["responMention"] == True: ret_ += "\n   [ ON ] ReplyMention"
                                    else: ret_ += "\n   [ OFF ] ReplyMention"
                                    if settings["autoLeave"] == True: ret_ += "\n   [ ON ] Auto Leave Room"
                                    else: ret_ += "\n   [ OFF ] Auto Leave Room"
                                    ret_ +="\n  Add Friends Messages : {}".format(settings["autoAddMessage"])
                                    ret_ +="\n  Join Groups Messages : {}".format(settings["autoJoinMessage"])
                                    ret_ +="\n  Auto Reply Mention : {}".format(settings["autoResponMessage"])
                                    sendMessageWithFooter(to, str(ret_))
                                except Exception as e:
                                    sendMessageWithFooter(to, str(e))
              ## LURKING ##                      
                            elif text.lower() == '#ceksider on':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read['readPoint']:
                                        try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                        except:
                                            pass
                                        read['readPoint'][msg.to] = msg.id
                                        read['readMember'][msg.to] = ""
                                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                        read['ROM'][msg.to] = {}
                                        with open('read.json', 'w') as fp:
                                            json.dump(read, fp, sort_keys=True, indent=4)
                                            puy.sendMessage(to, "「 Ceksider Diaktifkan 」\n\nWaktu :\n" + readTime)
                                else:
                                    try:
                                        del read['readPoint'][msg.to]
                                        del read['readMember'][msg.to]
                                        del read['readTime'][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][msg.to] = msg.id
                                    read['readMember'][msg.to] = ""
                                    read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                    read['ROM'][msg.to] = {}
                                    with open('read.json', 'w') as fp:
                                        json.dump(read, fp, sort_keys=True, indent=4)
                                        #sendMention(to, "@!\n「 Ceksider Diaktifkan 」\n" + readTime, [sender])
                                        puy.sendMessage(to, "「 Ceksider Diaktifkan 」\n\n" + readTime)
                            
                            elif text.lower() == '#ceksider off':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to not in read['readPoint']:
                                    #sendMention(to, "「 Ceksider telah dimatikan  」\n@!\nWaktu :\n" + readTime, [sender])
                                    puy.sendMessage(to, "「 Ceksider telah dimatikan  」\n\nWaktu :\n" + readTime)
                                else:
                                    try:
                                        del read['readPoint'][msg.to]
                                        del read['readMember'][msg.to]
                                        del read['readTime'][msg.to]
                                    except:
                                          pass
                                    #sendMention(to, "「 Ceksider telah dimatikan  」\n@!\n" + readTime, [sender])
                                    puy.sendMessage(to, "「 Ceksider telah dimatikan  」\n\n" + readTime)
        
                            elif text.lower() == '#ceksider reset':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read["readPoint"]:
                                    try:
                                        del read["readPoint"][msg.to]
                                        del read["readMember"][msg.to]
                                        del read["readTime"][msg.to]
                                    except:
                                        pass
                                    #sendMention(to, "「 Mengulangi riwayat pembaca 」 :\n@!\n" + readTime, [sender])
                                    puy.sendMessage(to, "「 Ceksider telah direset 」\n\n" + readTime)
                                else:
                                    #sendMention(to, "「 Ceksider belum diaktifkan 」\n@!", [sender])
                                    puy.sendMessage(to, "「 Ceksider telah direset 」\n\n" + readTime)

                            elif text.lower() == '#ceksider':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        puy.sendMessage(receiver,"   「 Daftar Pembaca 」\nNone")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = puy.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = ' 「 Daftar Pembaca 」\n\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\n[ Waktu ] : \n" + readTime
                                    try:
                                        puy.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    puy.sendMessage(receiver,"*Ceksider belum diaktifkan\nKetik 「 #ceksider on 」 untuk mengaktifkan.")
                                     
                            elif text.lower() == '#lurking':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        puy.sendMessage(receiver,"[ Reader ]:\nNone")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = puy.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '   「 Daftar Pembaca 」\n\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\n[ Waktu ] : \n" + readTime
                                    try:
                                        puy.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    #sendMention(receiver,"*Ceksider belum diaktifkan\nKetik 「 #ceksider on 」 untuk mengaktifkan\n@!")
                                    puy.sendMessage(receiver,"*Ceksider belum diaktifkan\nKetik 「 #ceksider on 」 untuk mengaktifkan.")
                                    
                            elif cmd.startswith("#keluar"):
                                #tgb = puy.getGroup(op.param1)
                                #dan = puy.getContact(op.param2)
                                #gid = puy.getGroup(to)
                                puy.sendMessage(to, "Gbye")
                                #sendMentionFooter(op.param1, "@!, Gbye", [op.param2])
                                puy.getGroupIdsJoined()
                                puy.leaveGroup(to)
                                         
                            elif cmd.startswith("bc: "):
                              if msg._from in Owner:
                                sep = text.split(" ")
                                pesan = text.replace(sep[0] + " ","")
                                saya = puy.getGroupIdsJoined()
                                for group in saya:
                                   sendMessageWithFooter(group,"" + str(pesan))
####SC#####

                            elif cmd.startswith("carimusik "):
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                cond = query.split("*")
                                search = str(cond[0])
                                url = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = url.json()
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "  [ Result Music ]"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n  {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n  [ Total {} Music ]".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk mengirim music, silahkan gunakan command {} CariMusik {}*1".format(str(setKey), str(search))
                                    puy.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        url = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = url.json()
                                        ret_ = "  [ Musik ]"
                                        ret_ += "\n  Judul : {}".format(str(data["result"]["song"]))
                                        ret_ += "\n  Album : {}".format(str(data["result"]["album"]))
                                        ret_ += "\n  Ukuran : {}".format(str(data["result"]["size"]))
                                        ret_ += "\n  Alamat : {}".format(str(data["result"]["mp3"][0]))
                                        puy.sendImageWithURL(to, str(data["result"]["img"]))
                                        puy.sendMessage(to, str(ret_))
                                        puy.sendAudioWithURL(to, str(data["result"]["mp3"][0]))

                            elif cmd.startswith("carilirik "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                cond = txt.split("*")
                                query = cond[0]
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0"
                                    url = web.get("https://www.musixmatch.com/search/{}".format(urllib.parse.quote(query)))
                                    data = BeautifulSoup(url.content, "html.parser")
                                    result = []
                                    for trackList in data.findAll("ul", {"class":"tracks list"}):
                                        for urlList in trackList.findAll("a"):
                                            title = urlList.text
                                            url = urlList["href"]
                                            result.append({"title": title, "url": url})
                                    if len(cond) == 1:
                                        ret_ = "   [ Musixmatch Result ]"
                                        num = 0
                                        for title in result:
                                            num += 1
                                            ret_ += "\n  {}. {}".format(str(num), str(title["title"]))
                                        ret_ += "\n  [ Total {} Lirik ]".format(str(len(result)))
                                        ret_ += "\n\nUntuk melihat lirik, silahkan gunakan command {} CariLirik {}*1".format(str(setKey), str(query))
                                        puy.sendMessage(to, ret_)
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(result):
                                            data = result[num - 1]
                                            with requests.session() as web:
                                                web.headers["user-agent"] = "Mozilla/5.0"
                                                url = web.get("https://www.musixmatch.com{}".format(urllib.parse.quote(data["url"])))
                                                data = BeautifulSoup(url.content, "html5lib")
                                                for lyricContent in data.findAll("p", {"class":"mxm-lyrics__content "}):
                                                    lyric = lyricContent.text
                                                    puy.sendMessage(to, lyric)

                            elif cmd.startswith("carigambar "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(txt))
                                data = url.json()
                                puy.sendImageWithURL(to, random.choice(data["result"]))
                                                    
                            elif cmd.startswith('About puy'):
                                try:
                                    arr = []
                                    Ownerz = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                    creator = puy.getContact(Ownerz)
                                    contact = puy.getContact(puyMid)
                                    grouplist = puy.getGroupIdsJoined()
                                    contactlist = puy.getAllContactIds()
                                    blockedlist = puy.getBlockedContactIds()
                                    #ret_ = "「 HELPER  」"
                                    #ret_ += "\n  Name : {}".format(contact.displayName)
                                    #ret_ += "\n  Group : {}".format(str(len(grouplist)))
                                    #ret_ += "\n  Friend : {}".format(str(len(contactlist)))
                                    #ret_ += "\n  Blocked : {}".format(str(len(blockedlist)))
                                    #ret_ += "\n  [ About Selfbot ]"
                                    #ret_ += "\n  Version : Premium"
                                    #ret_ += "\n  Creator : {}".format(creator.displayName)
                                    #ret_ += "\n  Creator : @!".format(Owner)
                                    #puy.sendMessage(to, str(ret_))
                                    sendMention(to, "「 About Puy 」\n\nThe Beginning of this Bot Comes from Helloworld, I'm just Reworked This!\nOf Course Special Thanks To HelloWorld, And the Friends Around Me!\n\nCreator : @!", [Ownerz])
                                except Exception as e:
                                    puy.sendMessage(msg.to, str(e))

                            elif cmd.startswith("instainfo"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("http://rahandiapi.herokuapp.com/instainfo/{}?key=betakey".format(txt))
                                data = url.json()
                                #icon = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/599px-Instagram_icon.png"
                                #name = "Instagram"
                                #link = "https://www.instagram.com/{}".format(data["result"]["username"])
                                result = "   [ Instagram Info ]"
                                result += "\n  Nama : {}".format(data["result"]["name"])
                                result += "\n  Username: {}".format(data["result"]["username"])
                                result += "\n  Bio : {}".format(data["result"]["bio"])
                                result += "\n  Pengikut : {}".format(data["result"]["follower"])
                                result += "\n  Mengikuti : {}".format(data["result"]["following"])
                                result += "\n  Privasi Acc : {}".format(data["result"]["private"])
                                result += "\n  Post : {}".format(data["result"]["mediacount"])
                                #result += "\n  [ Finish ]"
                                puy.sendImageWithURL(to, data["result"]["url"])
                                puy.sendMessage(to, result)

                            elif cmd.startswith("instastory "):
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                cond = query.split("*")
                                search = str(cond[0])
                                if len(cond) == 2:
                                    url = requests.get("http://rahandiapi.herokuapp.com/instastory/{}?key=betakey".format(search))
                                    data = url.json()
                                    num = int(cond[1])
                                    if num <= len(data["url"]):
                                        search = data["url"][num - 1]
                                        if search["tipe"] == 1:
                                            puy.sendImageWithURL(to, str(search["link"]))
                                        elif search["tipe"] == 2:
                                            puy.sendVideoWithURL(to, str(search["link"]))

                            elif cmd.startswith("youtubesearch "):
                                sep = text.split(" ")
                                txt = msg.text.replace(sep[0] + " ","")
                                cond = txt.split("*")
                                search = cond[0]
                                url = requests.get("http://api.w3hills.com/youtube/search?keyword={}&api_key=86A7FCF3-6CAF-DEB9-E214-B74BDB835B5B".format(search))
                                data = url.json()
                                if len(cond) == 1:
                                    no = 0
                                    result = "  [ Youtube Video Search ]"
                                    for anu in data["videos"]:
                                        no += 1
                                        result += "\n  {}. {}".format(str(no),str(anu["title"]))
                                    result += "\n [ Total {} Result ]\nUntuk melihat details video , silahkan gunakan command Youtubesearch text*1".format(str(len(data["videos"])))
                                    puy.sendMessage(to, result)
                                elif len(cond) == 2:
                                    num = int(str(cond[1]))
                                    if num <= len(data):
                                        search = data["videos"][num - 1]
                                        ret_ = "  [ Youtube Info ]"
                                        ret_ += "\n  Channel : {}".format(str(search["publish"]["owner"]))
                                        ret_ += "\n  Judul : {}".format(str(search["title"]))
                                        ret_ += "\n  Release : {}".format(str(search["publish"]["date"]))
                                        ret_ += "\n  Penonton : {}".format(str(search["stats"]["views"]))
                                        ret_ += "\n  Suka : {}".format(str(search["stats"]["likes"]))
                                        ret_ += "\n  Tidak Suka : {}".format(str(search["stats"]["dislikes"]))
                                        ret_ += "\n  Nilai : {}".format(str(search["stats"]["rating"]))
                                        ret_ += "\n  Deskripsi : {}".format(str(search["description"]))
                                        ret_ += "\n   [ {} ]".format(str(search["webpage"]))
                                        puy.sendImageWithURL(to, str(search["thumbnail"]))
                                        puy.sendMessage(to, str(ret_))
                                    
                            elif cmd == "quotes":
                                url = requests.get("https://botfamily.faith/api/quotes/?apikey=beta")
                                data = url.json()
                                result = "   [ Quotes ]"
                                result += "\n  Pembuat : {}".format(data["result"]["author"])
                                result += "\n  Kategori : {}".format(data["result"]["category"])
                                result += "\n  Quote : {}".format(data["result"]["quote"])
                                puy.sendMessage(to, result)

                            elif cmd == 'mentionall':
                                group = puy.getGroup(to)
                                midMembers = [contact.mid for contact in group.members]
                                midSelect = len(midMembers)//100
                                for mentionMembers in range(midSelect+1):
                                    no = 0
                                    ret_ = "  [ Mention Members ]"
                                    dataMid = []
                                    for dataMention in group.members[mentionMembers*100 : (mentionMembers+1)*100]:
                                        dataMid.append(dataMention.mid)
                                        no += 1
                                        ret_ += "\n  {}. @!".format(str(no))
                                    ret_ += "\n  [ Total {} Members]".format(str(len(dataMid)))
                                    sendMention(to, ret_, dataMid)

                            elif cmd.startswith("doujinsearch "):
                                     query = cmd.replace("doujinsearch ","")
                                     cond = query.split("|")
                                     search = str(cond[0])
                                     r = requests.get("https://nhentai.net/search/?&q={}".format(str(search)))
                                     soup = BeautifulSoup(r.content, 'html5lib')
                                     data = soup.findAll('div', attrs={'class':'gallery'})
                                     if len(cond) == 1:
                                         num = 0
                                         ret_ = "[ Doujin#Search ]"
                                         for dou in data:
                                             title = dou.find('a').text
                                             link = dou.find('a')['href']
                                             num += 1
                                             ret_ += "\n{}. {}".format(str(num), str(title))
                                             ret_ += "\nhttps://nhentai.net{}".format(str(link))
                                         ret_ += "\n\nType .doujin#search {}| (num)".format(str(search))                                        
                                         puy.sendMessage(to, str(ret_))
                                     elif len(cond) == 2:
                                         num = int(cond[1])
                                         if num <= len(data):
                                             dou = data[num - 1]                                       
                                             r = requests.get("https://nhentai.net{}".format(str(dou.find('a')['href'])))
                                             soup = BeautifulSoup(r.content, 'html5lib')                                           
                                             for sam in soup.findAll('img', attrs={'class':'lazyload'}):                        
                                                 path = sam.get('data-src')                                                
                                                 puy.sendImageWithURL(to,str(path))

                            elif cmd.startswith("sticker .add "):
                                loads()
                                global stickers
                                with open('sticker.json','r') as f:
                                    stickers = json.loads(f)                                                      
                                name = cmd.replace("sticker .add ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["addSticker"]["status"] = True
                                    settings["addSticker"]["name"] = name.lower()
                                    stickers[name.lower()] = {}
                                    f = codecs.open('sticker.json','w','utf-8')
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    puy.sendMessage(to," 「 Stickers 」\nType: Add Sticker\nStatus: Send a sticker to add to command {}.".format(name.lower()))
                                else:
                                    puy.sendMessage(to," 「 Stickers 」\nType: Add Sticker\nStatus: Sticker no to add to command {} because in the list.".format(name.lower()))
                            elif cmd.startswith("sticker .del "):                                
                                loads()                        
                                with open('sticker.json','r') as f:
                                    stickers = json.loads(f)                              
                                name = cmd.replace("sticker .del ","")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[name.lower()]
                                    f = codecs.open('sticker.json','w','utf-8')
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    puy.sendMessage(to," 「 Stickers 」\nType: Del Sticker\nStatus: Sticker to del to command {}.".format(name.lower()))
                                else:
                                    puy.sendMessage(to," 「 Stickers 」\nType: Del Sticker\nStatus: Sticker no to del to command {} because not in the list.".format(name.lower()))                                                 
                                                 
                            elif cmd.startswith("cancelpending"):
                                if msg.toType == 2:
                                    group = puy.getGroup(to)
                                    if group.invitee is None or group.invitee == []:
                                       puy.sendMessage(to, "Tidak ada pendingan")
                                    else:
                                        invitee = [contact.mid for contact in group.invitee]
                                        for inv in invitee:
                                           puy.cancelGroupInvitation(to, [inv])
                                           time.sleep(1)
                                        puy.sendMessage(to, "Berasil membatalkan undangan {} anggota.".format(str(len(invitee))))

                            elif cmd.startswith('gcancel'):
                                gid = puy.getGroupIdsInvited() 
                                start = time.time()
                                for i in gid:
                                    puy.rejectGroupInvitation(i)
                                elapsed_time = time.time() - start
                                puy.sendMessage(to, "Semua Undangan Dibatalkan")
                                puy.sendMessage(to, "Waktu: %s Seconds" % (elapsed_time))

                            elif "take" in msg.text:
                                list_ = msg.text.split(":")
                                try:
                                    puy.acceptGroupInvitationByTicket(list_[1],list_[2])
                                    G = puy.getGroup(list_[1])
                                    if G.preventedJoinByTicket == True:
                                        pass
                                    else:
                                        G.preventedJoinByTicket = True
                                        puy.updateGroup(G)
                                except:
                                    puy.sendMessage(msg.to,"error\n"+list_[1]+'\n'+list_[2])                                                                
                                
                            elif cmd.startswith("igpost"):
                                separate = msg.text.split(" ")
                                user = msg.text.replace(separate[0] + " ","")
                                profile = "https://www.instagram.com/" + user
                                with requests.session() as x:
                                    x.headers['user-agent'] = 'Mozilla/5.0'
                                    end_cursor = ''
                                    for count in range(1, 999):
                                        print('PAGE: ', count)
                                        r = x.get(profile, params={'max_id': end_cursor})
                        
                                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                                        j    = json.loads(data)
                        
                                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                                            if node['is_video']:
                                                page = 'https://www.instagram.com/p/' + node['code']
                                                r = x.get(page)
                                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                                print(url)
                                                puy.sendVideoWithURL(msg.to,url)
                                            else:
                                                print (node['display_src'])
                                                puy.sendImageWithURL(msg.to,node['display_src'])
                                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)

                            elif cmd.startswith("myautorespon"):
                                if message["replyPesan"] is not None:
                                    puy.sendMessage(to,"My Set AutoRespon : " + str(message["replyPesan"]))
                                else:
                                    puy.sendMessage(msg.to,"My Set AutoRespon : No messages are set")
                            elif cmd.startswith("responchange: "):
                                sep = msg.text.split(" ")
                                text = msg.text.replace(sep[0] + " ","")
                                try:
                                    message["replyPesan"] = text
                                    puy.sendMessage(to,"「 AutoRespon 」Changed to : " + text)
                                except:
                                    puy.sendMessage(to,"「 AutoRespon 」\nFailed to replace message")
                                    
                            elif cmd.startswith("responchanged: "):
                                sep = text.split(" ")
                                texts = text.replace(sep[0] + " ","")
                                if " " in texts:
                                    puy.sendMessage(to, "Tanpa spasi.")                                
                                else:
                                    message["replyPesan"] = str(texts).lower()
                                    #message["replyPesan"] = text
                                    sendMessageWithFooter(to, "Auto Respon has been Changed to [ {} ]".format(str(texts).lower()))

                        if text.lower() == 'login win10':
                            req = requests.get('https://api.eater.tech/WIN10')
                            a = req.text
                            b = json.loads(a)
                            tknop= codecs.open("tkn.json","r","utf-8")
                            tkn = json.load(tknop)
                            tkn['{}'.format(msg._from)] = []
                            tkn['{}'.format(msg._from)].append({
                            'qr': b['result'][0]['linkqr'],
                            'tkn': b['result'][0]['linktkn']
                                })
                            qrz = b['result'][0]['linkqr']
                            puy.sendMessage(to, 'Buka Link dibawah dan Tekan Login\n\n{}'.format(qrz))
                            #dap.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                            with open('tkn.json', 'w') as outfile:
                                json.dump(tkn, outfile)
                            tknop= codecs.open("tkn.json","r","utf-8")
                            tkn = json.load(tknop)
                            a = tkn['{}'.format(msg._from)][0]['tkn']
                            req = requests.get(url = '{}'.format(a))
                            b = req.text
                            aa = puy.getContact(sender).displayName
                            ab = puy.getGroup(msg.to).name
                            ac = puy.getContact(sender).mid
                            #sendMention(to, '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            puy.sendMessage(to, '「 WIN 10 」\nUntuk : '+aa+'\nDari Grup : '+ab+'\nMid Kamu : '+ac+'\n\n-「 TOKEN 」  : \n{}\n\n- UA : Line/8.3.2\n- LA : WIN10 8.8.3 PUY x64\n\n*「 From BotEater / Edited By PUY 」\n'.format(b))
                            #puy.sendMessage(receiver, '「 WIN 10 」\nUntuk : '+as+'\nDari Grup : '+ab+'\nMid Kamu : '+ac+'\n\n-「 TOKEN 」  : \n{}\n\n- UA : Line/8.3.2\n- LA : WIN10 8.8.3 NADYA-TJ x64\n\n*「 From NadyaTJ & BotEater / Edited By PUY 」\n@!'.format(b)
                             
                        if text.lower() == '#login chrome':
                            req = requests.get('https://api.eater.tech/CHROMEOS')                            
                            a = req.text
                            b = json.loads(a)
                            tknop= codecs.open("tkn.json","r","utf-8")
                            tkn = json.load(tknop)
                            tkn['{}'.format(msg._from)] = []
                            tkn['{}'.format(msg._from)].append({
                                'qr': b['result'][0]['linkqr'],
                                'tkn': b['result'][0]['linktkn']
                                })
                            qrz = b['result'][0]['linkqr']
                            puy.sendMessage(to, 'Buka Link dibawah dan Tekan Login\n\n{}'.format(qrz))
                            #dap.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                            with open('tkn.json', 'w') as outfile:
                                json.dump(tkn, outfile)
                            tknop= codecs.open("tkn.json","r","utf-8")
                            tkn = json.load(tknop)
                            a = tkn['{}'.format(msg._from)][0]['tkn']
                            req = requests.get(url = '{}'.format(a))
                            b = req.text
                            aa = puy.getContact(sender).displayName
                            ab = puy.getGroup(msg.to).name
                            ac = puy.getContact(sender).mid
                            #sendMention(to, '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            #dap.sendMessage(to,'「 CHROMEOS 」\nUntuk: '+aa+'\nFrom Group: '+ab+'\nMid User: '+ac+'\n\n- TOKEN : \n{}'.format(b))
                            sendMention(to,'「 CHROME 」\nUntuk : @!\nDari Grup : '+ab+'\nMid Kamu : '+ac+'\n\n-「 TOKEN 」  : \n{}\n\n- UA : Line/8.3.2\n- LA : CHROMEOS 8.8.3 PUY x64\n\n*「 From BotEater / Edited By PUY 」'.format(b), [sender])
                               
                        if text.lower() == '#login iospad':
                            req = requests.get('https://api.eater.tech/IOSPAD')
                            a = req.text
                            b = json.loads(a)
                            tknop= codecs.open("tkn.json","r","utf-8")
                            tkn = json.load(tknop)
                            tkn['{}'.format(msg._from)] = []
                            tkn['{}'.format(msg._from)].append({
                                'qr': b['result'][0]['linkqr'],
                                'tkn': b['result'][0]['linktkn']
                                })
                            qrz = b['result'][0]['linkqr']
                            puy.sendMessage(to, 'Buka Link dibawah dan Tekan Login\n\n{}'.format(qrz))
                            #puy.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                            with open('tkn.json', 'w') as outfile:
                                json.dump(tkn, outfile)
                            tknop= codecs.open("tkn.json","r","utf-8")
                            tkn = json.load(tknop)
                            a = tkn['{}'.format(msg._from)][0]['tkn']
                            req = requests.get(url = '{}'.format(a))
                            b = req.text
                            aa = puy.getContact(sender).displayName
                            ab = puy.getGroup(msg.to).name
                            ac = puy.getContact(sender).mid
                            #sendMention(to, '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            #puy.sendMessage(to,'「 CHROMEOS 」\nUntuk: '+aa+'\nFrom Group: '+ab+'\nMid User: '+ac+'\n\n- TOKEN : \n{}'.format(b))
                            sendMention(to,'「 IOSPAD 」\nUntuk : @!\nDari Grup : '+ab+'\nMid Kamu : '+ac+'\n\n-「 TOKEN 」  : \n{}\n\n- UA : Line/8.3.2\n- LA : IOSPAD 8.8.3 PUY x64\n\n*「 From BotEater / Edited By PUY 」'.format(b), [sender])
                                
                        if text.lower() == '#login desktopwin':
                            req = requests.get('https://api.eater.tech/DESKTOPWIN')
                            a = req.text
                            b = json.loads(a)
                            tknop= codecs.open("tkn.json","r","utf-8")
                            tkn = json.load(tknop)
                            tkn['{}'.format(msg._from)] = []
                            tkn['{}'.format(msg._from)].append({
                                'qr': b['result'][0]['linkqr'],
                                'tkn': b['result'][0]['linktkn']
                                })
                            qrz = b['result'][0]['linkqr']
                            puy.sendMessage(to, 'Buka Link dibawah dan Tekan Login\n\n{}'.format(qrz))
                            #dap.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                            with open('tkn.json', 'w') as outfile:
                                json.dump(tkn, outfile)
                            tknop= codecs.open("tkn.json","r","utf-8")
                            tkn = json.load(tknop)
                            a = tkn['{}'.format(msg._from)][0]['tkn']
                            req = requests.get(url = '{}'.format(a))
                            b = req.text
                            aa = puy.getContact(sender).displayName
                            ab = puy.getGroup(msg.to).name
                            ac = puy.getContact(sender).mid
                            #sendMention(to, '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            #dap.sendMessage(to,'「 CHROMEOS 」\nUntuk: '+aa+'\nFrom Group: '+ab+'\nMid User: '+ac+'\n\n- TOKEN : \n{}'.format(b))
                            sendMention(to,'「 DESKTOPWIN 」\nUntuk : @!\nDari Grup : '+ab+'\nMid Kamu : '+ac+'\n\n-「 TOKEN 」  : \n{}\n\n- UA : DESKTOPWIN 8.8.3 PUY x64\n\n*「 From BotEater / Edited By PUY 」'.format(b), [sender])
                            
                        if text.lower() == '#login desktopmac':
                            req = requests.get('https://api.eater.tech/DESKTOPMAC')
                            a = req.text
                            b = json.loads(a)
                            tknop= codecs.open("tkn.json","r","utf-8")
                            tkn = json.load(tknop)
                            tkn['{}'.format(msg._from)] = []
                            tkn['{}'.format(msg._from)].append({
                                'qr': b['result'][0]['linkqr'],
                                'tkn': b['result'][0]['linktkn']
                                })
                            qrz = b['result'][0]['linkqr']
                            puy.sendMessage(to, 'Buka Link dibawah dan Tekan Login\n\n{}'.format(qrz))
                            #dap.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                            with open('tkn.json', 'w') as outfile:
                                json.dump(tkn, outfile)
                            tknop= codecs.open("tkn.json","r","utf-8")
                            tkn = json.load(tknop)
                            a = tkn['{}'.format(msg._from)][0]['tkn']
                            req = requests.get(url = '{}'.format(a))
                            b = req.text
                            aa = puy.getContact(sender).displayName
                            ab = puy.getGroup(msg.to).name
                            ac = puy.getContact(sender).mid
                            #sendMention(to, '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            #dap.sendMessage(to,'「 CHROMEOS 」\nUntuk: '+aa+'\nFrom Group: '+ab+'\nMid User: '+ac+'\n\n- TOKEN : \n{}'.format(b))
                            sendMention(to,'「 DESKTOPMAC 」\nUntuk : @!\nDari Grup : '+ab+'\nMid Kamu : '+ac+'\n\n-「 TOKEN 」  : \n{}\n\n- UA : Line/8.3.2\n- LA : DESKTOPMAC 8.8.3 PUY x64\n\n*「 From BotEater / Edited By PUY 」'.format(b), [sender])

                        elif cmd.startswith("setautoadd: "):
                          if msg._from in Owner:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            try:
                                settings["autoAddMessage"] = txt
                                puy.sendMessage(to, "Pesan Add diubah menjadi : 「{}」".format(txt))
                            except:
                                puy.sendMessage(to, "Gagal mengubah pesan Add")

                        elif cmd.startswith("setautojoin: "):
                          if msg._from in Owner:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            try:
                                settings["autoJoinMessage"] = txt
                                puy.sendMessage(to, "Pesan Join diubah menjadi : 「{}」".format(txt))
                            except:
                                puy.sendMessage(to, "Gagal mengubah pesan Join")
								
                        elif cmd.startswith("setautoreply: "):
                          if msg._from in Owner:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            try:
                                settings["autoResponMessage"] = txt
                                puy.sendMessage(to, "Pesan autoReplyMention diubah menjadi : 「{}」".format(txt))
                            except:
                                puy.sendMessage(to, "Gagal mengubah pesan autoReplyMention")

                        elif cmd.startswith("setprefix:"):
                          if msg._from in Owner:
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            if " " in key:
                                puy.sendMessage(to, "\nTanpa spasi.\n")
                            else:
                                settings["keyCommand"] = str(key).lower()
                                sendMessageWithFooter(to, "prefix diubah menjadi [ {} ]".format(str(key).lower()))        
                        if text.lower() == "prefix":
                            puy.sendMessage(to, "\nPrefix Saat ini adalah [ {} ]\n".format(str(settings["keyCommand"])))                                                                                            
                        elif text.lower() == "prefix on":
                          if msg._from in Owner:
                            settings["setKey"] = True
                            puy.sendMessage(to, "[ Notified Prefix Key ]\nBerhasil mengaktifkan Prefix"
                        elif text.lower() == "prefix off":
                          if msg._from in Owner:
                            settings["setKey"] = False
                            puy.sendMessage(to, "[ Notified Prefix Key ]\nBerhasil menonaktifkan Prefix"
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)                            
        ## PREFIX ##          
        
        if op.type == 25:
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        puy.log("[%s]"%(msg._from)+msg.text)
                    else:
                        puy.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            print("[65] NOTIFIED_DESTROY_MESSAGE")
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in blacklist:
                            puy.sendMessage(at,"[ ! unsend messaging ]\n%s\n[ Messages ]\n%s"%(puy.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                            print ["Ingat Pesan"]
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        
                            
        if op.type == 26:
            try:
                print ("[ 26 ] RECIEVE MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                    #if text =='mute':
                        if sender != puy.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if settings["autoRead"] == True:
                        puy.sendChatChecked(to, msg_id)
                    if sender not in puyMid:
                        if msg.toType != 0 and msg.toType == 2:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    if puyMid in mention["M"]:
                                        if settings["autoRespon"] == True:
                                            puy.sendMention(sender, settings["autoResponMessage"], [sender])
                                        break
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True                       
                    if msg.contentType == 0:
                        if text is None:
                            return
                        if "/ti/g/" in msg.text.lower():
                            if settings["autoJoinTicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = puy.findGroupByTicket(ticket_id)
                                    puy.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    puy.sendMessage(to, "Successed Joined to Group %s" % str(group.name))
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if puyMid in mention["M"]:
                                    if settings["detectMention"] == True:
                                        contact = puy.getContact(sender)
                                        #puy.sendMessage(to, "Hey don't Tag Me! I'ts Annoying.")
                                        sendMention(to, " @!, Hey don't Tag Me! I'ts Annoying.", [sender])
                                        puy.sendContact(to, sender)
                                    break
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if puyMid in mention["M"]:
                                    if settings["autoRespon"] == True:
                                        sendMention(sender, " @!, Hey don't Tag Me! I'ts Annoying.", [sender])
                                    break
                        if settings["detectUnsend"] == True:
                            try:
                                unsendTime = time.time()
                                unsend[msg_id] = {"text": text, "from": sender, "time": unsendTime}
                            except Exception as error:
                                logError(error)
                    if msg.contentType == 1:
                        if settings["detectUnsend"] == True:
                            try:
                                unsendTime = time.time()
                                image = puy.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-image.bin".format(time.time()))
                                unsend[msg_id] = {"from": sender, "image": image, "time": unsendTime}
                            except Exception as error:
                                logError(error)
                    elif msg.contentType == 7:
                        if settings["addSticker"]["status"] == True:
                            stickers[settings["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                            stickers[settings["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                            stickers[settings["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                            f = codecs.open('sticker.json','w','utf-8')
                            json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                            puy.sendMessage(to," 「 Stickers 」\nType: Add Sticker\nStatus: Sticker successfully added to command {}.".format(str(settings["addSticker"]["name"])))
                            settings["addSticker"]["status"] = False
                            settings["addSticker"]["name"] = ""

                    elif msg.contentType == 13:
                        if settings["wblack"] == True:
                            if msg.contentMetadata["mid"] in black["blacklist"]:
                                puy.sendMessage(to, "Sudah ada di daftar hitam ")
                                settings["wblack"] = False
                            else:
                                black["blacklist"][msg.contentMetadata["mid"]] = True
                                puy.sendMessage(to, "Ditambahkan ke daftar hitam ")
                                settings["wblack"] = False
                            backupData()
                        elif settings["dblack"] == True:
                            if msg.contentMetadata["mid"] in black["blacklist"]:
                                del black["blacklist"][msg.contentMetadata["mid"]]
                                puy.sendMessage(to, "Daftar Hitam telah ditutup ")
                                settings["dblack"] = False
                            else:
                                puy.sendMessage(to, "Dia tidak masuk daftar hitam ")
                                settings["dblack"] = False
                            backupData()                            
                    elif msg.contentType == 16:
                        if settings["checkPost"] == True:
                            try:
                                ret_ = "\n  [ Details Post ]  "
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = puy.getContact(sender)
                                    auth = "\n  Author : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n  Author : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n  URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n  Object URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n  Object URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n  Object URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n  Object URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n  Sticker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n  the contents of writing : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n"
                                puy.sendMessage(to, str(ret_))
                            except:
                                puy.sendMessage(to, "\nInvalid post\n")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)

        if op.type == 65:
            print("[65] NOTIFIED_DESTROY_MESSAGE")
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            puy.sendMessage(at,"[ ! unsend messaging ]\n%s\n[ Messages ]\n%s"%(puy.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                            print ["Ingat Pesan"]
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)                
                
#===============================================================================[piMid - puyMid]
                if op.param3 in piMid:
                    if op.param2 in puyMid:
                        G = puy.getGroup(op.param1)
#                        ginfo = puy.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        puy.updateGroup(G)
                        invsend = 0
                        Ticket = puy.reissueGroupTicket(op.param1)
                        puy.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pi.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = puy.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        puy.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        puy.updateGroup(G)
                    else:
                        G = puy.getGroup(op.param1)
#                        ginfo = puy.getGroup(op.param1)
                        puy.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        puy.updateGroup(G)
                        invsend = 0
                        Ticket = puy.reissueGroupTicket(op.param1)
                        puy.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pi.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = puy.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        puy.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        puy.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki2MID]                
                
        if op.type == 19:
            try:
                if op.param3 in puyMid:
                    if op.param2 in piMid:
                        G = pi.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        pi.updateGroup(G)
                        invsend = 0
                        Ticket = pi.reissueGroupTicket(op.param1)
                        puy.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pi.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = pi.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        pi.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        pi.updateGroup(G)
                        puy.sendMessage(op.param1, "hmm?")
                    else:
                        G = pi.getGroup(op.param1)
                        pi.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        pi.updateGroup(G)
                        invsend = 0
                        Ticket = pi.reissueGroupTicket(op.param1)
                        puy.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pi.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = pi.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        pi.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        pi.updateGroup(G)
                        settings["blacklist"][op.param2] = True                        
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 65:
            try:
                if settings["detectUnsend"] == True:
                    to = op.param1
                    sender = op.param2
                    if sender in unsend:
                        unsendTime = time.time()
                        contact = puy.getContact(unsend[sender]["from"])
                        if "text" in unsend[sender]:
                            try:
                                sendTime = unsendTime - unsend[sender]["time"]
                                sendTime = timeChange(sendTime)
                                ret_ = "  [ Pesan DiUrungkan ]"
                                ret_ += "\n  Pengirim : @!"
                                ret_ += "\n  Pada : {} yang lalu".format(sendTime)
                                ret_ += "\n  Tipe pesan : Text"
                                ret_ += "\n  Isi pesan : {}".format(unsend[sender]["text"])
                                puy.sendMention(to, ret_, [contact.mid])
                                del unsend[sender]
                            except:
                                del unsend[sender]
                        elif "image" in unsend[sender]:
                            try:
                                sendTime = unsendTime - unsend[sender]["time"]
                                sendTime = timeChange(sendTime)
                                ret_ = "  [ Pesan DiUrungkan ]"
                                ret_ += "\n  Pengirim : @!"
                                ret_ += "\n  Pada : {} yang lalu".format(sendTime)
                                ret_ += "\n  Tipe pesan : Gambar"
                                ret_ += "\n  Gambar : Dibawah"
                                puy.sendMention(to, ret_, [contact.mid])
                                puy.sendImage(to, unsend[sender]["image"])
                                puy.deleteFile(unsend[sender]["image"])
                                del unsend[sender]
                            except:
                                puy.deleteFile(unsend[sender]["image"])
                                del unsend[sender]
                    else:
                        puy.sendMessage(to, "Unsend Chat Detected, Data Not Found")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)

        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)
        backupData()

while True:
    try:
        delete_log()
        ops = puyPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                puyBot(op)
                puyPoll.setRevision(op.revision)
    except Exception as error:
        logError(error)
        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
