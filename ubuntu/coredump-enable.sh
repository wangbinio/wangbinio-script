
#!/bin/bash

# 1.关闭systemd-coredump, 避免被截胡
systemctl stop systemd-coredump.socket 2>/dev/null || true
systemctl disable systemd-coredump.socket 2>/dev/null || true

# 2.创建 core dump 保存目录
CORE_DIR="/var/coredumps"
mkdir -p $CORE_DIR
chmod 777 $CORE_DIR

# 3.修改core文件命名规则
CORE_PATTERN="$CORE_DIR/core-%e-%p-%t"
echo "$CORE_PATTERN" > /proc/sys/kernel/core_pattern
echo "kernel.core_pattern=$CORE_PATTERN" >> /etc/sysctl.conf

# 4.设置ulimit
ulimit -c unlimited
echo "ulimit -c unlimited" >> /root/.bashrc
echo "ulimit -c unlimited" >> /root/.zshrc
echo "* soft core unlimited" >> /etc/security/limits.conf
echo "* hard core unlimited" >> /etc/security/limits.conf

echo "设置coredumps路径成功 ：$CORE_PATTERN"
