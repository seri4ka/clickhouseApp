## Проект по разворачиванию ClickHouse и взаимодействию с БД через Python

### Этап 1: Настройка и запуск контейнера ClickHouse

1. Создали директорию для проекта:
    ```bash
    mkdir clickhouse_project && cd clickhouse_project
    ```

2.  Создали файл ```docker-compose.yaml``` со следующими настройками:
    ```yaml
    version: '3'
    services:
        clickhouse:
            image: yandex/clickhouse-server:latest
            container_name: clickhouse_server
            ports:
                - "8123:8123"  # HTTP порт ClickHouse
                - "9000:9000"  # Порт для взаимодействия с клиентами
            volumes:
                - ./clickhouse_data:/var/lib/clickhouse  # Для сохранения данных
            restart: always
    ```

3. Запустили контейнер командой:
    ```bash
    docker-compose up -d
    ```

4. Убедились, что контейнер работает:
    ```bash
    docker ps
    ```

5. Проверили подключение к ClickHouse через HTTP интерфейс:
    ```bash
    curl http://localhost:8123
    ```

**Результат**: успешное подключение — сервер вернул ```Ok```.


### Этап 2: Подключение к ClickHouse через Python

1. Установили библиотеку для работы с ClickHouse:
    ```bash
    pip install clickhouse-connect
    ```

2. Создали файл ```clickhouse_test.py``` и добавили следующий код для тестирования подключения:
    ```python
    import clickhouse_connect

    # Указываем параметры подключения
    client = clickhouse_connect.get_client(host='localhost', port=8123)

    # Выполняем тестовый запрос
    result = client.query("SELECT 'Hello, ClickHouse!'").result_rows
    print(result)
    ```

3. Запустили тестовый скрипт:
    ```bash
    python3 clickhouse_test.py
    ```

**Результат**: успешное подключение и вывод ```[(‘Hello, ClickHouse!’,)]```.