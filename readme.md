> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-10-05

## Confirmados en el último día

| Macrodistrito   | Zona               |   Total |   Último Día |
|-----------------|--------------------|---------|--------------|
| SUR             | Achumani           |     455 |            2 |
| COTAHUMA        | Sopocachi Alto     |     349 |            1 |
| COTAHUMA        | Cotahuma           |      80 |            1 |
| COTAHUMA        | Villa Nuevo Potosí |     356 |            1 |
| MAX PAREDES     | Pura Pura          |     317 |            1 |
| PERIFERICA      | Vino Tinto         |     402 |            1 |
| PERIFERICA      | Zona Norte         |     265 |            1 |
| PERIFERICA      | Villa Fátima       |     428 |            1 |
| SAN ANTONIO     | Villa Copacabana   |     652 |            1 |
| SAN ANTONIO     | San Antonio        |     843 |            1 |
| CENTRO          | Miraflores         |    1143 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona               |   Total |   Último Día |
|-----------------|--------------------|---------|--------------|
| PERIFERICA      | Miraflores Alto    |     199 |            7 |
| SAN ANTONIO     | San Antonio        |     648 |            4 |
| COTAHUMA        | Tembladerani       |     273 |            4 |
| COTAHUMA        | Villa Nuevo Potosí |     272 |            3 |
| SUR             | Alto Obrajes       |     261 |            3 |
| PERIFERICA      | Villa El Carmen    |     192 |            3 |
| NO IDENTIFICADO | No Identificado    |    1282 |            3 |
| COTAHUMA        | Sopocachi          |     546 |            2 |
| SAN ANTONIO     | Pampahasi          |     419 |            2 |
| COTAHUMA        | Bello Horizonte    |     142 |            2 |
| PERIFERICA      | La Mercéd          |     121 |            2 |
| PERIFERICA      | Chuquiaguillo      |      65 |            2 |
| PERIFERICA      | Las Delicias       |     104 |            2 |
| SUR             | Meseta Achumani    |      29 |            2 |
| SUR             | Bella Vista        |     145 |            2 |
| MAX PAREDES     | 14 de Septiembre   |     125 |            2 |
| PERIFERICA      | Villa Fátima       |     344 |            2 |
| SUR             | Obrajes            |     371 |            1 |
| SUR             | Chasquipampa       |     115 |            1 |
| PERIFERICA      | 3 de Mayo          |      24 |            1 |
| COTAHUMA        | Pasankeri          |     144 |            1 |
| SAN ANTONIO     | 24 de Junio        |       7 |            1 |
| COTAHUMA        | Sopocachi Alto     |     262 |            1 |
| CENTRO          | Santa Barbara      |     132 |            1 |
| CENTRO          | Miraflores Sur     |     345 |            1 |
| COTAHUMA        | Tacagua            |     136 |            1 |
| PERIFERICA      | Barrio Gráfico     |      92 |            1 |
| PERIFERICA      | Santa Rosa de Tiji |      19 |            1 |
| COTAHUMA        | Kantutani          |      23 |            1 |
| PERIFERICA      | Poqueni            |      37 |            1 |
| PERIFERICA      | Agua de la Vida    |     100 |            1 |
| PERIFERICA      | Challapampa        |     143 |            1 |
| MAX PAREDES     | Chualluma          |       7 |            1 |
| MAX PAREDES     | Munaypata          |     308 |            1 |
| MAX PAREDES     | Villa Victoria     |     256 |            1 |
| MAX PAREDES     | El Tejar           |     299 |            1 |
| MAX PAREDES     | Pura Pura          |     251 |            1 |
| COTAHUMA        | San Pedro Alto     |     246 |            1 |
| COTAHUMA        | Obispo Bosque      |      52 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |     159 |            2 |

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