# AWS Aliases

Type an AWS service name in your terminal and the AWS console appears in your browser for that service.


![](aws-aliases.gif)

## Installation

- Install https://github.com/zquestz/s
- Make sure your ~/.config/s/config is a valid JSON document.
- Run this script

```bash
python aws-aliases.py web > /tmp/web-out.txt && cp /tmp/web-out.txt ~/.config/s/config
python aws-aliases.py alias
```

## Usage

```bash
$ ec2
$ s3 && sqs
```

 You should see the AWS console for these services appear in browser tabs.
