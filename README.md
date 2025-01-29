<p align="center">
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" height="60" width="60">
</p>

<div align="center">
  <h1>Receipt</h1>
</div>

This is my very first Python project where I created a simple receipt generator that calculates the total cost for a product purchase, including tax. The program prompts the user for the product's price, name, and quantity, then displays a neatly formatted receipt with the current date and time.

#### Key Features:
  - **Real-time Date and Time**: The receipt displays the current date and time, formatted to resemble an actual receipt
  - **Tax Calculation**: The program calculates a 7.125% tax on the subtotal and displays the tax amount separately
  - **Formatted Output**: The receipt is formatted to look professional, showing the product, quantity, subtotal, tax, and total with proper decimal precision
  - **User Input**: The user can input the product price, name, and quantity, and the program will calculate the total cost

## Code Walkthrough:
#### Library:
```python
  import datetime
```

  - ` datetime `: This library is used to fetch the current date and time, which is displayed on the receipt

#### Collecting User Input:
```python
  product_price = float(input("PRICE: "))
  product_name = input("PRODUCT: ")
  quantity = int(input("QTY: "))
```

  - The user is prompted to enter the price of the product, the product name, and the quantity. The price is converted to a float, and the quantity is converted to an integer

#### Displaying the Receipt:
```python
  print("---------------------------")
  print("          RECEIPT          ")
  print(current_time.strftime("%m/%d/%Y.........%H:%M:%S"))
  print(f"PRODUCT   : {product_name.upper()}")
  print(f"QTY       : {quantity}")
```

  - The program prints the formatted receipt header and uses strftime to display the current date and time in a receipt-like format. The product name is also converted to uppercase to enhance the receipt’s appearance

#### Calculating the Subtotal, Tax, and Total:
```python
  sub_total = product_price * quantity
  tax = 7.125 / 100 * sub_total
  total = tax + sub_total
```

  - The program calculates the subtotal, tax amount, and total cost by applying a 7.125% tax rate to the subtotal

#### Final Output:
```python
  print(f"SUB TOTAL : {sub_total:.2f}")
  print(f"TAX AMOUNT: ${tax:.2f}")
  print(f"TOTAL     : ${total:.2f}")
  print("---------------------------")
```

  - The receipt is displayed with the product details, calculated subtotal, tax amount, and total. All amounts are formatted to two decimal places for clarity

## Development Environment:
To develop this project, I used the online IDE [OnlineGDB.com](https://www.onlinegdb.com/online_python_compiler), which offers an easy-to-use compiler and debugger for Python.

## Contact:
Feel free to reach out to me with any questions, suggestions, or feedback!<br/>
[![GitHub](https://github.com/CLorant/readme-social-icons/blob/main/large/filled/github.svg)](https://github.com/mateuszcalderon)
[![Instagram](https://github.com/CLorant/readme-social-icons/blob/main/large/filled/instagram.svg)](https://www.instagram.com/mateuszcalderon/)
[![LinkedIn](https://github.com/CLorant/readme-social-icons/blob/main/large/filled/linkedin.svg)](https://www.linkedin.com/in/mateuszcalderonreis/)
