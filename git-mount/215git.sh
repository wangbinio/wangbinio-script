#!/bin/bash

directories=(
    maxsim_core
    maxsim_app
    qm
    XLUdpAgentShow
    CollectDataToDB
    battle_train_gateway
)

ip="192.168.11.215"

base_path="/home/szzh/git"

for dir in "${directories[@]}"; do
    mkdir -p "$base_path/$dir.git"
    sudo mount -t cifs "//$ip/git/$dir.git" "$base_path/$dir.git" -o username=szzh,password=1
done
