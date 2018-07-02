# -*- coding: utf-8 -*-

from PUY.linepy import *
from PUY.akad.ttypes import Message
from PUY.akad.ttypes import ChatRoomAnnouncementContents
from PUY.akad.ttypes import ContentType as Type
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, subprocess, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit

#dap = LINE()
dap = LINE("Eu3uZTYkIRM2fSpwaDw4.hv+9sZ7pkk5jYglvNr+V1a.VhhW/7dJnrAmDhL7sIZ/jQC64HM9Uz84BTnpLcHVcHQ=")
#dap = LINE('','')
dapMid = dap.profile.mid
dapProfile = dap.getProfile()
dapSettings = dap.getSettings()
dapPoll = OEPoll(dap)
botStart = time.time()

#pi = LINE()
pi = LINE("EuM23bztAld1YZDcOvXc.NNBWxvmEnnLSJ4NTVieR3a.lKUAkiCgbiyZg5R4HVyuNk1eh1B5ZdXnuv+36bE/Fio=")
#pi = LINE('','')
piMid = pi.profile.mid
piProfile = pi.getProfile()
piSettings = pi.getSettings()
dapPoll = OEPoll(pi)
botStart = time.time()

KAC = [dap,pi]

dapMID = dap.profile.mid
piMID = pi.profile.mid

msg_dict = {}

Bots = [dapMID,piMID]
Owner = ["uac8e3eaf1eb2a55770bf10c3b2357c33"]
Admin =["uac8e3eaf1eb2a55770bf10c3b2357c33","u9e76f05d531e34d96c8f89edbc812bdc"]

dapProfile = dap.getProfile()
piProfile = pi.getProfile()

lineSettings = dap.getSettings()
piSettings = pi.getSettings()

dapPoll = OEPoll(dap)
piPoll = OEPoll(pi)

responsename = dap.getProfile().displayName
responsename2 = pi.getProfile().displayName

settings = {
    "autoAdd": False,
    "autoJoin": True,
    "autoLeave": False,
    "autoRead": False,
    "ChangeVideoProfilevid": True,
    "ChangeVideoProfilePicture": True,
    "lurk": False,
    "autoRespon": False,
    "wblack": False,
    "limit": 50,
    "limits": 50,
    "dblack": False,
    "autoJoinTicket": True,
    "checkContact": False,
    "checkPost": False,
	"NatNat": False,
    "Inroom": True,
    "Outroom": True,
    "timeRestart": "18000",
    "protect": False,
    "blacklist": False,
    "qrprotect": False,
    "autoReject": False,
    "members": 1,
    "inviteprotect": False,
    "cancelprotect": False,
    "limituser": True,
    "checkSticker": False,
    "changeDisplayPicture": False,
    "changeGroupPicture": [],
    "wordban": [],
    "keyCommand": "",
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    },
    "setKey": False,
    "unsendMessage": True
}

wait = {
    'autoAdd': False,
    "tagme":"?? Don't Tag",
    "autoRespon": False,
    "detectMention": False,
    "pname": False,
    "winvite": False,
    "qr": False,
    "Lv": False,
    "lang":"JP",
    "pro_name":{},
    "unsend": False,
    "Addsticker":{
            "name": "",
            "status":False
            },
    'message':"""Thx for add!""",
    }
 
bc = {
  "txt": {},
  "mid": {},
  "img": False
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

list_language = {
    "list_textToSpeech": {
        "id": "Indonesia",
        "af" : "Afrikaans",
        "sq" : "Albanian",
        "ar" : "Arabic",
        "hy" : "Armenian",
        "bn" : "Bengali",
        "ca" : "Catalan",
        "zh" : "Chinese",
        "zh-cn" : "Chinese (Mandarin/China)",
        "zh-tw" : "Chinese (Mandarin/Taiwan)",
        "zh-yue" : "Chinese (Cantonese)",
        "hr" : "Croatian",
        "cs" : "Czech",
        "da" : "Danish",
        "nl" : "Dutch",
        "en" : "English",
        "en-au" : "English (Australia)",
        "en-uk" : "English (United Kingdom)",
        "en-us" : "English (United States)",
        "eo" : "Esperanto",
        "fi" : "Finnish",
        "fr" : "French",
        "de" : "German",
        "el" : "Greek",
        "hi" : "Hindi",
        "hu" : "Hungarian",
        "is" : "Icelandic",
        "id" : "Indonesian",
        "it" : "Italian",
        "ja" : "Japanese",
        "km" : "Khmer (Cambodian)",
        "ko" : "Korean",
        "la" : "Latin",
        "lv" : "Latvian",
        "mk" : "Macedonian",
        "no" : "Norwegian",
        "pl" : "Polish",
        "pt" : "Portuguese",
        "ro" : "Romanian",
        "ru" : "Russian",
        "sr" : "Serbian",
        "si" : "Sinhala",
        "sk" : "Slovak",
        "es" : "Spanish",
        "es-es" : "Spanish (Spain)",
        "es-us" : "Spanish (United States)",
        "sw" : "Swahili",
        "sv" : "Swedish",
        "ta" : "Tamil",
        "th" : "Thai",
        "tr" : "Turkish",
        "uk" : "Ukrainian",
        "vi" : "Vietnamese",
        "cy" : "Welsh"
    },
    "list_translate": {    
        "af": "afrikaans",
        "sq": "albanian",
        "am": "amharic",
        "ar": "arabic",
        "hy": "armenian",
        "az": "azerbaijani",
        "eu": "basque",
        "be": "belarusian",
        "bn": "bengali",
        "bs": "bosnian",
        "bg": "bulgarian",
        "ca": "catalan",
        "ceb": "cebuano",
        "ny": "chichewa",
        "zh-cn": "chinese (simplified)",
        "zh-tw": "chinese (traditional)",
        "co": "corsican",
        "hr": "croatian",
        "cs": "czech",
        "da": "danish",
        "nl": "dutch",
        "en": "english",
        "eo": "esperanto",
        "et": "estonian",
        "tl": "filipino",
        "fi": "finnish",
        "fr": "french",
        "fy": "frisian",
        "gl": "galician",
        "ka": "georgian",
        "de": "german",
        "el": "greek",
        "gu": "gujarati",
        "ht": "haitian creole",
        "ha": "hausa",
        "haw": "hawaiian",
        "iw": "hebrew",
        "hi": "hindi",
        "hmn": "hmong",
        "hu": "hungarian",
        "is": "icelandic",
        "ig": "igbo",
        "id": "indonesian",
        "ga": "irish",
        "it": "italian",
        "ja": "japanese",
        "jw": "javanese",
        "kn": "kannada",
        "kk": "kazakh",
        "km": "khmer",
        "ko": "korean",
        "ku": "kurdish (kurmanji)",
        "ky": "kyrgyz",
        "lo": "lao",
        "la": "latin",
        "lv": "latvian",
        "lt": "lithuanian",
        "lb": "luxembourgish",
        "mk": "macedonian",
        "mg": "malagasy",
        "ms": "malay",
        "ml": "malayalam",
        "mt": "maltese",
        "mi": "maori",
        "mr": "marathi",
        "mn": "mongolian",
        "my": "myanmar (burmese)",
        "ne": "nepali",
        "no": "norwegian",
        "ps": "pashto",
        "fa": "persian",
        "pl": "polish",
        "pt": "portuguese",
        "pa": "punjabi",
        "ro": "romanian",
        "ru": "russian",
        "sm": "samoan",
        "gd": "scots gaelic",
        "sr": "serbian",
        "st": "sesotho",
        "sn": "shona",
        "sd": "sindhi",
        "si": "sinhala",
        "sk": "slovak",
        "sl": "slovenian",
        "so": "somali",
        "es": "spanish",
        "su": "sundanese",
        "sw": "swahili",
        "sv": "swedish",
        "tg": "tajik",
        "ta": "tamil",
        "te": "telugu",
        "th": "thai",
        "tr": "turkish",
        "uk": "ukrainian",
        "ur": "urdu",
        "uz": "uzbek",
        "vi": "vietnamese",
        "cy": "welsh",
        "xh": "xhosa",
        "yi": "yiddish",
        "yo": "yoruba",
        "zu": "zulu",
        "fil": "Filipino",
        "he": "Hebrew"
    }
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("PUY")
    
with open('Owner.json', 'r') as fp:
    Owner = json.load(fp)
    
with open('Admin.json', 'r') as fp:
    Admin = json.load(fp)    
    
settings["myProfile"]["displayName"] = dapProfile.displayName
settings["myProfile"]["statusMessage"] = dapProfile.statusMessage
settings["myProfile"]["pictureStatus"] = dapProfile.pictureStatus
coverId = dap.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)

def autoRestart():
    if time.time() - botStart > int(settings["timeRestart"]):
        time.sleep(5)
        restartBot()
        
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
    dap.sendMessage(to, textx, {'AGENT_NAME':'@Muh.khadaffy on Instagram', 'AGENT_LINK': 'https://www.instagram.com/muh.khadaffy', 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + dap.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)    
    #'AGENT_LINK': 'line://ti/p/~{}'.format(puy.getProfile().userid),
    
def sendMessageWithFooter(to, text, name, url, iconlink):
        contentMetadata = {
            'AGENT_NAME': name,
            'AGENT_LINK': url,
            'AGENT_ICON': iconlink
        }
        return dap.sendMessage(to, text, contentMetadata, 0)
    
def sendMessageWithFooter(to, text):
 dap.reissueUserTicket()
 dap = dap.getProfile()
 ticket = "http://line.me/ti/p/"+dap.getUserTicket().id
 pict = "http://dl.profile.line-cdn.net/"+dap.pictureStatus
 name = dap.displayName
 dapi = {"AGENT_ICON": pict,
     "AGENT_NAME": name,
     "AGENT_LINK": ticket
 }
 dap.sendMessage(to, text, contentMetadata=dapi)
    
def sendMessageWithContent(to, name, link, url, iconlink):
        contentMetadata = {
            'AGENT_NAME': name,
            'AGENT_LINK': url,
            'AGENT_ICON': iconlink
            }
        return self.sendMessage(to, text, contentMetadata, 0)    
    
def logError(text):
    dap.log("[ ERROR ] {}".format(str(text)))
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
                dap.deleteFile(msg_dict[data]["path"])
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
    dap.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Sider User\nHaii ".format(str(len(mid)))
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
                    no = "\nâ•šâ•â•[ {} ]".format(str(titanz.getGroup(to).name))
                except:
                    no = "\nâ•šâ•â•[ Success ]"
        titanz.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        titanz.sendMessage(to, "[ INFO ] Error :\n" + str(error))
    
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
    helpMessage =   "\n  「 HELPER  」     " + "\n" + \
                    " " + key + "1) #Token" + "\n" + \
                    " " + key + "2) #Keluar" + "\n\n" + \
                    " " + key + " 「 CEKSIDER  」" + "\n" + \
                    " " + key + "3) #Ceksider On/Off - [For SetRead]" + "\n" + \
                    " " + key + "4) #Ceksider reset - [For Reset reader point]" + "\n" + \
                    " " + key + "5) #Ceksider - [For Ceksider]" + "\n\n" + \
                    " " + key + "   「 Use # For the Prefix 」" + "\n" + \
                    " 「 From Helloworld / Edited by Puy 」"
    return helpMessage

def helpstat():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpStat =      "\n[ Status Command ]" + "\n" + \
                    " " + key + "Reboot" + "\n" + \
                    " " + key + "Runtime" + "\n" + \
                    " " + key + "Speed" + "\n" + \
                    " " + key + "Status" + "\n" + \
                    " MyPrefix" + "\n" + \
                    " Prefix「On/Off」" + "\n" + \
                    ""
    return helpStat
    
def helpsett():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpSett =      "\n[ Settings Command ]     " + "\n" + \
                    " " + key + "1- AutoAdd「On/Off」" + "\n" + \
                    " " + key + "2- AutoJoin「On/Off」" + "\n" + \
                    " " + key + "3- AutoJoinTicket「On/Off」" + "\n" + \
                    " " + key + "4- AutoLeave「On/Off」" + "\n" + \
                    " " + key + "5- AutoRead「On/Off」" + "\n" + \
                    " " + key + "6- AutoRespon「On/Off」" + "\n" + \
                    " " + key + "7- CheckContact「On/Off」" + "\n" + \
                    " " + key + "8- CheckPost「On/Off」" + "\n" + \
                    " " + key + "9- CheckSticker「On/Off」" + "\n" + \
                    " " + key + "10-  UnsendChatDetect「On/Off」" + "\n" + \
                    " "
    return helpSett
    
def helpself():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpSelf =      "\n[ Self Command ]     " + "\n" + \
                    " " + key + "ChangeName:「Query」" + "\n" + \
                    " " + key + "ChangeBio:「Query」" + "\n" + \
                    " " + key + "Me" + "\n" + \
                    " " + key + "MyMid" + "\n" + \
                    " " + key + "MyName" + "\n" + \
                    " " + key + "MyBio" + "\n" + \
                    " " + key + "MyPicture" + "\n" + \
                    " " + key + "MyVideoProfile" + "\n" + \
                    " " + key + "MyCover" + "\n" + \
                    " " + key + "StealContact「Mention」" + "\n" + \
                    " " + key + "StealMid「Mention」" + "\n" + \
                    " " + key + "StealName「Mention」" + "\n" + \
                    " " + key + "StealBio「Mention」" + "\n" + \
                    " " + key + "StealPicture「Mention」" + "\n" + \
                    " " + key + "StealVideoProfile「Mention」" + "\n" + \
                    " " + key + "StealCover「Mention」" + "\n" + \
                    " " + key + "CloneProfile「Mention」" + "\n" + \
                    " " + key + "Mention" + "\n" + \
                    " " + key + "Lurking「On/Off/Reset」" + "\n" + \
                    " " + key + "Lurking" + "\n" + \
                    " " + key + "RestoreProfile" + "\n" + \
                    " " + key + "Crash" + "\n" + \
                    " " + key + "BackupProfile" + "\n" + \
                    " " + key + "Changedp" + "\n" + \
                    " "
    return helpSelf

def helpmessaged():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpMessaged =      "\n[ CONTINUANCE ]     " + "\n\n" + \
                        " " + key + "10-   #List Token" + "\n" + \
                        " " + key + "11-   #Me" + "\n" + \
                        " " + key + "12-   #Mentioning" + "\n" + \
                        " " + key + "13-   #InstaStory (UserName)*(Number)" + "\n" + \
                        " " + key + "14-   #Acaratv" + "\n" + \
                        " " + key + "15-   #Pc @ (text)" + "\n" + \
                        " " + key + "16-   #Pm @ (text)" + "\n" + \
                        " " + key + "17-   #Carigambar (text)" + "\n" + \
                        " " + key + "18-   #Screenshot (1/2/3) (urlweb)" + "\n" + \
                        " " + key + "19-  #Carimusik (judul dan penyanyi)" + "\n" + \
                        " " + key + "20-  #Murottal [numb 1/2/3]" + "\n" + \
                        " " + key + "21-  #GroupCreator" + "\n" + \
                        " " + key + "22-  #Announce" + " ~[OFF]\n" + \
                        " " + key + "23-  #Delannounce" + "\n" + \
                        " " + key + "24-  #GroupId" + "\n" + \
                        " " + key + "25-  #GroupName" + "\n" + \
                        " " + key + "26-  #GroupPicture" + "\n" + \
                        " " + key + "27-  #GroupTicket ON/OFF" + "\n" + \
                        " " + key + "28-  #GroupTicket" + "\n" + \
                        " " + key + "29-  #GroupList" + "\n" + \
                        " " + key + "30-  #spam text*number" + "\n" + \
                        " " + key + "31-  #GroupMemberList" + "\n" + \
                        " " + key + "32-  #GroupInfo" + "\n" + \
                        " " + key + "33-  #Call [nomor]" + "\n" + \
                        " " + key + "34-  #Sms [nomor]" + "\n\n" + \
                        " " + key + " [ Use # ]" + "\n" + \
                        " "
    return helpMessaged

def helpgroup():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpGroup =     "\n[ Group Command ]     " + "\n" + \
                    " " + key + "GroupCreator" + "\n" + \
                    " " + key + "Announce" + "\n" + \
                    " " + key + "Delannounce" + "\n" + \
                    " " + key + "GroupId" + "\n" + \
                    " " + key + "GroupName" + "\n" + \
                    " " + key + "GroupPicture" + "\n" + \
                    " " + key + "GroupTicket" + "\n" + \
                    " " + key + "GroupTicket「On/Off」" + "\n" + \
                    " " + key + "GroupList" + "\n" + \
                    " " + key + "GroupMemberList" + "\n" + \
                    " " + key + "GroupInfo" + "\n" + \
                    " " + key + "Changegp" + "\n" + \
                    "   " + "" + "" + \
                    "   "
    return helpGroup
    
def helptexttospeech():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpTextToSpeech =  "     [ Help TextToSpeech ]    " + "\n" + \
                        "   " + key + "af : Afrikaans" + "\n" + \
                        "   " + key + "sq : Albanian" + "\n" + \
                        "   " + key + "ar : Arabic" + "\n" + \
                        "   " + key + "hy : Armenian" + "\n" + \
                        "   " + key + "bn : Bengali" + "\n" + \
                        "   " + key + "ca : Catalan" + "\n" + \
                        "   " + key + "zh : Chinese" + "\n" + \
                        "   " + key + "zhcn : Chinese (Mandarin/China)" + "\n" + \
                        "   " + key + "zhtw : Chinese (Mandarin/Taiwan)" + "\n" + \
                        "   " + key + "zhyue : Chinese (Cantonese)" + "\n" + \
                        "   " + key + "hr : Croatian" + "\n" + \
                        "   " + key + "cs : Czech" + "\n" + \
                        "   " + key + "da : Danish" + "\n" + \
                        "   " + key + "nl : Dutch" + "\n" + \
                        "   " + key + "en : English" + "\n" + \
                        "   " + key + "enau : English (Australia)" + "\n" + \
                        "   " + key + "enuk : English (United Kingdom)" + "\n" + \
                        "   " + key + "enus : English (United States)" + "\n" + \
                        "   " + key + "eo : Esperanto" + "\n" + \
                        "   " + key + "fi : Finnish" + "\n" + \
                        "   " + key + "fr : French" + "\n" + \
                        "   " + key + "de : German" + "\n" + \
                        "   " + key + "el : Greek" + "\n" + \
                        "   " + key + "sk : Slovak" + "\n" + \
                        "   " + "" + "\n" + \
                        "[ Usage : " + key + "say-id Dap ]"
    return helpTextToSpeech
    
def helptexttospeechh():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpTextToSpeechh = "     [ Help TextToSpeech 2 ]    " + "\n" + \
                        "   " + key + "hi : Hindi" + "\n" + \
                        "   " + key + "hu : Hungarian" + "\n" + \
                        "   " + key + "is : Icelandic" + "\n" + \
                        "   " + key + "id : Indonesian" + "\n" + \
                        "   " + key + "it : Italian" + "\n" + \
                        "   " + key + "ja : Japanese" + "\n" + \
                        "   " + key + "km : Khmer (Cambodian)" + "\n" + \
                        "   " + key + "ko : Korean" + "\n" + \
                        "   " + key + "la : Latin" + "\n" + \
                        "   " + key + "lv : Latvian" + "\n" + \
                        "   " + key + "mk : Macedonian" + "\n" + \
                        "   " + key + "no : Norwegian" + "\n" + \
                        "   " + key + "pl : Polish" + "\n" + \
                        "   " + key + "pt : Portuguese" + "\n" + \
                        "   " + key + "ro : Romanian" + "\n" + \
                        "   " + key + "ru : Russian" + "\n" + \
                        "   " + key + "sr : Serbian" + "\n" + \
                        "   " + key + "si : Sinhala" + "\n" + \
                        "   " + key + "es : Spanish" + "\n" + \
                        "   " + key + "eses : Spanish (Spain)" + "\n" + \
                        "   " + key + "esus : Spanish (United States)" + "\n" + \
                        "   " + key + "sw : Swahili" + "\n" + \
                        "   " + key + "sv : Swedish" + "\n" + \
                        "   " + key + "ta : Tamil" + "\n" + \
                        "   " + key + "th : Thai" + "\n" + \
                        "   " + key + "tr : Turkish" + "\n" + \
                        "   " + key + "uk : Ukrainian" + "\n" + \
                        "   " + key + "vi : Vietnamese" + "\n" + \
                        "   " + key + "cy : Welsh" + "\n" + \
                        "   " + "" + "\n" + \
                        "[ Usage : " + key + "say-id Dap ]"
    return helpTextToSpeechh
    
def helptranslate():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpTranslate = "     [ Help Translate ]     " + "\n" + \
                    "   " + key + "af : afrikaans" + "\n" + \
                    "   " + key + "sq : albanian" + "\n" + \
                    "   " + key + "am : amharic" + "\n" + \
                    "   " + key + "ar : arabic" + "\n" + \
                    "   " + key + "hy : armenian" + "\n" + \
                    "   " + key + "az : azerbaijani" + "\n" + \
                    "   " + key + "eu : basque" + "\n" + \
                    "   " + key + "be : belarusian" + "\n" + \
                    "   " + key + "bn : bengali" + "\n" + \
                    "   " + key + "bs : bosnian" + "\n" + \
                    "   " + key + "bg : bulgarian" + "\n" + \
                    "   " + key + "ca : catalan" + "\n" + \
                    "   " + key + "ceb : cebuano" + "\n" + \
                    "   " + key + "ny : chichewa" + "\n" + \
                    "   " + key + "zhcn : chinese (simplified)" + "\n" + \
                    "   " + key + "zhtw : chinese (traditional)" + "\n" + \
                    "   " + key + "co : corsican" + "\n" + \
                    "   " + key + "hr : croatian" + "\n" + \
                    "   " + key + "cs : czech" + "\n" + \
                    "   " + key + "da : danish" + "\n" + \
                    "   " + key + "nl : dutch" + "\n" + \
                    "   " + key + "en : english" + "\n" + \
                    "   " + key + "eo : esperanto" + "\n" + \
                    "   " + key + "et : estonian" + "\n" + \
                    "   " + key + "tl : filipino" + "\n" + \
                    "   " + key + "fi : finnish" + "\n" + \
                    "   " + key + "fr : french" + "\n" + \
                    "   " + key + "fy : frisian" + "\n" + \
                    "   " + key + "gl : galician" + "\n" + \
                    "   " + key + "ka : georgian" + "\n" + \
                    "   " + key + "de : german" + "\n" + \
                    "   " + "\n" + "\n" + \
                    "[ Usage : " + key + "tr-id Dapi ]"
    return helpTranslate

def helptranslated():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpTranslated ="     [ Help Translate 2 ]     " + "\n" + \
                    "   " + key + "hi : hindi" + "\n" + \
                    "   " + key + "hmn : hmong" + "\n" + \
                    "   " + key + "hu : hungarian" + "\n" + \
                    "   " + key + "is : icelandic" + "\n" + \
                    "   " + key + "ig : igbo" + "\n" + \
                    "   " + key + "id : indonesian" + "\n" + \
                    "   " + key + "ga : irish" + "\n" + \
                    "   " + key + "it : italian" + "\n" + \
                    "   " + key + "ja : japanese" + "\n" + \
                    "   " + key + "jw : javanese" + "\n" + \
                    "   " + key + "kn : kannada" + "\n" + \
                    "   " + key + "kk : kazakh" + "\n" + \
                    "   " + key + "km : khmer" + "\n" + \
                    "   " + key + "ko : korean" + "\n" + \
                    "   " + key + "ku : kurdish (kurmanji)" + "\n" + \
                    "   " + key + "ky : kyrgyz" + "\n" + \
                    "   " + key + "lo : lao" + "\n" + \
                    "   " + key + "la : latin" + "\n" + \
                    "   " + key + "lv : latvian" + "\n" + \
                    "   " + key + "lt : lithuanian" + "\n" + \
                    "   " + key + "ro : romanian" + "\n" + \
                    "   " + key + "uk : ukrainian" + "\n" + \
                    "   " + key + "ur : urdu" + "\n" + \
                    "   " + key + "uz : uzbek" + "\n" + \
                    "   " + key + "vi : vietnamese" + "\n" + \
                    "   " + key + "cy : welsh" + "\n" + \
                    "   " + key + "xh : xhosa" + "\n" + \
                    "   " + key + "yi : yiddish" + "\n" + \
                    "   " + key + "yo : yoruba" + "\n" + \
                    "   " + key + "zu : zulu" + "\n" + \
                    "   " + key + "fil : Filipino" + "\n" + \
                    "   " + key + "he : Hebrew" + "\n" + \
                    "   " + "" + "\n" + \
                    "[ Usage : " + key + "tr-id Dapi ]"
    return helpTranslated
     
#def puyBot(op):
#    try:
#        if op.type == 0:
#            print ("[ 0 ] END OF OPERATION")
#            return
#        if op.type == 5:
#            print ("[ 5 ] NOTIFIED ADD CONTACT")
#            if settings["autoAdd"] == True:
#                dap.sendMessage(op.param1, "Halo {} terimakasih telah menambahkan saya sebagai teman :D".format(str(dap.getContact(op.param1).displayName)))
#        if op.type == 13:
#            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
#            group = dap.getGroup(op.param1)
#            contact = dap.getContact(op.param2)
#            if settings["autoJoin"] == True:
#                if settings["autoReject"]["status"] == True:
#                    if len(group.members) > settings["autoReject"]["members"]:
#                        dap.acceptGroupInvitation(op.param1)
#                    else:
#                        dap.rejectGroupInvitation(op.param1)
#                else:
#                    dap.acceptGroupInvitation(op.param1)
#            gInviMids = []
#            for z in group.invitee:
#                if z.mid in op.param3:
#                    gInviMids.append(z.mid)
#            listContact = ""
#            if gInviMids != []:
#                for j in gInviMids:
#                   name_ = dap.getContact(j).displayName
#                   listContact += "\n      + {}".format(str(name_))
                   
#           arg = "   Group Name : {}".format(str(group.name))
#           arg += "\n   Executor : {}".format(str(contact.displayName))
#           arg += "\n   List User Invited : {}".format(str(listContact))
#           print (arg)
     
def dapBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return

        #if op.type == 5:
        #    print ("[ 5 ] NOTIFIED ADD CONTACT")
        #    if settings["autoAdd"] == True:
        #        dap.findAndAddContactsByMid(op.param2)
        #        sendMessageWithFooter(op.param1, "Thx for add")

        if op.type == 5:
            if wait["autoAdd"] == True:
                dap.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    dap.sendMessage(op.param1,str(wait["message"]))        
        
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            contact = dap.getContact(op.param2)
            if settings["autoAdd"] == True:
                dap.sendMessage(op.param1, "Hi {} Thx for add".format(str(dap.getContact(op.param1).displayName)))
                
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            if settings["autoJoin"] == True:
                gid = dap.getGroup(op.param1)
                gid = pi.getGroup(op.param1)
                dap.sendMessage(op.param2, "[ Nama Group ]\n" + gid.name)            
                dap.acceptGroupInvitation(op.param1)
                dap.sendMessage(op.param2, "Thx for invite me to group\nKetik help untuk lebih lanjut")
                dap.sendMessage(op.param2, "Thx for invited me\n'help' for more!")

        if op.type == 17:
            if op.param2 in Admin:
              if op.param2 not in Bots:    
                return
            ginfo = dap.getGroup(op.param1)
            contact = dap.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            c = Message(to=op.param1, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            dap.sendMessage(c)
            dap.sendMessage(op.param1," Hi" + dap.getContact(op.param2).displayName + "\nWlc To ☞ " + str(ginfo.name) + " ☜" + "\n")
            dap.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "247",
                                    "STKPKGID": "3",
                                    "STKVER": "100" }
            dap.sendMessage(d)             
            print ("MEMBER JOIN TO GROUP")
                
        if op.type in [22, 24]:
            print ("[ 22 And 24 ] NOTIFIED INVITE INTO ROOM & NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                sendMention(op.param2, "@! hmm?")
                dap.leaveRoom(op.param1)

        if op.type == 19:
            print ("[ 19 ] NOTIFIED KICKOUT FROM GROUP")
            group = dap.getGroup(op.param1)
            contact = dap.getContact(op.param2)
            victim = dap.getContact(op.param3)
            arg = "   Group Name : {}".format(str(group.name))
            arg += "\n   Executor : {}".format(str(contact.displayName))
            arg += "\n   Victim : {}".format(str(victim.displayName))
            print (arg)
           
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        dap.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        dap.sendMessage(msg.to,"Itu tidak berkomentar")
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        dap.sendMessage(msg.to,"Done")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        dap.sendMessage(msg.to,"Tidak ada dalam daftar hitam")
                        
        if op.type == 26:
            try:
                print ("[ 26 ] SEND MESSAGE")
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
                        if sender != dap.profile.mid:
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
                                dap.sendMessage(to, str(helpMessage),{'AGENT_ICON':'http://dl.profile.line-cdn.net/0hkY3juiptNHYOExk5wsdLITJWOht5PTI-diUpGX8RPhZ0IydzMSV_FC0VaxV0I3JyMCZ4Ei8VOEQh','AGENT_LINK':'https://line.me/ti/p/~yapuy','AGENT_NAME':'Help Message'})
                                #sendMentionFooter(to, "@! - Selamat Mencoba", str(helpMessage), {'AGENT_LINK': 'line://ti/p/~yapuy'.'AGENT_ICON':'https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=uac8e3eaf1eb2a55770bf10c3b2357c33&oid=8a257936867f1ac24ef8434b13b799e5','AGENT_NAME':'HELPER'})
                                #sendMention(to, "@!", str(helpMessage), [sender]))
                                #dap.sendMessage(to, str(helpMessage),{'AGENT_ICON':'http://dl.profile.line-cdn.net/'+dap.pictureStatus,'AGENT_LINK':'https://line.me/ti/p/~yapuy','AGENT_NAME':'Mkhadaffy'})
                            if cmd == "help2":
                                helpMessaged = helpmessaged()
                                dap.sendMessage(to, str(helpMessaged),{'AGENT_ICON':'http://dl.profile.line-cdn.net/0hkY3juiptNHYOExk5wsdLITJWOht5PTI-diUpGX8RPhZ0IydzMSV_FC0VaxV0I3JyMCZ4Ei8VOEQh','AGENT_LINK':'https://line.me/ti/p/~yapuy','AGENT_NAME':'Help Message 2'})
                            #if cmd.startswith('ls'):
                                #a = subprocess.getoutput(cmd[1])
                                #dap.sendMessage(to, a)
                            #if cmd[0].startswith('cd'):
                                #a = subprocess.getoutput(cmd[1])
                                #dap.sendMessage(to, a)
                            if cmd == "tts2":
                                helpTextToSpeechh = helptexttospeechh()
                                dap.sendMessage(to, str(helpTextToSpeechh),{'AGENT_ICON':'http://dl.profile.line-cdn.net/0hkY3juiptNHYOExk5wsdLITJWOht5PTI-diUpGX8RPhZ0IydzMSV_FC0VaxV0I3JyMCZ4Ei8VOEQh','AGENT_LINK':'https://line.me/ti/p/~yapuy','AGENT_NAME':'Help TTS 2'})                                
                            elif cmd == "tts":
                                helpTextToSpeech = helptexttospeech()
                                #dap.sendMessage(to, str(helpTextToSpeech))
                                dap.sendMessage(to, str(helpTextToSpeech),{'AGENT_ICON':'http://dl.profile.line-cdn.net/0hkY3juiptNHYOExk5wsdLITJWOht5PTI-diUpGX8RPhZ0IydzMSV_FC0VaxV0I3JyMCZ4Ei8VOEQh','AGENT_LINK':'https://line.me/ti/p/~yapuy','AGENT_NAME':'Help TTS'})
                            elif cmd == "#token generator":
                                sendMentionFooter(to, "「 TOKEN TIPE  」\n1* DESKTOPWIN\n2* WIN10\n3* DESKTOPMAC\n4* IOSPAD\n5* CHROME\n\n*Usage : Type #login with Token Type\n\n*Example : #login chrome\n\n[ From BotEater / Edited by Puy ]\n@! - Selamat Mencoba.", [sender])
                            elif cmd == "#token":
                                sendMentionFooter(to, "「 TOKEN TIPE  」\n1* DESKTOPWIN\n2* WIN10\n3* DESKTOPMAC\n4* IOSPAD\n5* CHROME\n\n*Usage : Type #login with Token Type\n\n*Example : #login chrome\n\n[ From BotEater / Edited by Puy ]\n@! - Selamat Mencoba.", [sender])
                            elif cmd == "selfcmd":
                              if msg._from in Owner:
                                helpSelf = helpself()
                                dap.sendMessage(to, str(helpSelf),{'AGENT_ICON':'http://dl.profile.line-cdn.net/0hkY3juiptNHYOExk5wsdLITJWOht5PTI-diUpGX8RPhZ0IydzMSV_FC0VaxV0I3JyMCZ4Ei8VOEQh','AGENT_LINK':'https://line.me/ti/p/~yapuy','AGENT_NAME':'Help Self'})                                
                            elif cmd == "translate":
                              if msg._from in Owner:
                                helpTranslate = helptranslate()
                                dap.sendMessage(to, str(helpTranslate),{'AGENT_ICON':'http://dl.profile.line-cdn.net/0hkY3juiptNHYOExk5wsdLITJWOht5PTI-diUpGX8RPhZ0IydzMSV_FC0VaxV0I3JyMCZ4Ei8VOEQh','AGENT_LINK':'https://line.me/ti/p/~yapuy','AGENT_NAME':'Help Translate'})
                                #dap.sendMessage(to, str(helpTranslate))
                            elif cmd == "statcmd":
                              if msg._from in Owner:
                                helpStat = helpstat()
                                dap.sendMessage(to, str(helpStat),{'AGENT_ICON':'http://dl.profile.line-cdn.net/0hkY3juiptNHYOExk5wsdLITJWOht5PTI-diUpGX8RPhZ0IydzMSV_FC0VaxV0I3JyMCZ4Ei8VOEQh','AGENT_LINK':'https://line.me/ti/p/~yapuy','AGENT_NAME':'Help Stat'})                                
                            elif cmd == "settcmd":
                              if msg._from in Owner:
                                helpSett = helpsett()
                                dap.sendMessage(to, str(helpSett),{'AGENT_ICON':'http://dl.profile.line-cdn.net/0hkY3juiptNHYOExk5wsdLITJWOht5PTI-diUpGX8RPhZ0IydzMSV_FC0VaxV0I3JyMCZ4Ei8VOEQh','AGENT_LINK':'https://line.me/ti/p/~yapuy','AGENT_NAME':'Help Sett'})                                
                            elif cmd == "groupcmd":
                              if msg._from in Owner:
                                helpGroup = helpgroup()
                                dap.sendMessage(to, str(helpGroup),{'AGENT_ICON':'http://dl.profile.line-cdn.net/0hkY3juiptNHYOExk5wsdLITJWOht5PTI-diUpGX8RPhZ0IydzMSV_FC0VaxV0I3JyMCZ4Ei8VOEQh','AGENT_LINK':'https://line.me/ti/p/~yapuy','AGENT_NAME':'Help Group'})                                
                            elif cmd == "translate2":
                              if msg._from in Owner:
                                helpTranslated = helptranslated()
                                dap.sendMessage(to, str(helpTranslated),{'AGENT_ICON':'http://dl.profile.line-cdn.net/0hkY3juiptNHYOExk5wsdLITJWOht5PTI-diUpGX8RPhZ0IydzMSV_FC0VaxV0I3JyMCZ4Ei8VOEQh','AGENT_LINK':'https://line.me/ti/p/~yapuy','AGENT_NAME':'Help Translate 2'})                                
                            elif cmd.startswith("changeprefix:"):
                              if msg._from in Owner:
                                sep = text.split(" ")
                                key = text.replace(sep[0] + " ","")
                                if " " in key:
                                    dap.sendMessage(to, "\nTanpa spasi.\n")
                                else:
                                    settings["keyCommand"] = str(key).lower()
                                    dap.sendMessage(to, "text [ {} ]".format(str(key).lower()))
                            elif cmd == "#speed":
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
                                start = time.time()
                                if msg.to not in read['readPoint']:
                                    #dap.sendMessage(to, "「 NOTIFIED BOT SPEED 」\nKecepatan mengirim pesan {} detik dap".format(str(elapsed_time)))
                                    dap.sendMessage(msg.to, "「 NOTIFIED BOT SPEED 」\n\n" + Timed)
                                #dap.sendMessage(to, "")
                                elapsed_time = time.time() - start
                                dap.sendMessage(to, "[ Speed ]\nKecepatan mengirim pesan {} detik dap".format(str(elapsed_time)))
                            elif cmd == "#runtime":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                dap.sendMessage(to, "Bot has been Active for {} puy".format(str(runtime)))
                            #elif cmd == "lurk":
                            #    dap.sendMessage(to, "[ Notified Check Readers ]\n\n  Usage : type lurking on , lurking ")
                            elif cmd == "#restart":
                              if msg._from in Owner:
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
                                start = time.time()
                                if msg.to not in read['readPoint']:
                                    dap.sendMessage(msg.to, "「 NOTIFIED BOT SPEED 」\n\n" + Timed)
                                sendMention(to, "@! \nBot Restarted", [sender])
                                restartBot()
                              else:
                                  dap.sendMessage("Permission Denied")
# Pembatas Script #
                            elif cmd.startswith("#add:admin "):
                                if msg._from in Owner:
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
                                    if msg.to not in read['readPoint']:
                                        dap.sendMessage(msg.to, "「 NOTIFIED ADDED ADMIN 」")
                                    targets = []
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            Admin[target] = True
                                            f=codecs.open('Admin.json','w','utf-8')
                                            json.dump(Admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                            dap.sendMessage(msg.to,"Successed Added 1 Admin\n\n" + Timed)
                                            break
                                        except:
                                            dap.sendMessage(msg.to,"Failed\n\n" + Timed)
                                            break
                                else:
                                    dap.sendMessage(msg.to,"Owner Permission Required" + Timed)
                                    
                            elif cmd.startswith("#remove:admin "):
                                if msg._from in Owner:
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
                                    if msg.to not in read['readPoint']:
                                        dap.sendMessage(msg.to, "「 NOTIFIED REMOVED ADMIN 」")
                                    targets = []
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            del Admin[target]
                                            f=codecs.open('Admin.json','w','utf-8')
                                            json.dump(Admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                            dap.sendMessage(msg.to,"Successed Removed 1 Admin\n\n" + Timed)
                                            break
                                        except:
                                            dap.sendMessage(msg.to,"Failed\n\n" + Timed)
                                        break
                                else:
                                    dap.sendMessage(msg.to,"Owner Permission Required" + Timed)
                                    
                            elif cmd.startswith('#adminlist'):
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
                                    if msg.to not in read['readPoint']:
                                        dap.sendMessage(msg.to, "「 Please Wait  」")
                                    if Admin == []:
                                        dap.sendMessage(msg.to,"「 No one Admin  」")
                                    else:
                                        #dap.sendMessage(msg.to,"")
                                        mc = " 「 Admin List 」\n\n"
                                        for mi_d in Admin:
                                            mc += "" +dap.getContact(mi_d).displayName + "\n\n"
                                        dap.sendMessage(msg.to,mc + "" + Timed)
                                    
                            elif cmd.startswith('#ownerlist'):
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
                                    if msg.to not in read['readPoint']:
                                        dap.sendMessage(msg.to, "「 Please Wait  」")
                                    if Owner == []:
                                        dap.sendMessage(msg.to,"「 No one Owner  」")
                                    else:
                                        #dap.sendMessage(msg.to,"")
                                        mc = " 「 Owner List 」\n\n"
                                        for mi_d in Owner:
                                            mc += "" +dap.getContact(mi_d).displayName + "\n\n"
                                        dap.sendMessage(msg.to,mc + " " + Timed)
                                    
#-------------------------------------------------------------------------------
                            elif cmd.startswith('#protect on'):
                                if msg._from in Owner:
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
                                    if msg.to not in read['readPoint']:
                                        dap.sendMessage(msg.to, "「 NOTIFIED ACTIVIED PROTECTION  」")
                                    if settings["protect"] == True:
                                        if settings["lang"] == "JP":
                                            dap.sendMessage(msg.to,"Protection Already On At\n\n" + Timed)
                                        else:
                                            dap.sendMessage(msg.to,"Protection Set To On At\n\n" + Timed)
                                    else:
                                        settings["protect"] = True
                                        if settings["lang"] == "JP":
                                            dap.sendMessage(msg.to,"Protection Set To On At\n\n" + Timed)
                                        else:
                                            dap.sendMessage(msg.to,"Protection Already On At\n\n" + Timed)
                                
                            elif cmd.startswith('#protect off'):
                                if msg._from in Owner:
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
                                    if msg.to not in read['readPoint']:
                                        dap.sendMessage(msg.to, "「 NOTIFIED UNACTIVIED PROTECTION  」")                          
                                    if settings["protect"] == False:
                                        if settings["lang"] == "JP":
                                            dap.sendMessage(msg.to,"Protection Already Off At\n\n" + Timed)
                                        else:
                                            dap.sendMessage(msg.to,"Protection Set To Off At\n\n" + Timed)
                                    else:
                                        settings["protect"] = False
                                        if settings["lang"] == "JP":
                                            dap.sendMessage(msg.to,"Protection Set To Off At\n\n" + Timed)
                                        else:
                                            dap.sendMessage(msg.to,"Protection Already Off At\n\n" + Timed)
#----------------------------------------------------------------------------------------                        
                            elif cmd.startswith('#qrprotect on'):
                                if msg._from in Owner:
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
                                    if msg.to not in read['readPoint']:
                                        dap.sendMessage(msg.to, "「 NOTIFIED ACTIVIED QR PROTECTION  」")                                                                
                                    if settings["qrprotect"] == True:
                                        if settings["lang"] == "JP":
                                            dap.sendMessage(msg.to,"Protection Qr Already On\n\n" + Timed)
                                        else:
                                            dap.sendMessage(msg.to,"Protection Qr Set To On\n\n")
                                    else:
                                        settings["qrprotect"] = True
                                        if settings["lang"] == "JP":
                                            dap.sendMessage(msg.to,"Protection Qr Set To On\n\n" + Timed)
                                        else:
                                            dap.sendMessage(msg.to,"Protection Qr Already On\n\n")
                                
                            elif cmd.startswith('#qrprotect off'):
                                if msg._from in Owner:
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
                                    if msg.to not in read['readPoint']:
                                        dap.sendMessage(msg.to, "「 NOTIFIED UNACTIVIED QR PROTECTION  」")                                                                
                                    if settings["qrprotect"] == False:
                                        if settings["lang"] == "JP":
                                            dap.sendMessage(msg.to,"Protection Qr Already Off\n\n" + Timed)
                                        else:
                                            dap.sendMessage(msg.to,"Protection Qr Set To Off\n\n")
                                    else:
                                        settings["qrprotect"] = False
                                        if settings["lang"] == "JP":
                                            dap.sendMessage(msg.to,"Protection Qr Set To Off\n\n" + Timed)
                                        else:
                                            dap.sendMessage(msg.to,"Protection Qr Already Off\n\n")
#-------------------------------------------------------------------------------
                            elif cmd.startswith('#inviteprotect on'):
                                if msg._from in Owner:
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
                                    if msg.to not in read['readPoint']:
                                        dap.sendMessage(msg.to, "「 NOTIFIED ACTIVIED INVITE PROTECTION  」")
                                    if settings["inviteprotect"] == True:
                                        if settings["lang"] == "JP":
                                            dap.sendMessage(msg.to,"➲ Protection Invite Already On\n\n" + Timed)
                                        else:
                                            dap.sendMessage(msg.to,"➲ Protection Invite Set To On\n\n" + Timed)
                                    else:
                                        settings["inviteprotect"] = True
                                        if settings["lang"] == "JP":
                                            dap.sendMessage(msg.to,"➲ Protection Invite Set To On\n\n" + Timed)
                                        else:
                                            dap.sendMessage(msg.to,"➲ Protection Invite Already On\n\n" + Timed)
                                
                            elif cmd.startswith('#inviteprotect off'):
                                if msg._from in Owner:
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
                                    if msg.to not in read['readPoint']:
                                        dap.sendMessage(msg.to, "「 NOTIFIED UNACTIVIED INVITE PROTECTION  」")                                
                                    if settings["inviteprotect"] == False:
                                        if settings["lang"] == "JP":
                                            dap.sendMessage(msg.to,"➲ Protection Invite Already Off\n\n" + Timed)
                                        else:
                                            dap.sendMessage(msg.to,"➲ Protection Invite Set To Off\n\n" + Timed)
                                    else:
                                        settings["inviteprotect"] = False
                                        if settings["lang"] == "JP":
                                            dap.sendMessage(msg.to,"➲ Protection Invite Set To Off\n\n" + Timed)
                                        else:
                                            dap.sendMessage(msg.to,"➲ Protection Invite Already Off\n\n" + Timed)
#-------------------------------------------------------------------------------
                            elif cmd.startswith('#cancelprotect on'):
                                if msg._from in Owner:
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
                                    if msg.to not in read['readPoint']:
                                        dap.sendMessage(msg.to, "「 NOTIFIED ACTIVIED CANCEL PROTECTION  」")
                                    if settings["cancelprotect"] == True:
                                        if settings["lang"] == "JP":
                                            dap.sendMessage(msg.to,"➲ Protection Cancel Invite Already On\n\n" + Timed)
                                        else:
                                            dap.sendMessage(msg.to,"➲ Protection Cancel Invite Set To On\n\n" + Timed)
                                    else:
                                        settings["cancelprotect"] = True
                                        if settings["lang"] == "JP":
                                            dap.sendMessage(msg.to,"➲ Protection Cancel Invite Set To On\n\n" + Timed)
                                        else:
                                            dap.sendMessage(msg.to,"➲ Protection Cancel Invite Already On\n\n" + Timed)
                                
                            elif cmd.startswith('#cancelprotect off'):
                                if msg._from in Owner:
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
                                    if msg.to not in read['readPoint']:
                                        dap.sendMessage(msg.to, "「 NOTIFIED UNACTIVIED CANCEL PROTECTION  」")                                
                                    if settings["cancelprotect"] == False:
                                        if settings["lang"] == "JP":
                                            dap.sendMessage(msg.to,"➲ Protection Cancel Invite Already Off\n\n" + Timed)
                                        else:
                                            dap.sendMessage(msg.to,"➲ Protection Cancel Invite Set To Off\n\n" + Timed)
                                    else:
                                        settings["cancelprotect"] = False
                                        if settings["lang"] == "JP":
                                            dap.sendMessage(msg.to,"➲ Protection Cancel Invite Set To Off\n\n" + Timed)
                                        else:
                                            dap.sendMessage(msg.to,"➲ Protection Cancel Invite Already Off\n\n" + Timed)
#-------------------------------------------------------------------------------
                            elif cmd.startswith('#setpro on'):
                                if msg._from in Owner:
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
                                    if msg.to not in read['readPoint']:
                                        dap.sendMessage(msg.to, "「 NOTIFIED ACTIVIED PROTECTION  」")                                
                                    settings["protect"] = True
                                    settings["qrprotect"] = True
                                    settings["inviteprotect"] = True
                                    settings["cancelprotect"] = True
                                    dap.sendMessage(msg.to,"All Protection Set To On\n\n" + Timed)
                                else:
                                    dap.sendMessage(msg.to,"This Command only Applies to Owner\n\n" + Timed)
                        		            
                            elif cmd.startswith('#setpro off'):
                                if msg._from in Owner:
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
                                    if msg.to not in read['readPoint']:
                                        dap.sendMessage(msg.to, "「 NOTIFIED UNACTIVIED PROTECTION  」")
                                    settings["protect"] = False
                                    settings["qrprotect"] = False
                                    settings["inviteprotect"] = False
                                    settings["cancelprotect"] = False
                                    dap.sendMessage(msg.to,"All Protection Set To Of\n\nf" + Timed)
                                else:
                                    dap.sendMessage(msg.to,"This Command only Applies to Owner\n\n" + Timed)
#-------------------------------------------------------------------------------
                            elif cmd.startswith("#pi:join"):
                              if msg._from in Owner:
                                  G = dap.getGroup(msg.to)
                                  ginfo = dap.getGroup(msg.to)
                                  G.preventedJoinByTicket = False
                                  dap.updateGroup(G)
                                  invsend = 0
                                  Ticket = dap.reissueGroupTicket(msg.to)
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
                                  pi.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  pi.sendMessage(to,"Hii Everyone!\n\n" + Timed)
                                  if msg.to not in read['readPoint']:
                                      sendMention(msg.to, "「 NOTIFIED INVITED TO ROOM 」\nStatus - Successed\n@!\n\n" + Timed, [sender])
                                  G = dap.getGroup(msg.to)
                                  G.preventedJoinByTicket = True
                                  dap.updateGroup(G)
                                  G.preventedJoinByTicket(G)
                                  dap.updateGroup(G)
                                
                            elif cmd == "autoadd on":
                              if msg._from in Owner:
                                settings["autoAdd"] = True
                                sendMessageWithMentionAndFooter(to, "@! \n\n[ Notified Auto Add ]\nBerhasil mengaktifkan Auto add", [sender])
                            elif cmd == "inroom on":
                              if msg._from in Owner:
                                settings["Inroom"] == True
                                sendMention(to, "[ Notified Inroom ]\nBerhasil mengaktifkan Sambutan @!", [sender])
                            elif cmd == "inroom off":
                              if msg._from in Owner:
                                settings["Inroom"] == False
                                sendMention(to, "[ Notified Inroom ]\nBerhasil menonaktifkan Sambutan @!", [sender])
                            elif cmd == "outroom on":
                              if msg._from in Owner:
                                settings["Outroom"] == True
                                sendMention(to, "[ Notified Outroom ]\nBerhasil mengaktifkan Sambutan @!", [sender])
                            elif cmd == "outroom off":
                              if msg._from in Owner:
                                settings["Outroom"] == False
                                sendMention(to, "[ Notified Outroom ]\nBerhasil menonaktifkan Sambutan @!", [sender])                                                               
                            elif cmd == "autoadd off":
                              if msg._from in Owner:
                                settings["autoAdd"] = False
                                sendMention(to, "[ Notified Auto Add ]\nBerhasil menonaktifkan Auto add @!", [sender])
                            elif cmd == "autojoin on":
                              if msg._from in Owner:
                                settings["autoJoin"] = True
                                sendMention(to, "[ Notified Auto Join ]\nBerhasil mengaktifkan Auto Join @!", [sender])
                            elif cmd == "autojoin off":
                              if msg._from in Owner:
                                settings["autoJoin"] = False
                                sendMention(to, "[ Notified Auto Join ]\nBerhasil menonaktifkan Auto Join @!", [sender])   
                            elif cmd == "changedp on":
                              if msg._from in Owner:
                                settings["changeDisplayPicture"] = True
                                sendMention(to, "[ Notified Dp Changer ]\nBerhasil mengaktifkan DP changer @!", [sender]) 
                            elif cmd == "changedp off":
                              if msg._from in Owner:
                                settings["changeDisplayPicture"] = False
                                sendMention(to, "[ Notified Dp Changer ]\nBerhasil menonaktifkan DP changer @!", [sender])                                
                            elif cmd == "lurkingset on":
                              if msg._from in Owner:
                                settings["lurk"] = True
                                dap.sendMessage(to, "Lurking is Actived!")     
                            elif cmd == "lurkingset off":
                              if msg._from in Owner:
                                settings["lurk"] = False
                                dap.sendMessage(to, "Lurking is Nonactived!")                                
                            elif cmd == "autoleave on":
                              if msg._from in Owner:
                                settings["autoLeave"] = True
                                sendMention(to, "[ Notified Auto Leave ]\nBerhasil mengaktifkan Auto leave @!", [sender])
                            elif cmd == "autoleave off":
                              if msg._from in Owner:
                                settings["autoLeave"] = False
                                sendMention(to, "[ Notified Auto Leave ]\nBerhasil menonaktifkan Auto leave @!", [sender])
                            elif cmd == "autorespon on":
                              if msg._from in Owner:
                                settings["autoRespon"] = True
                                sendMention(to, "[ Notified Auto Respon ]\nBerhasil mengaktifkan Auto Respon @!", [sender])
                            elif cmd == "autorespon off":
                              if msg._from in Owner:
                                settings["autoRespon"] = False
                                sendMention(to, "[ Notified Auto Respon ]\nBerhasil menonaktifkan Auto Respon @!", [sender])
                            elif cmd == "autoread on":
                              if msg._from in Owner:
                                settings["autoRead"] = True
                                sendMention(to, "[ Notified Auto Read ]\nBerhasil mengaktifkan Auto Read @!", [sender])
                            elif cmd == "autoread off":
                              if msg._from in Owner:
                                settings["autoRead"] = False
                                sendMention(to, "[ Notified Auto Read ]\nBerhasil menonaktifkan Auto Read @!", [sender])
                            elif cmd == "autojointicket on":
                              if msg._from in Owner:
                                settings["autoJoinTicket"] = True
                                sendMention(to, "[ Notified Auto Join Ticket ]\nBerhasil mengaktifkan Auto join ticket @!", [sender])
                            elif cmd == "autoJoinTicket off":
                              if msg._from in Owner:
                                settings["autoJoin"] = False
                                sendMention(to, "[ Notified Auto Join Ticket ]\nBerhasil menonaktifkan Auto join ticket @!", [sender])
                            elif cmd == "checkcontact on":
                              if msg._from in Owner:
                                settings["checkContact"] = True
                                sendMention(to, "[ Notified Check Contact ]\nBerhasil mengaktifkan Check contact @!", [sender])
                            elif cmd == "checkcontact off":
                              if msg._from in Owner:
                                settings["checkContact"] = False
                                sendMention(to, "[ Notified Check Contact ]\nBerhasil menonaktifkan Check contact @!", [sender])
                            elif cmd == "checkpost on":
                              if msg._from in Owner:
                                settings["checkPost"] = True
                                sendMention(to, "[ Notified Check Post ]\nBerhasil mengaktifkan Check Post @!", [sender])
                            elif cmd == "checkpost off":
                              if msg._from in Owner:
                                settings["checkPost"] = False
                                sendMention(to, "[ Notified Check Post ]\nBerhasil menonaktifkan Check Post @!", [sender])
                            elif cmd == "checksticker on":
                              if msg._from in Owner:
                                settings["checkSticker"] = True
                                sendMention(to, "[ Notified Check Sticker ]\nBerhasil mengaktifkan Check Sticker @!", [sender])
                            elif cmd == "checksticker off":
                              if msg._from in Owner:
                                settings["checkSticker"] = False
                                sendMention(to, "[ Notified Check Sticker ]\nBerhasil menonaktifkan Check Sticker @!", [sender])
                            elif cmd == "unsendchat on":
                              if msg._from in Owner:
                                settings["unsendMessage"] = True
                                sendMention(to, "[ Notified UnsendMsg Detect ]\nBerhasil mengaktifkan Unsend Detect @!", [sender])                               
                            elif cmd == "unsendchat off":
                              if msg._from in Owner:
                                settings["unsendMessage"] = False
                                sendMention(to, "[ Notified UnsendMsg Detect ]\nBerhasil menonaktifkan Unsend Detect @!", [sender])
                            elif cmd == "protect on":
                              if msg._from in Owner:
                                settings["protect"] = True
                                sendMention(to, "[ Notified ProtectGroup ]\nBerhasil mengaktifkan protect\n@!", [sender])
                            elif cmd == "protect off":
                              if msg._from in Owner:
                                settings["protect"] = False
                                sendMention(to, "[ Notified ProtectGroup ]\nBerhasil menonaktifkan protect\n@!", [sender])
                            elif cmd == "qrprotect on":
                              if msg._from in Owner:
                                settings["qrprotect"] = True
                                sendMention(to, "[ Notified ProtectGroup ]\nBerhasil mengaktifkan qrprotect\n@!", [sender])
                            elif cmd == "qrprotect off":
                              if msg._from in Owner:
                                settings["qrprotect"] = False
                                sendMention(to, "[ Notified ProtectGroup ]\nBerhasil menonaktifkan qrprotect\n@!", [sender])
                            elif cmd == "invcancel on":
                              if msg._from in Owner:
                                settings["inviteprotect"] = True
                                sendMention(to, "[ Notified ProtectGroup ]\nBerhasil mengaktifkan InviteCancel\n@!", [sender])
                            elif cmd == "invcancel off":
                              if msg._from in Owner:
                                settings["inviteprotect"] = False
                                sendMention(to, "[ Notified ProtectGroup ]\nBerhasil mengaktifkan InviteCancel\n@!", [sender])
                            elif cmd == "cancel on":
                              if msg._from in Owner:
                                settings["cancelprotect"] = True
                                sendMention(to, "[ Notified ProtectGroup ]\nBerhasil mengaktifkan Cancelprotect\n@!", [sender])
                            elif cmd == "cancel off":
                              if msg._from in Owner:
                                settings["cancelprotect"] = False
                                sendMention(to, "[ Notified ProtectGroup ]\nBerhasil mengaktifkan Cancelprotect\n@!", [sender])
                            elif cmd == "status":
                              if msg._from in Admin:
                                try:
                                    ret_ = "\n   [ BOT STATUS ]\n"
                                    if settings["autoAdd"] == True: ret_ += "\n   [ ON ] Auto Add"
                                    else: ret_ += "\n   [ OFF ] Auto Add"
                                    if settings["autoJoin"] == True: ret_ += "\n   [ ON ] Auto Join"
                                    else: ret_ += "\n   [ OFF ] Auto Join"
                                    if settings["autoLeave"] == True: ret_ += "\n   [ ON ] Auto Leave Room"
                                    else: ret_ += "\n   [ OFF ] Auto Leave Room"
                                    if settings["autoJoinTicket"] == True: ret_ += "\n   [ ON ] Auto Join Ticket"
                                    else: ret_ += "\n   [ OFF ] Auto Join Ticket"
                                    if settings["autoRead"] == True: ret_ += "\n   [ ON ] Auto Read"
                                    else: ret_ += "\n   [ OFF ] Auto Read"
                                    if settings["protect"] == True: ret_ += "\n   [ ON ] Protect"
                                    else: ret_ += "\n   [ OFF ] Protect"
                                    if settings["qrprotect"] == True: ret_ += "\n   [ ON ] Qr Protect"
                                    else: ret_ += "\n   [ OFF ] Qr Protect"
                                    if settings["inviteprotect"] == True: ret_ += "\n   [ ON ] Invite Protect"
                                    else: ret_ += "\n   [ OFF ] Invite Protect"
                                    if settings["cancelprotect"]     == True: ret_ += "\n   [ ON ] Cancel Protect"
                                    else: ret_ += "\n   [ OFF ] Cancel Protect"                                    
                                    if settings["autoRespon"] == True: ret_ += "\n   [ ON ] Detect Mention"
                                    else: ret_ += "\n   [ OFF ] Detect Mention"
                                    if settings["checkContact"] == True: ret_ += "\n   [ ON ] Check Contact"
                                    else: ret_ += "\n   [ OFF ] Check Contact"
                                    if settings["checkPost"] == True: ret_ += "\n   [ ON ] Check Post"
                                    else: ret_ += "\n   [ OFF ] Check Post"
                                    if settings["checkSticker"] == True: ret_ += "\n   [ ON ] Check Sticker"
                                    else: ret_ += "\n   [ OFF ] Check Sticker"
                                    if settings["lurk"] == True: ret_ += "\n   [ ON ] Lurkset"
                                    else: ret_ += "\n   [ OFF ] Lurkset"                                    
                                    if settings["setKey"] == True: ret_ += "\n   [ ON ] Set Key"
                                    else: ret_ += "\n   [ OFF ] Set Key"
                                    if settings["Inroom"] == True: ret_ += "\n   [ ON ] Inroom Detect"
                                    else: ret_ += "\n   [ OFF ] Inroom Detect"
                                    if settings["Outroom"] == True: ret_ += "\n   [ ON ] Outroom Detect"
                                    else: ret_ += "\n   [ OFF ] Outroom detect"                                    
                                    if settings["unsendMessage"] == True: ret_ += "\n   [ ON ] Unsend Message"
                                    else: ret_ += "\n   [ OFF ] Unsend Message\n"
                                    ret_ += ""
                                    dap.sendMessage(to, str(ret_))
                                except Exception as e:
                                    dap.sendMessage(to, str(e))
# Pembatas Script #
                            elif cmd.startswith("respon"):
                                dap.sendMessage(to,responsename)
                                pi.sendMessage(to,responsename2)
                            elif cmd.startswith('absen'):
                                if msg._from in Admin:
                                    dap.sendContact(to, dapMID)
                                    pi.sendContact(to, piMID)
                            elif cmd == "crash":
                              if msg._from in Owner:
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                            elif cmd == "spamcrash":
                              if msg._from in Owner:
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                dap.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")                                
                            elif cmd.startswith("##changename:"):
                              if msg._from in Owner:
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = dap.getProfile()
                                    profile.displayName = string
                                    dap.updateProfile(profile)
                                    dap.sendMessage(to,"Successfully changed display name to {}".format(str(string)))
                            elif cmd.startswith("##changebio:"):
                              if msg._from in Owner:
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = dap.getProfile()
                                    profile.statusMessage = string
                                    dap.updateProfile(profile)
                                    dap.sendMessage(to,"Successfully changed status message to {}".format(str(string)))
                            elif cmd == "#me":
                                #sendMention(to, "@!", [sender])
                                #tgb = dap.getGroup(op.param1)
                                #dan = dap.getContact(op.param2)
                                contact = dap.getContact(sender)
                                sendMentionFooter(to, "At here @!", [sender])
                                dap.sendContact(to, sender)                                
                                dap.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                     
                            elif cmd == "#mymid":
                                contact = dap.getContact(sender)
                                dap.sendMessage(to, "[ MID ]\n{}".format(sender))
                                dap.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "#myname":
                                contact = dap.getContact(sender)
                                dap.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                                dap.sendMessage(to, "[ Display Name ]\n{}".format(contact.displayName))
                            elif cmd == "#mybio":
                                contact = dap.getContact(sender)
                                dap.sendMessage(to, "[ Status Message ]\n{}".format(contact.statusMessage))
                                dap.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "#mypicture":
                                contact = dap.getContact(sender)
                                dap.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "#myvideoprofile":
                                contact = dap.getContact(sender)
                                dap.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                            elif cmd == "#mycover":
                                channel = dap.getProfileCoverURL(sender)          
                                path = str(channel)
                                dap.sendImageWithURL(to, path)
                            elif cmd.startswith("#cloneprofile "):
                              if msg._from in Owner:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = dap.getContact(ls)
                                        dap.cloneContactProfile(ls)
                                        dap.sendMessage(to, "Successfully clone profile {}".format(contact.displayName))
                            elif cmd == "#restoreprofile":
                              if msg._from in Owner:
                                try:
                                    clientProfile = dap.getProfile()
                                    clientProfile.displayName = str(settings["myProfile"]["displayName"])
                                    clientProfile.statusMessage = str(settings["myProfile"]["statusMessage"])
                                    clientProfile.pictureStatus = str(settings["myProfile"]["pictureStatus"])
                                    dap.updateProfileAttribute(8, clientProfile.pictureStatus)
                                    dap.updateProfile(clientProfile)
                                    coverId = str(settings["myProfile"]["coverId"])
                                    dap.updateProfileCoverById(coverId)
                                    dap.sendMessage(to, "Successfully restore profile wait a while until profile change")
                                except Exception as e:
                                    dap.sendMessage(to, "Failed restore profile")
                                    logError(error)
                            elif cmd == "#backupprofile":
                              if msg._from in Owner:
                                try:
                                    profile = dap.getProfile()
                                    settings["myProfile"]["displayName"] = str(profile.displayName)
                                    settings["myProfile"]["statusMessage"] = str(profile.statusMessage)
                                    settings["myProfile"]["pictureStatus"] = str(profile.pictureStatus)
                                    coverId = dap.getProfileDetail()["result"]["objectId"]
                                    settings["myProfile"]["coverId"] = str(coverId)
                                    dap.sendMessage(to, "Successfully backup profile")
                                except Exception as e:
                                    dap.sendMessage(to, "Failed backup profile")
                                    logError(error)
                            elif cmd.startswith("#stealmid "):
                              if msg._from in Owner:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    ret_ = "[ Mid User ]"
                                    for ls in lists:
                                        ret_ += "\n{}".format(str(ls))
                                    dap.sendMessage(to, str(ret_))
                            elif cmd.startswith("stealname "):
                              if msg._from in Owner:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = dap.getContact(ls)
                                        dap.sendMessage(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                            elif cmd.startswith("#stealbio "):
                              if msg._from in Owner:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = dap.getContact(ls)
                                        dap.sendMessage(to, "[ Status Message ]\n{}".format(str(contact.statusMessage)))
                            elif cmd.startswith("#stealpicture"):
                              if msg._from in Owner:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = dap.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                        dap.sendImageWithURL(to, str(path))
                            elif cmd.startswith("#stealvideoprofile "):
                              if msg._from in Owner:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = dap.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                        dap.sendVideoWithURL(to, str(path))
                            elif cmd.startswith("#stealcover "):
                              if msg._from in Owner:
                                if dap != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            channel = dap.getProfileCoverURL(ls)
                                            path = str(channel)
                                            dap.sendImageWithURL(to, str(path))
# Pembatas Script #
                            elif cmd == '#groupcreator':
                                group = dap.getGroup(to)
                                GS = group.creator.mid
                                dap.sendContact(to, GS)
                            elif cmd == '#groupid':
                                gid = dap.getGroup(to)
                                dap.sendMessage(to, "[ ID Group ]\n" + gid.id)
                            elif cmd == '#grouppicture':
                                group = dap.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                dap.sendImageWithURL(to, path)
                            elif cmd == '#groupname':
                                gid = dap.getGroup(to)
                                dap.sendMessage(to, "[ Nama Group ]\n" + gid.name)
                            elif cmd == '#groupticket':
                                if msg.toType == 2:
                                    group = dap.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        ticket = dap.reissueGroupTicket(to)
                                        dap.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                                    else:
                                        dap.sendMessage(to, "Group Qr not has been Set\nPlease type #groupticket on for opened a groupqr{}openqr".format(str(settings["keyCommand"])))
                            elif cmd == '#groupticket on':
                                if msg.toType == 2:
                                    group = dap.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        sendMentionFooter(to, "[ Group Ticket ]\n Status - GROUP TICKET HAS BEEN ENABLED!\n@!", [sender])
                                    else:
                                        group.preventedJoinByTicket = False
                                        dap.updateGroup(group)
                                        sendMentionFooter(to, "[ Group Ticket ]\n Status - GROUP TICKET HAS BEEN ENABLED!\n@!", [sender])
                            elif cmd == '#groupticket off':
                                if msg.toType == 2:
                                    group = dap.getGroup(to)
                                    if group.preventedJoinByTicket == True:
                                        sendMentionFooter(to, "[ Group Ticket ]\n Status - GROUP TICKET HAS BEEN DISABLED!\n@!", [sender])
                                        #dap.sendMessage(to, "The qr group is already closed")
                                    else:
                                        group.preventedJoinByTicket = True
                                        dap.updateGroup(group)
                                        sendMentionFooter(to, "[ Group Ticket ]\n Status - GROUP TICKET HAS BEEN DISABLED!\n@!", [sender])
                                        #sendMessage(to, "Failed menutup grup qr")
                            elif cmd == '#groupinfo':
                                group = dap.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Mati"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Hidup"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(dap.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "\n  [ Group Info ]"
                                ret_ += "\n   Nama Grup : {}".format(str(group.name))
                                ret_ += "\n   ID Grup : {}".format(group.id)
                                ret_ += "\n   Pembuat Grup : {}".format(str(gCreator))
                                ret_ += "\n   Anggota : {}".format(str(len(group.members)))
                                ret_ += "\n   Anggota yang pending : {}".format(gPending)
                                ret_ += "\n   Qr Grup : {}".format(gQr)
                                ret_ += "\n   Qr : {}".format(gTicket)
                                ret_ += ""
                                dap.sendMessage(to, str(ret_))
                                dap.sendImageWithURL(to, path)
                            elif cmd == '#groupmemberlist':
                                if msg.toType == 2:
                                    group = dap.getGroup(to)
                                    ret_ = "\n   [ Member List ]   "
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n[ Ada {} ]\n".format(str(len(group.members)))
                                    dap.sendMessage(to, str(ret_))
                            elif cmd == '#grouplist':
                              if msg._from in Owner:
                                    groups = dap.groups
                                    ret_ = "\n [ Group List ]\n   "
                                    no = 0 + 1
                                    for gid in groups:
                                        group = dap.getGroup(gid)
                                        ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                        no += 1
                                    ret_ += "\n\n[ Ada {} Groups ]\n".format(str(len(groups)))
                                    dap.sendMessage(to, str(ret_))
# Pembatas Script #
                            elif cmd == "#changedp":
                              if msg._from in Owner:
                                settings["changeDisplayPicture"] = True
                                dap.sendMessage(to, "\n[ Change Display Picture ]\n\nUsage : send 1 pict what u want and, DisplayPicture has been Changed\n")
                            elif cmd.startswith("#fbroadcast: "):
                              if msg._from in Owner:                            
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                friends = dap.friends
                                for friend in friends:
                                    sendMention(friend, "[ Broadcast ]\n@!\n\n{}".format(str(txt), [sender]))
                                    dap.sendMessage(to, "Berhasil broadcast ke {} teman".format(str(len(friends))))                                
                            elif cmd == "#changegp":
                              if msg._from in Admin:
                                if msg.toType == 2:
                                    if to not in settings["changeGroupPicture"]:
                                        settings["changeGroupPicture"].append(to)
                                    dap.sendMessage(to, "\n[Change Group Picture]\n\nUsage : send 1 pict what u want and, GroupPicture has been Changed\n")
                            elif cmd == '#mentioning':                            
                                group = dap.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//100
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*100 : (a+1)*100]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Zero \n'
                                    dap.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    dap.sendMessage(to, "All Mentioned : {} ".format(str(len(nama))))
                                    #sendMention(to, "@!\n\nAll Mentioned : {} ".format(str(len(nama)), [sender])
                                    
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
                                            #sendMention(to, "@!\n「 Ceksider Diaktifkan 」\n\n" + readTime, [sender])
                                            dap.sendMessage(to, "「 Ceksider Diaktifkan 」\n\n" + readTime)
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
                                        dap.sendMessage(to, "「 Ceksider Diaktifkan 」\n\n" + readTime)
                            
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
                                    dap.sendMessage(to, "「 Ceksider telah dimatikan  」\n\n" + readTime)
                                else:
                                    try:
                                        del read['readPoint'][msg.to]
                                        del read['readMember'][msg.to]
                                        del read['readTime'][msg.to]
                                    except:
                                          pass
                                    #sendMention(to, "「 Ceksider telah dimatikan  」\n@!\nWaktu :\n" + readTime, [sender])
                                    dap.sendMessage(to, "「 Ceksider telah dimatikan  」\n\n" + readTime)
        
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
                                    #sendMention(to, "「 Mengulangi riwayat pembaca 」\n@!\n" + readTime, [sender])
                                    dap.sendMessage(to, "「 Ceksider telah direset 」\n\n" + readTime)
                                else:
                                    #sendMention(to, "「 Ceksider belum diaktifkan 」\n@!", [sender])
                                    dap.sendMessage(to, "「 Ceksider telah direset 」\n\n" + readTime)

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
                                        dap.sendMessage(receiver,"   「 Daftar Pembaca 」\nNone")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = dap.getContacts(chiya) 
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
                                        dap.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    dap.sendMessage(receiver,"*Ceksider belum diaktifkan\nKetik 「 #ceksider on 」 untuk mengaktifkan.")
                                                                        
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
                                        dap.sendMessage(receiver,"[ Reader ]:\nNone")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = dap.getContacts(chiya) 
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
                                        dap.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    #sendMention(receiver,"*Ceksider belum diaktifkan\nKetik 「 #ceksider on 」 untuk mengaktifkan\n@!")
                                    dap.sendMessage(receiver,"*Ceksider belum diaktifkan\nKetik 「 #ceksider on 」 untuk mengaktifkan.")
                                    
                            elif text.lower() == '###spamcall':
                                if msg.toType == 2:
                                    group = dap.getGroup(to)
                                    members = [mem.mid for mem in group.members]
                                    call.acquireGroupCallRoute(to)
                                    call.inviteIntoGroupCall(to, contactIds=members)
                                    dap.sendMessage(to, "Berhasil mengundang kedalam telponan group")
                                    
                            elif cmd.startswith('##clearallmessage'):
                              if msg._from in Owner:
                                dap.removeAllMessages(op.param2)
                                dap.sendMessage(to, "Success deleted allMessage for this room")
                                
                            elif cmd.startswith('##youtubemp3 '):
                              if msg._from in Owner:
                                try:
                                    dap.sendMessage(to,"hm wait")
                                    textToSearch = text.replace('##youtubemp3 ', "").strip()
                                    query = urllib.parse.quote(textToSearch)
                                    url = "https://www.youtube.com/results?search_query=" + query
                                    response = urllib.request.urlopen(url)
                                    html = response.read()
                                    soup = BeautifulSoup(html, "html.parser")
                                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                    dl = 'https://www.youtube.com' + results['href']
                                    vid = pafy.new(dl)
                                    stream = vid.audiostreams
                                    for s in stream:
                                        start = timeit.timeit()
                                        vin = s.url
                                        img = vid.bigthumbhd
                                        hasil = vid.title
                                        hasil += '\n\nDi upload oleh ✍️ ' +str(vid.author)
                                        hasil += '\nDurasi ⏱️ ' +str(vid.duration)+ ' (' +s.quality+ ') '
                                        hasil += '\nDi Like sebanyak👍 ' +str(vid.rating)
                                        hasil += '\nDi tonton sebanyak 👬 ' +str(vid.viewcount)+ 'x '
                                        hasil += '\nDi upload pada 📆 ' +vid.published
                                        hasil += '\n\nWaktunya⏲️ %s' % (start)
                                        hasil += '\n\n Waitting proses mp3....'
                                    dap.sendAudioWithURL(to, vin)
                                    dap.sendImageWithURL(to, img)
                                    dap.sendMessage(to, hasil)
                                except:
                                    dap.sendMessage(to, "Fail")                                
                                
                            elif cmd.startswith('##pimention'):
                              if msg._from in Owner:
                                group = dap.getGroup(msg.to)
                                k = len(group.members)//100
                                for j in range(k+1):
                                    aa = []
                                    for x in group.members:
                                        aa.append(x.mid)
                                    try:
                                        arrData = ""
                                        textx = "     [ Mention {} Members ]    \n1 - ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + " - "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(dap.getGroup(msg.to).name))
                                                except:
                                                   no = "[ Success ]"
                                        msg.to = msg.to
                                        msg.text = textx
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        dap.sendMessage(msg)
                                    except Exception as e:
                                        dap.sendMessage(to, str(e))                                
                                
                            elif cmd.startswith("##Gbcpict "):
                              if msg._from in Owner:
                                  txt = msg.text.split(" ")
                                  bcteks = msg.text.replace("Gbcpict "+txt[1]+" "+txt[2]+" ","")
                                  n = dap.getGroupIdsJoined()
                                  for people in n:     
                                        dap.sendImageWithURL(people, txt[2]) 
                                        dap.sendMessage(people, bcteks)
                                        dap.sendContact(people, txt[1])                                                                         
                            
                            elif cmd.startswith("##botproblem "):
                              if msg._from in Owner:
                                at = text.replace("##botproblem ","")
                                aa = dap.getContact(sender).displayName
                                ab = dap.getGroup(msg.to).name
                                ac = dap.getContact(sender).mid
                                dap.sendMessage(to,"Your message has been added to the que")
                                dap.sendMessage(to,"「 List Problem 」\nName: "+aa+"\nFrom Group: "+ab+"\nProblem: "+at+"\nMid User: "+ac)
                                dap.sendContact(ac)
                            
                            elif cmd.startswith("#murottal"):
                               try:
                                  sep = msg.text.split(" ")
                                  surah = int(text.replace(sep[0] + " ",""))
                                  if 0 < surah < 115:
                                      if surah not in [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 16, 17, 18, 20, 21, 23, 26, 37]:
                                          if len(str(surah)) == 1:
                                              audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-00" + str(surah) + "-muslimcentral.com.mp3"
                                              dap.sendAudioWithURL(to, audionya)
                                          elif len(str(surah)) == 2:
                                              audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-0" + str(surah) + "-muslimcentral.com.mp3"
                                              dap.sendAudioWithURL(to, audionya)
                                          else:
                                              audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-" + str(surah) + "-muslimcentral.com.mp3"
                                              dap.sendAudioWithURL(to, audionya)
                                      else:
                                          dap.sendMessage(to, "Surah terlalu panjang")
                                  else:
                                      dap.sendMessage(to, "Quran hanya 114 surah")
                               except Exception as error:
                                 dap.sendMessage(to, "error\n"+str(error))
                                 logError(error)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
                            elif cmd.startswith("#screenshot "):
                                type_ = msg.text.lower()[11:12]
                                params = {'url':msg.text.lower()[13:]}
                                if type_ == '1':
                                    url = 'https://dzin.xyz/api/screenshot/phone.php?url=instagram.com'
                                elif type_ == '2':
                                    url = 'https://dzin.xyz/api/screenshot/desktop.php?'
                                elif type_ == '3':
                                    url = 'https://dzin.xyz/api/screenshot/tablet.php?'
                                data = requests.get(url, params=params).json()
                                dap.sendImageWithURL(msg.to, data['image'])
                            
                            elif cmd == "#siderrr":
                                tz = pytz.timezone("Asia/Makassar")
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
                                        dap.sendMessage(receiver,"Tidak Ada Sider")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = dap.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '[R E A D E R ]\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\n" + readTime
                                    try:
                                        dap.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    dap.sendMessage(receiver,"Lurking belum diaktifkan")
                            elif cmd.startswith("#mimicadd"):
                              if msg._from in Owner:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        settings["mimic"]["target"][target] = True
                                        dap.sendMessage(msg.to,"\nTarget ditambahkan!\n")
                                        break
                                    except:
                                        dap.sendMessage(msg.to,"\ Gagal menambahkan target\n")
                                        break
                            elif cmd.startswith("#mimicdel"):
                              if msg._from in Owner:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        del settings["mimic"]["target"][target]
                                        dap.sendMessage(msg.to,"\n Target dihapuskan!\n")
                                        break
                                    except:
                                        dap.sendMessage(msg.to,"\n Gagal menghapus target\n")
                                        break
                                    
                            elif cmd == "#mimiclist":
                              if msg._from in Owner:
                                if settings["mimic"]["target"] == {}:
                                    dap.sendMessage(msg.to,"\n Tidak Ada Target\n")
                                else:
                                    mc = "    [ Mimic List ]    "
                                    for mi_d in settings["mimic"]["target"]:
                                        mc += "\n "+dap.getContact(mi_d).displayName
                                    mc += "\n    [ MIMIC CMD]   "
                                    dap.sendMessage(msg.to,mc)
                                                
                            elif cmd.startswith("#wordbanlist"):
                              if msg._from in Owner:
                                         if wordban not in [[]]:
                                          no = 1
                                          wordbans = "[ WordBan List ]\n"
                                          for word in wordban:
                                           wordbans+="\n{}. {}".format(str(no),str(word))
                                           no+=1
                                          wordbans+="\n"
                                          #dap.sendMessage(to, str(wordbans))
                                          dap.sendMessage(to, str(wordbans),{'AGENT_ICON':'http://dl.profile.line-cdn.net/0hkY3juiptNHYOExk5wsdLITJWOht5PTI-diUpGX8RPhZ0IydzMSV_FC0VaxV0I3JyMCZ4Ei8VOEQh','AGENT_LINK':'https://line.me/ti/p/~yapuy','AGENT_NAME':'WordBan List'})
                                         if wordban == []:
                                          dap.sendMessage(to, "[ Notified Word Ban ]\nNo WordBan yet")
                
                            elif cmd.startswith("#addwordban: "):
                              #if msg._from in Owner:
                             word = text.replace("addwordban: ","")
                             if word not in wordban:
                              wordban.append(word)
                              dap.sendMessage(to, "[ Notified Word Ban ]\nSuccess Added {} From WordBan".format(str(word)))
                             else:
                              dap.sendMessage(to, "[ Notified Word Ban ]\n{} Already added".format(str(word)))

                            elif cmd.startswith("#delwordban: "):
                              #if msg._from in Owner:
                                word = text.replace("delwordban: ","")
                                if word in wordban:
                                 wordban.remove(word)
                                 dap.sendMessage(to, "[ Notified Word Ban ]\nSuccess Deleted {} From WordBan".format(str(word)))
                                else:
                                 dap.sendMessage(to, "[ Notified Word Ban ]\n{} Notfound".format(str(word)))

                            elif text.lower() == "#wordban":
                              #if msg._from in Owner:
                                dap.sendMessage(to, "[ Notified Word Ban ]\n{} Registered to WordBan\nSorry".format(str(text)))
                                dap.kickoutFromGroup(to, [sender])

                            elif cmd.startswith("#mimic"):
                              if msg._from in Owner:
                                sep = text.split(" ")
                                mic = text.replace(sep[0] + " ","")
                                if mic == "on":
                                    if settings["mimic"]["status"] == False:
                                        settings["mimic"]["status"] = True
                                        dap.sendMessage(msg.to,"\n Reply Message on\n")
                                elif mic == "off":
                                    if settings["mimic"]["status"] == True:
                                        settings["mimic"]["status"] = False
                                        dap.sendMessage(msg.to,"\n Reply Message off\n")
# Pembatas Script #   
                            elif cmd.startswith("#checkwebsite"):
                              if msg._from in Owner:
                                try:
                                    sep = text.split(" ")
                                    query = text.replace(sep[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                    data = r.text
                                    data = json.loads(data)
                                    dap.sendImageWithURL(to, data["result"])
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("#checkdate"):
                              if msg._from in Owner:
                                try:
                                    sep = msg.text.split(" ")
                                    tanggal = msg.text.replace(sep[0] + " ","")
                                    r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                    data=r.text
                                    data=json.loads(data)
                                    ret_ = "[ D A T E ]"
                                    ret_ += "\nDate Of Birth : {}".format(str(data["data"]["lahir"]))
                                    ret_ += "\nAge : {}".format(str(data["data"]["usia"]))
                                    ret_ += "\nBirthday : {}".format(str(data["data"]["ultah"]))
                                    ret_ += "\nZodiak : {}".format(str(data["data"]["zodiak"]))
                                    dap.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                                   
                            elif text.lower().startswith("#spam "):
                                syd=text.split(" ")
                                syd=text.replace(syd[0]+" ","")
                                syd=syd.split('*')
                                txt=str(syd[0])
                                num=int(syd[1])
                                if num <=100:
                                    for spammer in range(0,num):
                                        dap.sendMessage(to,txt)
                                else:
                                    dap.sendMessage(to,'?')            
                                    
                            elif cmd.startswith("#checkpraytime "):
                              if msg._from in Owner:
                                separate = msg.text.split(" ")
                                location = msg.text.replace(separate[0] + " ","")
                                r = requests.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(location))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isya : ":
                                    ret_ = "* Jadwal Sholat Sekitar *" + data[0] + " ]"
                                    ret_ += "\n* Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n* Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\n* " + data[1]
                                    ret_ += "\n* " + data[2]
                                    ret_ += "\n* " + data[3]
                                    ret_ += "\n* " + data[4]
                                    ret_ += "\n* " + data[5]
                                    ret_ += ""
                                    dap.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("#jadwalsholat"):
                              if msg._from in Owner:
                                anunya = text.replace("jadwalsholat ","")
                                r = requests.get("http://leert.corrykalam.gq/praytime.php?location={}".format(str(anunya)))
                                data = r.text
                                data = json.loads(data)
                                try:
                                    fine = "   [ Jadwal Sholat ]   \n\n"
                                    fine += "Subuh : {}".format(str(data["pray_time"]["subuh"]))
                                    fine += "\nDhuhur : {}".format(str(data["pray_time"]["dzuhur"]))
                                    fine += "\nAshar : {}".format(str(data["pray_time"]["ashar"]))
                                    fine += "\nMaghrib : {}".format(str(data["pray_time"]["maghrib"]))
                                    fine += "\nIsya : {}".format(str(data["pray_time"]["isha"]))
                                    fine += "\nImsak : {}".format(str(data["pray_time"]["imsak"]))
                                    fine += "\n\nTimezone : {}".format(str(data["info"]["timezone"]))
                                    fine += "\nDate : {}".format(str(data["info"]["date"]))
                                    fine += "\nLatitude : {}".format(str(data["info"]["latitude"]))
                                    fine += "\nLongitude : {}".format(str(data["info"]["longitude"]))
                                    fine += "\nSource : {}".format(str(data["info"]["source"]))
                                    dap.sendMessage(to, str(fine))
                                except Exception as error:
                                    dap.sendMessage(to,str(error))                                    
                                                                                                                                                                                                                                      
                            elif cmd.startswith("kintil"):
                                dap.sendImageWithURL(to, "https://stickershop.line-scdn.net/stickershop/v1/sticker/26911499/ANDROID/sticker.png")                             
                                dap.sendMessage(to, "kerad")    

                            #elif cmd.startswith("unsend ") and sender == "uac8e3eaf1eb2a55770bf10c3b2357c33":
                            #    args = text.replace('unsend','')
                            #    mes = 0
                            #    try:
                            #        mes = int(args[1])
                            #    except:
                            #        mes = 1
                            #    M = cliet.getRecentMessagesV2(to, 101)
                            #    MId = []
                            #    for ind,i in enumerate(M):
                            #        if ind == 0:
                            #            pass
                            #        else:
                            #            if i._from == dap.profile.mid:
                            #                MId.append(i.id)
                            #                if len(MId) == mes:
                            #                    break
                            #    def unsMes(id):
                            #        dap.unsendMessage(id)
                            #    for i in MId:
                            #        thread1 = threading.Thread(target=unsMes, args=(i,))
                            #        thread1.start()
                            #        thread1.join()
                            #    dap.sendMessage(to, '[ Unsend {} message ]'.format(len(MId)))

#################PUY##############

                            elif text.lower() == "#acaratv":
                                         result = requests.get("http://ari-api.herokuapp.com/jadwaltv").json()["result"];no=1;tv="   [ Jadwal Acara TV ]   \n\n"
                                         for wildan in result:
                                          tv+="{}. {} - {} ({})\n".format(str(no), str(wildan["channelName"]), str(wildan["acara"]), str(wildan["jam"]))
                                          no+=1
                                         tv+="\n";dap.sendMessage(to, str(tv))                                         
                                         
                            elif cmd.startswith("keluar"):
                                tgb = dap.getGroup(op.param1)
                                dan = dap.getContact(op.param2)   
                                sendMentionFooter(op.param1, "@!, Gbye", [op.param2])
                                pi.leaveGroup(to)
                                dap.leaveGroup(to)
                                         
                            elif cmd.startswith("#keluar"):
                                #tgb = dap.getGroup(op.param1)
                                #dan = dap.getContact(op.param2)
                                #gid = dap.getGroup(to)
                                dap.sendMessage(to, "Gbye")
                                #sendMentionFooter(op.param1, "@!, Gbye", [op.param2])
                                dap.getGroupIdsJoined()
                                pi.leaveGroup(to)
                                dap.leaveGroup(to)
                                
                            elif cmd.startswith("#pi:keluar"):
                                #tgb = dap.getGroup(op.param1)
                                #dan = dap.getContact(op.param2)
                                #gid = dap.getGroup(to)
                                pi.sendMessage(to, "Gbye")
                                #sendMentionFooter(op.param1, "@!, Gbye", [op.param2])
                                pi.getGroupIdsJoined()
                                pi.leaveGroup(to)

                            elif cmd.startswith("#pm"):
                                  sep = msg.text.split(" ")
                                  name = msg.text.replace(sep[0] + " ","")
                                  mention = eval(msg.contentMetadata["MENTION"])
                                  mention1 = mention["MENTIONEES"][0]["M"]
                                  contact = dap.getContact(mention1)
                                  pisah = name.replace("@"+contact.displayName,"")
                                  ginfo = dap.getGroup(receiver).name
                                  pengirim = dap.getContact(sender).displayName
                                  result = "Sender : "+ pengirim +"\nFrom group : "+ ginfo +"\n\nMessage : "+pisah
                                  try:
                                      dap.sendMessage(contact.mid, result)
                                      sendMentionFooter(to, "[ SendMessage to Member ]\n Status - Message has been Sent!\n@!", [sender])
                                  except Exception as e:
                                      dap.sendMessage(to, str(e))
                                                                                                      
                            elif cmd.startswith("#pc"):
                                  sep = msg.text.split(" ")
                                  name = msg.text.replace(sep[0] + " ","")
                                  mention = eval(msg.contentMetadata["MENTION"])
                                  mention1 = mention["MENTIONEES"][0]["M"]
                                  contact = dap.getContact(mention1)
                                  pisah = name.replace("@"+contact.displayName,"")
                                  #ginfo = dap.getGroup(receiver).name
                                  #pengirim = dap.getContact(sender).displayName
                                  result = ""+pisah 
                                  try:
                                      dap.sendMessage(contact.mid, result)
                                      sendMentionFooter(to, "[ SendMessage to Member ]\n Status - Message has been Sent!\n@!", [sender])
                                  except Exception as e:
                                      dap.sendMessage(to, str(e))
                                                                
                            elif cmd.startswith('#pcallmember '):
                                   try:
                                    sendMentionFooter(to, "[ SendMessage to AllMember ]\n Status - Sending Message...\n@!", [sender])
                                    sep = msg.text.split(" ")
                                    text = msg.text.replace(sep[0] + " ","")
                                    pengirim = dap.getContact(sender).displayName
                                    gpinfo = dap.getGroup(msg.to).name                                    
                                    kontak = dap.getGroup(msg.to)
                                    grup = kontak.members
                                    for ids in grup:
                                        mids = dap.getProfile().mid
                                        midd = ids.mid
                                        if midd == mids:
                                            pass
                                        else:
                                            #result = "Isi Pesan :"+text+"\nPesan Dari : "+ pengirim +"\nDari Grup : "+ gpinfo
                                            result = "Sender : "+ pengirim +"\nFrom Group : "+ gpinfo +"\n\nMessage : "+ text
                                            dap.sendMessage(ids.mid, str(result))
                                    sendMentionFooter(to, "[ SendMessage to All Member ]\n Status - Message has been Sent!\n@!", [sender])
                                   except Exception as e:
                                       dap.sendMessage(to, str(e))

                            elif cmd.startswith("pcid"):
                                dan = text.split("|")
                                x = dap.findContactsByUserid(dan[1])
                                a = dap.getContact(sender)
                                dap.sendMessage(x.mid,"Anda mendapatkan pesan dari "+a.displayName+"\n\n"+dan[2])
                                dap.sendMessage(to,"Sukses mengirim pesan ke "+x.displayName+"\nDari: "+a.displayName+"\nPesan: "+dan[2])    

                            elif cmd.startswith("sholatttt"):
                              #if msg._from in Owner:
                              try:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               api = requests.get("https://farzain.xyz/api/shalat.php?apikey={}&id={}".format(str(search)))
                               data = api.text
                               data = json.loads(data)
                               if data["status"] == "success":
                                hasil = "Subuh : {}".format(str(data["respon"]["shubuh"]))
                                hasil += "\nDzuhur : {}".format(str(data["respon"]["dzuhur"]))
                                hasil += "\nAshar : {}".format(str(data["respon"]["ashar"]))
                                hasil += "\nMaghrib : {}".format(str(data["respon"]["maghrib"]))
                                hasil += "\nIsya : {}".format(str(data["respon"]["isya"]))
                                path = str(data["peta_gambar"])
                                dap.sendImageWithURL(msg.to, str(path))
                                dap.sendMessage(msg.to, str(hasil))
                               else:
                                sendMentionFooter(msg.to, "Maaf @!,lokasi tidak ditemukan", [sender])
                              except Exception as error:
                                dap.sendMessage(msg.to, str(error))                        

                            elif cmd.startswith("filmmmm"):
                                try:
                                 sep = msg.text.split(" ")
                                 search = msg.text.replace(sep[0] + " ","")
                                 api = requests.get("https://farzain.xyz/api/film.php?apikey={}&id={}".format(str(search)))
                                 data = api.text
                                 data = json.loads(data)
                                 if data["status"] == "success":
                                  hasil = "[ Result Film ]"
                                  hasil += "\nTitle : {}".format(str(data["Title"]))
                                  hasil += "\nYear : {}".format(str(data["Year"]))
                                  hasil += "\nRated : {}".format(str(data["Rated"]))
                                  hasil += "\nReleased : {}".format(str(data["Released"]))
                                  hasil += "\nDuration : {}".format(str(data["Runtime"]))
                                  hasil += "\nGenre : {}".format(str(data["Genre"]))
                                  path = str(data["Poster"])
                                  dap.sendImageWithURL(msg.to, str(path))
                                  dap.sendMessage(msg.to, str(hasil))
                                 else:
                                  sendMentionV2(msg.to, "Maaf @!,hasil pencarin tidak ditemukan", [sender])
                                except Exception as error:
                                 dap.sendMessage(msg.to, str(error))                               
                       
                            elif cmd.startswith("spmid: "):
                               #if msg.from_ in Admin or msg.from_ in staff or msg.from_ in creator or msg.from_ in penyewa:
                                  korban2 = msg.text.split(" ")
                                  gs = dap.getGroup(msg.to)
                                  jmlh = int(korban2[4]) 
                                  txt = msg.text.split(" ")
                                  text = msg.text.replace(cmd+ "spmid: "+str(korban2[3])+" "+ str(jmlh)+ " ","")
                                  x = dap.findContactsByUserid(korban2[3])
                                  dap.sendMessage(msg.to,"Dimulai ya")
                                  if jmlh <= 1000:
                                   for baba in range(jmlh):
                                    try:
                                      dap.sendMessage(x.mid, text)
                                    except:
                                       pass
                                   dap.sendMessage(msg.to, "Sudah di spamin XD")
                                  else:
                                      dap.sendMessage(msg.to,"Jumlah melebihi batas")
 
                            elif cmd.startswith ("invitegroupcall "):
                              if msg._from in Owner:
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    strnum = text.replace(sep[0] + " ","")
                                    num = int(strnum)
                                    dap.sendMessage(to, "Berhasil mengundang kedalam telponan group")
                                    for var in range(0,num):
                                       group = dap.getGroup(to)
                                       members = [mem.mid for mem in group.members]
                                       dap.acquireGroupCallRoute(to)                                      
                                       dap.inviteIntoGroupCall(to, contactIds=members)                            
 
                            elif cmd == "#delannounce":
                               a = dap.getChatRoomAnnouncements(to)
                               anu = []
                               for b in a:
                                   c = b.announcementSeq
                                   anu.append(c)
                                   dap.removeChatRoomAnnouncement(to, c)
                                   sendMentionFooter(to, "[Notified Announcement]\n - Success Removed Announce @!", [sender])
                                                                                                                                            
                            elif text.lower() == 'limitlist':
                                  if msg._from not in creator:
                                    if settings["limituser"] == {}:
                                        dap.sendMessage(to, "Kosong")
                                    else:
                                        mc = "Daftar Limit："
                                        for mi_d in settings["limituser"]:
                                          if settings["limituser"][mi_d]["count"] == 5:
                                            mc += "\n\n• Nama : " + dap.getContact(mi_d).displayName + "\n• Count : "+settings['limituser'][mi_d]['count'] + "\n• Limit : "+settings['limituser'][mi_d]['limit']
                                        dap.sendMessage(to, mc)
                            
                            elif cmd.startswith("#announce "):
                                sep = text.split(" ")   
                                a = text.replace(sep[0] + " ","")
                                z = dap.getGroupIdsJoined()
                                b = dap.getContact(sender)
                                c = ChatRoomAnnouncementContents()
                                c.displayFields = 5
                                c.text = a
                                c.link = "https://line.me/ti/p/~yapuy"
                                c.thumbnail = "http://dl.profile.line-cdn.net/0hkY3juiptNHYOExk5wsdLITJWOht5PTI-diUpGX8RPhZ0IydzMSV_FC0VaxV0I3JyMCZ4Ei8VOEQ"
                                c.iconlink = "http://dl.profile.line-cdn.net/0hkY3juiptNHYOExk5wsdLITJWOht5PTI-diUpGX8RPhZ0IydzMSV_FC0VaxV0I3JyMCZ4Ei8VOEQh"
                                try:            
                                    dap.createChatRoomAnnouncement(to, 1, c)
                                    sendMentionFooter(to, "[Notified Announcement]\n - Success Added Announce @!", [sender])
                                except Exception as e:
                                   dap.sendMessage(to, str(e))
                                   
                            elif cmd.startswith("#retrowavetextlist"):
                             dap.sendMessage(to, "Retrowave Text List\n\n- Text 1\n- Text 2\n- Text 3\n- Text 4\n\nUntuk melihat gambar text, silahkan ketik retrowavetext-num")

                            elif text.lower() == "#retrowavebglist":
                             dap.sendMessage(to, "Retrowave Background List\n\n- Background 1\n- Background 2\n- Background 3\n- Background 4\n- Background 5\n\nUntuk melihat gambar background, silahkan ketik retrowavebg-num")
                             
                            elif cmd.startswith("#retrowavebg-"):
                             num = text.replace("#retrowavebg-","")
                             if num not in ["1","2","3","4","5"]:dap.sendMessage(to,"maaf jenis retrowavebg {} tidak ada\n\nuntuk melihat daftar retrowavebg silahkan ketik retrowavebglist.".format(num))
                             else:
                              if num == "1":
                               dap.sendImageWithURL(to, "https://cdn.photofunia.com/effects/retro-wave/resources/1txxjga.jpg")
                              elif num == "2":
                               dap.sendImageWithURL(to, "https://cdn.photofunia.com/effects/retro-wave/resources/ign25g.jpg")
                              elif num == "3":
                               dap.sendImageWithURL(to, "https://cdn.photofunia.com/effects/retro-wave/resources/vtejls.jpg")
                              elif num == "4":
                               dap.sendImageWithURL(to, "https://cdn.photofunia.com/effects/retro-wave/resources/2t537o.jpg")
                              elif num == "5":
                               dap.sendImageWithURL(to, "https://cdn.photofunia.com/effects/retro-wave/resources/11rfhkj.jpg")
                               
                            elif cmd.startswith("#retrowavetext-"):                            
                             num = text.replace("#retrowavetext-","")
                             if num not in ["1","2","3","4"]:dap.sendMessage(to,"maaf jenis retrowavetext {} tidak ada\n\nuntuk melihat daftar retrowavetext silahkan ketik retrowavetextlist.".format(num))
                             else:
                              if num == "1":
                               dap.sendImageWithURL(to, "https://cdn.photofunia.com/effects/retro-wave/resources/eye191.jpg")
                              elif num == "2":
                               dap.sendImageWithURL(to, "https://cdn.photofunia.com/effects/retro-wave/resources/1xxre9n.jpg")
                              elif num == "3":
                               dap.sendImageWithURL(to, "https://cdn.photofunia.com/effects/retro-wave/resources/9ddnhx.jpg")
                              elif num == "4":
                               dap.sendImageWithURL(to, "https://cdn.photofunia.com/effects/retro-wave/resources/dlxine.jpg")
                               
                            elif cmd.startswith("#retrowave"):
                             dan = text.split("|")
                             text1 = dan[1]
                             text2 = dan[2]
                             text3 = dan[3]
                             btype = dan[4]
                             ttype = dan[5]
                             if btype in ["1","2","3","4","5"] and ttype in ["1","2","3","4"]:
                              data = requests.get("http://corrykalam.gq/retrowave.php?text1={}&text2={}&text3={}&btype={}&ttype={}".format(text1,text2,text3,btype,ttype)).json()
                              dap.sendImageWithURL(to, data["image"])
                             else:
                              dap.sendMessage(to, "Background Type atau Text Type salah, silahkan cek :\n- retrowavetextlist\n- retrowavebglist")
                             
                            elif cmd.startswith("#changedual"):
                              if msg._from in Owner:
                                if msg.contentType == 0:
                                       settings["ChangeVideoProfilevid"] = True
                                       #dap.sendMessage(to, "Send 1 Video")
                                       sendMentionFooter(to, "[ Notified ChangeDual ]\nChangeDual Started!\n\nSend 1 Video what u want\n@!", [sender])
                                       if msg.contentType == 2:
                                           path = dap.downloadObjectMsg(msg_id,saveAs="tmp/vid.bin")
                                           settings["ChangeVideoProfilevid"] = False
                                           settings["ChangeVideoProfilePicture"] = True
                                           #dap.sendMessage(to, "Send 1 Picture")
                                           sendMentionFooter(to, "[ Notified ChangeDual ]\nChangeDual Started!\n\nSend 1 Picture what u want\n@!", [sender])
                                           if msg.contentType == 1:
                                               path = dap.downloadObjectMsg(msg_id)
                                               settings["ChangeVideoProfilePicture"] = False
                                               dap.updateProfileVideoPicture(path)
                                               #dap.sendMessage(to, "success")
                                               sendMentionFooter(to, "[ Notified ChangeDual ]\nSuccessed Changedual\n @!", [sender])

                            elif cmd.startswith("#gitlabprofile "):
                              if msg._from in Owner:
                                dan = "[ GitLab Profile ]\n\n"
                                user = text.replace("gitlabprofile ","")
                                data = requests.get("http://moeapi.panel.moe/api/gitlab/profile/?apikey=beta&username="+user).json()
                                if "message" not in data:
                                 dan+="Name: "+str(data["result"]["name"])
                                 dan+="\nUsername: "+str(data["result"]["username"])
                                 dan+="\nBio: "+str(data["result"]["bio"])
                                 dan+="\nSince: "+str(data["result"]["since"])
                                 dap.sendImageWithURL(to, data["result"]["image"])
                                 dan+="\n\n[ Finish ]"
                                 dap.sendMessage(to, str(dan))                        
                                            
                            elif cmd.startswith("#clonegroup "):
                              if msg._from in Owner:
                                gname = msg.text.replace("clonegroup ", "")
                                group = dap.getGroup(msg.to)
                                members = [mem.mid for mem in group.members] + [pen.mid for pen in group.invitee] if group.invitee else [mem.mid for mem in group.members]
                                members.remove(dap.profile.mid)
                                for mem in members:
                                    dap.findAndAddContactsByMid(mem)
                                dap.createGroup(gname, members)                                                                       
                                            
                            elif cmd.startswith("#unsend "):
                              if msg._from in Owner:
                                args = text.replace("unsend","")
                                #args = removeCmd("unsend", text)
                                mes = 0
                                try:
                                    mes = int(args[1])
                                except:
                                    mes = 1
                                M = dap.getRecentMessages(to, 101)
                                MId = []
                                for ind,i in enumerate(M):
                                    if ind == 0:
                                        pass
                                    else:
                                        if i._from == dap.profile.mid:
                                            MId.append(i.id)
                                            if len(MId) == mes:
                                                break
                                def unsMes(id):
                                    dap.unsendMessage(id)
                                for i in MId:
                                    thread1 = threading.Thread(target=unsMes, args=(i,))
                                    thread1.start()
                                    thread1.join()
                                dap.sendMessage(to, '「 Unsend {} message 」'.format(len(MId)))

                            elif cmd.startswith("mantap"):
                                dap.sendImageWithURL(to, "https://stickershop.line-scdn.net/stickershop/v1/sticker/47751647/ANDROID/sticker.png")
                                sendMention(to, "@!", [sender])

                            elif cmd.startswith("logout"):
                                dap.sendImageWithURL(to, "https://stickershop.line-scdn.net/stickershop/v1/sticker/16365599/ANDROID/sticker.png")                             
                                
                            elif cmd.startswith("hmm"):
                                dap.sendImageWithURL(to, "https://stickershop.line-scdn.net/stickershop/v1/sticker/31093005/ANDROID/sticker.png")
                                         
                            elif cmd.startswith("#bc"):
                                wildan = cmd.split("*")
                                bc["txt"] = wildan[1];bc["mid"] = wildan[2];bc["img"] = True
                                dap.sendMessage(to, "Send 1 image")
                                         
                            elif cmd.startswith("bc: "):
                              if msg._from in Owner:
                                sep = text.split(" ")
                                pesan = text.replace(sep[0] + " ","")
                                saya = dap.getGroupIdsJoined()
                                for group in saya:
                                   dap.sendMessage(group,"" + str(pesan))
                                         
                            elif cmd.startswith("#Bc*Usage"):       
                                #sendMentionFooter(to, "[ Broadcast ]\n\nUsage : dap-bc*bctext*yourmid.")
                                sendMentionFooter(to, "[ Broadcast Usage ]\n\nUsage : dap-bc*bctext*yourmid\n @!", [sender])

                            elif cmd.startswith("#Profile Changer*Usage"):       
                                #sendMentionFooter(to, "[ Profile Changer ]\n\n - Change Group Picture\nUsage : type Changegp and send 1 pict what u want.\n\n - Change Display Picture\nUsage : type Changedp and Send 1 pict what u want.")                                                            
                                sendMentionFooter(to, "[ Profile Changer ]\n\n - Change Group Picture\nUsage : type Changegp and send 1 pict what u want.\n\n - Change Display Picture\nUsage : type Changedp and Send 1 pict what u want\n @!", [sender])
                                
                            elif cmd.startswith("#Announcement*Usage"):       
                                #dap.dap.sendMessage(to, "[ Announcement Usage ]\n\n - Add Announcement\nUsage : Announce (text)\n\n - Remove Announcement\nUsage : Delannounce")                                         
                                sendMentionFooter(to, "[ Announcement Usage ]\n\n - Add Announcement\nUsage : Announce (text)\n\n - Remove Announcement\nUsage : Delannounce\n @!", [sender])
                                
                            elif cmd.startswith("#checkweather "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    tz = pytz.timezone("Asia/Makassar")
                                    timeNow = datetime.now(tz=tz)
                                    if "result" not in data:
                                        ret_ = "* Weather Status *"
                                        ret_ += "\n* Location : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\n* Suhu : " + data[1].replace("Suhu : ","") + "°C"
                                        ret_ += "\n* Kelembaban : " + data[2].replace("Kelembaban : ","") + "%"
                                        ret_ += "\n* Tekanan udara : " + data[3].replace("Tekanan udara : ","") + "HPa"
                                        ret_ += "\n* Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + "m/s"
                                        ret_ += "\n* Time Status *"
                                        ret_ += "\n* Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                        ret_ += "\n* Jam : " + datetime.strftime(timeNow,'%H:%M:%S') + " WIB"
                                        ret_ += ""
                                        dap.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("#checklocation "):   
                                sep = text.split(" ")
                                location = text.replace(sep[0] + " ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = random.choice(settings["userAgent"])
                                    r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                    data = r.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "╔══[ Details Location ]"
                                        ret_ += "\n╠ Lokasi : " + data[0]
                                        ret_ += "\n╠ Google Maps : " + link
                                        ret_ += "\n╚══[ Complete ]"
                                    else:
                                        ret_ = "[ Details Location ] Error : Lokasi tidak ditemukan"
                                        dap.sendMessage(to,str(ret_))
							
							#elif cmd.startswith('Quran '):
							#    try:
                            #    query = txt.replace('Quran ','')
                            #    text = query.split("|")
                            #    surah = int(text[0])
                            #    ayat1 = int(text[1])
                            #    ayat2 = int(text[2])
                            #    result = requests.get("https://farzain.xyz/api/alquran.php?id={}&from={}&to={}".format(surah, ayat1, ayat2))
                            #    data = result.text
                            #    data = json.loads(data)
                            #    if data["status"] == "done":
                            #        hasil = "[ Al-Qur'an ]\n"
                            #        hasil += "\n  Name : {}".format(str(data["nama_surat"]))
                            #        hasil += "\n  Meaning : {}".format(str(data["arti_surat"]))
                            #        hasil += "\n  Ayat :"
                            #        for ayat in data["ayat"]:
                            #            hasil += "\n{}".format(str(ayat))
                            #        hasil += "\n  Meaning Ayat :"
                            #        for arti in data["arti"]:
                            #            hasil += "\n{}".format(str(arti))
                            #        dap.sendMessage(to, str(hasil))
                            
                            elif cmd.startswith("#spamcall"):
                              if msg._from in Owner:
                                if msg.toType == 2:
                                   group = dap.getGroup(to)
                                   members = [mem.mid for mem in group.members]
                                   jmlh = int(settings["limit"])
                                   dap.sendMessage(msg.to, "Invitation Call Groups {} In Progress ".format(str(settings["limit"])))
                                   if jmlh <= 9999:
                                    for x in range(jmlh):
                                     try:
                                        dap.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        dap.sendMessage(msg.to,str(e))
                                    else:
                                        dap.sendMessage(msg.to,"Invitation Call Groups Successed")
                                
                            
                            elif cmd.startswith('invgroupcall'):
                                if msg.toType == 2:
                                    group = dap.getGroup(to)
                                    members = [mem.mid for mem in group.members]
                                    call.acquireGroupCallRoute(to)
                                    call.inviteIntoGroupCall(to, contactIds=members)
                                    dap.sendMention(to, "[ Notified GroupCall ]\nInvited Groupcall Status - Successed\n@!", [sender])                    
                    
                            elif cmd.startswith("#tagid: "):
                                try:
                                 id = text.replace("tagid: ","")
                                 dan = line.findContactsByUserid(id)
                                 sM2(to, "Hai @!", [dan.mid])
                                except Exception as wk:
                                 #line.sendMessage(to, "Tidak ada id {}".format(str(id)))
                                 line.sendMessage(to, str(wk))        
                    
                            elif cmd.startswith('tes'):
                                 dap.sendMessage(to, 'tis')
                    
                            elif cmd.startswith('#call '):
                                try:
                                    call = text.replace('#call ','')
                                    r = requests.get('https://farzain.xyz/api/prank().php?apikey=&id='+call+'&type=2')
                                    sendMention(receiver, "@! Sukses melakukan panggilan ke nomor  "+call,[sender])
                                except Exception as e:
                                    dap.sendMessage(receiver, str(e))
                                    logError(e)

                            elif cmd.startswith('#sms '):
                                try:
                                    sms = text.replace('#sms ','')
                                    r = requests.get('https://farzain.xyz/api/prank().php?apikey=&id='+sms+'&type=1')
                                    sendMention(receiver, "@! Sukses mengirim pesan ke nomor  "+sms,[sender])
                                except Exception as e:
                                    dap.sendMessage(receiver, str(e))
                                    logError(e)									
                            elif cmd.startswith("#instainfo"):
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.farzain.com/ig_post.php".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "     [ Profile Instagram ]     "
                                        ret_ += "\n  Nama : {}".format(str(data["graphql"]["user"]["full_name"]))
                                        ret_ += "\n  Username : {}".format(str(data["graphql"]["user"]["username"]))
                                        ret_ += "\n  Bio : {}".format(str(data["graphql"]["user"]["biography"]))
                                        ret_ += "\n  Followers : {}".format(str(data["graphql"]["user"]["edge_followed_by"]["count"]))
                                        ret_ += "\n  Following : {}".format(str(data["graphql"]["user"]["edge_follow"]["count"]))
                                        if data["graphql"]["user"]["is_verified"] == True:
                                            ret_ += "\n  Verified : Verified"
                                        else:
                                            ret_ += "\n  Verified : Not"
                                        if data["graphql"]["user"]["is_private"] == True:
                                            ret_ += "\n  Private Account : Ya"
                                        else:
                                            ret_ += "\n  Private Account : Not"
                                        ret_ += "\n  Total Post : {}".format(str(data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]))
                                        ret_ += "\n  [ https://www.instagram.com/{} ]".format(search)
                                        path = data["graphql"]["user"]["profile_pic_url_hd"]
                                        dap.sendImageWithURL(to, str(path))
                                        dap.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                                    
                            elif cmd.startswith("#alqur'an "):
                                query = text.replace("#alqur'an ","")
                                text = query.split("|")
                                surah = int(text[0])
                                ayat1 = int(text[1])
                                ayat2 = int(text[2])
                                result = requests.get("https://farzain.xyz/api/alquran.php?id={}&from={}&to={}".format(surah, ayat1, ayat2))
                                data = result.text
                                data = json.loads(data)
                                if data["status"] == "success":
                                    hasil = "「 Al-Qur'an 」\n"
                                    hasil += "\nName : {}".format(str(data["nama_surat"]))
                                    hasil += "\nMeaning : {}".format(str(data["arti_surat"]))
                                    hasil += "\nAyat :"
                                    for ayat in data["ayat"]:
                                        hasil += "\n{}".format(str(ayat))
                                    hasil += "\nMeaning Ayat :"
                                    for arti in data["arti"]:
                                        hasil += "\n{}".format(str(arti))
                                    dap.sendMessage(to, str(hasil))                                   
                                    
                            elif cmd.startswith("#instapost"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")   
                                    cond = text.split("|")
                                    username = cond[0]
                                    no = cond[1] 
                                    r = requests.get("http://api.farzain.com/ig_post.php?id=https://www.instagram.com/p/URgHXv1R5zqVz4v9BLE8tb9r5/?_a=1&apikey=beta".format(str(username), str(no)))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["find"] == True:
                                        if data["media"]["mediatype"] == 1:
                                            dap.sendImageWithURL(msg.to, str(data["media"]["url"]))
                                        if data["media"]["mediatype"] == 2:
                                            dap.sendVideoWithURL(msg.to, str(data["media"]["url"]))
                                        ret_ = "     [ Info Post ]     "
                                        ret_ += "\n  Number of Like : {}".format(str(data["media"]["like_count"]))
                                        ret_ += "\n  Number of Comment : {}".format(str(data["media"]["comment_count"]))
                                        ret_ += "\n    [ Caption ]\n{}".format(str(data["media"]["caption"]))
                                        dap.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("#instastory"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")
                                    cond = text.split("*")
                                    search = str(cond[0])
                                    if len(cond) == 2:
                                        r = requests.get("http://rahandiapi.herokuapp.com/instastory/{}?key=betakey".format(search))
                                        data = r.text
                                        data = json.loads(data)
                                        if data["url"] != []:
                                            num = int(cond[1])
                                            if num <= len(data["url"]):
                                                search = data["url"][num - 1]
                                                if search["tipe"] == 1:
                                                    dap.sendImageWithURL(to, str(search["link"]))
                                                if search["tipe"] == 2:
                                                    dap.sendVideoWithURL(to, str(search["link"]))
                                except Exception as error:
                                    logError(error)

                            elif cmd.startswith("#say-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("#say-" + lang + " ","")
                                if lang not in list_language["list_textToSpeech"]:
                                    return dap.sendMessage(to, "\nLanguage not found\n")
                                tts = gTTS(text=say, lang=lang)
                                tts.save("hasil.mp3")
                                dap.sendAudio(to,"hasil.mp3")
                                
                            elif cmd.startswith("#carigambar"):
                                try:
                                    separate = msg.text.split(" ")
                                    search = msg.text.replace(separate[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        items = data["result"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        dap.sendImageWithURL(to, str(path))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("#carimusik "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "\n    [ Result Music ]   "
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n* {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n  [ Total {} Music ]\n".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk Melihat Details Music, silahkan gunakan command {}SearchMusic {}|「number」\n".format(str(setKey), str(search))
                                    dap.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "   [ Music ]   "
                                            ret_ += "\n  Title : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n  Album : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n  Size : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n  Link : {}".format(str(data["result"]["mp3"][0]))
                                            ret_ += "\n"
                                            dap.sendImageWithURL(to, str(data["result"]["img"]))
                                            dap.sendMessage(to, str(ret_))
                                            dap.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
                            elif cmd.startswith("#carilirik"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "\n     [ Result Lyric ]     "
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n [ Total {} Music ]".format(str(len(data["results"])))
                                    ret_ += "\n\nUntuk Melihat Details Lyric, silahkan gunakan command {}SearchLyric {}|「number」\n".format(str(setKey), str(search))
                                    dap.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        dap.sendMessage(msg.to, str(lyric))
                            elif cmd.startswith("#cariyoutube"):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                params = {"search_query": search}
                                r = requests.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "* Youtube Result *"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n  [ {} ]".format(str(data["title"]))
                                    ret_ += "\n  https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n  [ Total {} ]".format(len(datas))
                                dap.sendMessage(to, str(ret_))
                            elif cmd.startswith("#tr-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("#tr-" + lang + " ","")
                                if lang not in list_language["list_translate"]:
                                    return dap.sendMessage(to, "Language not found")
                                translator = Translator()
                                hasil = translator.translate(say, dest=lang)
                                A = hasil.text
                                dap.sendMessage(to, str(A))
# Pembatas Script #
# Pembatas Script #
                        if text.lower() == "##prefix":
                            dap.sendMessage(to, "\nPrefix Saat ini adalah [ {} ]\n".format(str(settings["keyCommand"])))
                            
                        #elif text.lower() == "token done":
                        #    tknop= codecs.open("tkn.json","r","utf-8")
                        #    tkn = json.load(tknop)
                        #    a = tkn['{}'.format(msg._from)][0]['tkn']
                        #    req = requests.get(url = '{}'.format(a))
                        #    b = req.text
                        #    dap.sendMessage(msg.to, 'Your token : \n{}'.format(b))
                                                        
                        if text.lower() == '#login win10':              
                            req = requests.get('https://api.eater.tech/WIN10')
                            #contact = dap.getContact(mid)
                            #dap.sendMessage(to, "[ MID ]\n{}".format(sender))
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
                            dap.sendMessage(to, 'Buka Link dibawah dan Tekan Login\n\n{}'.format(qrz))
                            #dap.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                            with open('tkn.json', 'w') as outfile:
                                json.dump(tkn, outfile)
                            tknop= codecs.open("tkn.json","r","utf-8")
                            tkn = json.load(tknop)
                            a = tkn['{}'.format(msg._from)][0]['tkn']
                            req = requests.get(url = '{}'.format(a))
                            b = req.text
                            aa = dap.getContact(sender).displayName
                            ab = dap.getGroup(msg.to).name
                            ac = dap.getContact(sender).mid
                            #sendMention(to, '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            sendMention(to,'「 WIN 10 」\nUntuk : @!\nDari Grup : '+ab+'\nMid Kamu : '+ac+'\n\n-「 TOKEN 」  : \n{}\n\n- UA : Line/8.3.2\n- LA : WIN10 8.8.3 NADYA-TJ x64\n\n*「 From NadyaTJ & BotEater / Edited By PUY 」'.format(b), [sender])
                            
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
                            dap.sendMessage(to, 'Buka Link dibawah dan Tekan Login\n\n{}'.format(qrz))
                            #dap.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                            with open('tkn.json', 'w') as outfile:
                                json.dump(tkn, outfile)
                            tknop= codecs.open("tkn.json","r","utf-8")
                            tkn = json.load(tknop)
                            a = tkn['{}'.format(msg._from)][0]['tkn']
                            req = requests.get(url = '{}'.format(a))
                            b = req.text
                            aa = dap.getContact(sender).displayName
                            ab = dap.getGroup(msg.to).name
                            ac = dap.getContact(sender).mid
                            #sendMention(to, '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            #dap.sendMessage(to,'「 CHROMEOS 」\nUntuk: '+aa+'\nFrom Group: '+ab+'\nMid User: '+ac+'\n\n- TOKEN : \n{}'.format(b))
                            sendMention(to,'「 CHROME 」\nUntuk : @!\nDari Grup : '+ab+'\nMid Kamu : '+ac+'\n\n-「 TOKEN 」  : \n{}\n\n- UA : Line/8.3.2\n- LA : CHROMEOS 8.8.3 NADYA-TJ x64\n\n*「 From NadyaTJ & BotEater / Edited By PUY 」'.format(b), [sender])
                                
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
                            dap.sendMessage(to, 'Buka Link dibawah dan Tekan Login\n\n{}'.format(qrz))
                            #dap.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                            with open('tkn.json', 'w') as outfile:
                                json.dump(tkn, outfile)
                            tknop= codecs.open("tkn.json","r","utf-8")
                            tkn = json.load(tknop)
                            a = tkn['{}'.format(msg._from)][0]['tkn']
                            req = requests.get(url = '{}'.format(a))
                            b = req.text
                            aa = dap.getContact(sender).displayName
                            ab = dap.getGroup(msg.to).name
                            ac = dap.getContact(sender).mid
                            #sendMention(to, '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            #dap.sendMessage(to,'「 CHROMEOS 」\nUntuk: '+aa+'\nFrom Group: '+ab+'\nMid User: '+ac+'\n\n- TOKEN : \n{}'.format(b))
                            sendMention(to,'「 IOSPAD 」\nUntuk : @!\nDari Grup : '+ab+'\nMid Kamu : '+ac+'\n\n-「 TOKEN 」  : \n{}\n\n- UA : Line/8.3.2\n- LA : IOSPAD 8.8.3 NADYA-TJ x64\n\n*「 From NadyaTJ & BotEater / Edited By PUY 」'.format(b), [sender])
                                
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
                            dap.sendMessage(to, 'Buka Link dibawah dan Tekan Login\n\n{}'.format(qrz))
                            #dap.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                            with open('tkn.json', 'w') as outfile:
                                json.dump(tkn, outfile)
                            tknop= codecs.open("tkn.json","r","utf-8")
                            tkn = json.load(tknop)
                            a = tkn['{}'.format(msg._from)][0]['tkn']
                            req = requests.get(url = '{}'.format(a))
                            b = req.text
                            aa = dap.getContact(sender).displayName
                            ab = dap.getGroup(msg.to).name
                            ac = dap.getContact(sender).mid
                            #sendMention(to, '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            #dap.sendMessage(to,'「 CHROMEOS 」\nUntuk: '+aa+'\nFrom Group: '+ab+'\nMid User: '+ac+'\n\n- TOKEN : \n{}'.format(b))
                            sendMention(to,'「 DESKTOPWIN 」\nUntuk : @!\nDari Grup : '+ab+'\nMid Kamu : '+ac+'\n\n-「 TOKEN 」  : \n{}\n\n- UA : DESKTOPWIN 8.8.3 NADYA-TJ x64\n\n*「 From NadyaTJ & BotEater / Edited By PUY 」'.format(b), [sender])
                            
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
                            dap.sendMessage(to, 'Buka Link dibawah dan Tekan Login\n\n{}'.format(qrz))
                            #dap.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                            with open('tkn.json', 'w') as outfile:
                                json.dump(tkn, outfile)
                            tknop= codecs.open("tkn.json","r","utf-8")
                            tkn = json.load(tknop)
                            a = tkn['{}'.format(msg._from)][0]['tkn']
                            req = requests.get(url = '{}'.format(a))
                            b = req.text
                            aa = dap.getContact(sender).displayName
                            ab = dap.getGroup(msg.to).name
                            ac = dap.getContact(sender).mid
                            #sendMention(to, '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            #dap.sendMessage(to,'「 CHROMEOS 」\nUntuk: '+aa+'\nFrom Group: '+ab+'\nMid User: '+ac+'\n\n- TOKEN : \n{}'.format(b))
                            sendMention(to,'「 DESKTOPMAC 」\nUntuk : @!\nDari Grup : '+ab+'\nMid Kamu : '+ac+'\n\n-「 TOKEN 」  : \n{}\n\n- UA : Line/8.3.2\n- LA : DESKTOPMAC 8.8.3 NADYA-TJ x64\n\n*「 From NadyaTJ & BotEater / Edited By PUY 」'.format(b), [sender])
                                
                        #elif cmd.startswith("Meme:"):
                        #   try:
                        #      txt = msg.text.split(" ")
                        #      teks = msg.text.replace("Meme: "+txt[1]+" ","")
                        #      data = []
                        #      r = requests.get("http://captaintools.tk/bot.php")
                        #      r = eval(r.text)
                        #      for a in r:
                        #          data.append(a)
                        #      c = random.choice(data)
                        #      foto = "https://memegen.link/"+c+"/"+txt[1]+"/"+teks+".jpg"
                        #      puy.sendImageWithURL(msg.to, foto)
                        #    except:
                        #        puy.sendMessage(to, str(e))
###PREFIX###                    
                        elif text.lower() == "##prefix on":
                            settings["setKey"] = True
                            dap.sendMention(to, "@! \n\n[ Notified Prefix Key ]\nBerhasil mengaktifkan Prefix", [sender])
                        elif text.lower() == "##prefix off":
                            settings["setKey"] = False
                            dap.sendMention(to, "@! \n\n[ Notified Prefix Key ]\nBerhasil menonaktifkan Prefix", [sender])
                                                                                     
                    elif msg.contentType == 1:
                        if settings["changeDisplayPicture"] == True:
                            path = dap.downloadObjectMsg(msg_id)
                            settings["changeDisplayProfile"] = False
                            dap.updateProfilePicture(path)
                            dap.sendMessage(to, "\nDisplay Picture has been Changed\n")
                        if msg.toType == 2:
                            if to in settings["changeGroupPicture"]:
                                path = dap.downloadObjectMsg(msg_id)
                                settings["changeGroupPicture"].remove(to)
                                dap.updateGroupPicture(to, path)
                                dap.sendMessage(to, "\nGroup picture has been Changed\n")
                    elif msg.contentType == 1 and sender == dapMID:
                        if bc["img"] == True:
                            path = dap.downloadObjectMsg(msg_id)
                            for gc in dap.groups:
                             dap.sendMessage(gc, bc["txt"])
                             dap.sendContact(gc, bc["mid"])
                             dap.sendImage(gc, path)
                            bc["img"] = False
                            dap.sendMessage(to, "Sukses broadcast ke {} grup.".format(str(len(dap.groups))))            
                    elif msg.contentType == 7:
                        if settings["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "\n     [ Sticker Info ]     "
                            ret_ += "\n  STICKER ID : {}".format(stk_id)
                            ret_ += "\n  STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n  STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n  STICKER URL : line://shop/detail/{}\n".format(pkg_id)
                            ret_ += ""
                            dap.sendMessage(to, str(ret_))
                    elif msg.contentType == 13:
                        if settings["checkContact"] == True:
                            try:
                                contact = dap.getContact(msg.contentMetadata["mid"])
                                if dap != None:
                                    cover = dap.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                    dap.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "\n[ Details Contact ]     "
                                ret_ += "\n  Name : {}".format(str(contact.displayName))
                                ret_ += "\n  MID : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\n  Bio : {}".format(str(contact.statusMessage))
                                ret_ += "\n  Profile Picture : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\n  Cover Picture : {}\n".format(str(cover))
                                ret_ += ""
                                dap.sendMessage(to, str(ret_))
                            except:
                                dap.sendMessage(to, "\nInvalid contact\n")
                    elif msg.contentType == 16:
                        if settings["checkPost"] == True:
                            try:
                                ret_ = "\n  [ Details Post ]  "
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = dap.getContact(sender)
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
                                dap.sendMessage(to, str(ret_))
                            except:
                                dap.sendMessage(to, "\nInvalid post\n")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)

        #if op.type == 26:
        #    msg = op.message
        #    text = msg.text
        #    msg_id = msg.id
        #    receiver = msg.to
        #    sender = msg.from_
        #    sender = msg._from
        #    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
        #        if msg.toType == 0:
        #            if msg._from != mid:
        #                to = msg._from
        #            else:
        #                to = msg.to
        #        elif msg.toType == 1:
        #            to = receiver
        #        elif msg.toType == 2:
        #            to = receiver
        #        elif msg.contentType==0:
                
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != dap.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    dap.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        dap.sendMessage(msg.to,text)
                #if msg.contentType == 0 and sender not in dapMID and msg.toType == 2:
                #    if 'MENTION' in msg.contentMetadata.keys()!= None:
                #        names = re.findall(r'@(\w+)', text)
                #        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                #        mentionees = mention['MENTIONEES']
                #        lists = []
                #        for mention in mentionees:
                #            if dapMID in mention["M"]:
                #                if settings["detectMention"] == True:
                #                    contact = dap.getContact(sender)
                #                    dap.sendMessage(to, "????")
                #                    sendMessageWithMention(to, contact.mid)
                            
                    #if settings["unsendMessage"] == True:
                    #    try:
                    #        msg = op.message
                    #        if msg.toType == 0:
                    #            dap.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                    #        else:
                    #            dap.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                    #            msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    #    except Exception as error:
                    #        logError(error)
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
                                    group = dap.findGroupByTicket(ticket_id)
                                    dap.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    pi.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    dap.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                        if 'MENTION' in msg.contentMetadata.keys() != None:
                                        if msg.to in mentionKick:
                                            name = re.findall(r'@(\w+)', msg.text)
                                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                            mentionees = mention['MENTIONEES']
                                            for mention in mentionees:
                                                if mention ['M'] in Xmid:
                                                    dap.sendMessage(msg.to, "Don't Tag")
                                                    #cl.kickoutFromGroup(msg.to, [msg._from])                                                   
                        if 'MENTION' in msg.contentMetadata.keys() != None:
                            if wait["CrashMention"] == True:
                                contact = dap.getContact(msg.from_)
                                cName = contact.displayName
                                balas = ["??? " + cName + "\n"]
                                ret_ = dap.choice(balas)
                                name = re.findall(r'@(\w+)', msg.text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                      if mention['M'] in Bots:
                                             dap.sendMessage(msg.to,ret_)
                                             break
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': "00000000000000000000000000000000',"}
                            dap.sendMessage(msg)                   
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if dapMid in mention["M"]:
                                    if settings["autoRespon"] == True:
                                        sendMention(sender, " @!, don't tag", [sender])
#                                    break
#            except Exception as error:
#                logError(error)
#                traceback.print_tb(error.__traceback__)
                
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if settings["unsendMessage"] == True:
                try:                  
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            contact = dap.getContact(msg_dict[msg_id]["from"])
                            ginfo = dap.getGroup(at)
                            if contact.displayNameOverridden != None:
                                name_ = contact.displayNameOverridden
                            else:
                                name_ = contact.displayName
                                ret_ = "[ Pesan Ditarik ]\n"
                                ret_ += "\nPengirim : @!"
                                #ret_ += "\nMengirim pada : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                #ret_ += "\nMengirim pada : {}".format(str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
                                #ret_ += "\nTipe pesan : {}".format(str(Type._VALUES_TO_NAMES[msg_dict[msg_id]["contentType"]]))
                                ret_ += "\nDari grup : {}".format(str(ginfo.name))
                                ret_ += "\nIsi : {}".format(str(msg_dict[msg_id]["text"]))
                                sendMentionFooter(at, str(ret_), [contact.mid])
                                dap.sendImageWithURL(receiver, "https://stickershop.line-scdn.net/stickershop/v1/sticker/16365599/ANDROID/sticker.png")
                            del msg_dict[msg_id]
                        else:
                            dap.sendMessage(at,"SentMessage cancelled,But I didn't have log data.\nSorry > <")
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)
               
        if op.type == 65:
            if settings["unsendMessage"] == True:
            
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya':  
                            ginfo = dap.getGroup(at)                           
                            contact = dap.getContact(msg_dict[msg_id]["from"])
                            zx = ""
                            zxc = ""
                            zx2 = []       
                            xpesan =  "「 Gambar Dihapus 」\n◤ Pengirim : "             
                            ret_ = "◤ Nama Grup : {}".format(str(ginfo.name))   
                            ret_ += "\n◤ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))  
                            ry = str(contact.displayName)
                            pesan = ''
                            pesan2 = pesan+"@x \n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':contact.mid}
                            zx2.append(zx)
                            zxc += pesan2
                            text = xpesan + zxc + ret_ + ""
                            dap.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            dap.sendImage(at, msg_dict[msg_id]["data"])     
                        else:              
                            ginfo = dap.getGroup(at)
                            contact = dap.getContact(msg_dict[msg_id]["from"])
                            ret_ =  "「 Pesan Dihapus 」\n"
                            ret_ += "◤ Pengirim : {}".format(str(contact.displayName))
                            ret_ += "\n◤ Nama Grup : {}".format(str(ginfo.name))
                            ret_ += "\n◤ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                            ret_ += "\n◤ Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                            dap.sendMessage(at, str(ret_))          
                        del msg_dict[msg_id]      
                except Exception as e:                    
                    print(e)
                    
        if op.type == 17:
            if settings["Inroom"] == True:
             dapii = dap.getGroup(op.param1)
             dancuk = dap.getContact(op.param2)
             #image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             sendMentionFooter(op.param1, "@!, Welcome".format(str(dapii.name)),[op.param2])
             dap.sendContact(op.param1, op.param2)

        if op.type == 15:
            if settings["Outroom"] == True:
             tgb = dap.getGroup(op.param1)
             dan = dap.getContact(op.param2)             
             #dap.sendContact(op.param1, op.param2)
             sendMentionFooter(op.param1, "@!, Gbye", [op.param2])
             dap.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net"+dap.getContact(op.param2).picturePath)
             #dap.sendContact(op.param1, op.param2)             
                
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
           
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                        json.dump(read, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass                            
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
        
#===============================================================================
#        if op.type == 19:
#            print ("[ 19 ] KICKOUT DAP MESSAGE")
#            try:
#                if op.param3 in dapMID:
#                    if op.param2 in kiMID:
#                        G = pi.getGroup(op.param1)
#                        ginfo = pi.getGroup(op.param1)
#                        G.preventedJoinByTicket = False
#                        pi.updateGroup(G)
#                        invsend = 0
#                        Ticket = pi.reissueGroupTicket(op.param1)
#                        dap.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        pi.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        #ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        #ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        #ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        G = pi.getGroup(op.param1)
#                        G.preventedJoinByTicket = True
#                        pi.updateGroup(G)
#                        G.preventedJoinByTicket(G)
#                        pi.updateGroup(G)
#                    else:
#                        G = pi.getGroup(op.param1)
#                        ginfo = pi.getGroup(op.param1)
#                        pi.kickoutFromGroup(op.param1,[op.param2])
#                        G.preventedJoinByTicket = False
#                        pi.updateGroup(G)
#                        invsend = 0
#                        Ticket = pi.reissueGroupTicket(op.param1)
#                        dap.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        pi.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        #ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        #ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        #ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        G = pi.getGroup(op.param1)
#                        G.preventedJoinByTicket = True
#                        pi.updateGroup(G)
#                        G.preventedJoinByTicket(G)
#                        pi.updateGroup(G)
#                        #settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------       

def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        dap.acceptGroupInvitation(op.param1)
        ki.acceptGroupInvitation(op.param1)
        #ki2.acceptGroupInvitation(op.param1)
        #ki3.acceptGroupInvitation(op.param1)
        #ki4.acceptGroupInvitation(op.param1)
    except Exception as e:
        dap.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
#=================================        
        
while True:
    try:
        delete_log()
        ops = dapPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                dapBot(op)
                dapPoll.setRevision(op.revision)
    except Exception as error:
        logError(error)
        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
