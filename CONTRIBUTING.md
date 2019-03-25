# I want to contribute :heart:

Thank you! :hatched_chick: :tada:

If you have any problems or questions you can contact me: **jarancio[at]fund-cenit.org.ar**

<details><summary><b>:chart_with_upwards_trend: Data model</b></summary>
<p>
This is the minimum proposed structure that allows us to map projects that are part of GOSH community. It's made taking into account the available items (Q) and properties (P) defined by the Wikidata community. 

*Check an example here: [Monitor Abierto de Calidad de Aire (MACA)](https://www.wikidata.org/wiki/Q62395443)*

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

</details>

<details><summary><b>:wrench: Adding a project to the map</b></summary>
<p>
If you know of an open science hardware project (or maybe it's your own project!) that isn't listed in our map, do the following:

1. Go to [Wikidata](https://wikidata.org) and create a user (not mandatory but I recommend it so you can trace your changes)
2. Look for the project in the search box. 

**--> If project already has a page in Wikidata**

3. Make sure the six statements explained in *'Data model'* are there with their corresponding values

**--> If you can't find your project in Wikidata**

3. Create an item
4. Add a label and description of your project
5. Make sure you add the six statements explained in *'Data model'*, with their corresponding values

Finally, check if your node has been added in [the map](http://tinyurl.com/y2ehx763). It's not automatic, may take a while to update (max 20').

<p>
 <b>Click on image for video tutorial</b>    
 
[![Tutorial](https://img.youtube.com/vi/lJge3_wojgA/0.jpg)](https://youtu.be/lJge3_wojgA)


<p>
</details>

<details><summary><b>:pencil: Translating data</b></summary>
<p>
Coming soon.
<p>
</details>

<details><summary><b>:sparkler: Better visualizations</b></summary>
<p>
Are you aware of any tools on top of wikidata that can make the map look better? Or visualizations that can be made using the data we're mapping? Contact me!
<p>
</details>
