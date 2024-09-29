# Change Calculator

This project implements a simple change calculator that determines the amount of change to return when a customer pays for a service or product. It takes into account US currency denominations and provides the optimal way to return change using the least number of notes and coins.

## Features

- Accepts the amount charged and the amount given by the customer.
- Calculates the difference between the two amounts.
- Returns the required change in the nearest available US currency denominations.
- Handles scenarios where no change is needed or when additional payment is required.

## Currency Denominations

The program considers the following US currency denominations:

- Notes: $100, $50, $20, $10, $5, $1
- Coins: 25¢, 10¢, 5¢, 1¢

## How to Use

1. Clone this repository to your local machine.
2. Open the Python file in your favorite code editor.
3. Run the script.
4. Enter the amount charged when prompted.
5. Enter the amount given by the customer when prompted.

## Example

```plaintext
Amount charged: 19.99
Amount given: 20.00
Output:

plaintext
Copy code
Change to return:
1¢: 1
```
## Code Overview

The main components of the code include:
```finding_nearest_note(diff)```: A helper function that returns the nearest denomination that does not exceed the difference in amounts.
```bill_collector()```: The core function that calculates the change to return and returns a dictionary with the count of each denomination.
