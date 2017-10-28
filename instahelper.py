import urllib.request, json, sys, time, string

QUERY_ID='GIMME'
if len(sys.argv) != 2:
    print("Usage: script.py insta_url")
else:
    user_id="BLAA"
    output=open("runme.bat","w")
    with urllib.request.urlopen(sys.argv[1]) as url:
        mybytes = url.read()
        mystr = mybytes.decode("utf8")
        url.close()
        for currentLine in mystr.split('\n'):
            if currentLine.find("window._sharedData") != -1:
                data=json.loads(currentLine[currentLine.find("window._sharedData")+21:-10])
                user_id=data['entry_data']['ProfilePage'][0]['user']['id']
                output.write('curl.exe --cacert cacert.pem -o '+data['entry_data']['ProfilePage'][0]['user']['username']+'-profile.jpg "'+data['entry_data']['ProfilePage'][0]['user']['profile_pic_url_hd'].replace("\/", "/")+'"\nping -n 1 127.0.0.1>NUL\n')
                time.sleep(2)
    with urllib.request.urlopen('https://www.instagram.com/graphql/query/?query_id='+QUERY_ID+'&variables={%22id%22:%22'+user_id+'%22,%22first%22:1}') as url:
        data = json.loads(url.read().decode())
        #with open('data.txt', 'w') as outfile:
        #    json.dump(data, outfile)
        #print(data['data']['user']['edge_owner_to_timeline_media']['count'])
        time.sleep(2)
        with urllib.request.urlopen('https://www.instagram.com/graphql/query/?query_id='+QUERY_ID+'&variables={%22id%22:%22'+user_id+'%22,%22first%22:'+str(data['data']['user']['edge_owner_to_timeline_media']['count'])+'}') as url:
            data = json.loads(url.read().decode())
            for image in data['data']['user']['edge_owner_to_timeline_media']['edges']:
                output.write('curl.exe --cacert cacert.pem -O "'+image['node']['display_url'].replace("\/", "/")+'"\nping -n 1 127.0.0.1>NUL\n')