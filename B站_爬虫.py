import requests #导入爬虫模块

#伪装信息(点击请求标头进行查找--找到user-Agent以及Referer)
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36 Edg/157.0.0.0",
    "referer":"https://www.bilibili.com/bangumi/play/ss47710?from_spmid=666.8.operation.2"
}

#获取视频url网址(注意：视频url一般有时间限制，失效了需要重新获取)
#步骤：
#1.打开网页，打开开发者工具；2.点击网络，点击Fetch/XHR；3.按大小排序，大内存为视频（有m4s字样）
url="https://cn-gdgz-fx-01-18.bilivideo.com/upgcxcode/43/50/1515895043/1515895043_x1-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&platform=pc&trid=00006fdb0382bbe546579663a3772c9e1ccp&deadline=1794731076&mid=507266419&oi=1849779178&uipk=5&nbs=1&gen=playurlv3&os=bcache&og=cos&upsig=8b935f3e8afc84232bac0021f5225b23&uparams=e,platform,trid,deadline,mid,oi,uipk,nbs,gen,os,og&cdnid=34902&bvc=vod&nettype=0&bw=1030113&lrs=0&V=v3.1.1.0&agrr=1&buvid=C02ED708-C312-D7FB-EB05-CD0D909DD4C186412infoc&build=0&dl=0&f=p_0_0&qn_dyeid=59899730e4fdfb570032bb0a6af95023&np=151371867&orderid=0,4"

#发送请求
res=requests.get(url,headers=headers)

#保存视频(mp4或其他)
open("视频.mp4","wb").write(res.content)

#获取音频url网址(注意：视频url一般有时间限制，失效了需要重新获取)
#步骤：
#1.打开网页，打开开发者工具；2.点击网络，点击Fetch/XHR；3.按大小排序，大内存为视频（有m4s字样）；4.找到同为m4s字样但数据名称不同的文件，即为音频
url="https://cn-gdgz-fx-01-16.bilivideo.com/upgcxcode/43/50/1515895043/1515895043-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&mid=507266419&nbs=1&trid=00006fdb0382bbe546579663a3772c9e1ccp&os=bcache&og=ali&oi=1849779178&platform=pc&deadline=1794731076&gen=playurlv3&upsig=7402b05ef7f1356597ffbbe07a49e7ea&uparams=e,uipk,mid,nbs,trid,os,og,oi,platform,deadline,gen&cdnid=42416&bvc=vod&nettype=0&bw=113129&lrs=0&V=v3.1.1.0&f=p_0_0&qn_dyeid=59899730e4fdfb570032bb0a6af95023&np=151371867&agrr=1&buvid=C02ED708-C312-D7FB-EB05-CD0D909DD4C186412infoc&build=0&dl=0&orderid=0,4"

#发送请求
res=requests.get(url,headers=headers)

#保存音频（mp3）
open("音频.mp3","wb").write(res.content)

#检查状态（显示200即为成功）
print(res.status_code)

#处理音频和视频
#导入模块
from moviepy.editor import *

#处理文件
video=VideoFileClip("视频.mp4")
audio=AudioFileClip("音频.mp3")

#合并
sp=video.set_audio(audio)
#保存视频
sp.write_videofile("铠甲勇士刑天第6集.mp4") 

