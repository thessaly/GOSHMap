# I want to add a project to the map

Thanks <3

If you have a GitHub account, keep reading the instructions.

If you don't have a GitHub account, send me an e-mail with the project name, location and a URL to julieta@rlab.be


### How does the map work?

The database of projects is contained in a .csv file you'll find in this repo, called [goshmap.csv](https://github.com/thessaly/GOSHMap/blob/master/goshmap.csv).

You can collaborate by generating pull requests to this file, that are reviewed for consistency and merged. 

The .csv file is then turned into a map by [Umap](http://umap.openstreetmap.fr), based on [Open Street Map](http://openstreetmap.org).


### How to collaborate?

If you know an open hardware project (or maybe it's your own project!) that isn't listed in our map, do the following:

#### 1. Log into your GitHub account and go to https://github.com/thessaly/GOSHMap

#### 2. Edit the file **openhwmap.csv** 

This file is a comma-separated values (CSV) one. It stores tabular data (numbers and text) in plain text. Each line of the file is a data record (in our case, each row is an open hardware project). Each record consists of one or more fields, separated by commas. 

So you just need to edit the file, go to the last row and add another row, with the following format:

##### > fields
`latitude,longitude,geometry,name,GOSH,status,type,url`

##### > example
`-31.4116703,-64.2315674,Point,"AlterMundi - Redes libres comunitarias",n,active,Non-academic,http://altermundi.net`

##### > data required

Up to now, we're requiring the following data for each Open Science Hardware project:

```
latitude: in decimal values    

longitud: in decimal values
```

If you don't have the coordinates for your point, you can easily obtain them by going to [GeoJSON.io](http://geojson.io), selecting the marker tool (A), creating a point (B) and copy&pasting the data (C) as follows 

![coordinates](/screenshots/coordinates.png) 

```
geometry: by default, value is always 'Point'    

name: name of the project    

GOSH: this field admits two different values - 'y'/'n'  
  y= this project is part of the GOSH community
  n= this project is not part of the GOSH community   

status: this field admits two different values - 'active'/'inactive'    
  active= project had some activity going on during the last year    
  inactive= there's been no activity in the project for the last year    

type: this field admits four different values - 'academic'/'non-academic'/'artist'/'business'    
  academic= depending on university or research institution    
  non-academic= outside academia community project   
  artist= independent or collective artists    
  business= for profit developments    

url: website, repo, a reference url where to find more about the project    
```

#### 3. Commit the change and make a [pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/)

#### 4. Wait for it to be approved and merged into the main file (won't take long, promise!)
