######################################
``Mapes Teste desenvolvedor Django``
######################################


Descrição
***********
| O teste consiste em implementar um caso de uso.
| Exigências: django, jquery, ajax, bootstrap, postgres, teste unitário.


:Date: **18/01/2019**
:Author: **Sidon Duarte**

TL;DR
*******
A aplicação foi hospedada no `Heroku <http://www.heroku.com>`_ . Para testá-la clique: https://sdn-mapes.herokuapp.com/.

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


2) Crie o banco de dados

.. code-block::

    $ python manage.py makemigrations
    $ python manage.py migrate

3) Execute os testes do sistema :

.. code-block::

    $ python manage.py test

4) Crie o banco de dados com os dados iniciais

.. code-block::

    $ python manage.py initialdata


5) Execute a aplicação:

.. code-block::

    $ python manage.py runserver

6) Acesse a pagina principal

.. code-block::

    http://127.0.0.1:8000/


Acessando a API via Curl
***********************************

API Root:
============
::

    $ curl https://sdn-mapes.herokuapp.com/api/
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


Listar somente as consultas do médio cujo código é 124
======================================================
::

    curl -H 'Accept:application/json;indent=4' -u admin:master.21 https://sdn-mapes.herokuapp.com/api/consultas/?codigo_medico=124

    [
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
                "self": "http://127.0.0.1:8000/api/consultas/302/"
            }
        },
        {
            "numero_guia_consulta": 7,
            "cod_medico": 124,
            "nome_medico": "José Ramos",
            "data_consulta": "2017-02-03",
            "valor_consulta": "91.00",
            "valor_exames": 0,
            "total_da_consulta": 91.0,
            "exames": [],
            "links": {
                "self": "http://127.0.0.1:8000/api/consultas/307/"
            }
        },
        {
            "numero_guia_consulta": 12,
            "cod_medico": 124,
            "nome_medico": "José Ramos",
            "data_consulta": "2017-02-04",
            "valor_consulta": "91.00",
            "valor_exames": 12.0,
            "total_da_consulta": 103.0,
            "exames": [
                {
                    "id": 247,
                    "exame": "Exame Laboratorial 4444",
                    "valor": 12.0
                }
            ],
            "links": {
                "self": "http://127.0.0.1:8000/api/consultas/312/"
            }
        },
        {
            "numero_guia_consulta": 17,
            "cod_medico": 124,
            "nome_medico": "José Ramos",
            "data_consulta": "2017-02-05",
            "valor_consulta": "91.00",
            "valor_exames": 12.0,
            "total_da_consulta": 103.0,
            "exames": [
                {
                    "id": 248,
                    "exame": "Exame Laboratorial 4444",
                    "valor": 12.0
                }
            ],
            "links": {
                "self": "http://127.0.0.1:8000/api/consultas/317/"
            }
        },
        {
            "numero_guia_consulta": 22,
            "cod_medico": 124,
            "nome_medico": "José Ramos",
            "data_consulta": "2017-02-07",
            "valor_consulta": "93.00",
            "valor_exames": 12.0,
            "total_da_consulta": 105.0,
            "exames": [
                {
                    "id": 250,
                    "exame": "Exame Laboratorial 4444",
                    "valor": 12.0
                }
            ],
            "links": {
                "self": "http://127.0.0.1:8000/api/consultas/322/"
            }
        },
        {
            "numero_guia_consulta": 27,
            "cod_medico": 124,
            "nome_medico": "José Ramos",
            "data_consulta": "2018-02-01",
            "valor_consulta": "93.00",
            "valor_exames": 12.0,
            "total_da_consulta": 105.0,
            "exames": [
                {
                    "id": 252,
                    "exame": "Exame Laboratorial 4444",
                    "valor": 12.0
                }
            ],
            "links": {
                "self": "http://127.0.0.1:8000/api/consultas/327/"
            }
        }
    ]
