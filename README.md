# A Flask backend example

## How to run?

### Docker

```
docker build -t example-be-image .
docker run -p 0.0.0.0:3002:5000 --name example-be-container -t example-be-image
```

Server address:
Docker: http://127.0.0.1:3002
Docker Toolbox: http://192.168.99.100:3002

### No Docker

1. Create new mysql database and modify `./foo/config.py`.

```
CREATE DATABASE `example` CHARACTER SET utf8mb4;
```

2. Install dependencies.

```
pip install -r requirements.txt
```

3. Init database.

```
python initdb.py
```

4. Run server.

```
python exampleserver.py
```

Server address: http://127.0.0.1:5000
