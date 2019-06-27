import time

longitude = '4.1'
latitude = '51.3'
count = 0
while True:
    with open ('position.kml', 'w') as pos:
        pos.write('''<kml xmlns="http://www.opengis.net/kml/2.2"
 xmlns:gx="http://www.google.com/kml/ext/2.2"><Placemark>
  <name>Live GPS</name>
  <description>Live GPS from master.</description>
  <Point>
    <coordinates>-%s,%s,0</coordinates>
  </Point>
</Placemark></kml>''' % (longitude,latitude))
    count = count + 1
    time.sleep(1)
    if count == 2:
        longitude = '4.3'
        latitude = '52.3'
        count = 0
    else:
        longitude = '4.2'
        latitude = '51.3'
