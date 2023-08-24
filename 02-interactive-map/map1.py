import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])


def color_producer(el):
    if el < 2000:
        return "green"
    elif el < 3500:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, li, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, li], radius=6, popup=str(
        el), fill_color=color_producer(el), color="grey", fill=True, fill_opacity=0.7))

fg.add_child(folium.GeoJson(
    data=(open("world.json", 'r+', encoding="utf-8-sig").read())))

map.add_child(fg)
map.save("Map1.html")
