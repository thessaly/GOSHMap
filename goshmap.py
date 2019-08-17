from flask import Flask
import folium, requests
import pandas as pd

app = Flask(__name__)

# download data with coords
df = pd.read_csv("https://raw.githubusercontent.com/thessaly/GOSHMap/master/goshdata.csv")

# rename columns
lat = df.lat
long = df.long
name = df.itemLabel
tipo = df.tipoLabel
area = df.areaLabel
url = df.url

# get set of areas and types
areas = area.unique()
tipos = tipo.unique()

# creates map
central_coords = 20.96, -5.318236

map = folium.Map(
    location=central_coords,
    zoom_start=3
    )

# clustering and grouping by area

from folium import plugins

mcg = folium.plugins.MarkerCluster(control=False)

map.add_child(mcg)

commsci = plugins.FeatureGroupSubGroup(mcg, areas[0])
academic= plugins.FeatureGroupSubGroup(mcg, areas[1])
education = plugins.FeatureGroupSubGroup(mcg, areas[2])
art = plugins.FeatureGroupSubGroup(mcg, areas[3])
business = plugins.FeatureGroupSubGroup(mcg, areas[4])

map.add_child(commsci)
map.add_child(academic)
map.add_child(education)
map.add_child(art)
map.add_child(business)

for i in range(0, len(df.lat)):

    url = '\"' + df.url[i] + '\"'

    if area[i] == 'education':
        folium.Marker([lat[i], long[i]],
                      popup='<a href='+ url +'>'+name[i]+'</a>',
                      tooltip=tipo[i],
                      icon=folium.Icon(color='green')
                      ).add_to(education)

    elif area[i] == 'community science':
        folium.Marker([lat[i], long[i]],
                      popup='<a href='+ url +'>'+name[i]+'</a>',
                      tooltip=tipo[i],
                      icon=folium.Icon(color='blue')
                      ).add_to(commsci)

    elif area[i] == 'academic research':
        folium.Marker([lat[i], long[i]],
                      popup='<a href='+ url +'>'+name[i]+'</a>',
                      tooltip=tipo[i],
                      icon=folium.Icon(color='purple')
                      ).add_to(academic)

    elif area[i] == 'art':
        folium.Marker([lat[i], long[i]],
                      popup='<a href='+ url +'>'+name[i]+'</a>',
                      tooltip=tipo[i],
                      icon=folium.Icon(color='red')
                      ).add_to(art)

    elif area[i] == 'social innovation':
        folium.Marker([lat[i], long[i]],
                      popup='<a href='+ url +'>'+name[i]+'</a>',
                      tooltip=tipo[i],
                      icon=folium.Icon(color='gray')
                      ).add_to(business)

folium.LayerControl(collapsed=False).add_to(map)

minimap = plugins.MiniMap()
map.add_child(minimap)

# display map in /goshmap
@app.route('/goshmap')
def mapshow():
        global map
        return map.get_root().render()

if __name__ == '__main__':
    app.run(debug=True)
