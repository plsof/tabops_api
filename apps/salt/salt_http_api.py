import yaml
import requests


class salt_api_token(object):
    """
    list_all = salt_api_token({'fun': 'cmd.run', 'tgt': node_list,
                                       'arg': cmd    },
                                      salt_api_url, {'X-Auth-Token' : token_api_id})
    """

    def __init__(self, data, url, token=None):
        self.data = data
        self.url = url
        self.headers = {
            'CustomUser-agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            "Accept": "application/x-yaml",
        }
        s = {"client": "local_async"}
        self.headers.update(token)
        self.data.update(s)

    def run(self):
        """
        异步执行任务
        :return:
        """
        req = requests.post(self.url, headers=self.headers, data=self.data, verify=False)
        context = req.text
        return yaml.safe_load(context)

    def CmdRun(self, client='local'):
        """
        同步执行任务
        :return:
        """
        self.data["client"] = client
        req = requests.post(self.url, headers=self.headers, data=self.data, verify=False)
        context = req.text
        return yaml.safe_load(context)
