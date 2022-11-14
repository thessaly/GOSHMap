## Welcome

This initiative aims to build a collaborative database of open science hardware projects around the world. It started with projects from Latin America as part of my [PhD](https://github.com/thessaly/phd/) and now we want to make it global as part of the [Global Open Source Hardware](https://openhardware.science) community. 

> [**The map**](http://thessaly.pythonanywhere.com)   

> [**Send your contribution**](/CONTRIBUTING.md)

***
## How does the map work?

#### Collaborative input via Wikidata

The map database is in Wikidata, although some items are missing geographic coordinates (that's work in progress). Contributions can be easily added to Wikidata through a form (see contribution guidelines in this repo).

[List of projects in Wikidata](https://query.wikidata.org/#SELECT%20DISTINCT%20%3Fitem%20%3FitemLabel%20%3FinstanceOfLabel%20%3FfieldLabel%20%3Furl%20%3Fcoords%0AWHERE%20%7B%0A%20%20%3Fitem%20wdt%3AP361%20wd%3AQ62391989%3B%0A%0A%20%20OPTIONAL%7B%3Fitem%20wdt%3AP856%20%3Furl%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20wdt%3AP31%20%3FinstanceOf%3B%0A%20%20%20%20%20%20%20%20%20%20wdt%3AP101%20%3Ffield%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20wdt%3AP625%20%3Fcoords.%7D%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%2Ces%22.%20%7D%0A%7D)     

The benefits I see from this approach are:    
- Anyone can contribute;
- Map is updated everytime you visit it;
- Easy to link with other sources of data (wikipedia articles, github repos, journal articles);
- Engagement with the bigger wikimedia community

#### Better visualization via Folium

I see two problems having the map only in Wikidata:

- There is a small possibility of vandalism
- The map looks horrible

That's why I keep a periodic [backup](goshdata.csv) of the database in this same repo, which is displayed as a pretty map via a simple [python script](https://github.com/thessaly/GOSHMap/blob/master/goshmap.py). This is the "official" map.
</details>


### Contributing to the map

You can contribute by adding nodes, translating data, enhancing visualizations or anything else that comes to your mind.

Check the [contribution guidelines](CONTRIBUTING.md) to see how.


> Problems, questions, suggestions? **jarancio[at]unsam.edu.ar**
