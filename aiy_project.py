from ArticutAPI import Articut
import requests,json
import vlc
import youtube_dl
weather API KEY = " ";
key ="  "; # google map key

nounlist = [];
placelist = [];
timelist = [];
verblist = [];  


ydl_opts = {
    'default_search': 'ytsearch1:',
    'format': 'bestaudio/best',
    'noplaylist': True,
    'quiet': True
}
vlc_instance = vlc.get_default_instance();
vlc_player = vlc_instance.media_player_new();

def get_url(city):
    return {    
    '宜蘭': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E5%AE%9C%E8%98%AD%E7%B8%A3",
    '花蓮': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E8%8A%B1%E8%93%AE%E7%B8%A3",
    '臺東': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E8%87%BA%E6%9D%B1%E7%B8%A3",
    '台東': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E8%87%BA%E6%9D%B1%E7%B8%A3",
    '澎湖': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E6%BE%8E%E6%B9%96%E7%B8%A3",
    '金門': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E9%87%91%E9%96%80%E7%B8%A3",
    '連江': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E9%80%A3%E6%B1%9F%E7%B8%A3",
    '臺北': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E8%87%BA%E5%8C%97%E5%B8%82",
    '台北': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E8%87%BA%E5%8C%97%E5%B8%82",
    '新北': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E6%96%B0%E5%8C%97%E5%B8%82",
    '桃園': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E6%A1%83%E5%9C%92%E5%B8%82",
    '臺中': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E8%87%BA%E4%B8%AD%E5%B8%82",
    '台中': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E8%87%BA%E4%B8%AD%E5%B8%82",
    '臺南': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E8%87%BA%E5%8D%97%E5%B8%82",
    '台南': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E8%87%BA%E5%8D%97%E5%B8%82",
    '高雄': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E9%AB%98%E9%9B%84%E5%B8%82",
    '基隆': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E5%9F%BA%E9%9A%86%E5%B8%82",
    '新竹': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E6%96%B0%E7%AB%B9%E5%B8%82",
    '苗栗': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E8%8B%97%E6%A0%97%E7%B8%A3",
    '彰化': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E5%BD%B0%E5%8C%96%E7%B8%A3",
    '南投': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E5%8D%97%E6%8A%95%E7%B8%A3",
    '雲林': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E9%9B%B2%E6%9E%97%E7%B8%A3",
    '嘉義': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E5%98%89%E7%BE%A9%E5%B8%82",
    '屏東': "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="+ weather API KEY +"&format=JSON&locationName=%E5%B1%8F%E6%9D%B1%E7%B8%A3",
    }.get(city,'error')

#-------抓資料---------------------------------------------
def get_today_weather_minT(city):#當日最低溫度
    url = get_url(city);
    if(url=='error'):
        return 'error'
    else:
        data = requests.get(url)
        data = json.loads(data.text);
        return (data["records"]["location"][0]["weatherElement"][2]["time"][0]["parameter"]["parameterName"]) 
    
def get_today_weather_maxT(city):#當日最高溫度
    url = get_url(city);
    if(url=='error'):
        return 'error'
    else:
        data = requests.get(url)
        data = json.loads(data.text);
        return (data["records"]["location"][0]["weatherElement"][4]["time"][0]["parameter"]["parameterName"]) 
   
def get_today_weather_wx(city):#天氣型態
    url = get_url(city);
    if(url=='error'):
        return 'error'
    else:
        data = requests.get(url)
        data = json.loads(data.text);
        return (data["records"]["location"][0]["weatherElement"][0]["time"][0]["parameter"]["parameterName"]) 
        
def get_today_weather_PoP(city):#降雨機率
    url = get_url(city);
    if(url=='error'):
        return 'error'
    else:
        data = requests.get(url)
        data = json.loads(data.text);
        return (data["records"]["location"][0]["weatherElement"][1]["time"][0]["parameter"]["parameterName"]) 

def get_tom_weather_minT(city):#明日最低溫度
    url = get_url(city);
    if(url=='error'):
        return 'error'
    else:
        data = requests.get(url)
        data = json.loads(data.text);
        return (data["records"]["location"][0]["weatherElement"][2]["time"][2]["parameter"]["parameterName"]) 
    
def get_tom_weather_maxT(city):#明日最高溫度 
    url = get_url(city);
    if(url=='error'):
        return 'error'
    else:
        data = requests.get(url)
        data = json.loads(data.text);
        return (data["records"]["location"][0]["weatherElement"][4]["time"][2]["parameter"]["parameterName"]) 
       
def get_tom_weather_wx(city):#明日天氣型態
    url = get_url(city);
    if(url=='error'):
        return 'error'
    else:
        data = requests.get(url)
        data = json.loads(data.text);
        return (data["records"]["location"][0]["weatherElement"][0]["time"][2]["parameter"]["parameterName"]) 
    
def get_tom_weather_PoP(city):#明日降雨機率
    url = get_url(city);
    if(url=='error'):
        return 'error'
    else:
        data = requests.get(url)
        data = json.loads(data.text);
        return (data["records"]["location"][0]["weatherElement"][1]["time"][2]["parameter"]["parameterName"]) 
    
#--------輸出------------------------------------------------
def weather_all(city):#天氣輸出
    if(get_today_weather_wx(city)!='error'):
        print(city ,"今天的氣候",get_today_weather_wx(city),"氣溫為",get_today_weather_minT(city),"到",get_today_weather_maxT(city),"度 降雨機率有",get_today_weather_PoP(city),"%");
    else:
        print("查無此地天氣，目前只能查詢各大縣市氣溫")
    
def weather_wx(city):#氣候輸出
    if(get_today_weather_wx(city)!='error'):
        print(city ,"今天的氣候" , get_today_weather_wx(city));
    else:
        print("查無此地天氣，目前只能查詢各大縣市氣溫")
        
def weather_PoP(city):#降雨機率輸出
    if(get_today_weather_PoP(city)!='error'):
        print(city ,"有",get_today_weather_PoP(city),"%的降雨機率");
    else:
        print("查無此地天氣，目前只能查詢各大縣市氣溫");
        
def tomweather_all(city):#明日天氣輸出
    if(get_tom_weather_wx(city)!='error'):
        print(city ,"明天的氣候",get_tom_weather_wx(city),"氣溫為",get_tom_weather_minT(city),"到",get_tom_weather_maxT(city),"度 降雨機率有",get_tom_weather_PoP(city),"%");
    else:
        print("查無此地天氣，目前只能查詢各大縣市氣溫");
        
def tomweather_wx(city):#明日氣候輸出
    if(get_tom_weather_wx(city)!='error'):
        print(city ,"明天的氣候" , get_tom_weather_wx(city));
    else:
        print("查無此地天氣，目前只能查詢各大縣市氣溫");
        
def tomweather_PoP(city):#明日降雨機率輸出
    if(get_tom_weather_PoP(city)!='error'):
        print(city ,"明天有",get_tom_weather_PoP(city),"%的降雨機率");
    else:
        print("查無此地天氣，目前只能查詢各大縣市氣溫");
        
#---------------輸入判斷----------------------------------------------------
def judge(nounlist,placelist,timelist,verblist):
    fun_code=0;
    for i in nounlist:
        if(choice_motion(i)!=0): 
                fun_code = choice_motion(i);
                break;
        else :
            continue;
    if(fun_code == 0):
        for j in verblist:
            if(choice_motion(j)!=0):
                fun_code = choice_motion(j);
                break;
            else :
                continue;
#---------------天氣部分----------------------------------------------------
    if(fun_code<4 and fun_code>0):
        if(len(placelist)==0): #定位並查詢
            city = covert_to_city()
            if(get_url(city)!='error' and fun_code == 1): #天氣
                if(len(timelist)==0): #無時間
                    weather_all(city);
                elif(timelist[0].find('明天')!=-1 or timelist[0].find('明日')!=-1):#明日 
                    tomweather_all(city);
                else:
                    weather_all(city);
            elif(get_url(city)!='error' and fun_code == 2): #降雨機率
                if(len(timelist)==0): #無時間
                    weather_PoP(city)
                elif(timelist[0].find('明天')!=-1 or timelist[0].find('明日')!=-1):#明日
                    tomweather_PoP(city)
                else: 
                    weather_PoP(city)
            elif(get_url(city)!='error' and fun_code == 3): #天氣型態
                if(len(timelist)==0): #無時間
                    weather_wx(city)
                elif(timelist[0].find('明天')!=-1 or timelist[0].find('明日')!=-1):#明日
                    weather_wx(city)
                else: 
                    weather_wx(city)
        else:
            for j in placelist:
                if(get_url(j)!='error' and fun_code == 1): #天氣
                    if(len(timelist)==0): #無時間
                        weather_all(j);
                    elif(timelist[0].find('明天')!=-1 or timelist[0].find('明日')!=-1):#明日 
                        tomweather_all(j);
                    else:
                        weather_all(j);
                elif(get_url(j)!='error' and fun_code == 2): #降雨機率
                    if(len(timelist)==0): #無時間
                        weather_all(j);
                    elif(timelist[0].find('明天')!=-1 or timelist[0].find('明日')!=-1):#明日 
                        tomweather_all(j);
                    else:
                        weather_all(j);
                elif(get_url(j)!='error' and fun_code == 3): #天氣型態
                    if(len(timelist)==0): #無時間
                        weather_all(j);
                    elif(timelist[0].find('明天')!=-1 or timelist[0].find('明日')!=-1):#明日 
                        tomweather_all(j);
                    else:
                        weather_all(j);
#----------------地圖部分----------------------------------------------------    
    elif(fun_code == 4): #地圖部分
        if(text.find('附近')!= -1 or text.find('周遭')!= -1): #搜尋附近店家
            nearby_search();
        else: #搜尋特定店家
            print("搜尋特定店家");
#----------------------------------------------------------------------------
    elif(fun_code == 5):
        music_client = CloudSpeechClient();
        name = input("請輸入歌曲名稱") #say('請說出歌曲名稱');
        #name = client.recognize(language_code=zh-TW,hint_phrases=None)
        play_music(name);
def get_lat_lng(): #定位 return 經緯度
    url="https://www.googleapis.com/geolocation/v1/geolocate?key="+key
    geo_res=requests.post(url)
    geo_res = geo_res.text;
    lat = geo_res[geo_res.find("lat")+6:geo_res.find("lng")-6]
    lng = geo_res[geo_res.find("lng")+6:geo_res.find("},")-1]
    return lat+lng;

def covert_to_city():
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" +get_lat_lng()+"&key="+key+"&language=zh-TW";
    add = requests.get(url);
    add = add.text;
    formatadd = add[add.find("formatted_address"):add.find("geometry")-1];
    city = formatadd[formatadd.find("台灣")+2:formatadd.find("台灣")+4];
    return city;
    
#搜尋附近
def nearby_search():
    url="https://maps.googleapis.com/maps/api/place/nearbysearch/json?key="+key+"&location="+get_lat_lng()+"&language=zh-TW&radius=500&type=restaurant"
    nearby_res = requests.get(url)
    nearby_res = json.loads(nearby_res.text);
    restaurant_list = nearby_res["results"];
    for i in restaurant_list:
        print(i["name"]);
        
def choice_motion(target): #1:查詢天氣 2:查詢降雨機率 3:查詢天氣型態 4:搜尋附近店家 5:
    return {
    '天氣':1,
    '下雨':2,
    '氣候':3,
    '餐廳':4,
    '美食':4,
    '店家':4,
    '想聽':5,
    '聽':5,
    '播放':5
    }.get(target,0)

def handle_result(temp_str_noun=" ",temp_str_place=" ",temp_str_time=" ",temp_str_verb=" ") :
    filtter = ", \'"; #切好的list只抓出需要部份
    filtter2 = "\')"
    index = 0;
    while index<len(temp_str_noun): #將字串篩掉多於的符號再丟入新的list(nounlist)
        index = temp_str_noun.find(filtter,index)
        if index == -1:
            break;
        index+=3;
        end = temp_str_noun.find(filtter2,index);
        temp_str = temp_str_noun[index:end];
        nounlist.append(temp_str)
    index = 0;
    while index<len(temp_str_place): #將字串篩掉多於的符號再丟入新的list(placelist)
        index = temp_str_place.find(filtter,index)
        if index == -1:
            break;
        index+=3;
        end = temp_str_place.find(filtter2,index);
        temp_str = temp_str_place[index:end];
        placelist.append(temp_str)
    index = 0;
    while index<len(temp_str_time): #將字串篩掉多於的符號再丟入新的list(timelist)
        index = temp_str_time.find(filtter,index)
        if index == -1:
            break;
        index+=3;
        end = temp_str_time.find(filtter2,index);
        temp_str = temp_str_time[index:end];
        timelist.append(temp_str)
    index = 0;
    while index<len(temp_str_verb): #將字串篩掉多於的符號再丟入新的list(verblist)
        index = temp_str_verb.find(filtter,index)
        if index == -1:
            break;
        index+=3;
        end = temp_str_verb.find(filtter2,index);
        temp_str = temp_str_verb[index:end];
        verblist.append(temp_str)

def play_music(name):
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(name, download=False)
    except Exception:
        say('抱歉，無法找到此首歌曲')
        return

    if meta:
        info = meta['entries'][0]
        vlc_player.set_media(vlc_instance.media_new(info['url']))
        print ('為您播放' + re.sub(r'[^\s\w]', '', info['title']));#say('為您播放' + re.sub(r'[^\s\w]', '', info['title']))
        vlc_player.play();

text = input("輸入 :");
articut = Articut(username="", apikey="")
result = articut.parse(text)

noun = articut.getNounStemLIST(result,indexWithPOS=False);
place = articut.getLocationStemLIST(result);
time = articut.getTimeLIST(result);
verb = articut.getVerbStemLIST(result);

if noun:
    temp_str_noun = " ".join([str(x) for x in noun]);#將List轉回string方便處理
if place:
    temp_str_place = " ".join([str(x) for x in place]);
if time:
    temp_str_time = " ".join([str(x) for x in time]);
if verb:
    temp_str_verb = " ".join([str(x) for x in verb]);

nounlist.clear();
placelist.clear();
timelist.clear();
verblist.clear();  

handle_result(temp_str_noun,temp_str_place,temp_str_time,temp_str_verb);

if(vlc_player.get_state() == vlc.State.Playing || vlc_player.get_state() == vlc_player.Paused):
    if(text.find('暫停')!=-1):
        vlc_player.set_pause(True);
        continue
    elif(text.find('繼續')!=-1||text.find('播放')!=-1):
        vlc_player.set_pause(False);
        continue;
    elif(text.find('停止')!=-1):
        vlc.player.stop();
        continue;
        
judge(nounlist,placelist,timelist,verblist);

"""
>>> text = 'Allowed Hello Hollow'
>>> index = 0
>>> while index < len(text):
        index = text.find('ll', index)
        if index == -1:
            break
        print('ll found at', index)
        index += 2 # +2 because len('ll') == 2

ll found at  1
ll found at  10
ll found at  16
"""