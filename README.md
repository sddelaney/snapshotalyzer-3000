# snapshotalyzer-3000
Demo project to manage EC2 snapshots

## About

This project is a demo, uses boto3 to manage AWS EC2 instance snapshots

## Configuring

shotty uses the configuration file created by the AWS cli

`aws configure --profile shotty`

## Running

`pipenv run python shotty/shotty.py <command> <--project=PROJECT>``

*command* is instances, volumes, or snapshots
*subcommand* is list, start, or stop
*project* is optional
