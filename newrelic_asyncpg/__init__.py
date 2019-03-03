from newrelic import agent
from newrelic.hooks.database_dbapi2 import (
    ConnectionFactory as DBAPI2ConnectionFactory,
)


class ConnectionFactory(DBAPI2ConnectionFactory):
    """"""

    @staticmethod
    async def __connection_wrapper__(wrapped, *args, **kwargs):
        return await wrapped

    def __call__(self, *args, **kwargs):
        agent.wrap_function_wrapper(kwargs['connection_class'], '_execute', self._execute_wrapper)
        return super(ConnectionFactory, self).__call__(*args, **kwargs)

    async def _execute_wrapper(self, wrapped, instance, args, kwargs):
        """"""

        db_host, db_port = instance._addr
        db_name = instance._params.database

        trace_kwargs = {
            "transaction": agent.current_transaction(),
            "dbapi2_module": self._nr_dbapi2_module,
            "host": db_host,
            "port_path_or_id": db_port,
            "database_name": db_name,
            "sql": args[0],
            "sql_parameters": args[1:]
        }

        with agent.DatabaseTrace(**trace_kwargs):
            return await wrapped(*args, **kwargs)


def instrument(module):
    """"""

    agent.register_database_client(
        module,
        database_product='Postgres',
        quoting_style='single+dollar',
        # explain_query='explain',
        # explain_stmts=('select', 'insert', 'update', 'delete'),
    )

    agent.wrap_object(module, 'connection.connect', ConnectionFactory, (module,))
    agent.wrap_object(module, 'connect', ConnectionFactory, (module,))
