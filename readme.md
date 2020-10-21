> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-10-20

## Confirmados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |    2256 |            9 |
| SUR             | Calacoto        |     227 |            3 |
| PERIFERICA      | Zona Norte      |     269 |            2 |
| SUR             | Chasquipampa    |     156 |            2 |
| PERIFERICA      | Huaychani       |      17 |            1 |
| CENTRO          | San Sebastián   |     152 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado       |    1388 |           14 |
| CENTRO          | Miraflores            |     974 |            6 |
| SAN ANTONIO     | San Antonio           |     687 |            5 |
| PERIFERICA      | Achachicala           |     318 |            4 |
| PERIFERICA      | Villa de la Cruz      |     116 |            3 |
| SUR             | Irpavi II             |      44 |            3 |
| SAN ANTONIO     | Villa Copacabana      |     541 |            3 |
| COTAHUMA        | Alpacoma              |      11 |            2 |
| SUR             | Alto Obrajes          |     288 |            2 |
| SUR             | Bella Vista           |     157 |            2 |
| SUR             | Calacoto              |     179 |            2 |
| SUR             | Meseta Achumani       |      29 |            2 |
| SAN ANTONIO     | Villa Armonía         |     196 |            2 |
| COTAHUMA        | Tembladerani          |     288 |            2 |
| COTAHUMA        | Sopocachi             |     574 |            2 |
| MAX PAREDES     | La Portada            |     164 |            1 |
| MAX PAREDES     | Callampaya            |     122 |            1 |
| COTAHUMA        | Sopocachi Alto        |     278 |            1 |
| CENTRO          | San Sebastián         |     126 |            1 |
| COTAHUMA        | Villa Nuevo Potosí    |     284 |            1 |
| COTAHUMA        | Belén                 |     101 |            1 |
| SUR             | Ovejuyo               |      35 |            1 |
| SUR             | San Miguel            |      50 |            1 |
| COTAHUMA        | San Pedro Alto        |     262 |            1 |
| MAX PAREDES     | Caja Ferroviaria      |      33 |            1 |
| SUR             | Cota Cota             |     187 |            1 |
| MAX PAREDES     | 14 de Septiembre      |     133 |            1 |
| MAX PAREDES     | Chijini               |     201 |            1 |
| COTAHUMA        | Cotahuma              |      67 |            1 |
| MAX PAREDES     | Mariscal Santa Cruz   |     141 |            1 |
| PERIFERICA      | Villa El Carmen       |     208 |            1 |
| PERIFERICA      | Las Delicias          |     110 |            1 |
| MAX PAREDES     | El Tejar              |     311 |            1 |
| PERIFERICA      | Agua de la Vida       |     104 |            1 |
| COTAHUMA        | 8 de Diciembre        |      40 |            1 |
| PERIFERICA      | Villa 18 de Mayo      |      31 |            1 |
| PERIFERICA      | Agua de la Vida Norte |      16 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona        |   Total |   Último Día |
|-----------------|-------------|---------|--------------|
| SUR             | Bella Vista |      10 |            1 |

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