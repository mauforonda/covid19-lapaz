> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-11-10

## Confirmados en el último día

| Macrodistrito   | Zona               |   Total |   Último Día |
|-----------------|--------------------|---------|--------------|
| COTAHUMA        | Villa Nuevo Potosí |     359 |            1 |
| COTAHUMA        | San Pedro Alto     |     329 |            1 |
| MAX PAREDES     | Los Andes          |     111 |            1 |
| PERIFERICA      | Villa de la Cruz   |     148 |            1 |
| PERIFERICA      | Zona Norte         |     280 |            1 |
| PERIFERICA      | La Mercéd          |     152 |            1 |
| SAN ANTONIO     | San Isidro         |     137 |            1 |
| SUR             | San Miguel         |      56 |            1 |
| SUR             | Obrajes            |     495 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado       |    1514 |           27 |
| CENTRO          | Miraflores            |    1044 |           18 |
| SAN ANTONIO     | San Antonio           |     756 |           15 |
| SAN ANTONIO     | Villa Copacabana      |     578 |            9 |
| COTAHUMA        | Tembladerani          |     313 |            7 |
| PERIFERICA      | Villa Fátima          |     386 |            7 |
| SAN ANTONIO     | Pampahasi             |     486 |            6 |
| PERIFERICA      | Vino Tinto            |     350 |            6 |
| CENTRO          | Miraflores Sur        |     391 |            5 |
| MAX PAREDES     | Gran Poder            |     202 |            5 |
| COTAHUMA        | San Pedro Alto        |     295 |            5 |
| COTAHUMA        | Sopocachi             |     610 |            5 |
| COTAHUMA        | Villa Nuevo Potosí    |     317 |            4 |
| MAX PAREDES     | Villa Victoria        |     290 |            4 |
| COTAHUMA        | San Pedro             |     508 |            4 |
| COTAHUMA        | 8 de Diciembre        |      45 |            4 |
| SUR             | Obrajes               |     439 |            4 |
| COTAHUMA        | Obispo Bosque         |      61 |            4 |
| PERIFERICA      | Zona Norte            |     242 |            4 |
| CENTRO          | Central               |     245 |            3 |
| CENTRO          | San Sebastián         |     138 |            3 |
| SUR             | Achumani              |     399 |            3 |
| SUR             | Calacoto              |     197 |            3 |
| PERIFERICA      | Challapampa           |     161 |            3 |
| PERIFERICA      | Villa de la Cruz      |     127 |            3 |
| MAX PAREDES     | Munaypata             |     342 |            3 |
| PERIFERICA      | Villa El Carmen       |     231 |            3 |
| PERIFERICA      | Achachicala           |     344 |            3 |
| COTAHUMA        | Bello Horizonte       |     165 |            3 |
| MAX PAREDES     | Obispo Indaburo       |     124 |            3 |
| PERIFERICA      | Miraflores Alto       |     218 |            2 |
| MAX PAREDES     | Alto Ciudadela        |      41 |            2 |
| CENTRO          | Santa Barbara         |     153 |            2 |
| SUR             | Alto Obrajes          |     310 |            2 |
| MAX PAREDES     | Ciudadela Ferroviaria |      92 |            2 |
| MAX PAREDES     | Chamoco Chico         |      85 |            2 |
| SAN ANTONIO     | Villa Armonía         |     208 |            2 |
| SAN ANTONIO     | San Isidro            |     126 |            2 |
| PERIFERICA      | La Mercéd             |     137 |            2 |
| COTAHUMA        | Tupac Amaru           |      21 |            2 |
| PERIFERICA      | Barrio Gráfico        |     105 |            2 |
| MAX PAREDES     | Callampaya            |     132 |            2 |
| PERIFERICA      | Alto Vino Tinto       |      31 |            2 |
| COTAHUMA        | Bajo Llojeta          |     148 |            2 |
| MAX PAREDES     | 14 de Septiembre      |     141 |            2 |
| MAX PAREDES     | La Portada            |     174 |            2 |
| PERIFERICA      | Plan Autopista        |      24 |            2 |
| COTAHUMA        | Cotahuma              |      73 |            2 |
| PERIFERICA      | Agua de la Vida       |     111 |            1 |
| SUR             | Bella Vista           |     181 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona      |   Total |   Último Día |
|-----------------|-----------|---------|--------------|
| MAX PAREDES     | Pura Pura |      10 |            1 |
| MAX PAREDES     | Munaypata |      13 |            1 |

## Activos desde el 1 de Julio

### Centro

![Centro](plots/activos_centro.png)

### Cotahuma

![Cotahuma](plots/activos_cotahuma.png)

### Hampaturi

![Hampaturi](plots/activos_hampaturi.png)

### Mallasa

![Mallasa](plots/activos_mallasa.png)

### Max Paredes

![Max Paredes](plots/activos_max_paredes.png)

### Periferica

![Periferica](plots/activos_periferica.png)

### San Antonio

![San Antonio](plots/activos_san_antonio.png)

### Sur

![Sur](plots/activos_sur.png)

---

### Notas

Consulto el servicio de datos del Gobierno Municipal cada día a las 10am y asumo que estos valores reflejan el estado de los casos para el día anterior. Algunas posibles fuentes de error son:

1. Si los datos se actualizaran contínuamente, una parte de los casos que asigno al día anterior corresponden en realidad al día en curso. [He consultado al encargado](https://twitter.com/mauforonda/status/1278727234765959168) del servicio si la inferencia que hago es correcta y no ha respondido.

2. A diario, algunos casos no son georeferenciados y no se reportan en el conteo de ninguna zona, pero sí aparecen en el conteo total de casos. Reporto el número diario de estos casos como 'No Identificado'.  Sin embargo, el Gobierno Municipal podría georeferenciar estos casos en los días siguientes y se sumarían al conteo de casos en sus zonas. Esto significa que una parte de los valores que asigno a cada zona podría representar casos de días pasados. En la actualidad, el Gobierno Municipal no ofrece una forma de corregir este error. Por esto, si deseas estudiar la curva epidemiológica para cada zona en base a estos datos, sugiero usar una media móvil de al menos 3 días.