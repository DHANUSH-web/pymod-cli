"""
    ************************************************************************
    Copyright (c) 2025 Dhanush H V. All rights reserved.
    Licensed under the MIT License. See the LICENSE file for more details.
    ************************************************************************
"""


import os
import datetime


# Logger colors
class Color:
    HEADER          = '\033[95m'
    BLUE            = '\033[94m'
    CYAN            = '\033[96m'
    SUCCESS         = '\033[92m'
    WARNING         = '\033[93m'
    ERROR           = '\033[91m'
    RESET           = '\033[0m'
    BOLD            = '\033[1m'
    GRAY            = '\033[90m'
    UNDERLINE       = '\033[4m'
    ITALIC          = '\033[3m'
    STRIKETHROUGH   = '\033[9m'


class Logger:

    def __init__(self, file_name: str = "pymod_debug.log", debug: bool = False) -> None:
        self.root_dir: str = os.path.join(os.getcwd(), "cache")
        self.file_name: str = os.path.join(self.root_dir, file_name)
        self._start_time: datetime.datetime = datetime.datetime.now()
        self._end_time: datetime.datetime | None = None
        self.log_count: int = 0
        self.debug: bool = debug

        # All available log types or log levels
        self.level: dict = {
            "debug": { "label": "DEBUG", "color": Color.SUCCESS, "count": 0 },
            "info": { "label": "INFO", "color": Color.CYAN, "count": 0 },
            "warning": { "label": "WARNING", "color": Color.WARNING, "count": 0 },
            "error": { "label": "ERROR", "color": Color.ERROR, "count": 0 },
            "fatal": { "label": "FATAL", "color": f"{Color.ERROR}{Color.BOLD}", "count": 0 },
            "message": { "label": "MESSAGE", "color": Color.BLUE, "count": 0 },
            "unknown": { "label": "UNKNOWN", "color": Color.GRAY, "count": 0 },
        }

        # Create the logger root directory
        os.makedirs(self.root_dir, exist_ok=True)

        # Create the log files inside the logger directory
        self.file = open(self.file_name, "w+")

        # Initialize the logger
        message = f">>> Logger initialized at {self._start_time} <<<"
        self.file.write(f"{message}\n")
        self.__print_log(message=f"{Color.BOLD}{message}", level="message")

    def get_start_time(self) -> datetime.datetime:
        return self._start_time

    def get_end_time(self) -> datetime.datetime | None:
        return self._end_time

    def get_log_count(self) -> int:
        return self.log_count

    def get_level_count(self, level: str) -> int:
        if not self.level.__contains__(level):
            raise ValueError(f"Invalid log level: {level}")

        return self.level[level]['count']

    def get_log_levels(self) -> list:
        return list(self.level.keys())

    def delete_log_file(self) -> None:
        if self.is_active():
            raise RuntimeError("Logger is active, please stop the logger before deleting log file")
        os.remove(self.file_name)

    def is_active(self) -> bool:
        return not self.file.closed

    def log(self, message: str, level: str = "message", debug_once: bool = False) -> None:
        dt = datetime.datetime.now()
        level = level if self.level.__contains__(level) else "unknown"
        message = f"{dt} {self.level[level]['label']} {message}"

        if self.debug or debug_once:
            self.__print_log(message=message, level=level)

        self.file.write(f"{message}\n")
        self.level[level]['count'] = self.level[level]['count'] + 1
        self.log_count += 1

    def __print_log(self, message: str, level: str = "message") -> None:
        if not self.level.__contains__(level):
            level = "unknown"

        print(f"{self.level[level]['color']}{message}{Color.RESET}", flush=True)

    def exit_logger(self) -> None:
        if not self.is_active():
            self.__print_log(message="No active logger found to exit", level="warning")
            return
        
        # update the stop logger timer
        self._end_time = datetime.datetime.now()

        # update final log about logger status
        message = f">>> Logger exited at {self._end_time} <<<"
        self.file.write(message)
        self.__print_log(message=f"{Color.BOLD}{message}", level="message")

        # close the logger file
        self.file.flush()
        self.file.close()
