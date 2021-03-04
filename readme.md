> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2021-03-03

## Confirmados en el último día

| Macrodistrito   | Zona              |   Total |   Último Día |
|-----------------|-------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado   |    4128 |           10 |
| SUR             | Obrajes           |     988 |            7 |
| CENTRO          | Miraflores        |    2066 |            3 |
| CENTRO          | Miraflores Sur    |     732 |            3 |
| SUR             | Cota Cota         |     391 |            3 |
| COTAHUMA        | Belén             |     219 |            1 |
| CENTRO          | Central           |     537 |            1 |
| CENTRO          | Santa Barbara     |     303 |            1 |
| SUR             | Bolognia          |     152 |            1 |
| SUR             | Jardines del Sur  |      67 |            1 |
| SUR             | Alto Irpavi       |     214 |            1 |
| SUR             | Irpavi            |     700 |            1 |
| SAN ANTONIO     | Kupini            |     269 |            1 |
| COTAHUMA        | Cotahuma          |     110 |            1 |
| SAN ANTONIO     | Villa Copacabana  |    1190 |            1 |
| SAN ANTONIO     | Valle Hermoso     |     194 |            1 |
| PERIFERICA      | Chuquiaguillo     |     120 |            1 |
| PERIFERICA      | Miraflores Alto   |     434 |            1 |
| PERIFERICA      | Poqueni           |      85 |            1 |
| PERIFERICA      | Challapampa       |     255 |            1 |
| PERIFERICA      | Villa Pabón       |     240 |            1 |
| MAX PAREDES     | Rincón La Portada |      34 |            1 |
| MAX PAREDES     | El Tejar          |     628 |            1 |
| MAX PAREDES     | Pura Pura         |     607 |            1 |
| COTAHUMA        | San Pedro Alto    |     600 |            1 |
| SAN ANTONIO     | San Antonio       |    1458 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona               |   Total |   Último Día |
|-----------------|--------------------|---------|--------------|
| SUR             | Alto Obrajes       |     408 |            6 |
| SAN ANTONIO     | Pampahasi          |     653 |            4 |
| COTAHUMA        | Villa Nuevo Potosí |     396 |            3 |
| COTAHUMA        | Sopocachi          |     800 |            2 |
| MAX PAREDES     | 14 de Septiembre   |     171 |            2 |
| SAN ANTONIO     | San Antonio        |     953 |            2 |
| NO IDENTIFICADO | No Identificado    |    2157 |            2 |
| MAX PAREDES     | Gran Poder         |     245 |            1 |
| MAX PAREDES     | Callampaya         |     159 |            1 |
| CENTRO          | Central            |     312 |            1 |
| COTAHUMA        | San Pedro Alto     |     377 |            1 |
| SUR             | Chasquipampa       |     177 |            1 |
| SUR             | Pedregal           |      49 |            1 |
| SUR             | Auquisamaña        |      49 |            1 |
| SUR             | Cota Cota          |     238 |            1 |
| SAN ANTONIO     | Villa Armonía      |     276 |            1 |
| SAN ANTONIO     | Villa Litoral      |      33 |            1 |
| MAX PAREDES     | Alto Pura Pura     |      31 |            1 |
| SAN ANTONIO     | Villa Salomé       |     229 |            1 |
| MAX PAREDES     | Los Andes          |     115 |            1 |
| COTAHUMA        | Bajo Llojeta       |     208 |            1 |
| PERIFERICA      | Miraflores Alto    |     279 |            1 |
| PERIFERICA      | Alto Vino Tinto    |      33 |            1 |
| MAX PAREDES     | La Portada         |     229 |            1 |
| PERIFERICA      | Las Delicias       |     134 |            1 |

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