> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-11-01

## Confirmados en el último día

| Macrodistrito   | Zona               |   Total |   Último Día |
|-----------------|--------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado    |    2272 |            3 |
| COTAHUMA        | Sopocachi          |     669 |            2 |
| COTAHUMA        | Villa Nuevo Potosí |     358 |            1 |
| COTAHUMA        | San Pedro          |     564 |            1 |
| PERIFERICA      | Vino Tinto         |     407 |            1 |
| PERIFERICA      | Challapampa        |     185 |            1 |
| PERIFERICA      | San Juan Lazareto  |      97 |            1 |
| PERIFERICA      | 3 de Mayo          |      28 |            1 |
| SAN ANTONIO     | Kupini             |     151 |            1 |
| SUR             | Alto Següencoma    |     119 |            1 |
| SUR             | Alto Obrajes       |     340 |            1 |
| CENTRO          | Miraflores         |    1150 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                 |   Total |   Último Día |
|-----------------|----------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado      |    1447 |            8 |
| SAN ANTONIO     | San Antonio          |     720 |            6 |
| MAX PAREDES     | Chijini              |     219 |            5 |
| SUR             | Obrajes              |     423 |            3 |
| COTAHUMA        | Sopocachi Alto       |     292 |            3 |
| COTAHUMA        | San Pedro            |     496 |            3 |
| CENTRO          | Miraflores Sur       |     372 |            3 |
| CENTRO          | Santa Barbara        |     145 |            2 |
| CENTRO          | San Jorge            |     246 |            2 |
| PERIFERICA      | Villa de la Cruz     |     120 |            2 |
| SUR             | Calacoto             |     188 |            2 |
| SAN ANTONIO     | San Isidro           |     117 |            2 |
| SAN ANTONIO     | Pampahasi            |     459 |            2 |
| CENTRO          | Central              |     234 |            2 |
| PERIFERICA      | Villa El Carmen      |     223 |            2 |
| CENTRO          | Miraflores           |    1006 |            2 |
| PERIFERICA      | Achachicala          |     335 |            2 |
| PERIFERICA      | Miraflores Alto      |     210 |            2 |
| MAX PAREDES     | El Tejar             |     321 |            2 |
| COTAHUMA        | Bajo Llojeta         |     142 |            2 |
| MAX PAREDES     | Villa Victoria       |     280 |            1 |
| SUR             | Los Pinos            |     154 |            1 |
| COTAHUMA        | Pasankeri            |     161 |            1 |
| COTAHUMA        | Obispo Bosque        |      55 |            1 |
| COTAHUMA        | Faro Murillo         |      22 |            1 |
| CENTRO          | San Sebastián        |     132 |            1 |
| COTAHUMA        | Villa Nuevo Potosí   |     300 |            1 |
| SUR             | Alto Següencoma      |      97 |            1 |
| COTAHUMA        | San Juan de Cotahuma |      24 |            1 |
| SUR             | Ovejuyo              |      38 |            1 |
| SUR             | Achumani             |     387 |            1 |
| SUR             | Alto Irpavi          |     101 |            1 |
| COTAHUMA        | Bello Horizonte      |     155 |            1 |
| SUR             | Cota Cota            |     193 |            1 |
| MAX PAREDES     | Munaypata            |     331 |            1 |
| COTAHUMA        | San Pedro Alto       |     278 |            1 |
| MAX PAREDES     | Pura Pura            |     273 |            1 |
| MAX PAREDES     | Chamoco Chico        |      82 |            1 |
| PERIFERICA      | Chuquiaguillo        |      70 |            1 |
| PERIFERICA      | La Mercéd            |     133 |            1 |
| PERIFERICA      | Villa Fátima         |     375 |            1 |
| MAX PAREDES     | Obispo Indaburo      |     121 |            1 |
| PERIFERICA      | Santa Rosa           |      47 |            1 |
| MAX PAREDES     | 14 de Septiembre     |     136 |            1 |
| MAX PAREDES     | Mariscal Santa Cruz  |     144 |            1 |
| PERIFERICA      | Vino Tinto           |     336 |            1 |
| MAX PAREDES     | Alto Villa Victoria  |      20 |            1 |
| COTAHUMA        | Sopocachi            |     588 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona             |   Total |   Último Día |
|-----------------|------------------|---------|--------------|
| SAN ANTONIO     | Villa Copacabana |      16 |            1 |

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