import requests
from bs4 import BeautifulSoup
import os
import time

def getIPFromBody(text):
    content = BeautifulSoup(text, "html.parser")
    spans = content.find_all('span', attrs={'class': 'Whwtdhalf w15-0 lh45', 'style': 'cursor:pointer;'})
    return [span.text for span in spans]

def warpHost(hostname, ips: list):
    for ip in ips:
        if (ip is not None and ip != ""):
            warp = str(ip).ljust(20) + hostname
            print(warp)
            return warp
    return ""

def getHosts():
    return ["github.githubassets.com",
            "central.github.com",
            "desktop.githubusercontent.com",
            "assets-cdn.github.com",
            "camo.githubusercontent.com",
            "github.map.fastly.net",
            "github.global.ssl.fastly.net",
            "gist.github.com",
            "github.io",
            "github.com",
            "api.github.com",
            "raw.githubusercontent.com",
            "user-images.githubusercontent.com",
            "favicons.githubusercontent.com",
            "avatars5.githubusercontent.com",
            "avatars4.githubusercontent.com",
            "avatars3.githubusercontent.com",
            "avatars2.githubusercontent.com",
            "avatars1.githubusercontent.com",
            "avatars0.githubusercontent.com",
            "avatars.githubusercontent.com",
            "codeload.github.com",
            "github-cloud.s3.amazonaws.com",
            "github-com.s3.amazonaws.com",
            "github-production-release-asset-2e65be.s3.amazonaws.com",
            "github-production-user-asset-6210df.s3.amazonaws.com",
            "github-production-repository-file-5c1aeb.s3.amazonaws.com",
            "githubstatus.com",
            "github.community",
            "media.githubusercontent.com",
            "copilot-proxy.githubusercontent.com",
            "cloud.githubusercontent.com",
            "pipelines.actions.githubusercontent.com",
            "objects.githubusercontent.com"]

url = "https://ip.tool.chinaz.com/"
host_warps = []
for hostname in getHosts():
    realUrl = url + hostname
    body = requests.get(realUrl).text
    ips = getIPFromBody(body)
    host_warp = warpHost(hostname, ips)
    if (host_warp != ""):
        host_warps.append(host_warp)

dest_host_file = os.path.split(os.path.realpath(__file__))[0] + '/host'
with open(dest_host_file, 'w') as f:
    f.writelines(host_warps)