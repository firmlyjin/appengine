#!/bin/bash

ip=$1
remote_df()
{
#for ip in `cat ip.txt`
#do
dfval=$(/usr/bin/expect <<EOF
spawn ssh  root@$ip
#expect {
#"yes/no" {send "yes\r";exp_continue}
#"*assword:" {send "111111\r"}
#expect "*assword:" {send "mkdir -p /root/data/hadoop\r"}
#}
#expect "*assword:" {send "111111\r"}
expect "*:~#" {send "df -h\r"}
sleep 0.1
expect -re {\d+\|(-?\d+)\|\d+} { puts $dfval(1,string) }
sleep 0.5
EOF
)
#done
echo $dfval |  awk '{split($0,b,"~#");print b[2]}'
}
remote_df

re=$1
show_links()
{
li=$(/usr/bin/expect <<EOF
spawn telnet localhost 4000
#expect {
#"yes/no" {send "yes\r";exp_continue}
#"*assword:" {send "111111\r"}
#expect "*assword:" {send "mkdir -p /root/data/hadoop\r"}
#}
#expect "MLdonkey command-line:*>*" {send "links\r"}
expect "*>*" {send "links\r"}
sleep 0.5
expect -re {\d+\|(-?\d+)\|\d+} { puts $li(1,string) }
sleep 0.5
EOF
)
#echo $li > testtest.txt
#cat testtest.txt  |awk '{split($0,b,"ed2k://");for (i=2;i<=length(b);i++){if(match(b[i],/'$re'/)){gsub(/^/," ed2k://",b[i]);{print b[i]}}}}'
echo $li | awk '{split($0,b,"ed2k://");for (i=2;i<=length(b);i++){if(match(b[i],/'$re'/)){gsub(/^/," ed2k://",b[i]);{print b[i]}}}}'
}
#show_links
