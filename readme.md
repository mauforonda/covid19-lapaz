> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-12-01

## Confirmados en el último día

| Macrodistrito   | Zona           |   Total |   Último Día |
|-----------------|----------------|---------|--------------|
| COTAHUMA        | San Pedro Alto |     338 |            2 |
| COTAHUMA        | Alto Tacagua   |      50 |            1 |
| MAX PAREDES     | La Portada     |     206 |            1 |
| SUR             | Obrajes        |     498 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                          |   Total |   Último Día |
|-----------------|-------------------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado               |    1773 |           33 |
| SUR             | Achumani                      |     439 |           10 |
| CENTRO          | Miraflores                    |    1098 |           10 |
| SUR             | Irpavi                        |     365 |            9 |
| SUR             | Calacoto                      |     224 |            8 |
| COTAHUMA        | Sopocachi Alto                |     336 |            7 |
| SAN ANTONIO     | San Antonio                   |     813 |            6 |
| PERIFERICA      | Villa El Carmen               |     249 |            5 |
| SAN ANTONIO     | Pampahasi                     |     538 |            5 |
| SUR             | Següencoma Bajo               |      81 |            4 |
| MAX PAREDES     | Obispo Indaburo               |     139 |            4 |
| PERIFERICA      | Miraflores Alto               |     245 |            4 |
| COTAHUMA        | San Pedro                     |     538 |            4 |
| COTAHUMA        | San Pedro Alto                |     316 |            3 |
| COTAHUMA        | Bello Horizonte               |     178 |            3 |
| COTAHUMA        | Bajo Llojeta                  |     159 |            3 |
| PERIFERICA      | Agua de la Vida Norte         |      22 |            3 |
| COTAHUMA        | Belén                         |     120 |            3 |
| MAX PAREDES     | Chijini                       |     248 |            3 |
| SUR             | Bella Vista                   |     200 |            3 |
| SUR             | Los Pinos                     |     167 |            3 |
| PERIFERICA      | Achachicala                   |     377 |            3 |
| SUR             | Obrajes                       |     471 |            3 |
| SAN ANTONIO     | Villa Copacabana              |     633 |            2 |
| SUR             | Cota Cota                     |     212 |            2 |
| SAN ANTONIO     | Villa Salomé                  |     195 |            2 |
| SAN ANTONIO     | Villa Armonía                 |     225 |            2 |
| SUR             | Chasquipampa                  |     150 |            2 |
| SUR             | La Florida                    |      41 |            2 |
| SUR             | Alto Següencoma               |     112 |            2 |
| SUR             | Alto Obrajes                  |     330 |            2 |
| COTAHUMA        | Sopocachi                     |     640 |            2 |
| COTAHUMA        | Villa Nuevo Potosí            |     338 |            2 |
| PERIFERICA      | San Juan Lazareto             |      92 |            2 |
| PERIFERICA      | Vino Tinto                    |     377 |            2 |
| PERIFERICA      | Villa de la Cruz              |     138 |            2 |
| PERIFERICA      | Santiago de Lacaya            |       7 |            1 |
| SUR             | Alto Irpavi                   |     118 |            1 |
| MAX PAREDES     | Pura Pura                     |     304 |            1 |
| SUR             | Koani                         |      29 |            1 |
| SUR             | Ovejuyo                       |      49 |            1 |
| MAX PAREDES     | Ciudadela Ferroviaria         |      99 |            1 |
| COTAHUMA        | Alto Tacagua                  |      44 |            1 |
| COTAHUMA        | Alpacoma                      |      13 |            1 |
| COTAHUMA        | Tembladerani                  |     338 |            1 |
| MAX PAREDES     | Alto Sagrado Corazón de Jesús |       4 |            1 |
| COTAHUMA        | Obispo Bosque                 |      65 |            1 |
| CENTRO          | San Jorge                     |     274 |            1 |
| CENTRO          | Central                       |     261 |            1 |
| CENTRO          | Miraflores Sur                |     415 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| PERIFERICA      | Villa El Carmen |      15 |            1 |

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