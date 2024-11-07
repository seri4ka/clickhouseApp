import clickhouse_connect

# Указываем параметры подключения
client = clickhouse_connect.get_client(host='localhost', port=8123)

# Выполняем тестовый запрос
result = client.query("SELECT 'Hello, ClickHouse!'").result_rows
print(result)
