# NewRelic extensions / asyncpg


## Install

```
pip install newrelic_asyncpg
```


1) Append in your newrelic.ini

```ini
[import-hook:asyncpg]
enabled = true
execute = newrelic_asyncpg:instrument
```

