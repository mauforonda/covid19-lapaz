> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-11-29

## Confirmados en el último día

| Macrodistrito   | Zona         |   Total |   Último Día |
|-----------------|--------------|---------|--------------|
| COTAHUMA        | Alto Tacagua |      49 |            1 |
| PERIFERICA      | Zona Norte   |     286 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                   |   Total |   Último Día |
|-----------------|------------------------|---------|--------------|
| SAN ANTONIO     | San Antonio            |     806 |            7 |
| CENTRO          | Miraflores             |    1087 |            4 |
| COTAHUMA        | Sopocachi Alto         |     329 |            3 |
| PERIFERICA      | Vino Tinto             |     374 |            3 |
| MAX PAREDES     | La Portada             |     184 |            2 |
| COTAHUMA        | Pasankeri              |     181 |            2 |
| COTAHUMA        | Bajo Llojeta           |     155 |            2 |
| PERIFERICA      | Miraflores Alto        |     241 |            2 |
| SUR             | Bella Vista            |     197 |            2 |
| SAN ANTONIO     | Valle de las Flores    |      25 |            2 |
| MAX PAREDES     | Pura Pura              |     302 |            2 |
| SUR             | Kantutani Bajo Llojeta |      51 |            2 |
| SAN ANTONIO     | Pampahasi              |     529 |            1 |
| SAN ANTONIO     | Villa Armonía          |     222 |            1 |
| COTAHUMA        | Sopocachi              |     638 |            1 |
| SAN ANTONIO     | Villa Copacabana       |     628 |            1 |
| SUR             | Los Rosales            |      29 |            1 |
| PERIFERICA      | La Mercéd              |     144 |            1 |
| PERIFERICA      | Chuquiaguillo          |      76 |            1 |
| SUR             | Achumani               |     428 |            1 |
| SUR             | Irpavi II              |      50 |            1 |
| SUR             | Alto Irpavi            |     116 |            1 |
| PERIFERICA      | Villa El Carmen        |     243 |            1 |
| SUR             | Ovejuyo                |      46 |            1 |
| SUR             | Ventilla               |      55 |            1 |
| SUR             | Gramadal               |      15 |            1 |
| SUR             | Bolognia               |      72 |            1 |
| CENTRO          | Central                |     260 |            1 |
| CENTRO          | Miraflores Sur         |     413 |            1 |
| PERIFERICA      | Villa Fátima           |     417 |            1 |
| PERIFERICA      | Poqueni                |      50 |            1 |
| PERIFERICA      | Barrio Gráfico         |     113 |            1 |
| PERIFERICA      | San Juan Lazareto      |      90 |            1 |
| COTAHUMA        | Las Lomas              |      37 |            1 |
| COTAHUMA        | Inca Llojeta           |      61 |            1 |
| COTAHUMA        | San Pedro              |     534 |            1 |
| COTAHUMA        | Belén                  |     116 |            1 |
| COTAHUMA        | San Pedro Alto         |     313 |            1 |
| MAX PAREDES     | Alto Pura Pura         |      25 |            1 |
| MAX PAREDES     | Los Andes              |     105 |            1 |
| MAX PAREDES     | Chijini                |     240 |            1 |
| MAX PAREDES     | Gran Poder             |     216 |            1 |
| MAX PAREDES     | Mariscal Santa Cruz    |     156 |            1 |
| MAX PAREDES     | El Tejar               |     339 |            1 |
| MAX PAREDES     | Villa Victoria         |     303 |            1 |
| MAX PAREDES     | Munaypata              |     361 |            1 |
| MAX PAREDES     | Alto Tejar             |      64 |            1 |
| PERIFERICA      | Zona Norte             |     263 |            1 |
| PERIFERICA      | Villa Pabón            |     132 |            1 |
| PERIFERICA      | Achachicala            |     372 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona         |   Total |   Último Día |
|-----------------|--------------|---------|--------------|
| MAX PAREDES     | Munaypata    |      16 |            1 |
| PERIFERICA      | Las Delicias |       1 |            1 |

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