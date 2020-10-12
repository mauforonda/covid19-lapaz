> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-10-11

## Confirmados en el último día

| Macrodistrito   | Zona             |   Total |   Último Día |
|-----------------|------------------|---------|--------------|
| PERIFERICA      | Agua de la Vida  |     125 |            2 |
| NO IDENTIFICADO | No Identificado  |    2248 |            2 |
| COTAHUMA        | Pasankeri        |     182 |            1 |
| PERIFERICA      | Villa de la Cruz |     145 |            1 |
| PERIFERICA      | Vino Tinto       |     402 |            1 |
| SAN ANTONIO     | Villa Copacabana |     652 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |    1351 |            3 |
| SAN ANTONIO     | Villa Salomé    |     166 |            3 |
| PERIFERICA      | Achachicala     |     301 |            2 |
| CENTRO          | Miraflores Sur  |     352 |            2 |
| SAN ANTONIO     | San Antonio     |     656 |            2 |
| MAX PAREDES     | La Portada      |     159 |            1 |
| PERIFERICA      | Vino Tinto      |     295 |            1 |
| CENTRO          | Miraflores      |     931 |            1 |
| COTAHUMA        | San Pedro Alto  |     254 |            1 |
| CENTRO          | Santa Barbara   |     138 |            1 |
| SUR             | Alto Obrajes    |     275 |            1 |
| SUR             | Bolognia        |      61 |            1 |
| SUR             | Chasquipampa    |     119 |            1 |
| SUR             | Calacoto        |     175 |            1 |
| SUR             | Irpavi          |     309 |            1 |
| SAN ANTONIO     | Villa Armonía   |     189 |            1 |
| SAN ANTONIO     | Kupini          |     112 |            1 |
| MAX PAREDES     | Los Andes       |      84 |            1 |
| COTAHUMA        | Tembladerani    |     280 |            1 |
| PERIFERICA      | Villa Fátima    |     354 |            1 |
| PERIFERICA      | Barrio Gráfico  |      93 |            1 |
| PERIFERICA      | 27 de Mayo      |      23 |            1 |
| MAX PAREDES     | Obispo Indaburo |     111 |            1 |
| PERIFERICA      | Zona Norte      |     213 |            1 |
| COTAHUMA        | Sopocachi       |     555 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona          |   Total |   Último Día |
|-----------------|---------------|---------|--------------|
| MAX PAREDES     | La Portada    |       7 |            1 |
| PERIFERICA      | Vino Tinto    |      14 |            1 |
| PERIFERICA      | Chuquiaguillo |       4 |            1 |

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