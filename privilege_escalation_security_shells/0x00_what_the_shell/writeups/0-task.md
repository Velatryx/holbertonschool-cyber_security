### Goal is to retrieve the flag in /home/user/flag, however, some commands and strings like `flag` are restricted.

First, I used ssh to connect to the machine: ssh user@IP

Then, I used shell globbing, matching the count of '?' to length of 'flag' string.

$ cat /home/user/????

CTF{who_needs_espace_when_u_have_bash_HASH : 03802581490b263f973aba02eac2ad2a}

---

Other file contents inside /home/user: (NOTE THAT 'sh' is also blacklisted, so I used shell globbing technique again)

$ cat /home/user/entrypoint.??

#!/bin/bash handler() { echo "Hemm, nice one but you can't escape." } set -e . /home/user/run.sh # Uncomment the trap to handle signals #trap handler 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 # Blacklist of commands blacklist="\* flag + bash sh zsh SHELL grep vi vim scp ssh awk tar nano pico ed ex gedit emacs kate lime jed find env | - echo for while do done if { }" echo "Your Goal is to read '/home/user/flag' content." echo "Have fun." # Jail loop while : do read -p "$ " x con=true for i in $blacklist do if echo "$x" | grep -q "$i" then echo "Hemm you know $i is blacklisted." con=false break fi done if $con then output=$(eval $x) echo $output fi done


$ cat /home/user/run.??

#!/bin/bash # Proudly Written by Yosri.me set -e # prepare env variables URL=https://cod.hbtn.io/api/get_github/`hostname | cut -d '-' -f 1` github_username=`curl $URL 2> /dev/null` . /usr/local/bin/gen_flag.sh $github_username #rm /usr/local/bin/gen_flag.sh # prepare the cert # /tmp/gen_certif.sh # rm /tmp/gen_certif.sh # clean up # start nginx


$ cat /home/user/wrapper.sh

Hemm you know sh is blacklisted.

$ cat /home/user/wrapper.??

#!/bin/bash # Change directory to root cd / # Execute the entrypoint script exec /home/user/entrypoint.sh
