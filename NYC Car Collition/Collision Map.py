#Shi Tao Luo
#Shitao.luo40@myhunter.cuny.edu
#Nov. 11 2019
#This program print out the collitions in nyc




import folium
import pandas as pd


inF = input("Enter a csv file:")
outF = input("Enter a output file:")

Colli = pd.read_csv(inF)

mapColli = folium.Map(location=[40.75, -74.125], zoom_start = 10, tiles="Cartodb Positron")

Colli = Colli.dropna(subset=["LATITUDE"])
Colli = Colli.dropna(subset=["LONGITUDE"])

for index,row in Colli.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    time = row["TIME"]
    newMarker = folium.Marker([lat, lon], popup=time)
    newMarker.add_to(mapColli)

mapColli.save(outfile=outF)
