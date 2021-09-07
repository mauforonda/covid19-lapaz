> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2021-09-06

## Confirmados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| PERIFERICA      | Zona Norte      |     896 |            3 |
| COTAHUMA        | Bello Horizonte |     465 |            1 |
| COTAHUMA        | San Pedro       |    1455 |            1 |
| PERIFERICA      | Villa Pabón     |     413 |            1 |
| PERIFERICA      | Agua de la Vida |     364 |            1 |
| PERIFERICA      | Vino Tinto      |    1098 |            1 |
| SUR             | Achumani        |    1458 |            1 |
| CENTRO          | Central         |     904 |            1 |
| CENTRO          | Miraflores      |    3387 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                   |   Total |   Último Día |
|-----------------|------------------------|---------|--------------|
| SUR             | Obrajes                |    1463 |           10 |
| SUR             | Achumani               |    1242 |            9 |
| CENTRO          | Miraflores             |    2882 |            9 |
| COTAHUMA        | Sopocachi              |    1978 |            8 |
| SUR             | Següencoma Bajo        |     192 |            7 |
| SAN ANTONIO     | San Isidro             |     370 |            7 |
| NO IDENTIFICADO | No Identificado        |    4646 |            7 |
| SUR             | Alto Obrajes           |    1122 |            5 |
| SAN ANTONIO     | San Antonio            |    1918 |            5 |
| MAX PAREDES     | Munaypata              |     801 |            4 |
| CENTRO          | San Jorge              |     693 |            4 |
| SUR             | Chasquipampa           |     481 |            4 |
| SUR             | Calacoto               |     627 |            4 |
| SUR             | Cota Cota              |     605 |            4 |
| SAN ANTONIO     | Villa Copacabana       |    1586 |            4 |
| SAN ANTONIO     | Villa Armonía          |     670 |            4 |
| PERIFERICA      | Zona Norte             |     778 |            3 |
| CENTRO          | San Sebastián          |     394 |            3 |
| PERIFERICA      | Miraflores Alto        |     624 |            3 |
| SUR             | San Miguel             |     136 |            3 |
| COTAHUMA        | Bajo Llojeta           |     525 |            2 |
| SUR             | Ventilla               |     112 |            2 |
| SUR             | Lomas de Achumani      |      48 |            2 |
| COTAHUMA        | San Pedro Alto         |     804 |            2 |
| SUR             | Irpavi                 |    1047 |            2 |
| SAN ANTONIO     | Callapa                |      52 |            2 |
| SAN ANTONIO     | Pampahasi              |    1458 |            2 |
| MAX PAREDES     | Pura Pura              |     810 |            2 |
| SAN ANTONIO     | Escobar Uría           |     145 |            2 |
| COTAHUMA        | Llojeta                |     401 |            2 |
| MALLASA         | Mallasa                |     153 |            1 |
| MALLASA         | Mallasilla             |     119 |            1 |
| COTAHUMA        | Belén                  |     318 |            1 |
| CENTRO          | Santa Barbara          |     391 |            1 |
| SUR             | Bella Vista            |     619 |            1 |
| SUR             | Bolognia               |     226 |            1 |
| COTAHUMA        | Tacagua                |     345 |            1 |
| COTAHUMA        | Tembladerani           |     819 |            1 |
| COTAHUMA        | Obispo Bosque          |     111 |            1 |
| CENTRO          | Central                |     754 |            1 |
| SUR             | Kantutani Bajo Llojeta |     131 |            1 |
| CENTRO          | Miraflores Sur         |     936 |            1 |
| SUR             | Wilacota               |      22 |            1 |
| SUR             | Villa Apaña            |       4 |            1 |
| SUR             | Pedregal               |     132 |            1 |
| MAX PAREDES     | 14 de Septiembre       |     330 |            1 |
| MAX PAREDES     | Alto Pura Pura         |      72 |            1 |
| MAX PAREDES     | Gran Poder             |     474 |            1 |
| MAX PAREDES     | Villa Victoria         |     746 |            1 |
| MAX PAREDES     | Chamoco Chico          |     203 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| MAX PAREDES     | Alto Ciudadela  |       6 |            1 |
| SAN ANTONIO     | Villa Armonía   |      28 |            1 |
| NO IDENTIFICADO | No Identificado |     233 |            1 |

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