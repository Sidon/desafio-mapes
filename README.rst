######################################
``Mapes Teste desenvolvedor Django``
######################################


Descrição
***********
O teste consiste em implementar um caso de uso.
Exigências: django, jquery, ajax, bootstrap, postgres, teste unitário.


:Date: **18/01/2019**
:Author: **Sidon Duarte**

TL;DR
*******
A aplicação foi hospedada no `Heroku <http://www.heroku.com>`_ . Para testá-la, `https://sdn-mapes.herokuapp.com/>`.

Ambiente de desenvolvimento:
****************************

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
1) Clone o repositório e navegue para o diretorio

.. code-block::

    $ git clone https://github.com/Sidon/desafio-mapes.git
    $ cd desafio-mapes

2) Instale os pacotes necessários

.. code-block::

    pip install -r requirements.txt

3) Execute os testes do sistema (criacao do BD):

.. code-block::

    $ python manage.py test

3) Crie o banco de dados com os dados iniciais

.. code-block::

    $ python manage.py initialdata


4) Execute a aplicação:

.. code-block::

    $ python manage.py runserver

5) Acesse a pagina principal

.. code-block::

    http://127.0.0.1:8000/


Acessando a API via Curl
***********************************

API Root:
============
::

    $ curl https://sdn-mapes.herokuapp.com/api/
    {"api/processos":"https://tikal-challenge.herokuapp.com/api/api/processos/",
    "api/logging":"https://tikal-challenge.herokuapp.com/api/api/logging/"}


Listar todas consultas
=========================
::


    curl -H 'Accept: application/json; indent=4' -u admin:master.21 https://sdn-mapes.herokuapp.com/api/consultas/
    [
        {
            "numero_guia_consulta": 1,
            "cod_medico": 123,
            "nome_medico": "João da Silva",
            "data_consulta": "2017-01-02",
            "valor_consulta": "90.00",
            "valor_exames": 23.0,
            "total_da_consulta": 113.0,
            "exames": [
                {
                    "id": 216,
                    "exame": "Exame Laboratorial 2222",
                    "valor": 15.0
                },
                {
                    "id": 227,
                    "exame": "Exame Laboratorial 3333",
                    "valor": 8.0
                }
            ],
            "links": {
                "self": "https://sdn-mapes.herokuapp.com/api/consultas/301/"
            }
        },

        .....

    ]
Listar somente as 2 primeiras consultas
=======================================
::

    curl -H 'Accept:application/json;indent=4' -u admin:master.21 https://sdn-mapes.herokuapp.com/api/consultas/?limit=2
    [
        {
            "numero_guia_consulta": 1,
            "cod_medico": 123,
            "nome_medico": "João da Silva",
            "data_consulta": "2017-01-02",
            "valor_consulta": "90.00",
            "valor_exames": 23.0,
            "total_da_consulta": 113.0,
            "exames": [
                {
                    "id": 216,
                    "exame": "Exame Laboratorial 2222",
                    "valor": 15.0
                },
                {
                    "id": 227,
                    "exame": "Exame Laboratorial 3333",
                    "valor": 8.0
                }
            ],
            "links": {
                "self": "https://sdn-mapes.herokuapp.com/api/consultas/301/"
            }
        },
        {
            "numero_guia_consulta": 2,
            "cod_medico": 124,
            "nome_medico": "José Ramos",
            "data_consulta": "2017-02-02",
            "valor_consulta": "91.00",
            "valor_exames": 12.0,
            "total_da_consulta": 103.0,
            "exames": [
                {
                    "id": 244,
                    "exame": "Exame Laboratorial 4444",
                    "valor": 12.0
                }
            ],
            "links": {
                "self": "https://sdn-mapes.herokuapp.com/api/consultas/302/"
            }
        }
    ]
