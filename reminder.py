import time 
from plyer import notification

if __name__ == "_main_":
    while True:
        notification.notify(
            title = "Time for a power nap!!",
            message = "Your have worked for a long time just take a power nap",
            app_icon='C:\ Users\hp\Desktop\Coding\.vscode\sleep.png',
            timeout=10
    )
    time.sleep(5)
    
