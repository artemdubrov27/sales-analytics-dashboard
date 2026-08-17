# Sales Analytics Dashboard

A modern desktop application for visualizing sales analytics using **CustomTkinter**, **SQLite**, **Pandas**, and **Matplotlib**.  
The dashboard provides interactive data exploration with tables, bar charts, line charts, and pie charts — all rendered locally without any browser.

---

## Features

- Modern GUI built with **CustomTkinter**
- Local SQLite database (`store.db`)
- Five analytical modules:
  - **Total Revenue**
  - **Revenue by Customers**
  - **Top Products**
  - **Average Order Value**
  - **Orders by Month**
- Multiple display options:
  - Table view
  - Bar chart
  - Line chart
  - Pie chart
- Safe window closing handler
- Fully offline, no API or browser required

---

## Technologies Used

- **Python 3.14**
- **CustomTkinter** — modern UI components
- **SQLite3** — lightweight local database
- **Pandas** — data manipulation
- **Matplotlib** — chart rendering inside Tkinter
- **Tkinter** — windowing system

---

## Analytics Modules

### 1. Total Revenue  
Calculates the sum of all sales from `OrderItems`.

### 2. Revenue by Customers  
Aggregates total spending per customer.

### 3. Top Products  
Shows which products generate the most revenue.

### 4. Average Order Value  
Computes the average value of all orders.

### 5. Orders by Month  
Counts how many orders were made each month.

---

## How to Run

1. Install dependencies:
pip install customtkinter pandas matplotlib

2. Navigate to the GUI folder:
cd gui

3. Run the application:

---

## About the Database (`store.db`)

The `store.db` file contains all sales data used by the dashboard:

- Customers  
- Orders  
- OrderItems  

It acts as the local data source for all analytics modules.

---

## Future Improvements

- Add filters (by month, customer, product)
- Add CSV export
- Add dashboard tabs
- Add light/dark theme switch
- Add animated charts

---

## Screenshots

### Main Window
The main window of the **Sales Analytics Dashboard**.  
It features a clean dark interface with five buttons for different analytics modules:  
**Total Revenue**, **Revenue by Customers**, **Top Products**, **Average Order Value**, and **Orders by Month**.
![Main Window](assets//Screenshot%202026-08-17%20133744.png)

### Display Options
A secondary window where the user can choose how to visualize data.  
Available options include **Table**, **Bar Chart**, **Line Chart**, and **Pie Chart**.  
![Display Options](assets//Screenshot%202026-08-17%20133759.png)

### Total Revenue Table
A simple table view showing the total revenue calculated from all orders.
![Total Revenue Table](assets//Screenshot%202026-08-17%20133812.png)

### Chart Unavailable Message
An error message displayed when the dataset contains fewer than two columns.  
It informs the user that charts require at least two columns of data.
![Chart Unavailable Message](assets//Screenshot%202026-08-17%20133825.png)

### Revenue by Customers - Table View
A table showing each customer’s total revenue.  
Example data:  
- Artem - 995.0  
- John Doe - 600.0  
- Maria Smith - 90.0
![Revenue by Customers - Table View](assets//Screenshot%202026-08-17%20134003.png)

### Revenue by Customers - Bar Chart
A bar chart comparing total revenue among customers.  
Artem leads with the highest revenue, followed by John Doe and Maria Smith.
![Revenue by Customers - Bar Chart](assets//Screenshot%202026-08-17%20134017.png)

### Revenue by Customers - Line Chart
A line chart showing the same data as above, visualized as a downward trend from Artem to Maria Smith.
![Revenue by Customers - Line Chart](assets//Screenshot%202026-08-17%20134026.png)

### Revenue by Customers - Pie Chart
A pie chart illustrating the percentage share of total revenue per customer:  
Artem (59.1%), John Doe (35.6%), and Maria Smith (5.3%).
![Revenue by Customers - Pie Chart](assets//Screenshot%202026-08-17%20134035.png)