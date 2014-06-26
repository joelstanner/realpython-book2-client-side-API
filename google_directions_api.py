# google directions API


from xml.etree import ElementTree as et
import requests

# URL for the API call to google directions
url = "http://maps.googleapis.com/maps/api/directions/xml?origin=San+Francisco&destination=Los+Angeles"

# request the data in XML form
#xml = requests.get(url)

# save data as a file and parse the XML
#with open("goog_directions.xml", "wb") as code:
#    code.write(xml.content)
    
output = et.parse("goog_directions.xml")

# loop through the info and print the directions in 'html_instructions'
    
for element in output.findall("route/leg/step"):
    print element.find("html_instructions").text
        
    
