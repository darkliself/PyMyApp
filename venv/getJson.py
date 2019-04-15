import json
import requests


class Logic: 
    def GetJsonFromItem(self, textArea, key, url):
        # 6735ebd44e9850ab188356ffba5cbb7cad8aa756
        itemUrl = "https://claims.cnetcontent.com/issues/" + url + ".json"
        headers = {'Content-type': 'application/json', 'X-Redmine-API-Key': key}
        response1 = requests.get(itemUrl, headers=headers)
        responseJSON = ""
        formatted = ""
        if response1.status_code == 200:
            responseJSON = response1.json()
            formattedJSON = json.dumps(responseJSON) #separators=(",", ":"))
            result = json.loads(formattedJSON)
            # you ended here
            print(result)
            formatted = result["issue"]["description"].replace("\r", "").replace('<pre><code class="sql">', '').replace('</code></pre>', '')
        elif response1.status_code == 404:
            print("Url not found")
        if len(formatted) > 0:
            textArea.setPlainText(formatted)
        else:
            print(response1.status_code)
            print("empty item or without description")
    def PutJsonToItem(self, text, key, url):
        itemUrl = "https://claims.cnetcontent.com/issues/" + url + ".json"
        headers = {'Content-type': 'application/json', 'X-Redmine-API-Key': key}
        dump = json.dumps(text, separators=(",", "\""))
        tmp = dump#.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r")
        print(tmp)
        someData = '{"issue": {"description": "%s"} }' % (tmp[1:-1])
       

        try:
            print(someData)
            print("here1")
            putJson = requests.put(itemUrl, data=someData, headers=headers)
            print(putJson.status_code)
        except Exception:
            print("its not working")

        #https://claims.cnetcontent.com/issues/325864
        
        