from couch_wrapper.couchdb_connector import CouchDBConnector

DEFAULT_MAX_QUEUE_SIZE = 100


class CouchDBConnectorBulk:
    def __init__(self, max_queue_size=DEFAULT_MAX_QUEUE_SIZE, **kwargs):
        self.couchdb_connector = CouchDBConnector(**kwargs)
        self.get_database_name = self.couchdb_connector.get_database_name

        self.documents_queue = []
        self.max_queue_size = max_queue_size

    def save(self, document):
        self.documents_queue.append(document)

        queue_size = len(self.documents_queue)

        if queue_size == self.max_queue_size:
            self._save_queued_documents()

    def _save_queued_documents(self):
        self.couchdb_connector.save_bulk(self.documents_queue)
        self.documents_queue = []

    def __del__(self):
        queue_size = len(self.documents_queue)
        if queue_size > 0:
            self._save_queued_documents()