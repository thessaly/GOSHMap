# Global Open Science Hardware Map

[:es:](README_es.md)

This initiative aims to build a collaborative database of open science hardware projects around the world. It started with projects from Latin America as part of my [PhD](https://github.com/thessaly/phd/) and now we want to make it global as part of the [Global Open Source Hardware](https://openhardware.science) community. 

[**:earth_americas: Map**](http://thessaly.pythonanywhere.com)   

[**:heart: I want to contribute**](CONTRIBUTING.md)


### How does the map work?
The database of projects is available in [this repository](https://github.com/thessaly/GOSHMap/blob/master/goshdata.csv) and displayed as a map via a simple [python script](https://github.com/thessaly/GOSHMap/blob/master/goshmap.py) also available in this repo.

<details><summary><b>Also in Wikidata</b></summary>
<p>
I've replicated the database in Wikidata too, but some items are missing geographic coordinates, therefore not all items are represented in the map view available through the Wikidata Query Service. That's work in progress.

[Wikidate list in table format](https://query.wikidata.org/#SELECT%20DISTINCT%20%3Fitem%20%3FitemLabel%20%3FinstanceOfLabel%20%3FfieldLabel%20%3Furl%20%3Fcoords%0AWHERE%20%7B%0A%20%20%3Fitem%20wdt%3AP361%20wd%3AQ62391989%3B%0A%0A%20%20OPTIONAL%7B%3Fitem%20wdt%3AP856%20%3Furl%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20wdt%3AP31%20%3FinstanceOf%3B%0A%20%20%20%20%20%20%20%20%20%20wdt%3AP101%20%3Ffield%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20wdt%3AP625%20%3Fcoords.%7D%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%2Ces%22.%20%7D%0A%7D)     

The benefits I see from this approach are:    
- Anyone can contribute;
- Map is updated everytime you visit it;
- Easy to link with other sources of data (wikipedia articles, github repos, journal articles);
- Engagement with the bigger wikimedia community

There is a small possibility of vandalism, that's why I keep a periodic [backup](goshmap.csv) of the database in this same repo.

</details>

<details><summary><b>Data model</b></summary>
<p>
This is the proposed structure to allows us map the projects that are part of GOSH community.  

*Check an example here: [Monitor Abierto de Calidad de Aire (MACA)](https://www.wikidata.org/wiki/Q62395443)*

1. Node must be `instance of (P31)` one of the following:

- `project (Q170584)`
- `community (Q177634)`
- `university research group (Q28863779)`
- `business (Q4830453)`
- `institution (Q178706)`

2. Node must have statement `field of work (P101)` with one of the following values:

- `education (Q8434)`
- `art (Q735)`
- `academic research (Q62393045)`
- `community science (Q62392920)`

4. Node must have statement `official website (P856)` with a link pointing to documentation

5. Node must have statement `location (P276)` with value corresponding to item of the city where node happens.

  *Note: if city or region item doesn't have coordinate locations within its own page, node won't be mapped*

6. Node must have statement `part of (P361)` with value `Global Open Science Hardware (Q62391989)`

</details>

### Contributing to the map

You can contribute by adding nodes, translating data, enhancing visualizations or anything else that comes to your mind.

Check the [contribution guidelines](CONTRIBUTING.md) to see how.


:mailbox: Problems, questions, suggestions? **jarancio[at]unsam.edu.ar**
