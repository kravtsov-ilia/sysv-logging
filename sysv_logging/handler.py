import json
import logging
import sysv_ipc


class SysvIPCBaseHandler(logging.Handler):
    def __init__(
        self,
        *,
        queue_key: int,
        max_message_size: int,
        level: int = logging.INFO
    ):
        super().__init__(level)
        self.messages_queue = sysv_ipc.MessageQueue(
            key=queue_key,
            flags=sysv_ipc.IPC_CREAT,
            max_message_size=max_message_size,
        )

    def prepare_log_data(self, record: logging.LogRecord) -> dict:
        raise NotImplementedError()

    def emit(self, record: logging.LogRecord) -> None:
        self.acquire()
        try:
            msg = self.prepare_log_data(record)
            self.messages_queue.send(json.dumps(msg).encode('utf-8'))
        finally:
            self.release()
