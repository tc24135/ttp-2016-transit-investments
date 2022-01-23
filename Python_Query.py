## NOTE: https://www.thetransportpolitic.com/transitexplorer/#6/38.625/-78.673
##https://python-overpy.readthedocs.io/en/latest/example.html
###Preliminary install Code

#conda install -c conda-forge overpy

###Running
import requests
import json

overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
[out:json];
(node["railway"="{0}"](38.511, -77.811, 39.711, -76.111);
 way["railway"="{0}"](38.511, -77.811, 39.711, -76.111);
 rel["railway"="{0}"](38.511, -77.811, 39.711, -76.111);
);
out center;
""".format(railway_types[1])

response = requests.get(overpass_url,
                        params={'data': overpass_query})
data = response.json()
#data

import numpy as np
import matplotlib.pyplot as plt

# Collect coords into list
coords = []
for element in data['elements']:
  if element['type'] == 'node':
    lon = element['lon']
    lat = element['lat']
    coords.append((lon, lat))
  elif 'center' in element:
    lon = element['center']['lon']
    lat = element['center']['lat']
    coords.append((lon, lat))

# Convert coordinates into numpy array
X = np.array(coords)

plt.plot(X[:, 0], X[:, 1], 'o')
plt.title('DC Area rail map')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.axis('equal')
plt.show()

#railway:preserved=yes + railway=*"
#railway=proposed and proposed=*
#railway=construction and construction=*
#Operational - "rail"  add start_date=*.
#result = api.query("""way["railway"="subway"];out;""")
