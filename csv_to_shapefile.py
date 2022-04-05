#This script converts from CSV to shapefile ormat to use GeoNode and other Geo management data services.

from sys import exit
import pandas as pd
from geopandas import GeoDataFrame
from shapely.geometry import Point
import fiona



__params = {'x': 'location-Longitude',
        'y': 'location-Latitude',
        'crs': '+init=epsg:4326',
        'driver': 'ESRI Shapefile',
        # Write down here the location of the CSV file to convert
        'csv': 'db/input.csv',
        'output': 'shapefiles/output.shp'
    }


def csv_to_shapefile(params):
    print(params.values())
    try:
        __df = pd.read_csv(params['csv'])
        __x = __df[params['x']]
        __y = __df[params['y']]
        __geo = [Point(xy) for xy in zip(__x,__y)]
        __gdf = GeoDataFrame(__df, crs=params['crs'], geometry=__geo)
        __gdf.to_file(driver=params['driver'], filename=params['output'])
        print('Success writting Shapefile')
        return True
    except:
        return False 



if __name__ == "__main__":
    if not csv_to_shapefile(__params):
        exit()
else:
    print(__name__ + " is imported as a Module")
