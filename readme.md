> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-10-23

## Confirmados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| SAN ANTONIO     | Villa Copacabana      |     655 |            2 |
| NO IDENTIFICADO | No Identificado       |    2252 |            2 |
| COTAHUMA        | Sopocachi             |     664 |            1 |
| COTAHUMA        | Llojeta               |     107 |            1 |
| MAX PAREDES     | Ciudadela Ferroviaria |     101 |            1 |
| MAX PAREDES     | Munaypata             |     389 |            1 |
| PERIFERICA      | Alto Las Delicias     |      48 |            1 |
| PERIFERICA      | Santa Rosa de Tiji    |      22 |            1 |
| PERIFERICA      | Barrio Gráfico        |     124 |            1 |
| PERIFERICA      | Villa El Carmen       |     267 |            1 |
| SAN ANTONIO     | San Antonio           |     846 |            1 |
| SUR             | Condores Lakota       |       5 |            1 |
| SUR             | Los Pinos             |     180 |            1 |
| SUR             | Ventilla              |      57 |            1 |
| SUR             | Obrajes               |     494 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                      |   Total |   Último Día |
|-----------------|---------------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado           |    1405 |           13 |
| CENTRO          | Miraflores                |     985 |            5 |
| SUR             | Obrajes                   |     406 |            4 |
| SUR             | Chasquipampa              |     126 |            2 |
| COTAHUMA        | Belén                     |     103 |            2 |
| COTAHUMA        | San Pedro Alto            |     265 |            2 |
| MAX PAREDES     | Alto Munaypata Cusicancha |      47 |            2 |
| CENTRO          | Miraflores Sur            |     366 |            1 |
| SAN ANTONIO     | Villa Armonía             |     198 |            1 |
| SUR             | Achumani                  |     377 |            1 |
| SUR             | Auquisamaña               |      37 |            1 |
| SUR             | Ovejuyo                   |      36 |            1 |
| SUR             | Virgen de Copacabana      |       5 |            1 |
| SUR             | Ventilla                  |      46 |            1 |
| SUR             | Kupillani                 |       9 |            1 |
| CENTRO          | San Jorge                 |     237 |            1 |
| SAN ANTONIO     | Villa Salomé              |     174 |            1 |
| SUR             | Bella Vista               |     163 |            1 |
| MALLASA         | Jupapina                  |      26 |            1 |
| CENTRO          | San Sebastián             |     128 |            1 |
| SAN ANTONIO     | San Isidro                |     112 |            1 |
| COTAHUMA        | Sopocachi                 |     580 |            1 |
| PERIFERICA      | La Mercéd                 |     130 |            1 |
| COTAHUMA        | Pasankeri                 |     151 |            1 |
| COTAHUMA        | Llojeta                   |      82 |            1 |
| COTAHUMA        | Tembladerani              |     295 |            1 |
| COTAHUMA        | Bello Horizonte           |     152 |            1 |
| MAX PAREDES     | Ciudadela Ferroviaria     |      85 |            1 |
| MAX PAREDES     | Chamoco Chico             |      81 |            1 |
| MAX PAREDES     | La Portada                |     168 |            1 |
| MAX PAREDES     | Alto Tejar                |      51 |            1 |
| MAX PAREDES     | Alto Mcal. Santa Cruz     |      73 |            1 |
| PERIFERICA      | Villa 18 de Mayo          |      32 |            1 |
| PERIFERICA      | Vino Tinto                |     323 |            1 |
| PERIFERICA      | Achachicala               |     324 |            1 |
| PERIFERICA      | San Juan                  |      73 |            1 |
| PERIFERICA      | Miraflores Alto           |     205 |            1 |
| PERIFERICA      | Alto Las Delicias         |      38 |            1 |
| PERIFERICA      | Villa El Carmen           |     213 |            1 |
| PERIFERICA      | Villa Fátima              |     371 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona       |   Total |   Último Día |
|-----------------|------------|---------|--------------|
| PERIFERICA      | Vino Tinto |      15 |            1 |

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