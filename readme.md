> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-11-30

## Confirmados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| MAX PAREDES     | Villa Victoria  |     330 |            1 |
| PERIFERICA      | Rosasani        |      36 |            1 |
| NO IDENTIFICADO | No Identificado |    2259 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| MAX PAREDES     | Chijini               |     245 |            5 |
| SAN ANTONIO     | Pampahasi             |     533 |            4 |
| COTAHUMA        | Villa Nuevo Potosí    |     336 |            4 |
| MAX PAREDES     | La Portada            |     188 |            4 |
| SAN ANTONIO     | Villa Copacabana      |     631 |            3 |
| PERIFERICA      | Achachicala           |     374 |            2 |
| SUR             | Ovejuyo               |      48 |            2 |
| PERIFERICA      | Villa Pabón           |     134 |            2 |
| MAX PAREDES     | Mariscal Santa Cruz   |     158 |            2 |
| NO IDENTIFICADO | No Identificado       |    1740 |            2 |
| COTAHUMA        | Tembladerani          |     337 |            2 |
| MAX PAREDES     | Chamoco Chico         |      92 |            1 |
| PERIFERICA      | Barrio Gráfico        |     114 |            1 |
| PERIFERICA      | Villa Fátima          |     418 |            1 |
| PERIFERICA      | 3 de Mayo             |      27 |            1 |
| COTAHUMA        | Tacagua               |     167 |            1 |
| SAN ANTONIO     | San Antonio           |     807 |            1 |
| SAN ANTONIO     | Kupini                |     147 |            1 |
| SAN ANTONIO     | Villa Armonía         |     223 |            1 |
| SUR             | Cota Cota             |     210 |            1 |
| SUR             | La Florida            |      39 |            1 |
| SUR             | Los Rosales           |      30 |            1 |
| SUR             | Alto Irpavi           |     117 |            1 |
| SUR             | Achumani              |     429 |            1 |
| COTAHUMA        | Cotahuma              |      78 |            1 |
| SUR             | Chasquipampa          |     148 |            1 |
| SUR             | Ventilla              |      56 |            1 |
| SUR             | Obrajes               |     468 |            1 |
| MALLASA         | Jupapina              |      28 |            1 |
| CENTRO          | Miraflores Sur        |     414 |            1 |
| CENTRO          | Miraflores            |    1088 |            1 |
| PERIFERICA      | Villa El Carmen       |     244 |            1 |
| PERIFERICA      | 27 de Mayo            |      30 |            1 |
| MAX PAREDES     | Barrio Lindo          |       9 |            1 |
| PERIFERICA      | Agua de la Vida Norte |      19 |            1 |
| MAX PAREDES     | Los Andes             |     106 |            1 |
| MAX PAREDES     | Obispo Indaburo       |     135 |            1 |
| MAX PAREDES     | 14 de Septiembre      |     148 |            1 |
| MAX PAREDES     | Pura Pura             |     303 |            1 |
| MAX PAREDES     | Alto Ciudadela        |      43 |            1 |
| MAX PAREDES     | El Tejar              |     340 |            1 |
| MAX PAREDES     | Callampaya            |     136 |            1 |
| COTAHUMA        | Belén                 |     117 |            1 |
| MAX PAREDES     | Alto Tejar            |      65 |            1 |
| MAX PAREDES     | Alto Mcal. Santa Cruz |      86 |            1 |
| PERIFERICA      | Villa de la Cruz      |     136 |            1 |
| PERIFERICA      | Villa 18 de Mayo      |      38 |            1 |
| PERIFERICA      | Vino Tinto            |     375 |            1 |
| COTAHUMA        | Bello Horizonte       |     175 |            1 |
| PERIFERICA      | Challapampa           |     175 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona   | Total   | Último Día   |
|-----------------|--------|---------|--------------|

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