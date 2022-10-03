import urllib
url = 'https://www.donneesquebec.ca/recherche/api/3/action/datastore_search?resource_id=cc5fe19b-12de-47c3-b69f-67c7418d7c59&limit=5&q=title:jones'  
fileobj = urllib.urlopen(url)
print(fileobj.read())
