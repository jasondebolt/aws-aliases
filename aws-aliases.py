
"""Type an AWS service name in your terminal and the AWS console appears in your browser for that service.

    $ s3 --> S3 console opens in browser.
    $ ec2 --> EC2 console opens in browser.
"""

import os
import sys
import json
import services

ALL_SERVICES = services.service_list + services.other_services

def get_service_url(service):
    default_url = 'https://console.aws.amazon.com/{0}/home'.format(service)
    exception_urls = {
        'chime': 'https://console.chime.aws.amazon.com/home',
        'ebs': 'https://console.aws.amazon.com/ec2/v2/home#Volumes:sort=desc:createTime',
        'elb': 'https://console.aws.amazon.com/ec2/v2/home?#LoadBalancers:sort=loadBalancerName',
        'eventbridge': 'https://console.aws.amazon.com/events',
        'ssm': 'https://console.aws.amazon.com/systems-manager',
        'vpc': 'https://console.aws.amazon.com/vpc/home#vpcs:sort=VpcId'
    }
    return exception_urls.get(service, default_url)
    
def write_service_alias_file(alias_list):
    filename = os.path.join(os.path.expanduser('~'), '.aws_service_aliases')
    with open(filename, 'w') as out_file:
        out_file.write('\n'.join(alias_list))

def main(args):
    if len(args) == 2 and args[1] == 'clean':
        # Empty the file but don't delete it so that that bash sourcing doesn't break.
        write_service_alias_file([])
    else:
        alias_list = []
        for service in ALL_SERVICES:
            alias_list.append('alias {0}="open {1}"'.format(service, get_service_url(service)))
        write_service_alias_file(alias_list)

if __name__ == '__main__':
    main(sys.argv)
