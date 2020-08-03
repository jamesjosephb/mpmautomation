import requests


def entercpup(MPM, password, terminal):
    urlCPUP = "http://mycryptopay.com/cgi-bin/merchcheck.sh"
    data = {"eventType": "AAS_PORTAL_START", "data": {"uid": "hfe3hf45huf33545", "aid": "1", "vid": "1"}}
    siteInfo = {"x": MPM,
                "y": password,
                "z": terminal
                }
    webSession = requests.Session()
    webSession.get(urlCPUP)
    webSession.post(urlCPUP, params=siteInfo, json=data)


if __name__ == '__main__':
    entercpup("MPM121212122", "$!@#%12rE27hH5", "LK777665")
