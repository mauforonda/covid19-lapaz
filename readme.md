> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-11-24

## Confirmados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |    2259 |            3 |

## Recuperados en el último día

| Macrodistrito   | Zona               |   Total |   Último Día |
|-----------------|--------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado    |    1703 |          106 |
| SAN ANTONIO     | San Antonio        |     785 |            6 |
| SUR             | Achumani           |     423 |            5 |
| MAX PAREDES     | Obispo Indaburo    |     130 |            4 |
| SAN ANTONIO     | Pampahasi          |     512 |            4 |
| PERIFERICA      | Achachicala        |     363 |            4 |
| COTAHUMA        | Pasankeri          |     175 |            3 |
| COTAHUMA        | Sopocachi Alto     |     325 |            2 |
| CENTRO          | Miraflores         |    1070 |            2 |
| SUR             | Obrajes            |     465 |            2 |
| SUR             | Chasquipampa       |     146 |            2 |
| SUR             | Calacoto           |     214 |            2 |
| SUR             | Irpavi             |     353 |            2 |
| SAN ANTONIO     | Villa Salomé       |     191 |            2 |
| SAN ANTONIO     | Villa Copacabana   |     610 |            2 |
| COTAHUMA        | Inca Llojeta       |      57 |            2 |
| PERIFERICA      | Poqueni            |      47 |            2 |
| PERIFERICA      | Vino Tinto         |     367 |            2 |
| MAX PAREDES     | Munaypata          |     353 |            2 |
| COTAHUMA        | San Pedro          |     528 |            2 |
| PERIFERICA      | Miraflores Alto    |     233 |            1 |
| MAX PAREDES     | Villa Victoria     |     300 |            1 |
| CENTRO          | Miraflores Sur     |     408 |            1 |
| CENTRO          | El Rosario         |     100 |            1 |
| SUR             | Bella Vista        |     195 |            1 |
| COTAHUMA        | Villa Nuevo Potosí |     328 |            1 |
| SUR             | Ventilla           |      52 |            1 |
| SUR             | Alto Calacoto      |      19 |            1 |
| MAX PAREDES     | Gran Poder         |     214 |            1 |
| SUR             | Los Pinos          |     163 |            1 |
| MAX PAREDES     | Huacataqui         |      27 |            1 |
| PERIFERICA      | Las Delicias       |     116 |            1 |
| SUR             | Cota Cota          |     207 |            1 |
| SAN ANTONIO     | Kupini             |     139 |            1 |
| PERIFERICA      | Plan Autopista     |      26 |            1 |
| SAN ANTONIO     | Pacasa             |      45 |            1 |
| PERIFERICA      | La Mercéd          |     142 |            1 |
| PERIFERICA      | Villa Fátima       |     412 |            1 |
| PERIFERICA      | Barrio Gráfico     |     111 |            1 |
| COTAHUMA        | Sopocachi          |     632 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |     164 |            2 |

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