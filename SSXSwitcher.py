import urllib.request
import os
from bs4 import BeautifulSoup
import biplist

def getDataByHtml(url):
    page =urllib.request.urlopen(url)
    page.encoding='utf-8'
    return getData(page.read())

def getData(html):
    soup=BeautifulSoup(html, "html.parser");
    section=soup.find("section",{'id':'free'})
    data=[]
    if(section is not None):
        divs=section.find_all("div",{'class':'col-sm-4 text-center'})
        for div in divs:
            h4s=div.find_all("h4")
            data.append({"proxy ip":dataFormat(h4s[0]),"proxy port":dataFormat(h4s[1]),
                              "proxy password":dataFormat(h4s[2]),"proxy encryption":dataFormat(h4s[3])})
    else:
        codes=soup.find_all("code")
        if(codes is not None):
            codes=[code.string for code in soup.find_all("code")]
            data.append({"proxy ip":codes[1],"proxy port":codes[2],
                         "proxy password":codes[3],"proxy encryption":codes[4]})

    return data

def dataFormat(val):
    if(val is not None):
        val=val.string
        return val[val.index(":")+1:]
    return ""

def setDataPlist(data):
    ss_plist = os.path.expanduser('~') + '/Library/Preferences/clowwindy.ShadowsocksX.plist'
    try:
        plist={};
        plist["proxy encryption"]=data["proxy encryption"]
        plist["proxy ip"]=data["proxy ip"]
        plist["proxy port"]=data["proxy port"]
        plist["proxy password"]=data["proxy password"]
        plist["ShadowsocksIsRunning"]=True
        plist["public server"]=False
        config='{"current":0,"profiles":[{"password":%s,"method":%s,"server_port":%s,"remarks":"GFW.Press","server":%s}]}'%(data["proxy password"],data["proxy encryption"],data["proxy port"],data["proxy ip"]);
        plist["config"]=config.encode()
        biplist.writePlist(plist,ss_plist)
        os.system("defaults import clowwindy.ShadowsocksX ~/Library/Preferences/clowwindy.ShadowsocksX.plist")
        os.system("ps aux | grep \[/]ShadowsocksX |awk '{print $2}' | xargs kill -9")
        os.system("open /Applications/ShadowsocksX.app")
    except IOError as ex:
        print(ex)

def updateProxy():
    urls=["http://freetizi.xyz/","http://www.ishadowsocks.net/"]
    datas={}
    for url in urls:
        try:
            datas[url]=getDataByHtml(url)
        except Exception as ex:
            print(ex)
        # ----------------显示查询出来的数据
    count=0
    newData={};
    for url in datas:
        print(url)
        for ips in datas[url]:
            count+=1
            newData[str(count)]=ips;
            print(str(count)+":")
            print("\t"+ips["proxy ip"])
            print("\t"+ips["proxy encryption"])
        # -----------------选择要设置的数据
    index=input("选择网络：")
    # ---------------设置数据
    if str(index) in newData :
        setDataPlist(newData[str(index)])
    else:
        print("选择错误，应用退出！")





if __name__ == '__main__':
    args=str(input("1 删除ShadowsocksX默认配置 ，2 修改网络:"))
    if args=='1':
        os.system("defaults delete clowwindy.ShadowsocksX")
        print("删除成功")
        input("按任意键结束")
    else:
        updateProxy()
    # getData(html);
