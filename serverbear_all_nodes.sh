sudo salt "*" cmd.run template=jinja "wget -N https://raw.github.com/Crowd9/Benchmark/master/sb.sh"
sudo salt "*" cmd.retcode template=jinja "screen -d -m bash sb.sh 'Baozishan' '{{grains.id}}' 'vashzhong@tencent.com' '' private"

