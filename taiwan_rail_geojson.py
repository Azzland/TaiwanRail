#-*-coding:utf8;-*-
#qpy:console

from geojson import Point, Feature, FeatureCollection, dump
import csv

input_csv = '/storage/emulated/0/Download/All stations Taiwan.csv'
geojson_output = '/storage/emulated/0/Download/All stations Taiwan.geojson'


data = []
attributes = []

with open(input_csv) as csv_file:
    print('Reading CSV.....')
    reader = csv.reader(csv_file) 
    for row in reader:
        data.append(row) 

#print(data)
attributes = data[0]
input_data = data[1:]
#print(input_data)
#print(attributes)        
features = []
num_stations = len(input_data)
num_attributes = len(attributes)

print('Writing Geojson file....')
for i in range(num_stations):
    #print(i)
    lon = float(input_data[i][num_attributes-2])
    lat = float(input_data[i][num_attributes-1])
    point = Point((lon, lat))
    feature_dict = {}
    
    for j in range(num_attributes-2):
        feature_dict[attributes[j]] = str(input_data[i][j])
    
    features.append(Feature(geometry=point, properties=feature_dict))

# add more features...
# features.append(...)

feature_collection = FeatureCollection(features)

with open(geojson_output, 'w') as f:
   dump(feature_collection, f)

