# mapbox-gl-heatmap
A small javascript web application, created on top of the mapbox gl js API, to create automated heamtps from geoJSON data.  

# Project Goals:

1) "Batteries Included" heatmapping tool.  Support continuous property data types from geoJson data format (no reverse geocoding required). User interface provided to select basemap, heatmap settings, geosjon properies to plot, heatmap parameter min/max bins, and color styles.

2) Client side javascript tool only.  Bring-your-own server to provide data to map.

3) Create print images of heatmaps for reporting/BI deliverables

4) No local dependancies.  Any user can open this tool up, and begin to heatmap in their browser provided they have internet access, a Mapbox free account, and a web-gl capable browser.

# How to Use:

1) Visit Mapbox.com and create an account.  Copy the Mapbox GL API key to your clipboard.

2) Open the "mapbox-gl-heatmap.html" file in this repo in your favorite browser.

3) Paste the Mapbox API token into the prompt that appears in your browser.  Click "Go".

4) At the top of the map that appears, enter the url to your Geojson data at the top of the map.

5) Wait for the data to load.

6) Adjust the heatmap look and feel using the designer toolbar.  Select the data parameter to heatmap, the blur/radius size of each point, the scale of the heat bins, and more.

7) Click "Save Design" to download a high-resolution image of your current map view.

# Credits
Mapbox

Bootleaf

AthleteDataViz

