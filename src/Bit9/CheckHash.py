import requests,json
from Launch.Launch import Launch

class CheckHash(object):

    @staticmethod
    def Run(hashvalue):
        launch=Launch()
        args=launch.get_args()
        b9serverurl,b9apitoken=launch.load_b9_config(args.configfile)
        authJson={
         'X-Auth-Token': b9apitoken, 
         'content-type': 'application/json'
                      }
        serverurl=b9serverurl+str("/api/bit9platform/v1/")
        md5url = serverurl+"fileCatalog?q=md5:"
        sha256url = serverurl+"fileCatalog?q=sha256:"
        b9StrongCert=True

        r = requests.get(md5url+hashvalue, headers=authJson, verify=b9StrongCert)
        r.raise_for_status()
        result = r.json()
        return result