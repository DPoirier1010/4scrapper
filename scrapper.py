from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen

#Author raider1010
#inspired by https://youtu.be/m_agcM_ds1c
#4chan Scrapper 1.0



hdr = {'User-Agent':'Mozilla/5.0'}
site = input("copy the url         :") #### path to a thread the thread you want all images
counter = 1
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, "html.parser")

#for script in soup(["script"]):
#    script.decompose() 

allImg = soup.findAll("a", class_="fileThumb") #### find all the url for the images
for i in allImg :
    image=i.get('href') ### get the url
    image2 = image
    image = 'http:' + image ### add the http for bs4
    req2 = Request(image,headers=hdr)
    page2 = urlopen(req)
    soup2 = BeautifulSoup(page2, "html.parser")
    filename = (image2).strip("/i4cdn.org/wg ")#strip the filename to only have number
    print("Image number " + counter + " have been saved")
    counter = counter+1


    imageFile = open(filename + ".png", 'wb')
    imageFile.write(urllib.request.urlopen(image).read()) #### Download and write the url
    imageFile.close()

print("CASH MONEY!")


#I should add an input for the path