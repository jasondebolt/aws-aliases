
"""Type an AWS service name in your terminal and the AWS console appears in your browser for that service.

    $ s3 --> S3 console opens in browser.
    $ ec2 --> EC2 console opens in browser.
   
   Installation:
     1) Install https://github.com/zquestz/s
     2) Run this script
     3) Copy the alias output to your .bash_profile
     4) Copy the web config to your ~/.config/s/config file.
     5) In your terminal, enter an AWS service name:
     
        $ ec2
     
    USAGE:
      python aws-aliases.py web > /tmp/web-out.txt && cp /tmp/web-out.txt ~/.config/s/config
      python aws-aliases.py alias >> ~/.bash_profile
"""

import os
import sys
import json
import services

def getExistingWebConfig():
    filename = os.path.join(os.path.expanduser('~'), '.config/s/config')
    currentConfig = open(filename, 'r').read()
    return json.loads(currentConfig)


def getExistingWebConfigKeys(web_config):
    return [key["name"] for key in web_config["customProviders"]]


def getWebVal(url, service):
    return {
        'name': '{0}'.format(service).replace('-', ''),
        'url': url,
        'tag': []
    }

def getServiceURL(service):
    url = 'https://console.aws.amazon%scom/' + service + '/home'
    if service == 'elb':
        url = 'https://us-west-2.console.aws.amazon%scom/ec2/v2/home?#LoadBalancers:sort=loadBalancerName'
    elif service == 'ssm':
        url = 'https://console.aws.amazon%scom/systems-manager'
    return url
  
def getServiceIndex(webConfig, service):
    for index, obj in enumerate(webConfig['customProviders']):
        if obj['name'] == service:
            return index
    raise Exception("Service not found")
  
def getNewWebConfig():  
        currentWebConfig = getExistingWebConfig()
        currentWebConfigKeys = getExistingWebConfigKeys(currentWebConfig)
        customProviders = []
        for service in services.service_list:
            url = getServiceURL(service)
            if service in currentWebConfigKeys:
                index = getServiceIndex(currentWebConfig, service)
                customProviders[index] = getWebVal(url, service)
            else:
                customProviders.append(getWebVal(url, service))
        currentWebConfig["customProviders"].extend(customProviders)
        return currentWebConfig

def main(args):
    if len(args) < 2:
        print("python aws-alises.py [web|alias]")
        raise SystemExit()

    cmd = args[1]
    if cmd == 'web':
        newWebConfig = getNewWebConfig()
        print(json.dumps(newWebConfig, indent=2))
    elif cmd == 'alias':
        aliasList = []
        for service in services.service_list:
            aliasList.append('alias {0}="s -p {0} ."'.format(service))
        print('\n## AWS Service Aliases\n')
        print('\n'.join(aliasList))


if __name__ == '__main__':
    main(sys.argv)
