# AWS Aliases

Type an AWS service name in your terminal and the AWS console appears in your browser for that service.

![](aws-aliases.gif)

## Installation

```bash
git clone https://github.com/jasondebolt/aws-aliases.git
cd aws-aliases
make install
```

## Usage

```bash
$ ec2
$ s3 && sqs
```

 You should see the AWS console for these services appear in browser tabs.

## Caveats
AWS console URL's are inconsistent. Some services don't work with this tool yet.
Feel free to create a pull request to add exception URL's to `aws-aliasess.py`.