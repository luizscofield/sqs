#!/bin/bash
apt-get update
apt-get install -y python3 python3-venv git
cd /root
git clone https://github.com/luizscofield/sqs.git
cd sqs
python3 -m venv venv
. venv/bin/activate
pip install boto3
echo "source /root/sqs/venv/bin/activate" >> /root/.bashrc