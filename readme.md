> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-11-25

## Confirmados en el último día

| Macrodistrito   | Zona           |   Total |   Último Día |
|-----------------|----------------|---------|--------------|
| COTAHUMA        | Sopocachi Alto |     356 |            1 |
| COTAHUMA        | Llojeta        |     109 |            1 |
| COTAHUMA        | Alto Tacagua   |      48 |            1 |
| COTAHUMA        | Belén          |     135 |            1 |
| MAX PAREDES     | Gran Poder     |     236 |            1 |
| SAN ANTONIO     | San Antonio    |     858 |            1 |
| SUR             | La Florida     |      43 |            1 |
| CENTRO          | San Jorge      |     287 |            1 |
| CENTRO          | El Rosario     |     108 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado       |    1718 |           15 |
| SAN ANTONIO     | Villa Copacabana      |     615 |            5 |
| SAN ANTONIO     | San Antonio           |     789 |            4 |
| MAX PAREDES     | Munaypata             |     356 |            3 |
| SUR             | Alto Obrajes          |     326 |            3 |
| SAN ANTONIO     | Pampahasi             |     515 |            3 |
| PERIFERICA      | Miraflores Alto       |     236 |            3 |
| COTAHUMA        | Sopocachi             |     635 |            3 |
| PERIFERICA      | Achachicala           |     365 |            2 |
| MAX PAREDES     | Chijini               |     238 |            2 |
| SAN ANTONIO     | Kupini                |     141 |            2 |
| PERIFERICA      | Villa El Carmen       |     240 |            2 |
| MAX PAREDES     | Pura Pura             |     298 |            2 |
| SUR             | Auquisamaña           |      43 |            2 |
| PERIFERICA      | Challapampa           |     171 |            2 |
| COTAHUMA        | Pasankeri             |     177 |            2 |
| SUR             | Ventilla              |      53 |            1 |
| COTAHUMA        | Villa Nuevo Potosí    |     329 |            1 |
| SUR             | Achumani              |     424 |            1 |
| MAX PAREDES     | Obispo Indaburo       |     131 |            1 |
| SUR             | Obrajes               |     466 |            1 |
| SAN ANTONIO     | Escobar Uría          |      58 |            1 |
| SUR             | Alto Següencoma       |     110 |            1 |
| COTAHUMA        | Inca Llojeta          |      58 |            1 |
| CENTRO          | San Sebastián         |     141 |            1 |
| CENTRO          | Miraflores Sur        |     409 |            1 |
| CENTRO          | Miraflores            |    1071 |            1 |
| COTAHUMA        | Tacagua               |     163 |            1 |
| PERIFERICA      | Villa Fátima          |     413 |            1 |
| SAN ANTONIO     | 24 de Junio           |       9 |            1 |
| COTAHUMA        | San Pedro             |     529 |            1 |
| PERIFERICA      | Kalajahuira           |      21 |            1 |
| MAX PAREDES     | 14 de Septiembre      |     143 |            1 |
| PERIFERICA      | Santa Rosa            |      50 |            1 |
| PERIFERICA      | 27 de Mayo            |      29 |            1 |
| MAX PAREDES     | Ciudadela Ferroviaria |      97 |            1 |
| PERIFERICA      | Agua de la Vida       |     121 |            1 |
| PERIFERICA      | Villa de la Cruz      |     132 |            1 |
| MAX PAREDES     | La Portada            |     179 |            1 |
| MAX PAREDES     | El Tejar              |     333 |            1 |
| MAX PAREDES     | Mariscal Santa Cruz   |     153 |            1 |
| MAX PAREDES     | Gran Poder            |     215 |            1 |
| PERIFERICA      | Alto Las Delicias     |      41 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| COTAHUMA        | Llojeta               |       2 |            1 |
| MAX PAREDES     | Ciudadela Ferroviaria |       3 |            1 |
| MAX PAREDES     | Munaypata             |      15 |            1 |

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