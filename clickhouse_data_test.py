import clickhouse_connect

# Подключаемся к ClickHouse
client = clickhouse_connect.get_client(host='localhost', port=8123)

# Выполняем запрос для проверки вставленных данных
result = client.query("SELECT * FROM transactions").result_rows

print("Содержимое таблицы 'transactions':")
for string in result:
    print(string)
