import logging
from time import strftime, gmtime

TIME_ZONE = strftime("%z", gmtime())


class SysVLogFilter(logging.Filter):
    def filter(self, record):
        custom_logs_params = (
            ('request_id', '--'),
            ('trace_id', '--'),
            ('span_id', '--'),
            ('parent_id', '--'),
            ('payload', None),
            ('client_host', '--'),
            ('client_port', '--'),
            ('timezone', TIME_ZONE),
        )
        for custom_param, default_value in custom_logs_params:
            if not hasattr(record, custom_param):
                setattr(record, custom_param, default_value)
        return True
