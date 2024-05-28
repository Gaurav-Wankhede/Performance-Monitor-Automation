import psutil
import time
import pyodbc

con = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-F8QC9QH\SQLEXPRESS;'
    'Database=System_Information;'
    'Trusted_Connection=yes;'
)

cursor = con.cursor()

while True:
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory()[2]

    cpu_interrupts = psutil.cpu_stats()[1]
    cpu_calls = psutil.cpu_stats()[3]

    memory_used = psutil.virtual_memory()[3]
    memory_free = psutil.virtual_memory()[4]

    bytes_sent = psutil.net_io_counters()[0]
    bytes_received = psutil.net_io_counters()[1]

    disk_usage = psutil.disk_usage('/')[3]

    cursor.execute(
        'INSERT INTO Performance1 (Time, cpu_usage, memory_usage, cpu_interrupts, cpu_calls, memory_used, memory_free, bytes_sent, bytes_received, disk_usage) VALUES (GETDATE(),'
        + str(cpu_usage) + ','
        + str(memory_usage) + ','
        + str(cpu_interrupts) + ','
        + str(cpu_calls) + ','
        + str(memory_used) + ','
        + str(memory_free) + ','
        + str(bytes_sent) + ','
        + str(bytes_received) + ','
        + str(disk_usage) + ')')

    con.commit()
    print(cpu_usage)
    time.sleep(1)
