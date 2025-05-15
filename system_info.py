import psutil

ram_data = psutil.virtual_memory()._asdict()
memory_data = psutil.swap_memory()._asdict()
battery_usage = ""


total_ram = round(ram_data['total']/1073741824, 1)
used_ram = round(ram_data['used']/1073741824, 2)

ram_usage = f"RAM Usage: {total_ram} GB / {used_ram} GB"
free_disk = f"Disk Space: {round(int(psutil.disk_usage("/home")._asdict()['free'])/1073741824, 2)} GB free"

if type(psutil.sensors_battery()) != type(int):
    battery_usage = f"Battery: 100%"
else:
    battery_usage = f"Battery: {psutil.sensors_battery()}%"
