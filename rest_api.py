import requests
import logging




class Api(object):
    def __init__(self, host = "http://localhost", api_key=None, api_key_prefix = 'Bearer ', ssl_ca_cert = None,log_dest = 'api.log'):
        if api_key is None:
            self.headers = {}
        else:
            self.headers = {'Authorization': '{0} {1}'.format(api_key_prefix,api_key)} 
        self.host = host
        self.ssl_ca_cert = ssl_ca_cert
        logging.basicConfig(filename=log_dest,level=logging.DEBUG)
    
    def vm_action(self,name,namespace,action):
        url = f"/apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachines/{name}/{action}"
        requests.put(self.host + url, headers=self.headers, verify=self.ssl_ca_cert)

    def test(self,url):
        response = requests.get(self.host + url, headers=self.headers, verify=self.ssl_ca_cert)
        print(response.content)