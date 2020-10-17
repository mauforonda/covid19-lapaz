> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-10-16

## Confirmados en el último día

| Macrodistrito   | Zona             |   Total |   Último Día |
|-----------------|------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado  |    2245 |            3 |
| COTAHUMA        | Bello Horizonte  |     180 |            1 |
| PERIFERICA      | Miraflores Alto  |     253 |            1 |
| PERIFERICA      | Huaychani        |      16 |            1 |
| SAN ANTONIO     | Villa Copacabana |     652 |            1 |
| SAN ANTONIO     | San Antonio      |     845 |            1 |
| SAN ANTONIO     | Pampahasi        |     550 |            1 |
| SUR             | Alto Achumani    |      33 |            1 |
| SUR             | Alto Següencoma  |     117 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                |   Total |   Último Día |
|-----------------|---------------------|---------|--------------|
| CENTRO          | Miraflores          |     960 |            4 |
| COTAHUMA        | San Pedro           |     478 |            4 |
| NO IDENTIFICADO | No Identificado     |    1361 |            3 |
| SAN ANTONIO     | San Antonio         |     671 |            3 |
| SAN ANTONIO     | Pampahasi           |     442 |            3 |
| SUR             | Los Pinos           |     145 |            2 |
| PERIFERICA      | Vino Tinto          |     312 |            2 |
| MAX PAREDES     | La Portada          |     163 |            2 |
| SAN ANTONIO     | Kupini              |     115 |            2 |
| MAX PAREDES     | Mariscal Santa Cruz |     139 |            2 |
| SAN ANTONIO     | Valle Hermoso       |      76 |            2 |
| SUR             | Alto Obrajes        |     282 |            2 |
| SAN ANTONIO     | Villa Copacabana    |     528 |            1 |
| SUR             | La Florida          |      36 |            1 |
| SUR             | San Miguel          |      48 |            1 |
| SUR             | Achumani            |     369 |            1 |
| SUR             | Següencoma Bajo     |      72 |            1 |
| MALLASA         | Mallasilla          |      30 |            1 |
| SUR             | Irpavi              |     316 |            1 |
| COTAHUMA        | Sopocachi           |     568 |            1 |
| PERIFERICA      | La Mercéd           |     127 |            1 |
| COTAHUMA        | Sopocachi Bajo      |      58 |            1 |
| MAX PAREDES     | Alto Villa Victoria |      19 |            1 |
| MAX PAREDES     | Callampaya          |     120 |            1 |
| MAX PAREDES     | El Tejar            |     309 |            1 |
| MAX PAREDES     | Gran Poder          |     179 |            1 |
| MAX PAREDES     | Obispo Indaburo     |     113 |            1 |
| MAX PAREDES     | Pura Pura           |     259 |            1 |
| COTAHUMA        | San Pedro Alto      |     257 |            1 |
| COTAHUMA        | Tacagua             |     144 |            1 |
| COTAHUMA        | Villa Nuevo Potosí  |     279 |            1 |
| COTAHUMA        | Bajo Llojeta        |     129 |            1 |
| COTAHUMA        | Pasankeri           |     148 |            1 |
| PERIFERICA      | 27 de Mayo          |      24 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| MAX PAREDES     | Los Andes       |       3 |            1 |
| PERIFERICA      | Agua de la Vida |       2 |            1 |
| PERIFERICA      | San Juan        |       3 |            1 |
| SUR             | Alto Achumani   |       1 |            1 |

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