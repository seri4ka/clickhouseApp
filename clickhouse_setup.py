import clickhouse_connect
from datetime import date

# Подключаемся к ClickHouse
client = clickhouse_connect.get_client(host='localhost', port=8123)

# Создаем таблицу, если она не существует
client.command(
    '''
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id UInt32,
            user_id UInt32,
            amount Float32,
            transaction_date Date
        ) ENGINE = MergeTree()
        ORDER BY transaction_id
    '''
)

print("Таблица 'transactions' создана.")

# Добавляем тестовые данные
client.command(
    '''
        INSERT INTO transactions (transaction_id, user_id, amount, transaction_date) VALUES
        (1, 101, 50.5, '2024-11-07'),
        (2, 102, 25.0, '2024-11-07'),
        (3, 103, 100.0, '2024-11-07')
    '''
)

print("Тестовые данные добавлены.")
