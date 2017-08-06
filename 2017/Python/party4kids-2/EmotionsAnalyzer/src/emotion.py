from tkinter import *
import http.client, urllib.request, urllib.parse, urllib.error, base64, sys
import io
import base64
import dropbox
from pprint import pprint
import json


#----------------------------[Dropbox]--------------------------------
access_token = ENTER_YOU_ACCESS_TOKEN READ README!!!


client = dropbox.client.DropboxClient(access_token)
link = client.metadata(path="/party4kids")
print(link)
pathtoimage = link["contents"][0]["path"]
sharelink = client.share(path = pathtoimage, short_url=False)
linkurl = sharelink["url"]
answer = linkurl.replace ("?dl=0", "?dl=1")
print(linkurl)
print(pathtoimage)


#----------------------------------[Основная часть]----------------------
root = Tk()

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'ecce20f1065f4a39b80a40b509a4fcbe',
}

params = urllib.parse.urlencode({ })

def gistogram():
    plt.figure(figsize=(7,5))
    x = [18, 15, 11, 9, 8, 6, 5, 10]
    labels = ['Anger', 'Contempt', 'Disgust', 'Fear', 'Happiness', 'Neutral', 'Sadness', 'Surprise']

    plt.pie(x, labels = labels, autopct = '%1.1f%%', shadow=True);
    plt.show()

def checkbutton():
        body = str({ "url": str(answer)})
        try:
            conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
            conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
            response = conn.getresponse()
            data = response.read().decode("utf-8")
            data_list = json.loads(data)
            for stats_dict in data_list:
                faceStats = stats_dict["scores"]
                result(faceStats)
                pprint(faceStats)
            close = Button(text= "Close", command = root.destroy)
            close.pack() 
            conn.close()
        except Exception as e:
            print(e.args)
            
def result(faceStats):
    anger = Label(text = "Anger: {:.2%}".format(faceStats["anger"]))
    contempt = Label(text = "Contempt: {:.2%}".format(faceStats["contempt"]))
    disgust = Label(text = "Disgust: {:.2%}".format(faceStats["disgust"]))
    fear = Label(text = "Fear: {:.2%}".format(faceStats["fear"]))
    happiness = Label(text = "Happiness: {:.2%}".format(faceStats["happiness"]))
    neutral = Label(text = "Neutral: {:.2%}".format(faceStats["neutral"]))
    sadness = Label(text = "Sadness: {:.2%}".format(faceStats["sadness"]))
    surprise = Label(text = "Surprise: {:.2%}".format(faceStats["surprise"]))
    emptylabel = Label()
    
#-----------------[pack]-------
    anger.pack()
    contempt.pack()
    disgust.pack()
    fear.pack()
    happiness.pack()
    neutral.pack()
    sadness.pack()
    surprise.pack()
    emptylabel.pack()
    
    
checkbutton()
root.mainloop()