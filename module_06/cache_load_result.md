### Сравнительная таблица результатов

Замеры произведены на следующем оборудовании:

    Процессор: Intel® Core™ i7-8650U CPU @ 1.90GHz × 8
    Объем оперативной памяти: 16Gb
    Диск: SSD
    OS: Ubuntu 22.04.2 LTS x64 

|                          | -d 60 -t 1 -c 1 | -d 60 -t 10 -c 10 | -d 60 -t 50 -c 50 |
|--------------------------|--------|---------|----------|
| Latency AVG              | 3.02ms | 34.69ms | 65.24ms  |
| Latency AVG (with cache) | 1.69ms | 15.78ms | 122.41ms |
| RPS AVG                  | 335.64 | 28.82   | 5.65     |
| RPS AVG (with cache)     | 626.26 | 63.67   | 7.50     |
| Requests                 | 20063  | 17295   | 23       |
| Requests (with cache)    | 37422  | 38202   | 24       |

### Результаты замеров работы сервиса без кеширования

```bash
~/arch/arch-com/arch-school/basic/module_06 (main)$ wrk -d 60 -t 1 -c 1 --latency -s ./get.lua http://localhost:8081/
Running 1m test @ http://localhost:8081/
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     3.02ms    1.12ms  27.22ms   95.68%
    Req/Sec   335.64     34.47   444.00     74.00%
  Latency Distribution
     50%    2.87ms
     75%    3.21ms
     90%    3.64ms
     99%    5.50ms
  20063 requests in 1.00m, 5.80MB read
Requests/sec:    334.18
Transfer/sec:     98.88KB
~/arch/arch-com/arch-school/basic/module_06 (main)$ wrk -d 60 -t 10 -c 10 --latency -s ./get.lua http://localhost:8081/
Running 1m test @ http://localhost:8081/
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    34.69ms    6.41ms  85.98ms   81.95%
    Req/Sec    28.82      5.00    40.00     74.68%
  Latency Distribution
     50%   33.90ms
     75%   36.83ms
     90%   41.08ms
     99%   59.72ms
  17295 requests in 1.00m, 4.89MB read
Requests/sec:    288.04
Transfer/sec:     83.40KB
~/arch/arch-com/arch-school/basic/module_06 (main)$ wrk -d 60 -t 50 -c 50 --latency -s ./get.lua http://localhost:8081/
Running 1m test @ http://localhost:8081/
  50 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    65.24ms   28.22ms  84.23ms   69.23%
    Req/Sec     5.65      5.07    10.00     56.52%
  Latency Distribution
     50%   82.84ms
     75%   83.45ms
     90%   84.11ms
     99%   84.23ms
  23 requests in 1.00m, 6.54KB read
  Socket errors: connect 0, read 4, write 0, timeout 10
  Non-2xx or 3xx responses: 1
Requests/sec:      0.38
Transfer/sec:     111.44B
```
### Результаты замеров работы сервиса с кешированием

```bash
~/arch/arch-com/arch-school/basic/module_06 (main)$ wrk -d 60 -t 1 -c 1 --latency -s ./get.lua http://localhost:8082/
Running 1m test @ http://localhost:8082/
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.69ms    1.26ms  25.19ms   97.80%
    Req/Sec   626.26     81.25   818.00     73.67%
  Latency Distribution
     50%    1.51ms
     75%    1.67ms
     90%    1.95ms
     99%    6.10ms
  37422 requests in 1.00m, 11.06MB read
Requests/sec:    623.37
Transfer/sec:    188.71KB
~/arch/arch-com/arch-school/basic/module_06 (main)$ wrk -d 60 -t 10 -c 10 --latency -s ./get.lua http://localhost:8082/
Running 1m test @ http://localhost:8082/
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    15.78ms    3.38ms  52.79ms   87.46%
    Req/Sec    63.67      7.06    90.00     89.72%
  Latency Distribution
     50%   15.33ms
     75%   16.79ms
     90%   18.46ms
     99%   32.41ms
  38202 requests in 1.00m, 10.89MB read
Requests/sec:    636.19
Transfer/sec:    185.64KB
~/arch/arch-com/arch-school/basic/module_06 (main)$ wrk -d 60 -t 50 -c 50 --latency -s ./get.lua http://localhost:8082/
Running 1m test @ http://localhost:8082/
  50 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   122.41ms   36.38ms 171.91ms   50.00%
    Req/Sec     7.50      2.55    10.00    100.00%
  Latency Distribution
     50%  128.74ms
     75%  160.53ms
     90%  171.63ms
     99%  171.91ms
  24 requests in 1.00m, 7.03KB read
Requests/sec:      0.40
Transfer/sec:     119.78B
```