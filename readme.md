> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-09-22

## Confirmados en el último día

| Macrodistrito   | Zona                      |   Total |   Último Día |
|-----------------|---------------------------|---------|--------------|
| MAX PAREDES     | Los Andes                 |     103 |            3 |
| SUR             | Achumani                  |     448 |            3 |
| SAN ANTONIO     | San Antonio               |     836 |            3 |
| PERIFERICA      | Villa El Carmen           |     263 |            2 |
| SUR             | Bella Vista               |     209 |            2 |
| SAN ANTONIO     | Kupini                    |     149 |            2 |
| PERIFERICA      | Challapampa               |     181 |            2 |
| CENTRO          | Miraflores                |    1136 |            2 |
| COTAHUMA        | Las Lomas                 |      41 |            2 |
| COTAHUMA        | San Pedro Alto            |     322 |            2 |
| MAX PAREDES     | Alto Pura Pura            |      27 |            1 |
| SAN ANTONIO     | Pampahasi                 |     544 |            1 |
| SUR             | Bolognia                  |      72 |            1 |
| SUR             | Obrajes                   |     492 |            1 |
| SUR             | Koani                     |      30 |            1 |
| COTAHUMA        | Villa Nuevo Potosí        |     355 |            1 |
| SUR             | Alto Irpavi               |     115 |            1 |
| SUR             | Los Pinos                 |     176 |            1 |
| SUR             | Los Rosales               |      31 |            1 |
| SAN ANTONIO     | San Isidro                |     133 |            1 |
| COTAHUMA        | Alto Tacagua              |      46 |            1 |
| SAN ANTONIO     | Villa Salomé              |     203 |            1 |
| COTAHUMA        | Belén                     |     134 |            1 |
| MAX PAREDES     | Chijini                   |     252 |            1 |
| PERIFERICA      | Chuquiaguillo             |      80 |            1 |
| PERIFERICA      | Huaychani                 |      15 |            1 |
| PERIFERICA      | Villa Fátima              |     426 |            1 |
| COTAHUMA        | Pasankeri                 |     178 |            1 |
| PERIFERICA      | Achachicala               |     385 |            1 |
| PERIFERICA      | Agua de la Vida           |     123 |            1 |
| PERIFERICA      | Zona Norte                |     262 |            1 |
| MAX PAREDES     | Alto Munaypata Cusicancha |      51 |            1 |
| MAX PAREDES     | Munaypata                 |     376 |            1 |
| MAX PAREDES     | La Portada                |     194 |            1 |
| MAX PAREDES     | Villa Victoria            |     326 |            1 |
| COTAHUMA        | Sopocachi                 |     658 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |    1358 |          149 |
| PERIFERICA      | Zona Norte      |     196 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |     161 |            6 |

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