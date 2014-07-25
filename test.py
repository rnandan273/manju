import csv
import mechanize
br = mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
#br.set_handle_robots(False)   # ignore robots
#br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox')]
urls=["http://www.asme.org","http://www.ca.gov/","http://www.shredit.com/Home.aspx"]
urls=["http://www.asme.org"]
tagList=[]

def writeListToFile(fileName,itemList):
    w=csv.writer(file(fileName,'wb'))
    for item in itemList:
        w.writerow([item,])
        
def subUrl(url):
    br.open(url)
    print "SUB URLS"
    for link in br.links():           
        tag = "%s : %s"%(link.text,link.url)
        print tag
        
def scrapeUrl(urls):
    fileCounter = 0
    for url in urls:
        fileCounter=fileCounter+1
        br.open(url)
        tags=[]
        for link in br.links():           
            tag = "%s : %s"%(link.text,link.url)
            print tag
            #subUrl(link.url)
            tags.append(tag)
        fileName = "/Users/raghu/work/projects/manju/%d.csv"%fileCounter
        writeListToFile(fileName,tags)

#scrapeUrl(urls)
print ', '.join("wq q")

from pymongo import MongoClient
client = MongoClient('localhost:27017')
print client.database_names()
db=client.todo
print db.collection_names()


    

print "contacts"   
for cont in db.contacts.find():
   print cont



db.drop_collection(db.contacts)
db.drop_collection(db.gmailcontacts)
db.drop_collection(db.linkedincontacts)


