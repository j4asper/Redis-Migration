import redis

OLD_CONNECTION_STRING = "redis://xxx.xxx.xxx.xxx:xxxxx"
OLD_PASSWORD = "SuperSecret"

with redis.from_url(url = OLD_CONNECTION_STRING, password = OLD_PASSWORD, decode_responses=True, retry_on_timeout=True) as db_con:
    keys = db_con.keys()
    values = db_con.mget(keys)
    db_dict = dict(zip(keys, values))


NEW_CONNECTION_STRING = "redis://xxx.xxx.xxx.xxx:xxxx"
NEW_PASSWORD = "SuperSecret1"

with redis.from_url(url = NEW_CONNECTION_STRING, password = NEW_PASSWORD, decode_responses=True, retry_on_timeout=True) as new_db_con:
    new_db_con.mset(db_dict)

print("db migrated")