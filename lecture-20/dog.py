import time
import logging
import logging.config
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys, os

class Watcher:
    def __init__(self):
        
        self.watchDirectory = sys.argv[1] if len(sys.argv) > 1 else '.'
        self.observer = Observer()

    def run(self):
        logging.config.fileConfig(os.path.dirname(__file__)+'/logging.conf')
        self.observer.schedule(Handler(), self.watchDirectory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            print('Observer Stopped')
        self.observer.join()

class Handler(FileSystemEventHandler):

   @staticmethod
   def on_any_event(event):
      
       logger = logging.getLogger("mainApp")
       message = f"[{time.asctime()}] noticed: Watchdog recived {event.event_type} event on {event.src_path}"
       print(message)

       logger.info(message)

if __name__ == "__main__":
   watcher = Watcher()
   watcher.run()
