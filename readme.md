> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-08-01

## Confirmados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| CENTRO          | Miraflores            |     626 |           31 |
| NO IDENTIFICADO | No Identificado       |     758 |           29 |
| PERIFERICA      | Achachicala           |     175 |           16 |
| CENTRO          | Miraflores Sur        |     240 |           13 |
| MAX PAREDES     | Munaypata             |     216 |           10 |
| PERIFERICA      | Villa Fátima          |     228 |           10 |
| SUR             | Obrajes               |     223 |            9 |
| COTAHUMA        | San Pedro Alto        |     169 |            9 |
| SAN ANTONIO     | Pampahasi             |     242 |            8 |
| MAX PAREDES     | La Portada            |     105 |            8 |
| MAX PAREDES     | Pura Pura             |     154 |            8 |
| SAN ANTONIO     | San Antonio           |     405 |            8 |
| MAX PAREDES     | El Tejar              |     210 |            7 |
| SUR             | Irpavi                |     204 |            7 |
| SUR             | Achumani              |     199 |            7 |
| COTAHUMA        | Tembladerani          |     168 |            7 |
| SUR             | Cota Cota             |     114 |            6 |
| SUR             | Calacoto              |     120 |            6 |
| CENTRO          | Central               |     164 |            6 |
| MAX PAREDES     | 14 de Septiembre      |      90 |            5 |
| SAN ANTONIO     | Villa Copacabana      |     320 |            5 |
| SUR             | Pedregal              |      21 |            5 |
| MAX PAREDES     | Villa Victoria        |     177 |            5 |
| SAN ANTONIO     | San Isidro            |      67 |            5 |
| PERIFERICA      | Miraflores Alto       |     119 |            5 |
| COTAHUMA        | Villa Nuevo Potosí    |     162 |            5 |
| COTAHUMA        | Bajo Llojeta          |      79 |            5 |
| MAX PAREDES     | Chijini               |     120 |            5 |
| MAX PAREDES     | Alto Mcal. Santa Cruz |      52 |            4 |
| PERIFERICA      | Vino Tinto            |     179 |            4 |
| CENTRO          | Santa Barbara         |      85 |            4 |
| COTAHUMA        | Tacagua               |      89 |            4 |
| MAX PAREDES     | Alto Tejar            |      28 |            4 |
| SAN ANTONIO     | Villa Armonía         |      99 |            4 |
| COTAHUMA        | Pasankeri             |      93 |            4 |
| COTAHUMA        | Sopocachi Alto        |     168 |            4 |
| SUR             | Koani                 |      13 |            4 |
| MAX PAREDES     | Chamoco Chico         |      47 |            4 |
| MAX PAREDES     | Callampaya            |      82 |            4 |
| PERIFERICA      | Poqueni               |      23 |            3 |
| SUR             | La Florida            |      25 |            3 |
| SAN ANTONIO     | Kupini                |      51 |            3 |
| SAN ANTONIO     | Villa Salomé          |     105 |            3 |
| SUR             | Chasquipampa          |      67 |            3 |
| PERIFERICA      | Barrio Gráfico        |      51 |            3 |
| PERIFERICA      | La Mercéd             |      69 |            3 |
| MAX PAREDES     | Gran Poder            |     122 |            3 |
| PERIFERICA      | Villa El Carmen       |     135 |            3 |
| PERIFERICA      | San Juan Lazareto     |      61 |            3 |
| COTAHUMA        | Sopocachi             |     372 |            3 |

## Recuperados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |      39 |           19 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |      32 |           13 |

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