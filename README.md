# Crowdedness Monitor

SE 101 Project

## Structure

    .
    ├── backend
    │   ├── app/:           source code of the app
    │   ├── config/:        configurations
    │   ├── migrations/
    │   ├── requirements.txt:`pip install -r requirements.txt`
    │   ├── var/            database for testing/developing purpose. you need to create one for yourself.
    │   │   └── test.db
    │   └── venv            `venv/Scripts/activate`
    ├── embedded/
    │   ├── .env:           put your environment variables here
    │   ├── bootstrap.sh:   this will be put in crontab to run after system boots
    │   ├── log:            log generated by the program
    │   ├── read_packet.py: module that reads packet generated by tshark
    │   ├── report.py:      report data to the backend server
    │   ├── run.sh:         this will be put in crontab to run every five minutes
    │   ├── setup.sh:       this should be run once only
    ├── frontend/
    └── README.md

## Install

### Embedded
`cd ./embedded/ && ./setup.sh`

* `bootstrap.sh` will be run every time the system boots.
* `run.sh` will be run every 5 minutes (a fixed interval).
* `.env` stores relevant variables.
* `log` stores logs.

### Backend
```
apt update && apt install libmysqlclient-dev
cd backend
python3 -m venv venv
venv/Scripts/activate
pip3 install -r requirements.txt
touch var/test.db
flask db upgrade
flask run
```
Recommended IDE: PyCharm Professional

### Frontend
[Frontend](https://git.uwaterloo.ca/STAZZ/crowdedness-monitor/tree/master/frontend)

## License
