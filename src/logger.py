"""
A module for logging messages to a file.

This module provides a "Logger" class that can be used to log messages to a file.
The logging can be configured to use either a simple or detailed logging mode,
which is controlled by the "LOGGER_SIMPLE_MODE" variable in the "config" module.

The "loggable" decorator can be used to automatically log the calling and return
of a function.
"""

from os import path, makedirs
from time import strftime, localtime
from functools import wraps
from typing import Callable, Union, Any, Optional
from config import LOGGER_ON, LOGGER_SIMPLE_MODE, LOG_DIRECTORY


class Logger:
    """
    A class for logging messages to a log file.

    Attributes:
        logger_on (bool): Indicates whether logging is enabled.
        simple_mode (bool): Indicates whether to use simple or detailed logging mode.
        log_file (str): The path to the log file.
    """
    def __init__(self, log_directory: str = LOG_DIRECTORY, logger_on: bool = LOGGER_ON,
                 simple_mode: bool = LOGGER_SIMPLE_MODE) -> None:
        """
        Initialize a new Logger instance.

        Args:
            log_directory (str): The directory to store the log file.
            logger_on (bool): Indicates whether logging is enabled.
            simple_mode (bool): Indicates whether to use simple or detailed logging mode.
        """
        self.logger_on: bool = logger_on
        self.simple_mode: bool = simple_mode

        # Get the project root directory
        project_root = path.dirname(path.abspath(__file__))
        log_directory = path.join(project_root, log_directory)

        # Ensure the log directory exists
        if logger_on and not path.exists(log_directory):
            makedirs(log_directory)

        timestamp = strftime('%Y%m%d_%H%M%S', localtime())
        self.log_file: str = path.join(log_directory, f"log_{timestamp}.log")

    def __str__(self) -> str:
        """
        Return a simple string representation of the Logger object.

        Returns:
            str: A simple string representation of the Logger object.
        """
        return f"Logger(log_file='{self.log_file}')"

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the Logger object.

        Returns:
            str: A string representation of the Logger object.
        """
        return f"Logger(log_file='{self.log_file}', logger_on={self.logger_on}, simple_mode={self.simple_mode})"

    def log(self, message: str, function_name: str = "", return_value: Optional[str] = None,
            args: tuple = (), kwargs: Optional[dict[str, Any]] = None) -> None:
        """
        Log a message using the appropriate logging mode.

        Args:
            message (str): The message to be logged.
            function_name (str): The name of the function being logged (optional).
            return_value (Optional[str]): The return value of the function being logged (optional).
            args (tuple): The arguments passed to the function being logged (optional).
            kwargs (Optional[dict[str, Any]]): The keyword arguments passed to the function being logged (optional).
        """
        if kwargs is None:
            kwargs = {}

        if self.simple_mode:
            self._log_simple(message)
        else:
            self._log_detailed(message, function_name, return_value, args, kwargs)

    def _log_simple(self, message: str) -> None:
        """
        Log a message in simple mode.

        Args:
            message (str): The message to be logged.
        """
        if self.logger_on:
            timestamp = strftime('%Y-%m-%d %H:%M:%S', localtime())
            log_message = f"{timestamp} - {message}\n"

            with open(self.log_file, mode="a", encoding="utf-8") as log_file:
                log_file.write(log_message)

    def _log_detailed(self, message: str, function_name: str, return_value: Union[str, None],
                      args: tuple, kwargs: dict[str, Any]) -> None:
        """
        Log a message in detailed mode.

        Args:
            message (str): The message to be logged.
            function_name (str): The name of the function being logged.
            return_value (Union[str, None]): The return value of the function being logged.
            args (tuple): The arguments passed to the function being logged.
            kwargs (dict[str, Any]): The keyword arguments passed to the function being logged.
        """
        if self.logger_on:
            timestamp = strftime('%Y-%m-%d %H:%M:%S', localtime())
            arg_str = ', '.join(repr(arg) for arg in args)
            kwarg_str = ', '.join(f"{key}={repr(value)}" for key, value in kwargs.items())
            log_message = (f"{timestamp} - {function_name}(args=({arg_str}), "
                           f"kwargs={{{kwarg_str}}}): {message} "
                           f"Return value: {repr(return_value)}\n")

            with open(self.log_file, mode="a", encoding="utf-8") as log_file:
                log_file.write(log_message)


def loggable(get_logger: Callable) -> Callable:
    """
    A decorator that logs the calling and return of a function.

    Args:
        get_logger (Callable): A function that returns a Logger instance.

    Returns:
        Callable: A decorator function that wraps the input function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = get_logger(*args, **kwargs)
            logger.log(f"Calling {func.__name__}", func.__name__, args=args, kwargs=kwargs)
            result = func(*args, **kwargs)
            logger.log(f"Function '{func.__name__}' returned", func.__name__, result, args, kwargs)
            return result
        return wrapper
    return decorator
