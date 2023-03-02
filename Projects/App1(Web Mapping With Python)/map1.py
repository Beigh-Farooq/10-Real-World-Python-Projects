'''import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat=list(data['LAT'])
lan=list(data['LON'])
elev=list(data['ELEV'])


def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")

fg=folium.FeatureGroup(name="My Map")

for lt,ln,el in zip(lat,lan,elev):
    #Adding Multiple Markers With Elevation and Colors of markers depending on Evelation value
    #fg.add_child(folium.Marker(location=[lt,ln], popup="Hi I am a marker",icon=folium.Icon(color='green')))
    #fg.add_child(folium.Marker(location=[lt,ln], popup=str(el)+" m",icon=folium.Icon(color='green')))
    fg.add_child(folium.Marker(location=[lt,ln], popup=str(el)+" m",icon=folium.Icon(color=color_producer(el))))
    #fg.add_child(folium.CircleMarker(location=[lt,ln], popup=str(el)+" m",icon=folium.Icon(color=color_producer(el))))

#Adding polygons according to population
fg.add_child(folium.GeoJson(data=open('world.json',"r",encoding='utf-8-sig').read(),
style_function=lambda x: {'fillcolor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'})

fg.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
 style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

#map.add_child(folium.Marker(location=[38.2,-99.1],popup="Hi i am a Marker",icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("Map1.html")'''



import folium
import pandas

def RAG(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


data = pandas.read_csv("volcanoes.txt")
lat = data["LAT"]
lon = data["LON"]
elev = data["ELEV"]
html = """<h4>Volcano Information:</h4>
Heigth: {}m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tile ="Stamen Terrain")

fgv = folium.FeatureGroup(name="MyMap")

for lt, ln, el in zip(lat, lon, elev):
    #fg.add_child(folium.Marker(location=[lt, ln], popup= folium.Popup(html.format(str(el))), icon=folium.Icon(color=RAG(el))))
    fgv.add_child(folium.CircleMarker(location=(lt, ln), radius = 6, popup= folium.Popup(html.format(str(el))), color=RAG(el),
     fill_color = RAG(el), opacity = 0.9, fill_opacity= 0.7, fill=True))

# you can break lines in Python when the expression is in brackets, round, square or curley

# here you add a whole dictionary in one go so there is no need to loop
#fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
#style_function=lambda x: {'fillColor':'green' if True}))
fgp = folium.FeatureGroup(name="Population")


fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
 style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
# lambda = in line function, e.g.
# >>> l= lambda x: x**2
# >>> l(5)
# 25
# not sure why you need a lambda function here intead of just fillcolor. Maybe because in the background it
#needs a function to fill a polyglon? No idea
# x in a dictionary? the way you access it is via the ["properties"]["POP2005"]; we're accessing the POP2005 value
# of the Properties key



map.add_child(fgv)
map.add_child(fgp)
#
# so you can switch off the layers, not the base layer
# if you only have 1 fg(FeatureGroup), it will switch all items in theis fg on and off
# if you create different fg for volcanos and population,
# before the for loop write fgv=folium.FeatureGroup(name="Volcanoes")
# in the loop replace fg with fgv
# after teh for loop write fgp = foliom.FeatureGroup(name="Population")
# map.add_child(fgv)
# map.add_child(fgp)
# map.add_child(folium.layerControl()) remains the same
map.add_child(folium.LayerControl())
map.save("Map1.html")
