> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-10-17

## Confirmados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| MAX PAREDES     | Los Andes       |     109 |            1 |
| PERIFERICA      | Rosasani        |      35 |            1 |
| PERIFERICA      | Miraflores Alto |     254 |            1 |
| PERIFERICA      | Villa Fátima    |     429 |            1 |
| SUR             | San Miguel      |      55 |            1 |
| CENTRO          | El Rosario      |     105 |            1 |
| CENTRO          | Miraflores      |    1146 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona               |   Total |   Último Día |
|-----------------|--------------------|---------|--------------|
| COTAHUMA        | San Pedro          |     481 |            3 |
| SAN ANTONIO     | San Antonio        |     674 |            3 |
| SAN ANTONIO     | Villa Copacabana   |     531 |            3 |
| CENTRO          | Miraflores Sur     |     359 |            2 |
| COTAHUMA        | Sopocachi Alto     |     275 |            2 |
| PERIFERICA      | Chuquiaguillo      |      70 |            1 |
| MALLASA         | Amor de Dios       |      16 |            1 |
| SUR             | Obrajes            |     389 |            1 |
| SUR             | Achumani           |     370 |            1 |
| SUR             | Irpavi II          |      41 |            1 |
| SAN ANTONIO     | Villa Armonía      |     193 |            1 |
| SAN ANTONIO     | Villa Salomé       |     169 |            1 |
| SAN ANTONIO     | Pampahasi          |     443 |            1 |
| SAN ANTONIO     | Valle Hermoso      |      77 |            1 |
| COTAHUMA        | Sopocachi          |     569 |            1 |
| PERIFERICA      | Challapampa        |     152 |            1 |
| PERIFERICA      | Villa Pabón        |     113 |            1 |
| PERIFERICA      | Zona Norte         |     219 |            1 |
| MAX PAREDES     | Munaypata          |     316 |            1 |
| MAX PAREDES     | Chamoco Chico      |      79 |            1 |
| COTAHUMA        | Villa Nuevo Potosí |     280 |            1 |
| COTAHUMA        | Cotahuma           |      66 |            1 |
| COTAHUMA        | Bajo Llojeta       |     130 |            1 |
| COTAHUMA        | Llojeta            |      80 |            1 |
| COTAHUMA        | Pasankeri          |     149 |            1 |
| PERIFERICA      | La Mercéd          |     128 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| CENTRO          | Santa Barbara   |       8 |            2 |
| COTAHUMA        | San Pedro Alto  |       8 |            1 |
| MAX PAREDES     | Obispo Indaburo |       3 |            1 |
| PERIFERICA      | Chuquiaguillo   |       5 |            1 |
| SUR             | Achumani        |      12 |            1 |
| MALLASA         | Jupapina        |       1 |            1 |

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