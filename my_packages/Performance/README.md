# Performance

A simple timer module for measuring performance of a piece of code.

## Installation

To install Performance, you can use pip.

```
pip install Performance
```

## Usage

The Performance module provides a simple timer class that can be used to measure the performance of a piece of code. The class has three main methods:

- start(): starts the timer
- stop(): stops the timer
- performance: returns the elapsed time between start and stop

It also has a custom exception class TimeError which is raised when the timer is not running or already running.

```
from Performance import Performance

timer = Performance()

timer.start()

# run the code to be timed here

timer.stop()
print(timer.performance)
```

## Contributing

If you want to contribute to the development of this package, feel free to fork the repository and create a pull request.

## License

This package is licensed under the MIT License. See the LICENSE file for more details.
