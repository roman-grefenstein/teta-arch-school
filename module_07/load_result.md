### Сравнительная таблица результатов

Замеры произведены на следующем оборудовании:

    Процессор: Intel® Core™ i7-8650U CPU @ 1.90GHz × 8
    Объем оперативной памяти: 16Gb
    Диск: SSD
    OS: Ubuntu 22.04.2 LTS x64 

| Параметр                 | -d 60 -t 1 -c 1 | -d 60 -t 10 -c 10 | -d 60 -t 50 -c 50 |
|--------------------------|----------|--------|---------|
| Latency AVG              | 1.23ms   | 9.42ms | 47.26ms |
| Latency AVG (with cache) | 762.28us | 6.23ms | 36.15ms |
| RPS AVG                  | 817.05   | 106.47 | 21.20   |
| RPS AVG (with cache)     | 1.30k    | 160.96 | 27.85   |
| Requests                 | 48810    | 63638  | 63559   |
| Requests (with cache)    | 77813    | 96325  | 100144  |

### Сравнение результатов с MariaDB

#### Без кеширования

| БД      | Параметр                 | -d 60 -t 1 -c 1 | -d 60 -t 10 -c 10 | -d 60 -t 50 -c 50 |
|---------|--------------------------|----------|---------|----------|
| MongoDB | Latency AVG              | 1.23ms   | 9.42ms  | 47.26ms  |
| MariaDB | Latency AVG              | 3.02ms   | 34.69ms | 65.24ms  |
| MongoDB | RPS AVG                  | 817.05   | 106.47  | 21.20    |
| MariaDB | RPS AVG                  | 335.64   | 28.82   | 5.65     |
| MongoDB | Requests                 | 48810    | 63638   | 63559    |
| MariaDB | Requests                 | 20063    | 17295   | 23       |

#### С кешированием

| БД      | Параметр                 | -d 60 -t 1 -c 1 | -d 60 -t 10 -c 10 | -d 60 -t 50 -c 50 |
|---------|--------------------------|----------|---------|----------|
| MongoDB | Latency AVG (with cache) | 762.28us | 6.23ms  | 36.15ms  |
| MariaDB | Latency AVG (with cache) | 1.69ms   | 15.78ms | 122.41ms |
| MongoDB | RPS AVG (with cache)     | 1.30k    | 160.96  | 27.85    |
| MariaDB | RPS AVG (with cache)     | 626.26   | 63.67   | 7.50     |
| MongoDB | Requests (with cache)    | 77813    | 96325   | 100144   |
| MariaDB | Requests (with cache)    | 37422    | 38202   | 24       |

#### Итог

Для данной задачи MongoDB выглядит более предпочтительнее, чем MariaDB, как в чистом виде, так и в связке с Redis.

### Результаты замеров работы сервиса без кеширования

```bash
~/arch/teta-arch-school/module_07 (main)$ wrk -d 60 -t 1 -c 1 --latency -s ./get.lua http://localhost:8081/
Running 1m test @ http://localhost:8081/
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.23ms  464.07us  29.98ms   98.92%
    Req/Sec   817.05     39.12     0.92k    81.50%
  Latency Distribution
     50%    1.18ms
     75%    1.26ms
     90%    1.38ms
     99%    1.71ms
  48810 requests in 1.00m, 12.66MB read
Requests/sec:    813.05
Transfer/sec:    215.97KB
~/arch/teta-arch-school/module_07 (main)$ wrk -d 60 -t 10 -c 10 --latency -s ./get.lua http://localhost:8081/
Running 1m test @ http://localhost:8081/
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     9.42ms    1.82ms  30.49ms   72.50%
    Req/Sec   106.47      8.42   131.00     80.57%
  Latency Distribution
     50%    9.34ms
     75%   10.43ms
     90%   11.59ms
     99%   14.46ms
  63638 requests in 1.00m, 17.07MB read
Requests/sec:   1059.91
Transfer/sec:    291.17KB
~/arch/teta-arch-school/module_07 (main)$ wrk -d 60 -t 50 -c 50 --latency -s ./get.lua http://localhost:8081/
Running 1m test @ http://localhost:8081/
  50 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    47.26ms   10.29ms 141.61ms   75.96%
    Req/Sec    21.20      4.93    40.00     74.33%
  Latency Distribution
     50%   46.04ms
     75%   51.89ms
     90%   58.65ms
     99%   83.33ms
  63559 requests in 1.00m, 17.13MB read
Requests/sec:   1058.34
Transfer/sec:    292.11KB
```
### Результаты замеров работы сервиса с кешированием

```bash
~/arch/teta-arch-school/module_07 (main)$ wrk -d 60 -t 1 -c 1 --latency -s ./get.lua http://localhost:8082/
Running 1m test @ http://localhost:8082/
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   762.28us  257.71us  22.39ms   99.27%
    Req/Sec     1.30k    41.58     1.42k    78.70%
  Latency Distribution
     50%  758.00us
     75%  797.00us
     90%  849.00us
     99%    0.99ms
  77813 requests in 1.00m, 21.00MB read
Requests/sec:   1294.73
Transfer/sec:    357.82KB
~/arch/teta-arch-school/module_07 (main)$ wrk -d 60 -t 10 -c 10 --latency -s ./get.lua http://localhost:8082/
Running 1m test @ http://localhost:8082/
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     6.23ms    1.33ms  28.70ms   84.06%
    Req/Sec   160.96     21.13   333.00     82.07%
  Latency Distribution
     50%    6.12ms
     75%    6.70ms
     90%    7.31ms
     99%   11.55ms
  96325 requests in 1.00m, 26.09MB read
Requests/sec:   1603.78
Transfer/sec:    444.79KB
~/arch/teta-arch-school/module_07 (main)$ wrk -d 60 -t 60 -c 60 --latency -s ./get.lua http://localhost:8082/
Running 1m test @ http://localhost:8082/
  60 threads and 60 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    36.15ms    9.56ms 236.33ms   84.90%
    Req/Sec    27.85      6.11   120.00     62.16%
  Latency Distribution
     50%   34.81ms
     75%   40.12ms
     90%   45.55ms
     99%   61.16ms
  100144 requests in 1.00m, 27.02MB read
Requests/sec:   1667.06
Transfer/sec:    460.61KB
```