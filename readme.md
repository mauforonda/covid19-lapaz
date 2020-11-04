> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-11-03

## Confirmados en el último día

| Macrodistrito   | Zona             |   Total |   Último Día |
|-----------------|------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado  |    2274 |            2 |
| MAX PAREDES     | 14 de Septiembre |     154 |            1 |
| SAN ANTONIO     | Pampahasi        |     554 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                |   Total |   Último Día |
|-----------------|---------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado     |    1457 |           10 |
| PERIFERICA      | Vino Tinto          |     341 |            5 |
| COTAHUMA        | Sopocachi Alto      |     297 |            5 |
| SAN ANTONIO     | Pampahasi           |     463 |            4 |
| SAN ANTONIO     | Villa Copacabana    |     562 |            4 |
| SUR             | Irpavi              |     330 |            3 |
| SUR             | Calacoto            |     191 |            3 |
| CENTRO          | Central             |     237 |            3 |
| COTAHUMA        | Villa Nuevo Potosí  |     303 |            3 |
| MAX PAREDES     | Chijini             |     222 |            3 |
| MAX PAREDES     | Munaypata           |     334 |            3 |
| SUR             | Alto Següencoma     |      99 |            2 |
| SAN ANTONIO     | San Isidro          |     119 |            2 |
| SUR             | Alto Irpavi         |     103 |            2 |
| PERIFERICA      | Villa El Carmen     |     225 |            2 |
| PERIFERICA      | Las Delicias        |     112 |            2 |
| SUR             | Auquisamaña         |      39 |            2 |
| SUR             | Bella Vista         |     175 |            2 |
| PERIFERICA      | La Mercéd           |     135 |            2 |
| MAX PAREDES     | Pura Pura           |     275 |            2 |
| COTAHUMA        | San Pedro Alto      |     280 |            2 |
| COTAHUMA        | San Pedro           |     498 |            2 |
| MAX PAREDES     | Alto Villa Victoria |      22 |            2 |
| SUR             | Los Pinos           |     155 |            1 |
| SUR             | Alto Obrajes        |     297 |            1 |
| MALLASA         | Mallasilla          |      32 |            1 |
| MALLASA         | Chiaraque           |       1 |            1 |
| SUR             | Achumani            |     388 |            1 |
| CENTRO          | San Sebastián       |     133 |            1 |
| CENTRO          | San Jorge           |     247 |            1 |
| CENTRO          | Miraflores Sur      |     373 |            1 |
| CENTRO          | Miraflores          |    1007 |            1 |
| SUR             | Huantaqui           |      64 |            1 |
| COTAHUMA        | Tembladerani        |     301 |            1 |
| SUR             | Meseta Achumani     |      30 |            1 |
| MAX PAREDES     | El Tejar            |     322 |            1 |
| COTAHUMA        | Alto Tacagua        |      42 |            1 |
| COTAHUMA        | Bello Horizonte     |     156 |            1 |
| COTAHUMA        | Belén               |     110 |            1 |
| MAX PAREDES     | Chamoco Chico       |      83 |            1 |
| MAX PAREDES     | Los Andes           |      93 |            1 |
| MAX PAREDES     | Gran Poder          |     194 |            1 |
| MAX PAREDES     | La Portada          |     170 |            1 |
| SAN ANTONIO     | Villa Armonía       |     201 |            1 |
| COTAHUMA        | Llojeta             |      89 |            1 |
| PERIFERICA      | Achachicala         |     336 |            1 |
| PERIFERICA      | Poqueni             |      39 |            1 |
| PERIFERICA      | Urkupiña            |      12 |            1 |
| COTAHUMA        | Pasankeri           |     162 |            1 |
| SAN ANTONIO     | Kupini              |     123 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona         |   Total |   Último Día |
|-----------------|--------------|---------|--------------|
| SUR             | Chasquipampa |       5 |            1 |

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