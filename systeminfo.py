import os
import platform

# Получаем информацию о системе
info = platform.uname()

# Открываем текстовый файл для записи
f = open("system_info.txt", "w")

# Записываем информацию о системе в файл
f.write("System: " + info.system + "\n")
f.write("Node Name: " + info.node + "\n")
f.write("Release: " + info.release + "\n")
f.write("Version: " + info.version + "\n")
f.write("Machine: " + info.machine + "\n")
f.write("Processor: " + info.processor + "\n")

# Закрываем файл
f.close()