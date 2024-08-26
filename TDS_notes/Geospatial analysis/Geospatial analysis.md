# Geospatial analysis
- [the notebook containing the analysis](https://colab.research.google.com/drive/1TwKw2pQ9XKSdTUUsTq_ulw7rb-xVhays?usp=sharing)(imp!!)

    - imports 
    ```python
        import pandas as pd
        import numpy as np
        import folium
        import geopy.distance
        from geopy.geocoders import Nominatim

        geolocator = Nominatim(user_agent="geoapiExercises")
    ```
    - to get the distances between 2 places
    ```python
        loc1 = geolocator.geocode(city1)
        loc2 = geolocator.geocode(city2)
        print(geopy.distance.distance((loc1.latitude, loc1.longitude), (loc2.latitude, loc2.longitude)).km)
    ```
    - working with maps 
    ```python
    #Empire State Building coordinates
    m = folium.Map(location=NY_coord, zoom_start= 15)

    #Place markers for the stores on the map
    for i,row in df.iterrows():
        lat = df.at[i, 'lat']
        lng = df.at[i, 'lng']
        store = df.at[i, 'store']

        if store == 'McDonalds':
            color = 'red'
        else:
            color = 'green'

        folium.Marker(location=[lat,lng], popup=store, icon= folium.Icon(color=color)).add_to(m)

    m
    ```

- QGIS is an opensource software to create and export shapefiles.

- [navigating through QGIS](https://youtu.be/tJhehs0o-ik?si=Xpq-h8bSeb852ncq)

---
# Network analysis 
- the sk learn network library will be used here. 



---
## References:
1. [folium](https://python-visualization.github.io/folium/latest/)

2. [QGIS software](https://www.qgis.org/)

3. [sklearn network library](https://scikit-network.readthedocs.io/en/latest/use_cases/votes.html)