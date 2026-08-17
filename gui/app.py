import customtkinter as ctk
import sqlite3
import pandas as pd
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# DATABASE QUERY FUNCTION
def run_query(sql):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, "..", "database", "store.db")

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df

# DISPLAY METHODS
def show_table(df):
    win = ctk.CTkToplevel()
    win.title("Table")
    win.geometry("600x400")

    textbox = ctk.CTkTextbox(win, width=580, height=380)
    textbox.pack(pady=10)

    textbox.insert("0.0", df.to_string(index=False))

def show_plot(df, chart_type):
    # If only one column — no chart
    if len(df.columns) < 2:
        win = ctk.CTkToplevel()
        win.title("Chart unavailable")
        ctk.CTkLabel(win, text="At least 2 columns are required for charts").pack(pady=20)
        return

    x = df[df.columns[0]]
    y = df[df.columns[1]]

    fig, ax = plt.subplots(figsize=(6, 4))

    if chart_type == "bar":
        ax.bar(x, y)
        ax.set_title("Bar Chart")
    elif chart_type == "line":
        ax.plot(x, y, marker="o")
        ax.set_title("Line Chart")
    elif chart_type == "pie":
        ax.pie(y, labels=x, autopct="%1.1f%%")
        ax.set_title("Pie Chart")
    else:
        return

    win = ctk.CTkToplevel()
    win.title("Chart")

    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack()

# MENU FOR DISPLAY OPTIONS
def choose_display(df):
    win = ctk.CTkToplevel()
    win.title("Display Options")
    win.geometry("300x300")

    ctk.CTkLabel(win, text="Choose display method").pack(pady=10)

    ctk.CTkButton(win, text="Table", command=lambda: show_table(df)).pack(pady=10)
    ctk.CTkButton(win, text="Bar Chart", command=lambda: show_plot(df, "bar")).pack(pady=10)
    ctk.CTkButton(win, text="Line Chart", command=lambda: show_plot(df, "line")).pack(pady=10)
    ctk.CTkButton(win, text="Pie Chart", command=lambda: show_plot(df, "pie")).pack(pady=10)

# ANALYTICS FUNCTIONS
def total_revenue():
    df = run_query("""
        SELECT SUM(price * quantity) AS TotalRevenue
        FROM OrderItems;
    """)
    choose_display(df)

def customers_revenue():
    df = run_query("""
        SELECT c.name AS Customer, SUM(oi.price * oi.quantity) AS Revenue
        FROM Customers c
        JOIN Orders o ON c.id = o.customer_id
        JOIN OrderItems oi ON o.id = oi.order_id
        GROUP BY c.id
        ORDER BY Revenue DESC;
    """)
    choose_display(df)

def top_products():
    df = run_query("""
        SELECT product AS Product, SUM(price * quantity) AS Revenue
        FROM OrderItems
        GROUP BY product
        ORDER BY Revenue DESC;
    """)
    choose_display(df)

def average_order_value():
    df = run_query("""
        SELECT AVG(order_total) AS AverageOrderValue
        FROM (
            SELECT o.id, SUM(oi.price * oi.quantity) AS order_total
            FROM Orders o
            JOIN OrderItems oi ON o.id = oi.order_id
            GROUP BY o.id
        );
    """)
    choose_display(df)

def orders_by_month():
    df = run_query("""
        SELECT substr(order_date, 1, 7) AS Month, COUNT(*) AS OrdersCount
        FROM Orders
        GROUP BY Month;
    """)
    choose_display(df)

# MAIN GUI WINDOW
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Sales Analytics Dashboard")
app.geometry("400x500")

ctk.CTkLabel(app, text="Sales Analytics", font=("Arial", 20)).pack(pady=20)

ctk.CTkButton(app, text="Total Revenue", command=total_revenue).pack(pady=10)
ctk.CTkButton(app, text="Revenue by Customers", command=customers_revenue).pack(pady=10)
ctk.CTkButton(app, text="Top Products", command=top_products).pack(pady=10)
ctk.CTkButton(app, text="Average Order Value", command=average_order_value).pack(pady=10)
ctk.CTkButton(app, text="Orders by Month", command=orders_by_month).pack(pady=10)

# SAFE WINDOW CLOSING
def on_closing():
    try:
        app.destroy()
    except:
        pass

app.protocol("WM_DELETE_WINDOW", on_closing)

app.mainloop()
