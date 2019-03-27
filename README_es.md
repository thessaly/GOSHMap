# Mapa de Hardware Científico Abierto Global (GOSH)

[:uk:](README.md)

Esta iniciativa tiene como objetivo construir una base de datos colaborativa de proyectos de hardware científico abierto a nivel global. Comenzó con iniciativas de Latinoamerica como parte de mi [tesis doctoral](https://github.com/thessaly/phd/) y ahora queremos ampliarlo como parte de la comunidad [GOSH - Global Open Source Hardware](https://openhardware.science). 

[**:earth_americas: Mapa**](http://tinyurl.com/y2ehx763)   

[**:heart: Quiero colaborar**](CONTRIBUTING_es.md)

### ¿Cómo funciona el mapa?
La base de datos de proyectos está disponible públicamente en [Wikidata](https://www.wikidata.org) y se puede visualizar como mapa a través del [Servicio de Query de Wikidata](https://query.wikidata.org).

<details><summary><b>¿Por qué Wikidata?</b></summary>
<p>
A modo muy simplificado, Wikidata es como Wikipedia pero en vez de editar artículos se contribuye con datos estructurados.

Esto significa que podés definir tu propio data model, agregar datos o importarlos de otras bases abiertas y después usar esa estructura para obtener información a través del servicio de Query. Éste último es el que permite visualizar resultados en forma de tablas, gráficos o mapas (si la data tiene coordenadas geográficas) entre otros.

[Datos en formato tabla](https://query.wikidata.org/#SELECT%20%3Fitem%20%3FitemLabel%20%3FlugarLabel%20%3FtipoLabel%20%3FareaLabel%20%3Fcoords%20WHERE%20%7B%0A%20%20%3Fitem%20wdt%3AP361%20wd%3AQ62391989%3B%0A%20%20%20%20%20%20%20%20wdt%3AP276%20%3Flugar%3B%0A%20%20%20%20%20%20%20%20wdt%3AP31%20%3Ftipo%3B%0A%20%20%20%20%20%20%20%20wdt%3AP366%20%3Farea.%0A%20%20%3Flugar%20wdt%3AP625%20%3Fcoords.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%7D)     
[Ejemplo de gráfico](/screenshots/graphgosh.png)    

Los beneficios que veo de este abordaje son:
- Cualquiera puede contribuir;
- El mapa se actualiza cada vez que lo visitás;
- Es fácil linkear con otras fuentes de datos (artículos de wikipedia, repos de github, papers académicos);
- Formar parte de la comunidad más grande de Wikimedia;
- Una contribución mínima tiene grandes beneficios, al linkear nuestros nodos con otra data disponible en wikidata obtenemos información nueva

Existe una pequeña chance de vandalismo, por lo cual mantengo un [backup](goshmap.csv) de la base de datos en este mismo repo.

</details>

<details><summary><b>Data model</b></summary>
<p>
Esta es la mínima estructura propuesta para mapear los proyectos de la comunidad GOSH. Está hecha teniendo en cuenta los ítems (Q) y propiedades (P) definidos por la comunidad de Wikidata.

*Chequeá un ejemplo acá: [Monitor Abierto de Calidad de Aire (MACA)](https://www.wikidata.org/wiki/Q62395443)*

1. El nodo debe ser `instancia de (P31)` alguno de los siguientes:

- `project (Q170584)`
- `community (Q177634)`
- `university research group (Q28863779)`
- `business (Q4830453)`
- `institution (Q178706)`

2. El nodo debe contener la declaración `uso (P366)` con uno de los siguientes valores:

- `education (Q8434)`
- `art (Q735)`
- `academic research (Q62393045)`
- `community science (Q62392920)`

3. El nodo debe contener la declaración  `campo de trabajo (P101)` con alguno de los siguientes valores (o cualquier otro que esté disponible y sea descriptivo):

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

4. El nodo debe contener la declaración `página web oficial (P856)` con un link a documentación

5. El nodo debe contener la declaración  `ubicación (P276)` con el valor correspondiente a la ciudad donde se realiza la actividad.

  *Nota: si la ciudad o región no especifican coordenadas geográficas en su propia página, el ítem no se mostrará en el mapa*

6. El nodo debe contener la declaración `forma parte de (P361)` con valor `Global Open Science Hardware (Q62391989)`

</details>

### Colaborando con el mapa

Podés contribuir añadiendo nodos, traduciendo datos, mejorando visualizaciones o cualquier otra cosa que se te ocurra. 

Chequeá las [guías para contribución](CONTRIBUTING_es.md) para entender cómo.

### Otros usos del mapa

Más allá de visualizar dónde están los proyectos de GOSH, creo que estructurar los datos de esta forma puede ser útil para otras cosas. Por ejemplo listar recursos que la gente considera útiles, linkear artículos científicos, instituciones que promueven el hardware científico abierto, eventos organizados por la comunidad, etc.

Esta información una vez organizada puede alimentar por ejemplo una página web para que gente externa a la comunidad pueda entender qué hacemos y qué recursos hay rápidamente. Otro uso puede ser el de evaluar cómo la comunidad cambia, si se crean, desaparecen o modifican nodos a través del tiempo.

:mailbox: Problemas, preguntas, sugerencias? **jarancio[at]fund-cenit.org.ar**
