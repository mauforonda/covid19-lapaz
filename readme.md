> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-11-06

## Confirmados en el último día

| Macrodistrito   | Zona             |   Total |   Último Día |
|-----------------|------------------|---------|--------------|
| COTAHUMA        | Sopocachi        |     670 |            1 |
| COTAHUMA        | 8 de Diciembre   |      51 |            1 |
| MAX PAREDES     | Obispo Indaburo  |     143 |            1 |
| MAX PAREDES     | 14 de Septiembre |     155 |            1 |
| SAN ANTONIO     | Valle Hermoso    |      97 |            1 |
| SUR             | Cota Cota        |     216 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                          |   Total |   Último Día |
|-----------------|-------------------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado               |    1486 |           11 |
| CENTRO          | Miraflores                    |    1022 |            9 |
| SAN ANTONIO     | San Antonio                   |     735 |            6 |
| SAN ANTONIO     | Pampahasi                     |     478 |            5 |
| COTAHUMA        | Sopocachi                     |     601 |            5 |
| SUR             | Obrajes                       |     431 |            4 |
| COTAHUMA        | Villa Nuevo Potosí            |     307 |            3 |
| PERIFERICA      | Poqueni                       |      42 |            3 |
| COTAHUMA        | San Pedro Alto                |     287 |            3 |
| MAX PAREDES     | Chijini                       |     230 |            3 |
| CENTRO          | Santa Barbara                 |     148 |            3 |
| SAN ANTONIO     | San Isidro                    |     123 |            3 |
| COTAHUMA        | Bajo Llojeta                  |     146 |            3 |
| PERIFERICA      | Villa Fátima                  |     379 |            3 |
| CENTRO          | Miraflores Sur                |     381 |            2 |
| CENTRO          | San Jorge                     |     253 |            2 |
| SUR             | Irpavi                        |     335 |            2 |
| SAN ANTONIO     | Kupini                        |     125 |            2 |
| SAN ANTONIO     | Villa Salomé                  |     181 |            2 |
| SAN ANTONIO     | Valle Hermoso                 |      82 |            2 |
| COTAHUMA        | Sopocachi Alto                |     301 |            2 |
| COTAHUMA        | San Pedro                     |     501 |            2 |
| SAN ANTONIO     | Villa Copacabana              |     566 |            2 |
| PERIFERICA      | Zona Norte                    |     237 |            2 |
| MAX PAREDES     | Pura Pura                     |     279 |            2 |
| MAX PAREDES     | La Portada                    |     172 |            2 |
| MAX PAREDES     | Munaypata                     |     337 |            2 |
| MAX PAREDES     | Gran Poder                    |     196 |            1 |
| SUR             | Achumani                      |     391 |            1 |
| SUR             | Auquisamaña                   |      41 |            1 |
| SUR             | Virgen de Copacabana          |       6 |            1 |
| SUR             | Kantutani Bajo Llojeta        |      44 |            1 |
| SUR             | Bella Vista                   |     177 |            1 |
| SUR             | Los Pinos                     |     157 |            1 |
| SUR             | Alto Obrajes                  |     304 |            1 |
| MALLASA         | Jupapina                      |      27 |            1 |
| MAX PAREDES     | Alto Sagrado Corazón de Jesús |       3 |            1 |
| CENTRO          | San Sebastián                 |     134 |            1 |
| MAX PAREDES     | Los Andes                     |      94 |            1 |
| COTAHUMA        | Obispo Bosque                 |      56 |            1 |
| MAX PAREDES     | Mariscal Santa Cruz           |     145 |            1 |
| PERIFERICA      | Achachicala                   |     338 |            1 |
| SUR             | Los Rosales                   |      27 |            1 |
| SUR             | El Vergel                     |      15 |            1 |
| MAX PAREDES     | El Tejar                      |     325 |            1 |
| MAX PAREDES     | Villa Victoria                |     286 |            1 |
| SAN ANTONIO     | Cuarto Centenario             |      72 |            1 |
| SAN ANTONIO     | Ciudad del Niño               |       2 |            1 |
| COTAHUMA        | Bello Horizonte               |     158 |            1 |
| MAX PAREDES     | Alto Tejar                    |      57 |            1 |

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