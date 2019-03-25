# I want to add a project to the map :heart:

### How does the map work?

The database of projects in the map is publicly available in [Wikidata](https://www.wikidata.org) and displayed as a map through the [Wikidata Query Service](https://query.wikidata.org).

In very very simple words, Wikidata is like Wikipedia but instead of writing articles you contribute to it with structured data. 

This means you can define your own data model, input data or import it from available sources and then use that same structure to search the database with the Query service. As part of the latter you can visualize results as a table, graph or map (if your data has geo coordinates).

[Database in table format](http://tinyurl.com/y6nxlzev)     
[Database in graph format]()    
[Database in map format]()

#### Why Wikidata?
The benefits I see from this approach are:    
- Anyone can contribute;
- Map is updated everytime you visit it;
- Easy to link with other sources of data (wikipedia articles, github repos, journal articles);
- Engagement with the bigger wikimedia community
- Small collaboration == big benefits - By linking our nodes with other info already in wikidata we get a bigger picture

There is a small possibility of vandalism, that's why I keep a periodic [backup]() of the database in this same repo.

#### Data model
This is the minimum proposed structure that allows us to map projects that are part of GOSH community. It's made taking into account the available items (Q) and properties (P) defined by the Wikidata community. 

1. Node must be `instance of (P31)` one of the following:

- `project (Q170584)`
- `community (Q177634)`
- `university research group (Q28863779)`
- `business (Q4830453)`
- `institution (Q178706)`

2. Node must have statement `use (P366)` with one of the following values:

- `education (Q8434)`
- `art (Q735)`
- `academic research (Q62393045)`
- `community science (Q62392920)`

3. Node must have statement `field of work (P101)` with one of the following values or any other value available and useful:

- `microscopy	Q1074953`
- `biohacking	Q5205179`
- `unmanned aerial vehicle	Q484000`
- `microfluidics	Q138845`
- `transfeminism Q3308597`
- `air quality	Q56245086`
- `soil quality	Q2034420`
- `water quality	Q625376`
- `health Q12147`
- `physics	Q413`
- `sound	Q11461`
- `audiovisual	Q2431196`
- `textile	Q28823`
- `social innovation	Q1399209`
- `STEAM education Q62393596`

4. Node must have statement `official website (P856)` with a link pointing to documentation

5. Node must have statement `location (P276)` with value corresponding to item of the city where node happens.

  *Note: if city or region item doesn't have coordinate locations within its own page, node won't be mapped*

6. Node must have statement `part of (P361)` with value `Global Open Science Hardware (Q62391989)`

Check an example here: [Monitor Abierto de Calidad de Aire (MACA)](https://www.wikidata.org/wiki/Q62395443)

### How to collaborate?

#### Add a project
Check this tutorial ---> Video

If you know of an open science hardware project (or maybe it's your own project!) that isn't listed in our map, do the following:

1. Go to [Wikidata](https://wikidata.org) and create a user (not mandatory but I recommend it so you can trace your changes)
2. Look for the project in the search box. 

**If project already has a page in Wikidata**

3. Make sure the six statements explained in *'Data model'* are there with their corresponding values

**If you can't find your project in Wikidata:**

3. Create an item
4. Add a label and description of your project
5. Make sure you add the six statements explained in *'Data model'*, with their corresponding values

Finally, check if your node has been added in [the map](http://tinyurl.com/y5d6hqb3). It's not automatic, may take a while to update (max 20').

If you have any problems or questions you can contact me: **jarancio[at]fund-cenit.org.ar**

#### Translate data
Check this tutorial ---> Video


### Further uses of the map 

Besides visualizing where GOSH projects are, I think structuring data this way can be useful for other things. E.g. listing resources that people find useful, links to journal articles, institutions supporting open science hardware, events organized by the community and so on. 

This organized information can then feed e.g. a landing page for people outside the community, but also be useful for evaluating through time how the community changes, if nodes are created, disappear or change.
