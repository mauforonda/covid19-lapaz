> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-11-26

## Confirmados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| SUR             | Alto Obrajes    |     344 |            2 |
| COTAHUMA        | San Pedro       |     569 |            1 |
| COTAHUMA        | Bello Horizonte |     183 |            1 |
| SAN ANTONIO     | Villa Armonía   |     248 |            1 |
| CENTRO          | Miraflores Sur  |     437 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado       |    1723 |            5 |
| SAN ANTONIO     | Villa Copacabana      |     618 |            3 |
| MAX PAREDES     | La Portada            |     181 |            2 |
| CENTRO          | Miraflores            |    1073 |            2 |
| SUR             | Calacoto              |     216 |            2 |
| SUR             | Irpavi                |     355 |            2 |
| PERIFERICA      | Achachicala           |     367 |            2 |
| PERIFERICA      | Zona Norte            |     260 |            2 |
| PERIFERICA      | Vino Tinto            |     369 |            2 |
| PERIFERICA      | Villa de la Cruz      |     134 |            2 |
| MAX PAREDES     | Munaypata             |     358 |            2 |
| COTAHUMA        | Sopocachi             |     637 |            2 |
| MAX PAREDES     | 14 de Septiembre      |     145 |            2 |
| COTAHUMA        | San Pedro Alto        |     309 |            2 |
| SUR             | Virgen de Copacabana  |       8 |            1 |
| SAN ANTONIO     | Villa Litoral         |      28 |            1 |
| SUR             | Los Pinos             |     164 |            1 |
| COTAHUMA        | Tacagua               |     164 |            1 |
| COTAHUMA        | Villa Nuevo Potosí    |     330 |            1 |
| SUR             | Ovejuyo               |      45 |            1 |
| SUR             | Wilacota              |       9 |            1 |
| SUR             | Chasquipampa          |     147 |            1 |
| SAN ANTONIO     | San Isidro            |     131 |            1 |
| SUR             | Ventilla              |      54 |            1 |
| SUR             | Obrajes               |     467 |            1 |
| SUR             | Alto Obrajes          |     327 |            1 |
| CENTRO          | San Sebastián         |     142 |            1 |
| CENTRO          | San Jorge             |     272 |            1 |
| COTAHUMA        | Tembladerani          |     333 |            1 |
| SAN ANTONIO     | Villa Armonía         |     217 |            1 |
| SAN ANTONIO     | Kupini                |     142 |            1 |
| MAX PAREDES     | Chamoco Chico         |      91 |            1 |
| PERIFERICA      | San Juan Lazareto     |      89 |            1 |
| MAX PAREDES     | Alto Mcal. Santa Cruz |      83 |            1 |
| PERIFERICA      | Plan Autopista        |      27 |            1 |
| MAX PAREDES     | Pura Pura             |     299 |            1 |
| MAX PAREDES     | Ciudadela Ferroviaria |      98 |            1 |
| PERIFERICA      | Villa Pabón           |     129 |            1 |
| COTAHUMA        | Bello Horizonte       |     173 |            1 |
| PERIFERICA      | Alto Las Delicias     |      42 |            1 |
| SAN ANTONIO     | Villa Salomé          |     192 |            1 |
| PERIFERICA      | Santa Rosa            |      51 |            1 |
| COTAHUMA        | Pasankeri             |     178 |            1 |
| PERIFERICA      | Villa Fátima          |     414 |            1 |
| COTAHUMA        | San Pedro             |     530 |            1 |
| SAN ANTONIO     | San Antonio           |     790 |            1 |
| SAN ANTONIO     | Pampahasi             |     516 |            1 |
| PERIFERICA      | Barrio Gráfico        |     112 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |     163 |            1 |

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