- How many samples Prometheus is ingesting per second averaged over one minute and produce a result?
```
rate(prometheus_tsdb_head_samples_appended_total[1m])
```

- Rate of network bytes received each minute
```
rate(node_network_receive_bytes_total[1m])
```

- Rate of hitting the url `localhost:8001` where python app is running
```
rate(hello_world_total[1m])
```

- Rate of exceptions occurrence in the python app
```
rate(hello_world_exceptions_total[1m])
```

- Exceptions out of all the requests
```
rate(hello_world_exceptions_total[1m])/rate(hello_world_total[1m])
```

- how many seconds it is since the last request?
```
time() - hello_world_last_time_seconds
```
