### Welcome
This code was created as part of a take home interview with the following directions:
Query this API that returns a randomized list of products in JSON format:
https://www.beautylish.com/rest/interview-product/list
- Display a list of products including only the brand name, product name, and price.
    - Filter out any products that are hidden or deleted.
    - Sort by lowest to highest price. If two items have the same price, sort by name.
    - If the same product is included twice, only display it once.


-  Display a summary that includes:
    - The total number of unique products
    - The total number of unique brands
    - The average price


### System Requirements
Python3 is required. Please install python3 if it's not already installed!

Pip is required to install the requirements. Please install pip if it's not already installed!

Then run: pip install -r requirements.txt in your shell to ensure all necessary packages are installed.

### How to Run the Code
In your shell, run the main.py script : python3 main.py

### How to Run the Tester
In the command line, run pytest: pytest
