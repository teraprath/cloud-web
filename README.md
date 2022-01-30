# Personal Cloud
Simple Cloud Webpanel with Python (Flask) and SQLite3 using my CSS Framework [SimpleUI](https://github.com/teraprath/simple-ui) (BETA)

![](https://i.imgur.com/8GKGboO.png)

## Installation
### Required libraries

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all libaries.

```bash
pip install -r requirements.txt
```

## Start

### Development Server (Local)
1. Start **app.py** file
3. Connect to webserver via *localhost:**5500***

### Deployment on Linux Server (Public)
1. Start the WSGI-Server
```bash
chmod 777 start.sh
./start.sh
```
3. Connect to webserver on port *:**3000** (Changeable in **config.py**)
