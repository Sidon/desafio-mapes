######################################
``Mapes Teste desenvolvedor Django``
######################################


Description
*************
O teste consiste em implementar um caso de uso.
Exigências: django, jquery, ajax, bootstrap, postgres, teste unitário.

A

:Date: **18/01/2019**
:Author: **Sidon Duarte**

TL;DR
*******
A aplicação foi hospedada no `Heroku <http://www.heroku.com>`_ . Para testá-la, `https://sdn-mapes.herokuapp.com/>`.

Work Environment:
******************

    +-------------------+---------------------------+------------+
    | Resource          | Description               | Version    |
    +===================+===========================+============+
    | Computer          | Desktop 8 GB Memory       | I5 G5      |
    +-------------------+---------------------------+------------+
    | Operating System  | Ubuntu  LTS               | 18.04      |
    +-------------------+---------------------------+------------+
    | Editor/IDE        | Pycharm                   | 2018.3.2   |
    +-------------------+---------------------------+------------+
    | venv              | Conda (Miniconda)         | 4.3.14     |
    +-------------------+---------------------------+------------+
    | Devel Platform    + Django/Python             |    3.7     |
    +-------------------+---------------------------+------------+
    | CI                | CircleCI                  | 2017-08    |
    +-------------------+---------------------------+------------+
    | Coverage          | Codecov                   |            |
    +-------------------+---------------------------+------------+
    | Django            | Main framework            | 2.1        |
    +-------------------+---------------------------+------------+
    | DRF               | dajano-rest-fw            |  3.9       |
    +-------------------+---------------------------+------------+


Para Instalar localmente
************************
Apos clonar o repoditorio, instale os requirements, e rode o sistema

```
git clone
cd
python manager.py runserver
```



Comandos Curl
***********************************

API Root:
============
::

    $ curl https://sdn-mapes.herokuapp.com/api/
    {"api/processos":"https://tikal-challenge.herokuapp.com/api/api/processos/",
    "api/logging":"https://tikal-challenge.herokuapp.com/api/api/logging/"}


Listar consultas
=========================
::

    curl -H 'Accept: application/json; indent=4' -u admin:master.21 curl https://sdn-mapes.herokuapp.com/api/consultas/
    {
        "count": 13,
        "next": "https://tikal-challenge.herokuapp.com/api/api/processos/?page=2",
        "previous": null,
        "results": [
            {
                "user": 1,
                "numero_processo": "00000000000000000001",
                "dados_processo": "Amet porttitor eget dolor morbi. Magna fringilla urna porttitor rhoncus. In vitae turpis massa sed elementum.",
                "links": {
                    "self": "https://tikal-challenge.herokuapp.com/api/api/processos/32/"
                }
            },

