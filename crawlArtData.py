from datetime import time
import numpy as np
import pandas as pd
import urllib.request, json, ssl


url = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=all"

def crawlFun(url):

    context = ssl._create_unverified_context()
    with urllib.request.urlopen(url, context=context) as jsondata:
        data = json.loads(jsondata.read().decode())

    df = pd.DataFrame.from_records(data) # transform json to dataframe

    # extract columns from feature(showInfo)
    timeArry = []
    locationArry = []
    locationNameArry = []
    onSalesArry = []
    priceArry = []
    latitudeArry = []
    longitudeArry = []
    endTimeArry = []

    for i in range(len(df)):
        timeArry.append(df["showInfo"][i][0]["time"])
        locationArry.append(df["showInfo"][i][0]["location"])
        locationNameArry.append(df["showInfo"][i][0]["locationName"])
        onSalesArry.append(df["showInfo"][i][0]["onSales"])
        priceArry.append(df["showInfo"][i][0]["price"])
        latitudeArry.append(df["showInfo"][i][0]["latitude"])
        longitudeArry.append(df["showInfo"][i][0]["longitude"])
        endTimeArry.append(df["showInfo"][i][0]["endTime"])

    df["time"] = timeArry
    df["location"] = locationArry
    df["locationName"] = locationNameArry
    df["onSale"] = onSalesArry
    df["price"] = priceArry
    df["latitude"] = latitudeArry
    df["longitude"] = longitudeArry
    df["endTime"] = endTimeArry

    df = df.drop(columns=["version", "showInfo", "sourceWebPromote", "sourceWebName", "masterUnit", "subUnit",
                          "supportUnit", "otherUnit", "descriptionFilterHtml", "imageUrl", "webSales", "comment",
                          "title", "price", "discountInfo", "showUnit", "location"])

    hitRate = []
    for i in range(len(df)):
        hitRate.append(str(df["hitRate"][i]))
    df["hitRate"] = hitRate
    #df["masterUnit"] = str(df["masterUnit"])
    #df["subUnit"] = str(df["subUnit"])
    #df["supportUnit"] = str(df["supportUnit"])
    #df["otherUnit"] = str(df["otherUnit"])

    return df

df = crawlFun(url)

