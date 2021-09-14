> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2021-09-13

## Confirmados en el último día

| Macrodistrito   | Zona         |   Total |   Último Día |
|-----------------|--------------|---------|--------------|
| CENTRO          | Miraflores   |    3401 |            2 |
| PERIFERICA      | La Mercéd    |     324 |            1 |
| SAN ANTONIO     | San Antonio  |    2260 |            1 |
| SAN ANTONIO     | Escobar Uría |     164 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| CENTRO          | Miraflores            |    2950 |           10 |
| CENTRO          | Central               |     775 |            7 |
| NO IDENTIFICADO | No Identificado       |    4719 |            6 |
| PERIFERICA      | Achachicala           |     920 |            6 |
| PERIFERICA      | Vino Tinto            |     943 |            6 |
| SUR             | Achumani              |    1278 |            6 |
| SUR             | Obrajes               |    1507 |            4 |
| COTAHUMA        | Sopocachi             |    2013 |            4 |
| MAX PAREDES     | Munaypata             |     818 |            3 |
| PERIFERICA      | Las Delicias          |     291 |            3 |
| PERIFERICA      | Villa Fátima          |    1053 |            3 |
| CENTRO          | San Jorge             |     704 |            3 |
| SUR             | Irpavi                |    1072 |            3 |
| SAN ANTONIO     | Villa Salomé          |     494 |            3 |
| PERIFERICA      | La Mercéd             |     286 |            2 |
| SUR             | Alto Achumani         |      85 |            2 |
| SAN ANTONIO     | Villa Copacabana      |    1608 |            2 |
| PERIFERICA      | Miraflores Alto       |     632 |            2 |
| SAN ANTONIO     | San Antonio           |    1951 |            2 |
| PERIFERICA      | Agua de la Vida       |     314 |            2 |
| PERIFERICA      | Zona Norte            |     789 |            2 |
| PERIFERICA      | Alto Vino Tinto       |      69 |            2 |
| SUR             | Alto Calacoto         |      62 |            2 |
| MAX PAREDES     | La Portada            |     454 |            2 |
| SAN ANTONIO     | Pampahasi             |    1493 |            2 |
| MAX PAREDES     | Alto Tejar            |     174 |            2 |
| COTAHUMA        | Cotahuma              |     145 |            2 |
| COTAHUMA        | San Pedro             |    1249 |            2 |
| SUR             | Alto Obrajes          |    1147 |            2 |
| COTAHUMA        | Villa Nuevo Potosí    |     839 |            2 |
| MAX PAREDES     | Ciudadela Ferroviaria |     221 |            2 |
| SUR             | Alto Següencoma       |     393 |            2 |
| MAX PAREDES     | Pura Pura             |     823 |            2 |
| CENTRO          | Santa Barbara         |     399 |            2 |
| MAX PAREDES     | Chamoco Chico         |     208 |            2 |
| MAX PAREDES     | El Tejar              |     883 |            2 |
| MAX PAREDES     | Callampaya            |     321 |            2 |
| COTAHUMA        | Las Lomas             |     129 |            2 |
| MALLASA         | Mallasa               |     156 |            1 |
| CENTRO          | El Rosario            |     346 |            1 |
| CENTRO          | Miraflores Sur        |     950 |            1 |
| SAN ANTONIO     | Villa Armonía         |     688 |            1 |
| SUR             | Alto Irpavi           |     298 |            1 |
| SUR             | Jardines del Sur      |      95 |            1 |
| SUR             | Calacoto              |     644 |            1 |
| SAN ANTONIO     | San Isidro            |     380 |            1 |
| SUR             | San Miguel            |     138 |            1 |
| SUR             | Bella Vista           |     636 |            1 |
| SUR             | Gramadal              |      40 |            1 |
| SUR             | Alto La Florida       |      21 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona    |   Total |   Último Día |
|-----------------|---------|---------|--------------|
| MAX PAREDES     | Chijini |      17 |            1 |

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