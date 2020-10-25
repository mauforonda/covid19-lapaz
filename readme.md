> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-10-24

## Confirmados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |    2256 |            4 |
| PERIFERICA      | Vino Tinto      |     404 |            2 |
| SUR             | Calacoto        |     228 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado       |    1410 |            5 |
| COTAHUMA        | San Pedro Alto        |     269 |            4 |
| PERIFERICA      | Achachicala           |     327 |            3 |
| CENTRO          | Miraflores            |     988 |            3 |
| SUR             | Obrajes               |     409 |            3 |
| SAN ANTONIO     | San Antonio           |     699 |            3 |
| COTAHUMA        | Sopocachi Alto        |     285 |            3 |
| MAX PAREDES     | El Tejar              |     318 |            3 |
| CENTRO          | Central               |     227 |            2 |
| SUR             | Bella Vista           |     165 |            2 |
| SAN ANTONIO     | Pampahasi             |     451 |            2 |
| SAN ANTONIO     | Villa Copacabana      |     546 |            2 |
| PERIFERICA      | Agua de la Vida       |     107 |            2 |
| COTAHUMA        | Sopocachi             |     582 |            2 |
| PERIFERICA      | Barrio Gráfico        |      97 |            2 |
| COTAHUMA        | Pasankeri             |     153 |            2 |
| MAX PAREDES     | Gran Poder            |     186 |            2 |
| COTAHUMA        | Villa Nuevo Potosí    |     292 |            2 |
| COTAHUMA        | Belén                 |     105 |            2 |
| SAN ANTONIO     | Villa Armonía         |     199 |            1 |
| COTAHUMA        | Las Lomas             |      31 |            1 |
| CENTRO          | San Jorge             |     238 |            1 |
| CENTRO          | San Sebastián         |     129 |            1 |
| SUR             | Chasquipampa          |     127 |            1 |
| SUR             | Alto Calacoto         |      18 |            1 |
| SUR             | Alto Achumani         |      29 |            1 |
| SUR             | Aruntaya              |      12 |            1 |
| SUR             | Calacoto              |     182 |            1 |
| SUR             | Los Pinos             |     148 |            1 |
| MAX PAREDES     | Villa Victoria        |     273 |            1 |
| MAX PAREDES     | Munaypata             |     320 |            1 |
| SAN ANTONIO     | Cuarto Centenario     |      72 |            1 |
| SAN ANTONIO     | Villa Salomé          |     175 |            1 |
| MAX PAREDES     | Alto Ciudadela        |      39 |            1 |
| MAX PAREDES     | Ciudadela Ferroviaria |      86 |            1 |
| SAN ANTONIO     | Valle Hermoso         |      78 |            1 |
| MAX PAREDES     | Chamoco Chico         |      82 |            1 |
| MAX PAREDES     | Los Andes             |      89 |            1 |
| PERIFERICA      | Miraflores Alto       |     206 |            1 |
| MAX PAREDES     | Callampaya            |     123 |            1 |
| PERIFERICA      | Villa Pabón           |     114 |            1 |
| PERIFERICA      | Zona Norte            |     221 |            1 |
| MAX PAREDES     | Alto Tejar            |      52 |            1 |
| SAN ANTONIO     | Kupini                |     115 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona         |   Total |   Último Día |
|-----------------|--------------|---------|--------------|
| SAN ANTONIO     | Escobar Uría |       2 |            1 |

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