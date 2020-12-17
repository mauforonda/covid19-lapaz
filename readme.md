> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-12-16

## Confirmados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado       |    2302 |           10 |
| SAN ANTONIO     | San Antonio           |     876 |            8 |
| COTAHUMA        | Sopocachi             |     696 |            8 |
| CENTRO          | Miraflores            |    1192 |            7 |
| SAN ANTONIO     | Villa Copacabana      |     670 |            4 |
| COTAHUMA        | San Pedro             |     586 |            4 |
| MAX PAREDES     | Chijini               |     270 |            3 |
| MAX PAREDES     | Gran Poder            |     241 |            3 |
| SAN ANTONIO     | Villa Armonía         |     257 |            3 |
| CENTRO          | Miraflores Sur        |     447 |            3 |
| MAX PAREDES     | Alto Mcal. Santa Cruz |      96 |            2 |
| CENTRO          | San Jorge             |     290 |            2 |
| MAX PAREDES     | Mariscal Santa Cruz   |     170 |            2 |
| COTAHUMA        | Villa Nuevo Potosí    |     366 |            2 |
| MAX PAREDES     | Villa Antofagasta     |      14 |            2 |
| MAX PAREDES     | Pura Pura             |     333 |            2 |
| SUR             | Achumani              |     471 |            2 |
| SUR             | Koani                 |      31 |            1 |
| SUR             | El Vergel             |      19 |            1 |
| SUR             | Cota Cota             |     224 |            1 |
| SUR             | Los Pinos             |     183 |            1 |
| SUR             | Huantaqui             |      70 |            1 |
| CENTRO          | El Rosario            |     113 |            1 |
| SUR             | Chasquipampa          |     163 |            1 |
| SUR             | Obrajes               |     503 |            1 |
| SUR             | Alto Obrajes          |     350 |            1 |
| SAN ANTONIO     | San Isidro            |     140 |            1 |
| MALLASA         | Mallasa               |      44 |            1 |
| CENTRO          | San Sebastián         |     158 |            1 |
| CENTRO          | Central               |     290 |            1 |
| SUR             | Bolognia              |      76 |            1 |
| COTAHUMA        | Tembladerani          |     362 |            1 |
| SAN ANTONIO     | Cuarto Centenario     |      84 |            1 |
| PERIFERICA      | Villa de la Cruz      |     151 |            1 |
| COTAHUMA        | Tacagua               |     179 |            1 |
| COTAHUMA        | Bello Horizonte       |     187 |            1 |
| COTAHUMA        | Belén                 |     137 |            1 |
| COTAHUMA        | San Pedro Alto        |     343 |            1 |
| MAX PAREDES     | 14 de Septiembre      |     161 |            1 |
| MAX PAREDES     | Villa Victoria        |     340 |            1 |
| MAX PAREDES     | La Portada            |     213 |            1 |
| PERIFERICA      | Vino Tinto            |     418 |            1 |
| SAN ANTONIO     | Pampahasi             |     577 |            1 |
| PERIFERICA      | Zona Norte            |     291 |            1 |
| PERIFERICA      | Las Nieves            |      14 |            1 |
| PERIFERICA      | Barrio Gráfico        |     129 |            1 |
| PERIFERICA      | Villa Fátima          |     447 |            1 |
| COTAHUMA        | Pasankeri             |     191 |            1 |
| PERIFERICA      | La Mercéd             |     159 |            1 |
| COTAHUMA        | Bajo Llojeta          |     169 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |    1899 |           34 |
| COTAHUMA        | Sopocachi Alto  |     342 |            1 |
| COTAHUMA        | Tembladerani    |     341 |            1 |
| COTAHUMA        | San Pedro       |     550 |            1 |
| MAX PAREDES     | Pura Pura       |     312 |            1 |
| PERIFERICA      | Miraflores Alto |     246 |            1 |
| SAN ANTONIO     | Villa Armonía   |     232 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| MAX PAREDES     | Ciudadela Ferroviaria |       4 |            1 |
| NO IDENTIFICADO | No Identificado       |     164 |            1 |

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