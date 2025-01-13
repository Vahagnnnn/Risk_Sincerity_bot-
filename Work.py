import os
import time
import psutil
import subprocess
from datetime import datetime

# Конфигурация
bot_script = "Main.py"  # Имя вашего бота
log_file = "bot_monitor.log"  # Файл для логов

def log_message(level, message):
    """Записывает сообщение в лог-файл с уровнем и временной меткой."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"[{timestamp}] [{level}] {message}\n"
    with open(log_file, "a") as log:
        log.write(formatted_message)
    print(formatted_message.strip())  # Дублируем лог в консоль для удобства

def is_bot_running(script_name):
    """Проверяет, запущен ли bot.py."""
    for process in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        try:
            if script_name in process.info['cmdline']:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

def run_bot(script_name):
    """Запускает bot.py через subprocess."""
    try:
        log_message("INFO", f"Бот не работает. Попытка запуска {script_name}...")
        process = subprocess.Popen(
            ['python3', script_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        log_message("SUCCESS", f"Бот {script_name} успешно запущен. PID: {process.pid}")
    except Exception as e:
        log_message("ERROR", f"Не удалось запустить бота. Ошибка: {e}")

if __name__ == "__main__":
    log_message("INFO", "Скрипт мониторинга запущен.")
    while True:
        if not is_bot_running(bot_script):
            log_message("WARNING", "Бот не найден в активных процессах.")
            run_bot(bot_script)
        else:
            log_message("INFO", "Бот работает корректно.")
        time.sleep(30)  # Проверка каждые 30 секунд