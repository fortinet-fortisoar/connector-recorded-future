from connectors.core.connector import Connector, ConnectorError, get_logger
from .operations import operations, test_connection
logger = get_logger('recorded-future')


class RecordedFuture(Connector):
    def execute(self, config, operation, params, **kwargs):
        action = operations.get(operation)
        return action(config, params)

    def check_health(self, config):
        try:
            logger.info('executing check health')
            return test_connection(config)
        except Exception as exp:
            logger.exception(str(exp))
            raise ConnectorError(str(exp))
