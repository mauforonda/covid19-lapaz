> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2021-09-20

## Confirmados en el último día

| Macrodistrito   | Zona   | Total   | Último Día   |
|-----------------|--------|---------|--------------|

## Recuperados en el último día

| Macrodistrito   | Zona                   |   Total |   Último Día |
|-----------------|------------------------|---------|--------------|
| COTAHUMA        | Sopocachi              |    2064 |           11 |
| CENTRO          | Miraflores             |    3016 |            9 |
| SAN ANTONIO     | Villa Copacabana       |    1645 |            7 |
| SUR             | Obrajes                |    1539 |            7 |
| SAN ANTONIO     | Pampahasi              |    1530 |            6 |
| PERIFERICA      | Achachicala            |     950 |            5 |
| PERIFERICA      | Villa Fátima           |    1075 |            4 |
| SAN ANTONIO     | San Antonio            |    1995 |            4 |
| MAX PAREDES     | Chijini                |     564 |            4 |
| SUR             | Huayllani              |      19 |            4 |
| MAX PAREDES     | Gran Poder             |     495 |            4 |
| MAX PAREDES     | Pura Pura              |     839 |            4 |
| PERIFERICA      | Vino Tinto             |     964 |            3 |
| PERIFERICA      | Villa El Carmen        |     640 |            3 |
| SUR             | Calacoto               |     658 |            3 |
| SUR             | Chasquipampa           |     507 |            3 |
| SUR             | Bella Vista            |     658 |            3 |
| COTAHUMA        | Villa Nuevo Potosí     |     859 |            3 |
| SUR             | Alto Obrajes           |    1174 |            3 |
| CENTRO          | Central                |     789 |            3 |
| PERIFERICA      | Zona Norte             |     804 |            3 |
| SUR             | Bolognia               |     238 |            2 |
| SUR             | Cota Cota              |     622 |            2 |
| CENTRO          | El Rosario             |     353 |            2 |
| PERIFERICA      | Miraflores Alto        |     641 |            2 |
| CENTRO          | Miraflores Sur         |     959 |            2 |
| COTAHUMA        | Sopocachi Alto         |     932 |            2 |
| PERIFERICA      | Agua de la Vida        |     323 |            2 |
| MAX PAREDES     | Los Andes              |     266 |            2 |
| COTAHUMA        | San Pedro Alto         |     837 |            2 |
| COTAHUMA        | San Pedro              |    1276 |            2 |
| MAX PAREDES     | Alto Tejar             |     178 |            2 |
| MAX PAREDES     | La Portada             |     457 |            2 |
| COTAHUMA        | Cotahuma               |     148 |            2 |
| PERIFERICA      | Villa 18 de Mayo       |      67 |            2 |
| CENTRO          | San Sebastián          |     417 |            1 |
| CENTRO          | Santa Barbara          |     404 |            1 |
| COTAHUMA        | Bajo Llojeta           |     565 |            1 |
| SUR             | Alto Següencoma        |     399 |            1 |
| COTAHUMA        | Pasankeri              |     360 |            1 |
| COTAHUMA        | Alto Tacagua           |      97 |            1 |
| COTAHUMA        | Belén                  |     335 |            1 |
| SUR             | Caliri                 |      55 |            1 |
| COTAHUMA        | Alpacoma               |      31 |            1 |
| SUR             | Kantutani Bajo Llojeta |     136 |            1 |
| SUR             | Alto Calacoto          |      64 |            1 |
| SUR             | Jardines del Sur       |      97 |            1 |
| SUR             | Los Rosales            |     113 |            1 |
| SUR             | Achumani               |    1300 |            1 |
| PERIFERICA      | Villa Pabón            |     370 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona               |   Total |   Último Día |
|-----------------|--------------------|---------|--------------|
| COTAHUMA        | Villa Nuevo Potosí |      23 |            1 |

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