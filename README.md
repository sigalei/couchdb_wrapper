# couchdb_wrapper
A wrapper for interaction with a CouchDB instance.


Testing.

```
virutalenv env
source env/bin/activate
pip install -e .
pytest
```

# TODO

- `CouchDBConnector`: A wrapper to operate couchdb using python

- `CouchDBConnectorBulk`: A wrapper of `CouchDBConnector` that accumulates
items and save it as a bulk.
