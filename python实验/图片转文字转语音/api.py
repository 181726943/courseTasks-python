from aip import AipOcr
from aip import AipSpeech
from playsound import playsound


#  这里填你的 APPID AK SK 
MY_APP_ID = '16007034'
MY_API_KEY = '9cVZDkCrl0sZP3wpQlMeqZq2'
MY_SECRET_KEY = 'lGTYdBrcomGUAgfPCt2jrYO9Rg68IMAB'

APP_ID = '22882014'
API_KEY = 'tteMH4Qo5RHfneTAuQ5EsMHF'
SECRET_KEY = 'Zi60uSuSC6jCOynSGDHkWg360CYlwIuu'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
clients = AipSpeech(MY_APP_ID,MY_API_KEY,MY_SECRET_KEY)
# 读取图片 
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('test6.jpg')


#  调用通用文字识别, 图片参数为本地图片 ,未定义识别参数
result = client.basicGeneral(image)
#print(result)


test6 = ''
for word in result['words_result']:
    test6 += word['words']
#print(test6)


##文字转语音
results = clients.synthesis(test6, 'zh', 1, { 'vol': 5,'per':4,'spd':5 })

#识别正确返回语音二进制 错误则返回dict 参照下面错误码 
if not isinstance(results, dict): 
    with open('test6.mp3', 'wb') as f: 
        f.write(results)
else:
    print(results)
playsound("test6.mp3")


 
    
