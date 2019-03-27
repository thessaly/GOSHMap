# Quiero colaborar :heart:

Gracias! :hatched_chick: :tada:

Si tenés algún problema o pregunta me podés contactar a: **jarancio[at]fund-cenit.org.ar**

<details><summary><b>:chart_with_upwards_trend: Data model</b></summary>
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

<details><summary><b>:wrench: Añadiendo un proyecto al mapa</b></summary>
<p>
Si sabés de algún proyecto de hardware científico abierto (quizás el tuyo!) que no está en el mapa:

1. Ir a [Wikidata](https://wikidata.org) y crear un usuario (no es obligatorio pero lo recomiendo para que quede en el history)
2. Buscar el proyecto en la opción de búsqueda

**--> Si el proyecto ya tiene una página en Wikidata**

3. Confirmá que las seis declaraciones explicadas en *'Data model'* están completas

**--> Si no encontrás el proyecto en Wikidata**

3. Creá un item
4. Añadí una etiqueta y descripción del proyecto
5. Confirmá que las seis declaraciones explicadas en *'Data model'* están completas

Finalmente chequeá si el nodo fue añadido al [map](http://tinyurl.com/y2ehx763). No es automático, puede tardar un poco en actualizar (max 20').

<p>
 <b>Click en la imagen para ver el tutorial en video</b>    
 
[![Tutorial](https://img.youtube.com/vi/lJge3_wojgA/0.jpg)](https://youtu.be/lJge3_wojgA)


<p>
</details>

<details><summary><b>:pencil: Traduciendo datos</b></summary>
<p>
Próximamente.
<p>
</details>

<details><summary><b>:sparkler: Mejorando la visualización</b></summary>
<p>
Sabés de herramientas que puedan utilizarse para mejorar la visualización del mapa? O para crear nuevas visualizaciones a partir de los datos que estamos cargando? Contactame!
<p>
</details>
