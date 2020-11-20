a={'channel': {'id': 911972, 'name': 'Water Level Monitoring', 'latitude': '0.0', 'longitude': '0.0', 'field1': 'Water Level', 'created_at': '2019-11-15T13:04:22Z', 'updated_at': '2019-12-25T12:09:23Z', 'last_entry_id': 160}, 'feeds': [{'created_at': '2020-01-12T10:55:04Z', 'entry_id': 159, 'field1': '210'}, {'created_at': '2020-01-12T10:55:24Z', 'entry_id': 160, 'field1': '240'}]}
b=a['feeds'][1]['field1']
print(b)
