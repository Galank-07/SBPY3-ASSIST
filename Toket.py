from SLACKBOT import *
from GALANK.ttypes import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from multiprocessing import Pool, Process
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, asyncio, timeit, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast, pafy, youtube_dl

# THANKS YA BUAT KALIAN
# KALAU BUKAN SUPPORT DARI KALIAN
# AKU GAK MUNGKIN KEK GINI/PASTI UDAH VAKUM BOT
# YANG MAU KEPO,IN[ADD AJA ID LINE DI BAWAH]
# MAU NANYA SILAHKAN
# [ADD ME] line.me/ti/p/~@ryp6149l

# LOGIN QR
#client = LineClient()
# LOGIN EMAIL DAN PASWORD LINE
#client = LineClient(id='email', passwd='pass')
#LOGIN TOKEN
client = LineClient(authToken='Eu0IyUSz5UZmVW3BmjP4.f25/kC26016m+rq78vfQTa.4YQ9ANbN/q/PupvRBSoATFDWrLHIEeRc17LLrDVtt2c=')
client.log("Auth Token : " + str(client.authToken))
channel = LineChannel(client)
client.log("Channel Access Token : " + str(channel.channelAccessToken))

helpMessage ="""╭═══════╬╬════════╮
╞☪ SELFBOT COMMAND
╰═══════╬╬════════╯
╭═══════╬╬════════╮
╞☪ Help
╞☪ Me
╞☪ Gc
╞☪ Youtube:
╞☪ Gn
╞☪ Getsq
╞☪ Image:
╞☪ Say:
╞☪ Unsend me
╞☪ Speed
╞☪ Lc
╞☪ Sticker
╞☪ Apakah
╞☪ Sytr:
╞☪ Tr:
╞☪ Stealpict
╞☪ Stealcover
╞☪ Mention
╞☪ Ceksider
╞☪ Offread
╞☪ Mode:self
╞☪ Mode:publik
╞☪ Restart
╰═══════╬╬════════╯
╭═══════╬╬════════╮
      sᴜᴘᴘᴏʀᴛᴇᴅ ʙʏ :
      TΣΔM SLΔCҜβΩT
    OWNER:
 line.me/ti/p/~@ryp6149l
╰═══════╬╬════════╯  
"""

poll = LinePoll(client)
mode='self'
cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

while True:
    try:
        ops=poll.singleTrace(count=50)
        if ops != None:
          for op in ops:
#=========================================================================================================================================#
            #if op.type in OpType._VALUES_TO_NAMES:
            #    print("[ {} ] {}".format(str(op.type), str(OpType._VALUES_TO_NAMES[op.type])))
#=========================================================================================================================================#
            if op.type == 26:
                msg = op.message
                if msg.text != None:
                    if msg.toType == 2:
                        may = client.getProfile().mid
                        if may in str(msg.contentMetadata) and 'MENTION' in str(msg.contentMetadata):
                            pilih = ['[Auto Respon]\nDont Tag Me!','[Auto Respon]\nAda Perlu Apa?','[Auto Respon]\nGw Masih Tidur,Kalo Penting Pc Aja!','[Auto Respon]\n Dont Tag Me!,Iam Busy','[Auto Respon]\nGak Usah Tag Kalo Penting Pc Aja!']
                            rslt = random.choice(pilih)
                            client.sendText(msg.to, str(rslt))
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            if op.type == 17:
                ginfo = client.getGroup(op.param1)
                contact = client.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                client.sendImageWithURL(op.param1,image)
                client.sendText(op.param1,"Hay    "+client.getContact(op.param2).displayName +"\nWelcome to"+"\nGroup》》"+ str(ginfo.name))
            if op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            client.sendChatChecked(receiver, msg_id)
                            contact = client.getContact(sender)
                            if text.lower() == 'me':
                                client.sendMessage(to, None, contentMetadata={'mid': sender}, contentType=13)
                                client.tag(to, sender)
                                client.sendText(to, 'Jangan sombong mhank')
                            elif ("Gn " in msg.text):
                                 X = client.getGroup(msg.to)
                                 X.name = msg.text.replace("Gn ","")
                                 client.updateGroup(X)
                            elif text.lower() == 'announce':
                                gett = client.getChatRoomAnnouncements(receiver)
                                for a in gett:
                                    aa = client.getContact(a.creatorMid).displayName
                                    bb = a.contents
                                    cc = bb.link
                                    textt = bb.text
                                    client.sendText(to, 'Link: ' + str(cc) + '\nText: ' + str(textt) + '\nMaker: ' + str(aa))
                            elif text.lower() == 'unsend me':
                                client.unsendMessage(msg_id)
                            elif text.lower() == 'getsq':
                                a = client.getJoinedSquares()
                                squares = a.squares
                                members = a.members
                                authorities = a.authorities
                                statuses = a.statuses
                                noteStatuses = a.noteStatuses
                                txt = str(squares)+'\n\n'+str(members)+'\n\n'+str(authorities)+'\n\n'+str(statuses)+'\n\n'+str(noteStatuses)+'\n\n'
                                txt2 = ''
                                for i in range(len(squares)):
                                    txt2 += str(i+1)+'. '+str(squares[i].invitationURL)+'\n'
                                client.sendText(to, txt2)
                            elif 'lc ' in text.lower():
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).mid
                                    s = client.getContact(u).displayName
                                    hasil = channel.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        channel.like(str(sender), str(result), likeType=random.choice(typel))
                                        channel.comment(str(sender), str(result), 'Auto Like by nrik')
                                    client.sendText(to, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif 'gc ' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    cname = client.getContact(u).displayName
                                    cmid = client.getContact(u).mid
                                    cstatus = client.getContact(u).statusMessage
                                    cpic = client.getContact(u).picturePath
                                    #print(str(a))
                                    client.sendText(to, 'Nama : '+cname+'\nMID : '+cmid+'\nStatus Msg : '+cstatus+'\nPicture : http://dl.profile.line.naver.jp'+cpic)
                                    client.sendMessage(to, None, contentMetadata={'mid': cmid}, contentType=13)
                                    if "videoProfile='{" in str(client.getContact(u)):
                                        client.sendVideoWithURL(to, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                    else:
                                        client.sendImageWithURL(to, 'http://dl.profile.line.naver.jp'+cpic)
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif 'sticker:' in msg.text.lower():
                                try:
                                    query = msg.text.replace("sticker:", "")
                                    query = int(query)
                                    if type(query) == int:
                                        client.sendImageWithURL(to, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        client.sendText(to, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        client.sendText(to, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif msg.text in ["Key","Help","Command","Cmd"]:
                                client.sendText(msg.to,helpMessage)
                                client.sendText(msg.to,"『Dilarang Typo Tanpa Izin Dari Owner: Galank』")
                            elif "youtube:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("yt:", "")
                                    query = query.replace(" ", "+")
                                    x = client.youtube(query)
                                    client.sendText(to, x)
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif "image:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("image:", "")
                                    images = client.image_search(query)
                                    client.sendImageWithURL(to, images)
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif 'say:' in msg.text.lower():
                                try:
                                    isi = msg.text.lower().replace('say:','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    client.sendAudio(to, 'temp.mp3')
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif 'apakah ' in msg.text.lower():
                                try:
                                    txt = ['iya','tidak','bisa jadi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    client.sendAudio(to, 'temp2.mp3')
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif "Sytr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text
                                    tts = gTTS(text=A, lang=isi[1], slow=False)
                                    tts.save('temp3.mp3')
                                    client.sendAudio(to, 'temp3.mp3')
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif "tr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text                               
                                    client.sendText(to, str(A))
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif text.lower() == 'speed':
                                start = time.time()
                                client.sendText(to, "Progress...!")
                                elapsed_time = time.time() - start
                                client.sendText(to, "%sdetik" % (elapsed_time))
                            elif 'stealpic' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).pictureStatus
                                    if "videoProfile='{" in str(client.getContact(u)):
                                        client.sendVideoWithURL(to, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                    else:
                                        client.sendImageWithURL(to, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif 'stealcover' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    client.sendImageWithURL(to, a)
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif text.lower() == 'mention':
                                group = client.getGroup(to)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    client.mention(to, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(to, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    client.mention(to, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(to, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(to, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(to, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(to, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(to, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    client.mention(to, nm5)             
                                client.sendText(to, "Members :"+str(jml))
                            elif text.lower() == 'ceksider':
                                try:
                                    del cctv['point'][to]
                                    del cctv['sidermem'][to]
                                    del cctv['cyduk'][to]
                                except:
                                    pass
                                cctv['point'][to] = msg.id
                                cctv['sidermem'][to] = ""
                                cctv['cyduk'][to]=True
                            elif text.lower() == 'offread':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][to]=False
                                    client.sendText(to, cctv['sidermem'][msg.to])
                                else:
                                    client.sendText(to, "Heh belom di Set")
                            elif text.lower() == 'mode:self':
                                mode = 'self'
                                client.sendText(to, 'Mode Public Off')
                            elif text.lower() == 'mode:public':
                                mode = 'public'
                                client.sendText(to, 'Mode Public ON')
                            elif text.lower() == 'restart':
                                restart_program()
                except Exception as e:
                    client.log("[SEND_MESSAGE] ERROR : " + str(e))
#=========================================================================================================================================#
            elif mode == 'self' and op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            contact = client.getContact(sender)
                            if text.lower() == 'me':
                                client.sendMessage(to, None, contentMetadata={'mid': sender}, contentType=13)
                                client.tag(to, sender)
                            elif 'gc ' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    cname = client.getContact(u).displayName
                                    cmid = client.getContact(u).mid
                                    cstatus = client.getContact(u).statusMessage
                                    cpic = client.getContact(u).picturePath
                                    #print(str(a))
                                    client.sendText(to, 'Nama : '+cname+'\nMID : '+cmid+'\nStatus Msg : '+cstatus+'\nPicture : http://dl.profile.line.naver.jp'+cpic)
                                    client.sendMessage(to, None, contentMetadata={'mid': cmid}, contentType=13)
                                    if "videoProfile='{" in str(client.getContact(u)):
                                        client.sendVideoWithURL(to, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                    else:
                                        client.sendImageWithURL(to, 'http://dl.profile.line.naver.jp'+cpic)
                                except Exception as e:
                                    client.sendText(to, str(e))                            
                            elif 'sticker:' in msg.text.lower():
                                try:
                                    query = msg.text.replace("sticker:", "")
                                    query = int(query)
                                    if type(query) == int:
                                        client.sendImageWithURL(to, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        client.sendText(to, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        client.sendText(to, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif "youtube:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("yt:", "")
                                    query = query.replace(" ", "+")
                                    x = client.youtube(query)
                                    client.sendText(to, x)
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif "image:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("image:", "")
                                    images = client.image_search(query)
                                    client.sendImageWithURL(to, images)
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif 'say:' in msg.text.lower():
                                try:
                                    isi = msg.text.lower().replace('say:','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    client.sendAudio(to, 'temp.mp3')
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif 'apakah ' in msg.text.lower():
                                try:
                                    txt = ['iya','tidak','bisa jadi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    client.sendAudio(to, 'temp2.mp3')
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif "Sytr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text
                                    tts = gTTS(text=A, lang=isi[1], slow=False)
                                    tts.save('temp3.mp3')
                                    client.sendAudio(to, 'temp3.mp3')
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif "Tr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text                               
                                    client.sendText(to, str(A))
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif text.lower() == 'speed':
                                start = time.time()
                                client.sendText(to, "TestSpeed")
                                elapsed_time = time.time() - start
                                client.sendText(to, "%sdetik" % (elapsed_time))
                            elif 'stealpic' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).pictureStatus
                                    if "videoProfile='{" in str(client.getContact(u)):
                                        client.sendVideoWithURL(to, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                    else:
                                        client.sendImageWithURL(to, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    client.sendText(to, str(e))
                            elif 'stealcover' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    client.sendImageWithURL(to, a)
                                except Exception as e:
                                    client.sendText(to, str(e))
                except Exception as e:
                    client.log("[SEND_MESSAGE] ERROR : " + str(e))
                    
#=========================================================================================================================================#
            elif op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                pref=['eh ada','hai kak','aloo..','nah','lg ngapain','halo','sini kak']
                                client.sendText(op.param1, str(random.choice(pref))+' '+Name)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

            else:
                pass
#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))
