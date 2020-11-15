> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-11-14

## Confirmados en el último día

| Macrodistrito   | Zona             |   Total |   Último Día |
|-----------------|------------------|---------|--------------|
| PERIFERICA      | Vino Tinto       |     413 |            2 |
| SAN ANTONIO     | Pampahasi        |     563 |            2 |
| COTAHUMA        | Sopocachi        |     672 |            1 |
| COTAHUMA        | Tacagua          |     175 |            1 |
| COTAHUMA        | San Pedro        |     566 |            1 |
| MAX PAREDES     | Pura Pura        |     323 |            1 |
| MAX PAREDES     | Obispo Indaburo  |     145 |            1 |
| MAX PAREDES     | 14 de Septiembre |     157 |            1 |
| MAX PAREDES     | El Tejar         |     358 |            1 |
| SUR             | Cota Cota        |     218 |            1 |
| SUR             | La Florida       |      42 |            1 |
| SUR             | Irpavi           |     383 |            1 |
| SUR             | Calacoto         |     230 |            1 |
| SUR             | Alto Irpavi      |     118 |            1 |
| SUR             | Achumani         |     466 |            1 |
| SUR             | Ventilla         |      58 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                     |   Total |   Último Día |
|-----------------|--------------------------|---------|--------------|
| COTAHUMA        | Sopocachi                |     618 |            3 |
| PERIFERICA      | Achachicala              |     350 |            3 |
| PERIFERICA      | Villa Fátima             |     396 |            3 |
| SUR             | Bella Vista              |     186 |            3 |
| MAX PAREDES     | Villa Victoria           |     294 |            2 |
| COTAHUMA        | Villa Nuevo Potosí       |     322 |            2 |
| SUR             | Achumani                 |     409 |            2 |
| COTAHUMA        | Llojeta                  |      95 |            2 |
| SAN ANTONIO     | Villa Copacabana         |     585 |            2 |
| CENTRO          | Central                  |     248 |            1 |
| CENTRO          | San Jorge                |     262 |            1 |
| CENTRO          | Santa Barbara            |     157 |            1 |
| SUR             | Alto Obrajes             |     314 |            1 |
| SUR             | Alto Següencoma          |     105 |            1 |
| SUR             | Irpavi                   |     339 |            1 |
| SUR             | Caliri                   |      15 |            1 |
| SUR             | Obrajes                  |     446 |            1 |
| SUR             | Virgen de Copacabana     |       7 |            1 |
| SUR             | Calacoto                 |     203 |            1 |
| SUR             | Huantaqui                |      66 |            1 |
| PERIFERICA      | Chuquiaguillo            |      74 |            1 |
| SUR             | Cota Cota                |     203 |            1 |
| SAN ANTONIO     | San Antonio              |     764 |            1 |
| COTAHUMA        | Sopocachi Alto           |     309 |            1 |
| PERIFERICA      | Villa El Carmen          |     232 |            1 |
| PERIFERICA      | Miraflores Alto          |     227 |            1 |
| PERIFERICA      | San Juan                 |      79 |            1 |
| PERIFERICA      | Agua de la Vida          |     115 |            1 |
| PERIFERICA      | Challapampa              |     166 |            1 |
| MAX PAREDES     | Munaypata                |     347 |            1 |
| MAX PAREDES     | El Tejar                 |     328 |            1 |
| MAX PAREDES     | 14 de Septiembre         |     142 |            1 |
| MAX PAREDES     | Sagrado Corazón de Jesús |      23 |            1 |
| MAX PAREDES     | Pura Pura                |     292 |            1 |
| CENTRO          | Miraflores               |    1055 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona                |   Total |   Último Día |
|-----------------|---------------------|---------|--------------|
| MAX PAREDES     | Mariscal Santa Cruz |       3 |            1 |
| SUR             | Los Pinos           |       8 |            1 |
| NO IDENTIFICADO | No Identificado     |     163 |            1 |

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