#!/bin/bash

directories=(
    maxsim_core
    maxsim_app
    qm
    XLUdpAgentShow
    CollectDataToDB
    battle_train_gateway
)

base_path=/home/szzh/git

for dir in "${directories[@]}"; do
    if [  -d "$base_path/$dir.git" ]; then
        echo "sudo umount \"$base_path/$dir.git\""
        sudo umount "$base_path/$dir.git"
    fi
done

