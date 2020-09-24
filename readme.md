> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-09-23

## Confirmados en el último día

| Macrodistrito   | Zona              |   Total |   Último Día |
|-----------------|-------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado   |    2220 |           16 |
| PERIFERICA      | Vino Tinto        |     388 |            3 |
| COTAHUMA        | Tembladerani      |     348 |            1 |
| MAX PAREDES     | Chijini           |     253 |            1 |
| PERIFERICA      | Villa 18 de Mayo  |      39 |            1 |
| SAN ANTONIO     | Cuarto Centenario |      81 |            1 |
| CENTRO          | San Jorge         |     282 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                |   Total |   Último Día |
|-----------------|---------------------|---------|--------------|
| SAN ANTONIO     | San Antonio         |     608 |           14 |
| CENTRO          | Miraflores          |     866 |            8 |
| SUR             | Calacoto            |     166 |            6 |
| SAN ANTONIO     | Pampahasi           |     397 |            6 |
| SAN ANTONIO     | Villa Copacabana    |     464 |            6 |
| COTAHUMA        | Villa Nuevo Potosí  |     256 |            5 |
| MAX PAREDES     | Pura Pura           |     236 |            4 |
| PERIFERICA      | Achachicala         |     280 |            4 |
| CENTRO          | Miraflores Sur      |     327 |            3 |
| CENTRO          | San Jorge           |     212 |            3 |
| MALLASA         | Jupapina            |      21 |            3 |
| SUR             | Bella Vista         |     136 |            3 |
| MAX PAREDES     | Obispo Indaburo     |     107 |            3 |
| COTAHUMA        | Sopocachi           |     518 |            3 |
| COTAHUMA        | Tacagua             |     132 |            2 |
| SUR             | Alto Obrajes        |     240 |            2 |
| SUR             | Los Rosales         |      23 |            2 |
| SAN ANTONIO     | Kupini              |      96 |            2 |
| SAN ANTONIO     | Valle de las Flores |      17 |            2 |
| SUR             | Irpavi II           |      36 |            2 |
| PERIFERICA      | Chuquiaguillo       |      59 |            2 |
| PERIFERICA      | Villa El Carmen     |     185 |            2 |
| SUR             | Chasquipampa        |     106 |            2 |
| SUR             | Ventilla            |      40 |            2 |
| SUR             | Meseta Achumani     |      26 |            2 |
| PERIFERICA      | Agua de la Vida     |      95 |            2 |
| COTAHUMA        | Tembladerani        |     242 |            2 |
| PERIFERICA      | Villa de la Cruz    |      97 |            2 |
| SUR             | Obrajes             |     356 |            2 |
| PERIFERICA      | Vino Tinto          |     265 |            2 |
| PERIFERICA      | Villa Pabón         |      98 |            2 |
| MAX PAREDES     | Chijini             |     180 |            2 |
| MAX PAREDES     | Gran Poder          |     167 |            2 |
| COTAHUMA        | Las Lomas           |      24 |            2 |
| MAX PAREDES     | Villa Victoria      |     244 |            2 |
| SUR             | Cota Cota           |     175 |            2 |
| PERIFERICA      | Villa 18 de Mayo    |      30 |            2 |
| MAX PAREDES     | La Portada          |     150 |            2 |
| MALLASA         | Mallasa             |      33 |            1 |
| COTAHUMA        | Tupac Amaru         |      15 |            1 |
| SUR             | La Florida          |      33 |            1 |
| SUR             | Bolognia            |      50 |            1 |
| SUR             | Los Pinos           |     132 |            1 |
| COTAHUMA        | Llojeta             |      68 |            1 |
| SUR             | Irpavi              |     292 |            1 |
| SUR             | Huantaqui           |      59 |            1 |
| SUR             | Pedregal            |      34 |            1 |
| COTAHUMA        | Faro Murillo        |      19 |            1 |
| SUR             | Kupillani           |       6 |            1 |
| SUR             | Alto Irpavi         |      84 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| COTAHUMA        | Sopocachi             |      14 |            2 |
| COTAHUMA        | Tembladerani          |       8 |            1 |
| MAX PAREDES     | El Tejar              |       9 |            1 |
| MAX PAREDES     | Alto Mcal. Santa Cruz |       6 |            1 |
| PERIFERICA      | La Mercéd             |       4 |            1 |
| CENTRO          | Miraflores            |      31 |            1 |

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