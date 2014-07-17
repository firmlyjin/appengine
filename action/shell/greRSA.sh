#!/bin/bash
scp_ssh_rsa ()
{
if [ -f id_rsa ];then
/usr/bin/expect <<EOF
spawn  ssh-keygen -t rsa
expect {
"*id_rsa):" {send "\r";exp_continue}
"Overwrite (y/n)?" {send "y\r"}
}
EOF
else
filepath=$(cd "$(dirname "$0")"; pwd)
for ip in `cat $filepath/ip.txt`
do
/usr/bin/expect <<EOF
spawn ssh-copy-id root@$ip
expect {
"yes/no" {send "yes\r";exp_continue}
"*assword:" {send "111111\r"}
}
#expect "*assword:" {send "111111\r"}
EOF
done
fi
}
scp_ssh_rsa