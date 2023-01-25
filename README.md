# Pyrobot

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)


## Overview

Current Version: **1.0.5**

A trading robot written in Python utilizing the [Lemon Markets API](https://www.lemon.markets/) designed to mimic a few common scenarios: 


1. Providing an interface for the user's trading account. The `PyRobot` object will    initialize a new instance of the robot and provide general information regarding the user's account. It will also serve as main object connecting all other objects to provide  easy access to other functionalities.

2. Maintaining a portfolio of multiple instruments. The `Portfolio` object will be able
   to calculate common portfolio risk metrics, display order information, and provide both historical and real-time prices for instruments.

3. Define an order that can be used to trade a financial instrument. With the `Trade` object, you can place, cancel and retrieve orders.

4. Define and calculate indicators using both historical and real-time prices. The `Indicator` object
   will help you easily define the input of your indicators, calculate them, and then update their values
   as new prices come.

5. Access new information daily. The `MarketData`,`TradingPositions` and `TradingAccount` objects will interact with the [Lemon Markets API](https://www.lemon.markets/) to ensure the trader is equipped with up-to-date information regarding the market and their portfolio.

## Setup

**Setup - PyPi Install:**

The project can be found at PyPI, if you'd like to view the project please use this
[link](https://pypi.org/project/python-trading-robot/). To **install** the library,
run the following command from the terminal.

```bash
pip install trad-robo-python
```


## Usage

To run the robot, you will need to provide a few pieces of information from your Lemon Markets Paper Trading Account
The following items are need for authentication:

- Market Data API Key: This will be provided when you register an account with the Lemon Markets website.  An example of a Market Data API key could look like the following `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJh`.

- Paper Trading API Key: This will be provided when you register an account with the Lemon Markets website.  An example of a Paper Trading API key could look like the following `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.`.



Once you've identfied those pieces of info, you can run the robot. Here is a simple example that will create a new instance
of it:

```python
from pyrobot.robot import PyRobot

# Initialize the robot
trading_robot = PyRobot(
    market_api_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJh',
    paper-trading_api_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.'
)
```

For more detailed examples, go to the `trading_robot.py` file to see an example of how to use the library along with all the different objects inside.

