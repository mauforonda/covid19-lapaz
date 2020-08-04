> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-08-03

## Confirmados en el último día

| Macrodistrito   | Zona               |   Total |   Último Día |
|-----------------|--------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado    |     842 |           60 |
| SAN ANTONIO     | San Antonio        |     437 |           28 |
| CENTRO          | Miraflores         |     663 |           27 |
| SUR             | Obrajes            |     251 |           22 |
| SAN ANTONIO     | Pampahasi          |     272 |           20 |
| SAN ANTONIO     | Villa Copacabana   |     344 |           19 |
| SUR             | Alto Obrajes       |     170 |           18 |
| COTAHUMA        | Sopocachi Alto     |     187 |           16 |
| COTAHUMA        | Villa Nuevo Potosí |     180 |           15 |
| COTAHUMA        | Sopocachi          |     392 |           14 |
| SUR             | Cota Cota          |     130 |           14 |
| MAX PAREDES     | Munaypata          |     237 |           13 |
| COTAHUMA        | Bello Horizonte    |      89 |           12 |
| MAX PAREDES     | Pura Pura          |     176 |           12 |
| PERIFERICA      | Achachicala        |     194 |           12 |
| PERIFERICA      | Vino Tinto         |     194 |           12 |
| PERIFERICA      | Zona Norte         |     141 |           11 |
| MAX PAREDES     | Villa Victoria     |     192 |           11 |
| SUR             | Achumani           |     214 |           11 |
| CENTRO          | San Jorge          |     157 |           10 |
| MAX PAREDES     | El Tejar           |     222 |           10 |
| COTAHUMA        | Tembladerani       |     184 |           10 |
| SAN ANTONIO     | Villa Armonía      |     113 |           10 |
| SUR             | Irpavi             |     216 |            9 |
| PERIFERICA      | La Mercéd          |      79 |            9 |
| COTAHUMA        | San Pedro Alto     |     181 |            9 |
| MAX PAREDES     | 14 de Septiembre   |      99 |            8 |
| COTAHUMA        | Tacagua            |      99 |            8 |
| PERIFERICA      | Villa Pabón        |      73 |            8 |
| PERIFERICA      | Villa Fátima       |     238 |            7 |
| COTAHUMA        | San Pedro          |     313 |            7 |
| CENTRO          | Miraflores Sur     |     249 |            7 |
| MAX PAREDES     | La Portada         |     114 |            7 |
| PERIFERICA      | Miraflores Alto    |     130 |            7 |
| SUR             | Meseta Achumani    |      15 |            7 |
| SUR             | Los Pinos          |     104 |            6 |
| PERIFERICA      | Villa El Carmen    |     145 |            6 |
| CENTRO          | Santa Barbara      |      96 |            6 |
| MAX PAREDES     | Gran Poder         |     128 |            6 |
| SUR             | Chasquipampa       |      73 |            6 |
| SUR             | Huantaqui          |      35 |            6 |
| MAX PAREDES     | Callampaya         |      89 |            5 |
| MAX PAREDES     | Obispo Indaburo    |      75 |            5 |
| MAX PAREDES     | Los Andes          |      58 |            5 |
| PERIFERICA      | Barrio Gráfico     |      57 |            4 |
| SAN ANTONIO     | Valle Hermoso      |      47 |            4 |
| COTAHUMA        | Obispo Bosque      |      33 |            4 |
| SAN ANTONIO     | Cuarto Centenario  |      42 |            4 |
| PERIFERICA      | San Juan           |      42 |            4 |
| PERIFERICA      | Villa de la Cruz   |      62 |            4 |

## Recuperados en el último día

| Macrodistrito   | Zona   | Total   | Último Día   |
|-----------------|--------|---------|--------------|

## Fallecidos en el último día

| Macrodistrito   | Zona   |   Total |   Último Día |
|-----------------|--------|---------|--------------|
| SAN ANTONIO     | Pacasa |       1 |            1 |

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