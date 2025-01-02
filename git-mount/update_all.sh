#!/bin/bash

directories=(
    maxsim_core
    maxsim_app
    qm
    XLUdpAgentShow
    CollectDataToDB
    battle_train_gateway
)

base_path=/home/szzh
biandao_path=$base_path/biandao_code

mkdir -p $biandao_path

for dir in "${directories[@]}"; do
    if [[ "$dir" == "maxsim_core" || "$dir" == "maxsim_app" ]]; then
        target_path="$base_path/$dir"
    else
        target_path="$biandao_path/$dir"
    fi

    if [ ! -d "$target_path" ]; then
        git clone "$base_path/git/$dir" "$target_path"
    else
        echo "git -C \"$target_path\" pull"
        git -C "$target_path" pull
    fi
done

