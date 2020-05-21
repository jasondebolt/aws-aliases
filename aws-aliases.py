
'''Type an AWS service name in your terminal an open in your browser:

    $ s3 --> S3 console opens in browser.
    $ ec2 --> EC2 console opens in browser.
   
   Installation:
     1) Install https://github.com/zquestz/s
     2) Run this script and copy output to your .bash_profile and your ~/.config/s/config file.
'''

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

def main(args):
    if len(args) != 2:
        print("python aws-alises.py [web|alias]")
        raise SystemExit()
    
    cmd = args[1]
    if cmd == 'web':
        currentWebConfig = getExistingWebConfig()
        currentWebConfigKeys = getExistingWebConfigKeys(currentWebConfig)
        customProviders = []
        for service in services.service_list:
            if service not in currentWebConfigKeys:
                customProviders.append(
                    {
                        'name': '{0}'.format(service),
                        'url': 'http://console.aws.amazon.com/{0}'.format(service),
                        'tags': []
                    }
                )
        currentWebConfig["customProviders"].extend(customProviders)
        print(json.dumps(currentWebConfig, indent=2))
    elif cmd == 'alias':
        aliasList = []
        for service in services.service_list:
            aliasList.append('alias {0}="s -p {0} ."'.format(service))
        print('\n'.join(aliasList))

if __name__ == '__main__':
    main(sys.argv)