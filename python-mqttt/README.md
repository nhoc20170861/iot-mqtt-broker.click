### Tạo Virtual Envỉronments

```sh
python3 -m venv .venv
```

### Kích hoạt Virtual Environment

```sh
source .venv/bin/activate
```

### Kiểm tra môi trường ảo đã khởi chạy thành công

```sh
which python
```

### Tải pip

```sh
python3 -m pip install --upgrade pip
```

### Tải các gói phụ trợ

```
pip install -r requirements.txt
```

### Chạy demo python-client

Chương trình sẽ public "Hello world" vào chủ đề "test/websocket/topic" với chu kỳ 2s.
Trước khi chạy file **client.py** các bạn hãy sửa giá trị biến `broker` tương ứng với tên Domain của bạn.

```sh
python client.py
```

Kết quả:

```sh
(venv) anhquan@homeservern100:~/python-mqttt$ python client.py
...
Connecting to broker iot-mqtt-broker.click on port 443 via WebSocket
Message 1 published successfully
Connected to broker via WebSocket
Message 3 published successfully
Received message: test/websocket/topic -> Hello, MQTT over WebSocket!
Message 4 published successfully
```
