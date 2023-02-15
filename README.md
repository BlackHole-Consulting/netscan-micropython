# netscan-micropython

A micropython port scanner


#### Scan ip range with a port list

```Python

import netscan

netscan.portscan("192.168.1.1-192.168.1.255", [22,88,80,443,445,8080,9200])

```
