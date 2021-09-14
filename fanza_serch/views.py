from django.shortcuts import render
from django.http import HttpResponse
from fanza_serch.forms import SeachForm
import requests
import json


def index(request):
    if request.method == 'POST':
        keyword = request.POST['name']
        cupword = request.POST['cup']
        height_gte = request.POST['max_height']
        height_lte = request.POST['min_height']
        kekka = []
        toal = 0

        for off in range(1, 10000, 100):
            off2 = str(off)
            # apiデータ取得
            url = 'https://api.dmm.com/affiliate/v3/ActressSearch?api_id=hFyNTuH4MpNCU7qNRKWg&affiliate_id=smsm257703-990&keyword=' + \
                keyword+'&gte_height='+height_gte+'&lte_height=' + \
                height_lte+'&hits=100&offset='+off2+'&output=json'

            # レスポンス内容を変数へ保存
            response = requests.get(url)

            # JSONデータに変換して変数へ保存
            jsonData = response.json()

            if jsonData["result"]["result_count"] == 0:
                break
            else:
                jsonData2 = jsonData["result"]["actress"]
                for i in jsonData2:
                    # 値がないkeyに値をいれる
                    if 'name' not in i.keys():
                        i['name'] = 'None'
                    elif 'cup' not in i.keys():
                        i['cup'] = 'None'
                    elif 'waist' not in i.keys():
                        i['waist'] = 'None'
                    elif 'hip' not in i.keys():
                        i['hip'] = 'None'
                    elif 'height' not in i.keys():
                        i['height'] = 'None'
                    elif 'birthday' not in i.keys():
                        i['birthday'] = 'None'
                    elif 'prefectures' not in i.keys():
                        i['prefectures'] = 'None'

                    # 写真
                    if 'imageURL' not in i.keys():
                        i['imageURL'] = 'None'

                    # url
                    if 'digital' not in i['listURL'].keys():
                        i['listURL']['digital'] = 'None'

                    if not cupword:
                        kekka.append(i)
                        # print("名前:", i["name"])
                        # print("カップ:", i["cup"])
                        # print("ウエスト:", i["waist"])
                        # print("ヒップ:", i["hip"])
                        # print("身長:", i["height"])
                        # print("生年月日:", i["birthday"])
                        # print("出身地:", i["prefectures"])
                        # print("動画URL:", a["digital"])
                    else:
                        if cupword == i["cup"]:
                            kekka.append(i)
                            # print("名前:", i["name"])
                            # print("カップ:", i["cup"])
                            # print("ウエスト:", i["waist"])
                            # print("ヒップ:", i["hip"])
                            # print("身長:", i["height"])
                            # print("生年月日:", i["birthday"])
                            # print("出身地:", i["prefectures"])
                            # print("動画URL:", a["digital"])
                    toal += 1
        f = SeachForm()
        return render(request, 'index.html', {'form1': f, 'serchlist': kekka, 'total': toal})
        # return render(request, 'index.html', {'serchlist': kekka})
    else:
        f = SeachForm()
        return render(request, 'index.html', {'form1': f})
