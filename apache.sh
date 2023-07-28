#!/bin/bash/

yum install -y httpd
cp -r /home/andy/palm1/* /var/www/html

systemctl start httpd
systemctl enable httpd

firewall-cmd --zone=public --add-service=http --permanent
firewall-cmd --reload