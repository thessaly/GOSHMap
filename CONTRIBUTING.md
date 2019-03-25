# I want to add a project to the map

Thanks for contributing :heart: 

### How does the map work?

The database of projects in the map is publicly available in [Wikidata](https://www.wikidata.org) and displayed as a map through a service also provided by Wikidata.

In very very simple words, Wikidata is like Wikipedia but instead of writing articles you contribute to it with structured data. 
This means you can define your own structure for data you're interested in, and then search the database with the [Query tool](https://query.wikidata.org) and get your results (and, like in our case, display them in a map). 

The interesting part is that with a small collaboration you can get big results. E.g., in order to display a map I need to know the geographical coordinates of each project. But I don't need to input them, as I can add which city the project works in, and the coordinates for that city are already on Wikidata so I just call them in my query. 

This is a super simple example but kinda illustrates how we can get new information by linking our contributions to existing data in Wikidata.

### How to collaborate?

So, if you know of an open science hardware project (or maybe it's your own project!) that isn't listed in our map, do the following:

1. Go to wikidata.org
2. Look for the project in the search box - if there is an item in Wikidata for this project, go to 3
3. Add a new statement 
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
