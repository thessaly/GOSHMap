[English version](README.md)

# Bienvenida al Mapa colaborativo de Hardware Abierto! 

[**El Mapa**](openhwmap.geojson) 

Esta iniciativa tiene como objetivo construir una base de datos -y un mapa- colaborativos con proyectos de hardware abierto a nivel global. Comenzó con proyectos de Latinoamerica como parte de mi [tesis doctoral](https://thessaly.github.io/phd/) y ahora queremos ampliarlo a la escala global como parte de la comunidad [GOSH - Global Open Source Hardware](https://openhardware.science). 

Las especificaciones del mapa están siendo discutidas en [este thread](https://forum.openhardware.science/t/map-cadastre-list-of-open-science-hardware-initiatives-in-chile-latam/835/3), en caso de que quieras chequear las últimas novedades. El mapa todavía se encuentra en estado de desarrollo.


### ¿Como funciona?

La base de datos se encuentra en un archivo .csv dentro de este repositorio, llamado [openhwmap.csv](https://github.com/thessaly/OpenHWMap/blob/master/openhwmap.csv).

Las usuarias pueden colaborar a traves de la generación de pull requests sobre este archivo, que luego son aprobadas y combinadas en el archivo principal.

Una vez combinadas la colaboración y la base de datos, se genera un [archivo .geojson](https://github.com/thessaly/OpenHWMap/blob/master/openhwmap.geojson) a partir de la base de datos actualizada. 

GitHub [muestra automáticamente como mapas](https://help.github.com/articles/mapping-geojson-files-on-github/) los archivos .geojson desde los repositorios, y de esa forma obtenemos nuestro mapa basico que puede ser embebido en cualquier otro sitio.


### ¿Como colaborar?

Si conoces un proyecto de hardware abierto (¡quizas sea tu propio proyecto!) que no se encuentre en el mapa, podes hacer lo siguiente:

#### 1. [Forkear](https://help.github.com/articles/fork-a-repo/) este repositorio

#### 2. Agregar la información del proyecto al archivo **openhwmap.csv** 

Un archivo CSV (comma-separated values) almacena datos tabulados (texto y numeros) en forma de texto plano. Cada línea del archivo es un registro (en nuestro caso, un proyecto de hardware abierto). Cada registro consiste de uno o ms campos, separados por comas.

As que solamente necesitas editar el archivo .csv, ir a la última fila y agregar una mas, bajo el siguiente formato:

##### > campos
`latitude,longitude,geometry,name,GOSH,status,type,url`

##### > ejemplo
`-31.4116703,-64.2315674,Point,"AlterMundi - Redes libres comunitarias",n,active,Non-academic,http://altermundi.net`

##### > data requerida

Hasta ahora, los datos que necesitamos para subir un nuevo proyecto de Hardware Abierto son: 

```
latitude: en valores decimales   

longitud: en valores decimales 
```

Si no conoces las coordenadas de tu proyecto, podes obtenerlas facilmente yendo a [GeoJSON.io](http://geojson.io), seleccionando la herramienta 'marcador' (A), creando un punto (B) y haciendo copy&paste de los datos (C) de la siguiente manera (**IMPORTANTE**: al editar el csv hay que agregar **primero** el valor de latitud y despues la longitud, cuidado porque geojson.io da los valores **al reves**): 

![coordinates](/screenshots/coordinates.png) 

```
geometry: por default, el valor siempre es 'Point'    

name: nombre del proyecto   

GOSH: este campo admite dos valores diferentes - 'y'/'n'      
  y= este proyecto es parte de la comunidad GOSH    
  n= este proyecto no forma parte de la comunidad GOSH   

status: este campo admite dos valores diferentes - 'active'/'inactive'    
  active= el proyecto presenta alguna actividad durante el último año    
  inactive= el proyecto no presenta ninguna actividad durante el último año    

type: este campo admite cuatro valores diferentes - 'academic'/'non-academic'/'artist'/'business'    
  academic= el proyecto depende de una universidad o centro de investigación    
  non-academic= el proyecto se realiza por fuera de la academia, en la comunidad    
  artist= artistas independientes o colectivos de artistas        
  business= desarrollos con fines de lucro       

url: website, repositorio, o referencia donde encontrar ms información del proyecto
```

#### 3. Crear una [pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/)

#### 4. Esperar a que se apruebe la pull request y se combine con la base de datos principal (prometo que no va a tardar mucho!)
