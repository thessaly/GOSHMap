# I want to contribute :heart:

Thank you! :hatched_chick: :tada:


If you have any problems or questions you can contact me: **jarancio[at]unsam.edu.ar**

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

2. Node must have statement `field of work (P101)` with one of the following values:

- `education (Q8434)`
- `art (Q735)`
- `academic research (Q62393045)`
- `community science (Q62392920)`

3. Node must have statement `official website (P856)` with a link pointing to documentation

4. Node must have statement `location (P276)` with value corresponding to item of the city where node happens.

  *Note: if city or region item doesn't have coordinate locations within its own page, node won't be mapped*

5. Node must have statement `part of (P361)` with value `Global Open Science Hardware (Q62391989)`

</details>

<details><summary><b>:wrench: Adding a project to the map</b></summary>
<p>
If you know of an open science hardware project (or maybe it's your own project!) you can easily add it to Wikidata [using this form](https://cradle.toolforge.org/#/subject/open_science_hardware_project).

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
