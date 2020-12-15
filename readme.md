> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-12-14

## Confirmados en el último día

| Macrodistrito   | Zona           |   Total |   Último Día |
|-----------------|----------------|---------|--------------|
| PERIFERICA      | Achachicala    |     416 |            2 |
| SUR             | Cota Cota      |     223 |            2 |
| CENTRO          | Miraflores     |    1183 |            2 |
| COTAHUMA        | Sopocachi      |     687 |            1 |
| COTAHUMA        | Sopocachi Alto |     368 |            1 |
| COTAHUMA        | San Pedro      |     581 |            1 |
| CENTRO          | El Rosario     |     112 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona              |   Total |   Último Día |
|-----------------|-------------------|---------|--------------|
| SAN ANTONIO     | Escobar Uría      |      62 |            2 |
| MAX PAREDES     | La Portada        |     195 |            1 |
| MAX PAREDES     | Alto Tejar        |      70 |            1 |
| PERIFERICA      | Villa Pabón       |     138 |            1 |
| SAN ANTONIO     | Cuarto Centenario |      79 |            1 |
| SAN ANTONIO     | Villa Armonía     |     230 |            1 |
| SUR             | Calacoto          |     225 |            1 |
| SUR             | Auquisamaña       |      44 |            1 |
| CENTRO          | Miraflores        |    1110 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona      |   Total |   Último Día |
|-----------------|-----------|---------|--------------|
| COTAHUMA        | Tacagua   |       7 |            1 |
| SAN ANTONIO     | Pampahasi |      14 |            1 |

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