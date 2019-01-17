import json
from core.models import Consulta, Logdb
from datetime import date

class Log_api:

    def _build_post(self, _data):
        data = json.dumps(_data)
        #  Utilizando curls
        curl = 'curl -d '+data+'-H "Content-Type: application/json" -u user:password -X POST https://url/da/api/'
        #  Utiliando requests (http for Humans :-)
        req = 'requests.post("https://url/api", data='+data
        return {'curl': curl, 'request': req}

    def update_api(self, data):
        post = self._build_post(data)
        Logdb.objects.create(post_req=post['request'], post_curl=post['curl'])

