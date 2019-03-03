# NewRelic extensions / asyncpg

**Unofficial** extension for the NewRelic Python Agent for support `asyncpg` database adapter

## Features

* Timing of database queries
* Capturing SQL for the database query
* Capturing a stack trace for long database queries

**not supported:**

* Capturing trace for database query operations `commit` `rollback`
* Capturing explain plans for slow database queries


## Installation

```bash
pip install newrelic_asyncpg
```

Append in your newrelic.ini

```ini
[import-hook:asyncpg]
enabled = true
execute = newrelic_asyncpg:instrument
```

