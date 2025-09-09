
#!/bin/bash

if [ -f "/etc/vsftpd.conf" ]; then
    sudo echo "
    anonymous_enable=NO
    local_enable=YES
    write_enable=YES
    chroot_local_user=YES
    allow_writeable_chroot=YES
    " >> /etc/vsftpd.conf
else
    echo "文件/etc/vsftpd.conf不存在，需要先安装ftp"
fi

