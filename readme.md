> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-10-10

## Confirmados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |    2246 |           11 |
| MAX PAREDES     | El Tejar        |     358 |            2 |
| MAX PAREDES     | Munaypata       |     385 |            2 |
| COTAHUMA        | Tacagua         |     172 |            1 |
| COTAHUMA        | San Pedro       |     559 |            1 |
| COTAHUMA        | San Pedro Alto  |     327 |            1 |
| MAX PAREDES     | Villa Victoria  |     327 |            1 |
| SAN ANTONIO     | San Antonio     |     844 |            1 |
| SAN ANTONIO     | Pampahasi       |     548 |            1 |
| SAN ANTONIO     | Villa Armonía   |     242 |            1 |
| SUR             | Los Pinos       |     179 |            1 |
| SUR             | Irpavi          |     378 |            1 |
| CENTRO          | San Jorge       |     282 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                          |   Total |   Último Día |
|-----------------|-------------------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado               |    1348 |           40 |
| SUR             | Irpavi                        |     308 |            3 |
| COTAHUMA        | Belén                         |      97 |            2 |
| PERIFERICA      | La Mercéd                     |     123 |            2 |
| PERIFERICA      | Achachicala                   |     299 |            2 |
| MAX PAREDES     | Pura Pura                     |     255 |            2 |
| SAN ANTONIO     | San Antonio                   |     654 |            2 |
| COTAHUMA        | San Pedro                     |     464 |            2 |
| COTAHUMA        | Tacagua                       |     142 |            2 |
| MALLASA         | Amor de Dios                  |      15 |            1 |
| SUR             | Bolognia                      |      60 |            1 |
| SUR             | Gramadal                      |      12 |            1 |
| SAN ANTONIO     | Cuarto Centenario             |      70 |            1 |
| SUR             | Ovejuyo                       |      32 |            1 |
| SUR             | Alto Achumani                 |      26 |            1 |
| SUR             | Achumani                      |     362 |            1 |
| SUR             | Alto Irpavi                   |      92 |            1 |
| CENTRO          | Santa Barbara                 |     137 |            1 |
| SUR             | Cota Cota                     |     182 |            1 |
| SAN ANTONIO     | Kupini                        |     111 |            1 |
| CENTRO          | San Jorge                     |     229 |            1 |
| SUR             | Chasquipampa                  |     118 |            1 |
| COTAHUMA        | Sopocachi Alto                |     269 |            1 |
| SAN ANTONIO     | Pampahasi                     |     428 |            1 |
| COTAHUMA        | Pasankeri                     |     146 |            1 |
| PERIFERICA      | Miraflores Alto               |     201 |            1 |
| PERIFERICA      | Las Nieves                    |      12 |            1 |
| PERIFERICA      | Zona Norte                    |     212 |            1 |
| PERIFERICA      | Vino Tinto                    |     294 |            1 |
| MAX PAREDES     | Alto Mcal. Santa Cruz         |      69 |            1 |
| MAX PAREDES     | Alto Tejar                    |      50 |            1 |
| MAX PAREDES     | Villa Victoria                |     262 |            1 |
| MAX PAREDES     | Gran Poder                    |     175 |            1 |
| MAX PAREDES     | Alto Sagrado Corazón de Jesús |       2 |            1 |
| COTAHUMA        | Bello Horizonte               |     147 |            1 |
| COTAHUMA        | Villa Nuevo Potosí            |     274 |            1 |
| COTAHUMA        | Llojeta                       |      77 |            1 |
| PERIFERICA      | Villa El Carmen               |     198 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona        |   Total |   Último Día |
|-----------------|-------------|---------|--------------|
| COTAHUMA        | Sopocachi   |      16 |            1 |
| MAX PAREDES     | El Tejar    |      11 |            1 |
| PERIFERICA      | Challapampa |       4 |            1 |
| SUR             | Bella Vista |       8 |            1 |
| CENTRO          | San Jorge   |       3 |            1 |
| CENTRO          | Central     |      10 |            1 |

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