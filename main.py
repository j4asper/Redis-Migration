import redis

# Old redis database credentials, set password to None, if the databsae doesn't have a password
OLD_CONNECTION_STRING = "redis://xxx.xxx.xxx.xxx:xxxxx"
OLD_PASSWORD = "SuperSecret"

# Connection to old database to extract all keys and values
with redis.from_url(url = OLD_CONNECTION_STRING, password = OLD_PASSWORD, decode_responses=True, retry_on_timeout=True) as db_con:
    keys = db_con.keys()
    values = db_con.mget(keys)
    db_dict = dict(zip(keys, values))


# New redis database credentials, set password to None, if the databsae doesn't have a password
NEW_CONNECTION_STRING = "redis://xxx.xxx.xxx.xxx:xxxx"
NEW_PASSWORD = "SuperSecret1"

# Connection to new database to insert the data from the old database
with redis.from_url(url = NEW_CONNECTION_STRING, password = NEW_PASSWORD, decode_responses=True, retry_on_timeout=True) as new_db_con:
    new_db_con.mset(db_dict)


# Print something to indicate that it's finished
print("db migrated")