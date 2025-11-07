from pymongo import MongoClient

client = MongoClient('mongodb://Automation_team:mrU67pNQ2P6CEwwwEr123@kero-mdb-prod-1.rushsports.io:27017/')
print(client)

uuid_to_find = 5204021735
print(uuid_to_find)

db_list = client.list_database_names()
# print(db_list)

for db_name in db_list:
    # Skip system databases
    if db_name in ['admin', 'local', 'config']:
        continue
    print(f"Searching database: {db_name}")
    db = client[db_name]
