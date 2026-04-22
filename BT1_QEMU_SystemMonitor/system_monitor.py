cpu_list = psutil.cpu_percent(interval=1, percpu=True)
cpu_avg = sum(cpu_list) / len(cpu_list)
ram = psutil.virtual_memory()
ram_used_mb = ram.used // (1024 ** 2)
ram_total_mb = ram.total // (1024 ** 2)
ram_pct = ram.percent


disk = psutil.disk_usage('/')
disk_pct = disk.percent

while True:
    # ... đọc CPU, RAM, Disk như trên ...
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f'[{now}] CPU: {cpu_avg:.1f}% | RAM: {ram_used_mb}/{ram_total_mb} MB ({ram_pct}%) | Disk: {disk_pct}%'
    print(line)
    sleep(2)
log_file = open('system_log.txt', 'w')


# Trong vòng lặp, sau print(line):
log_file.write(line + '\n')
log_file.flush()

try:
    while True:
        # ... code đọc + in + ghi ...if cpu_avg >= 70:
    status = 'CRITICAL'
elif cpu_avg >= 30:
    status = 'WARNING'
else:
    status = 'NORMAL'


# Thêm status vào cuối line:
line = f'[{now}] CPU: {cpu_avg:.1f}% | ... | {status}'


# Nếu WARNING hoặc CRITICAL, in riêng dòng cảnh báo:
if status != 'NORMAL':
    print(f'  ⚠ {status}: CPU đang ở {cpu_avg:.1f}%')


        sleep(2)
except KeyboardInterrupt:
    print('\nDừng giám sát.')
finally:
    log_file.close()
    print('Log saved to system_log.txt')


