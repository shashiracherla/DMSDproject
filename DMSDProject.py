# -*- coding: utf-8 -*-
"""
Created on Mon May  5 22:16:38 2025

@author: balaji
"""
import os
import sqlite3
from tabulate import tabulate


db_path = "dmsd.db"

conn = sqlite3.connect(db_path)
c = conn.cursor()


insert_initial_rows_for_store = [

"""INSERT INTO CUSTOMER (CID, FName, LName, EMail, Address, Phone, Status) VALUES
(1, 'Raj', 'Kumar', 'raj.kumar@example.com', '1234 Elm St, San Jose, CA 95112', '408-123-4567', 'Silver'),
(2, 'Sanjay', 'Verma', 'sanjay.verma@example.com', '5678 Oak Ave, Austin, TX 78701', '512-234-5678', 'Silver'),
(3, 'Srinivas', 'Rao', 'srinivas.rao@example.com', '9101 Maple Dr, Seattle, WA 98101', '206-345-6789', 'Gold'),
(4, 'Anita', 'Desai', 'anita.desai@example.com', '135 Pine St, Denver, CO 80202', '303-123-7890', 'Silver'),
(5, 'Vikram', 'Singh', 'vikram.singh@example.com', '246 Cedar Ave, Chicago, IL 60616', '773-456-7890', 'Silver'),
(6, 'Meena', 'Joshi', 'meena.joshi@example.com', '357 Birch Rd, Miami, FL 33101', '305-567-8901', 'Gold'),
(7, 'Arjun', 'Mehta', 'arjun.mehta@example.com', '468 Walnut Ln, Boston, MA 02108', '617-234-5678', 'Silver'),
(8, 'Kiran', 'Patel', 'kiran.patel@example.com', '579 Aspen Ct, Portland, OR 97201', '503-345-6789', 'Silver'),
(9, 'Priya', 'Nair', 'priya.nair@example.com', '680 Redwood St, Phoenix, AZ 85001', '602-456-7890', 'Silver'),
(10, 'Rohit', 'Sharma', 'rohit.sharma@example.com', '791 Spruce Dr, Atlanta, GA 30301', '404-567-8901', 'Gold'),
(11, 'Neha', 'Kapoor', 'neha.kapoor@example.com', '802 Sycamore Ln, New York, NY 10001', '212-678-9012', 'Silver'),
(12, 'Ajay', 'Tripathi', 'ajay.tripathi@example.com', '913 Poplar Way, Dallas, TX 75201', '214-789-0123', 'Silver'),
(13, 'Ramesh', 'Iyer', 'ramesh.iyer@example.com', '100 Willow Dr, Columbus, OH 43215', '614-890-1234', 'Silver');""",

"""INSERT INTO SILVER_AND_ABOVE (CID, CreditLine) VALUES
(3, 5000.00),
(6, 3000.00),
(10, 4000.00);""",

"""INSERT INTO CREDIT_CARD (CCNumber, SecNumber, OwnerName, CCType, BilAddress, ExpDate, StoredCardCID) VALUES
('4111111111111111', '123', 'Raj Kumar', 'Visa', '1234 Elm St, San Jose, CA 95112', '2027-05-01', 1),
('5500000000000004', '456', 'Sanjay Verma', 'MasterCard', '5678 Oak Ave, Austin, TX 78701', '2026-11-01', 2),
('3500000000000004', '457', 'Srinivas Rao', 'MasterCard', '5 Central Ave, Newark, NJ 73001', '2027-10-01', 3),
('340000000000009', '789', 'Anita Desai', 'Amex', '135 Pine St, Denver, CO 80202', '2025-09-01', 4),
('640000000000009', '789', 'Meena Joshi', 'Amex', '357 Birch Rd, Miami, FL 33101', '2027-09-01', 6),
('6011000000000004', '321', 'Arjun Mehta', 'Discover', '468 Walnut Ln, Boston, MA 02108', '2028-01-01', 7),
('378282246310005', '654', 'Neha Kapoor', 'Amex', '802 Sycamore Ln, New York, NY 10001', '2026-07-01', 11),
('108282246310005', '654', 'Rohit Sharma', 'Amex', '791 Spruce Dr, Atlanta, GA 30301', '2029-07-01', 10);""",

"""INSERT INTO SHIPPING_ADDRESS (CID, SAName, RecepientName, Street, SNumber, City, Zip, State, Country) VALUES
(1, 'Home', 'Raj Kumar', 'Elm St', '1234', 'San Jose', '95112', 'CA', 'USA'),
(2, 'Work', 'Sanjay Verma', 'Oak Ave', '5678', 'Austin', '78701', 'TX', 'USA'),
(4, 'Main', 'Anita Desai', 'Pine St', '135', 'Denver', '80202', 'CO', 'USA'),
(7, 'Office', 'Arjun Mehta', 'Walnut Ln', '468', 'Boston', '02108', 'MA', 'USA'),
(11, 'Apt', 'Neha Kapoor', 'Sycamore Ln', '802', 'New York', '10001', 'NY', 'USA'),
(3, 'Home', 'Srinivas Rao', 'Maple Dr', '9101', 'Seattle', '98101', 'WA', 'USA'),
(6, 'Home', 'Meena Joshi', 'Birch Rd', '357', 'Miami', '33101', 'FL', 'USA'),
(10, 'Home', 'Rohit Sharma', 'Spruce Dr', '791', 'Atlanta', '30301', 'GA', 'USA');""",

"""INSERT INTO PRODUCT (PID, PType, PName, PPRice, Description, PQuantity) VALUES
(1, 'Computer', 'Dell Inspiron', 700.00, 'Dell desktop with i5 CPU', 10),
(2, 'Laptop', 'HP Pavilion', 950.00, 'Lightweight HP laptop', 5),
(3, 'Printer', 'Canon Pixma', 120.00, 'Color inkjet printer', 8),
(4, 'Laptop', 'Lenovo ThinkPad', 1100.00, 'Business laptop', 6),
(5, 'Computer', 'Mac Mini', 999.00, 'Compact Apple desktop', 4),
(6, 'Printer', 'Brother HL-L2350DW', 150.00, 'Monochrome laser printer', 10),
(7, 'Laptop', 'Asus ZenBook', 850.00, 'Ultra-slim design', 7),
(8, 'Computer', 'Acer Aspire', 650.00, 'Budget desktop', 9),
(9, 'Printer', 'Epson EcoTank', 200.00, 'Ink-efficient printer', 6),
(10, 'Laptop', 'Dell XPS 13', 1300.00, 'Premium ultrabook', 3),
(11, 'Computer', 'HP Envy Desktop', 800.00, 'Performance PC', 5),
(12, 'Printer', 'HP LaserJet', 180.00, 'High-speed laser printer', 8),
(13, 'Laptop', 'Microsoft Surface', 1400.00, 'Tablet-laptop hybrid', 4);""",

"""INSERT INTO COMPUTER (PID, CPUType) VALUES
(2, 'i7'),
(4, 'r5'),
(7, 'r7'),
(10, 'i3'),
(13, 'i9');""",

"""INSERT INTO LAPTOP (PID, BType, Weight) VALUES
(2, 'HP', 2.2),
(4, 'Lenovo', 2.5),
(7, 'Asus', 1.8),
(10, 'Dell', 1.6),
(13, 'Microsoft', 1.2);""",

"""INSERT INTO PRINTER (PID, PrinterType, Resolution) VALUES
(3, 'Inkjet', '1200x600'),
(6, 'Laser', '2400x600'),
(9, 'Inkjet', '4800x1200'),
(12, 'Laser', '1200x1200');""",


"""INSERT INTO OFFER_PRODUCT (PID, OfferPrice) VALUES
(3, 99.99),
(6, 135.00),
(9, 180.00);""",


"""INSERT INTO BASKET (BID, CID) VALUES
(1, 1),
(2, 2),
(3, 4),
(4, 7),
(5, 11),
(6, 3),
(7, 6),
(8, 10),
(9,1),
(10,2),
(11,4),
(12,1);""",


"""INSERT INTO APPEARS_IN (BID, PID, Quantity, PriceSold) VALUES
(1, 1, 1, 700.00),
(1, 3, 1, 99.99),
(2, 2, 1, 950.00),
(3, 5, 1, 999.00),
(3, 6, 2, 270.00),
(4, 7, 1, 850.00),
(4, 9, 1, 180.00),
(5, 10, 1, 1300.00),
(5, 12, 1, 180.00),
(6, 12, 1, 180.00),
(6, 1, 1, 700.00),
(7, 1, 1, 700.00),
(7, 5, 1, 999.00),
(8, 1, 1, 700.00),
(8, 10, 1, 1300.00),
(12, 12, 1, 180.00),
(11, 12, 1, 180.00),
(11, 3, 1, 99.00);""",


"""INSERT INTO `TRANSACTION` (BID, CCNumber, CID, SAName, TDate, TTag) VALUES
(1, '4111111111111111', 1, 'Home', '2025-05-01', 'Order Placed'),
(2, '5500000000000004', 2, 'Work', '2025-05-03', 'Order Placed'),
(3, '340000000000009', 4, 'Main', '2025-05-04', 'Order Processed'),
(4, '6011000000000004', 7, 'Office', '2025-05-05', 'Order Processed'),
(5, '378282246310005', 11, 'Apt', '2025-05-06', 'Order Placed'),
(6, '3500000000000004', 3, 'Home', '2025-05-07', 'Order Placed'),
(7, '640000000000009', 6, 'Home', '2025-05-08', 'Order Placed'),
(8, '108282246310005', 10, 'Home', '2025-05-09', 'Order Placed'),
(11, '340000000000009', 4, 'Main', '2025-05-10', 'Order Placed');"""
]




def addCustomer():
    print("Add New Customer")
    print("Input Schema: CID,FName,LName,EMail,Address,Phone,Status")
    try:
        data = input("Enter customer data: ").strip().split(',')
        if len(data) != 7:
            raise ValueError("no of fields mismatch")
        
        cid = int(data[0].strip())
        fname = data[1].strip()
        lname = data[2].strip()
        email = data[3].strip()
        address = data[4].strip() or None
        phone = data[5].strip() or None
        status = data[6].strip() or None
        c.execute("INSERT INTO CUSTOMER VALUES (?,?,?,?,?,?,?)",
                  (cid, fname, lname, email, address, phone, status))
        if status==["Gold"]:
            creditLine = float(input("Enter the credit line\n").strip())
            c.execute("INSERT INTO SILVER_AND_ABOVE VALUES (?,?)",
                  (cid, creditLine))
        conn.commit()
        print("Customer added")

    except Exception as e:
        print(f"Error: {str(e)}")

def addCreditCard():
    print("Add New Credit Card")
    print("Input Schema: CCNumber,SecNumber,OwnerName,CCType,BilAddress,ExpDate,StoredCardCID")
    try:
        data = input("Enter credit card data: ").strip().split(',')
        if len(data) != 7:
            raise ValueError("no of fields mismatch")
        
        cc_number = data[0].strip()
        sec = data[1].strip()
        owner = data[2].strip()
        ctype = data[3].strip()
        bil_address = data[4].strip()
        exp_date = data[5].strip()
        cid = int(data[6].strip())
        c.execute("INSERT INTO CREDIT_CARD VALUES (?,?,?,?,?,?,?)",
                  (cc_number, sec, owner, ctype, bil_address, exp_date, cid))
        conn.commit()
        print("Credit card added")

    except Exception as e:
        print(f"Error: {str(e)}")

def addShippingAddress():
    print("Add New Shipping Address")
    print("Input schema: CID,SAName,RecepientName,Street,SNumber,City,Zip,State,Country")
    try:
        data = input("Enter shipping address data: ").strip().split(',')
        if len(data) != 9:
            raise ValueError("no of fields mismatch")
        
        cid = int(data[0].strip())
        sa_name = data[1].strip()
        recipient = data[2].strip()
        street = data[3].strip()
        snumber = data[4].strip()
        city = data[5].strip()
        zipcode = data[6].strip()
        state = data[7].strip()
        country = data[8].strip()
        c.execute("INSERT INTO SHIPPING_ADDRESS VALUES (?,?,?,?,?,?,?,?,?)",
                  (cid, sa_name, recipient, street, snumber, city, zipcode, state, country))
        conn.commit()
        print("Shipping address Added")

    except Exception as e:
        print(f"Error: {str(e)}")

def modCustomer():
    print("Modify Customer")
    try:
        cid = int(input("Enter CID to modify: "))
        # Check customer exists
        c.execute("SELECT * FROM CUSTOMER WHERE CID=?", (cid,))
        if not c.fetchone():
            print("Error: Customer not found!")
            return

        print("Leave blank to keep current value")
        new_fname = input("New First Name: ").strip()
        new_lname = input("New Last Name: ").strip()
        new_email = input("New Email: ").strip()
        new_address = input("New Address: ").strip()
        new_phone = input("New Phone: ").strip()
        new_status = input("New Status: ").strip()

        updates = []
        params = []
        if new_fname:
            updates.append("FName=?")
            params.append(new_fname)
        if new_lname:
            updates.append("LName=?")
            params.append(new_lname)
        if new_email:
            updates.append("EMail=?")
            params.append(new_email)
        if new_address != "":
            updates.append("Address=?")
            params.append(new_address if new_address else None)
        if new_phone != "":
            updates.append("Phone=?")
            params.append(new_phone if new_phone else None)
        if new_status != "":
            updates.append("Status=?")
            params.append(new_status if new_status else None)

        if not updates:
            print("No changes made.")
            return

        params.append(cid)
        query = f"UPDATE CUSTOMER SET {','.join(updates)} WHERE CID=?"
        c.execute(query, params)
        conn.commit()
        print("Customer updated")
    except Exception as e:
        print(f"Error: {str(e)}")

def modCreditCard():
    print("Modify Credit Card")
    try:
        cc_number = input("Enter CC Number to modify: ").strip()
        c.execute("SELECT * FROM CREDIT_CARD WHERE CCNumber=?", (cc_number,))
        if not c.fetchone():
            print("Error: Credit card not found")
            return

        print("Leave blank to keep current value")
        new_sec = input("New Security Code: ").strip()
        new_owner = input("New Owner Name: ").strip()
        new_type = input("New Card Type: ").strip()
        new_bil = input("New Billing Address: ").strip()
        new_exp = input("New Expiry Date: ").strip()

        updates = []
        params = []
        if new_sec:
            updates.append("SecNumber=?")
            params.append(new_sec)
        if new_owner:
            updates.append("OwnerName=?")
            params.append(new_owner)
        if new_type:
            updates.append("CCType=?")
            params.append(new_type)
        if new_bil:
            updates.append("BilAddress=?")
            params.append(new_bil)
        if new_exp:
            updates.append("ExpDate=?")
            params.append(new_exp)

        if not updates:
            print("No changes made.")
            return

        params.append(cc_number)
        query = f"UPDATE CREDIT_CARD SET {','.join(updates)} WHERE CCNumber=?"
        c.execute(query, params)
        conn.commit()
        print("Credit card updated")

    except Exception as e:
        print(f"Error: {str(e)}")

def modShippingAddress():
    print("\n--- Modify Shipping Address ---")
    try:
        cid = int(input("Customer ID (CID): "))
        sa_name = input("Address Nickname: ").strip()
        # Check address exists
        c.execute("SELECT * FROM SHIPPING_ADDRESS WHERE CID=? AND SAName=?", (cid, sa_name))
        if not c.fetchone():
            print("Error: Shipping address not found!")
            return

        print("Leave blank to keep current value")
        new_recipient = input("New Recipient Name: ").strip()
        new_street = input("New Street: ").strip()
        new_snumber = input("New Street Number: ").strip()
        new_city = input("New City: ").strip()
        new_zip = input("New Zip: ").strip()
        new_state = input("New State: ").strip()
        new_country = input("New Country: ").strip()

        updates = []
        params = []
        if new_recipient:
            updates.append("RecepientName=?")
            params.append(new_recipient)
        if new_street:
            updates.append("Street=?")
            params.append(new_street)
        if new_snumber:
            updates.append("SNumber=?")
            params.append(new_snumber)
        if new_city:
            updates.append("City=?")
            params.append(new_city)
        if new_zip:
            updates.append("Zip=?")
            params.append(new_zip)
        if new_state:
            updates.append("State=?")
            params.append(new_state)
        if new_country:
            updates.append("Country=?")
            params.append(new_country)

        if not updates:
            print("No changes made.")
            return

        params.extend([cid, sa_name])
        query = f"UPDATE SHIPPING_ADDRESS SET {','.join(updates)} WHERE CID=? AND SAName=?"
        c.execute(query, params)
        conn.commit()
        print("Shipping address")

    except Exception as e:
        print(f"Error: {str(e)}")

def createBasket():
    print("Create shopping basket")
    print("Input Schema: BID,CID")
    try:
        data = input("Enter basket data: ").strip().split(',')
        if len(data) != 2:
            raise ValueError("no of fields mismatch")
        bid=int(data[0].strip())
        cid=int(data[1].strip())
        c.execute("INSERT INTO BASKET VALUES (?,?)", (bid,cid))
    except Exception as e:
        print(f"Error: {str(e)}")

def addItemToBasket():
    print("Add Item to basket")
    print("Input Schema: BID,PID,Quantity,PriceSold")
    try:
        data = input("Enter data required: ").strip().split(',')
        if len(data) != 4:
            raise ValueError("no of fields mismatch")
        
        bid = int(data[0].strip())
        pid = int(data[1].strip())
        quantity = int(data[2].strip())
        price = float(data[3].strip())
        c.execute("INSERT INTO APPEARS_IN VALUES (?,?,?,?)",(bid,pid,quantity,price))
        conn.commit()
        print("item added")
    except Exception as e:
        print(f"Error: {str(e)}")

def placeOrder():
    print("Place Order")
    print("Input Schema: BID,CCNumber,CID,SAName,TDate")
    try:
        data = input("Enter order data: ").strip().split(',')
        if len(data) != 5:
            raise ValueError("no of fields mismatch")
        
        bid = int(data[0].strip())
        ccnumber = data[1].strip()
        cid = int(data[2].strip())
        saname = data[3].strip()
        tdate = data[4].strip()
        ttag = "Order Placed"
        c.execute("INSERT INTO `TRANSACTION` VALUES (?,?,?,?,?,?)",(bid,ccnumber,cid,saname,tdate,ttag))
        conn.commit()
        print("Order Placed")
    except Exception as e:
        print(f"Error: {str(e)}")

def processOrder():
    print("process Order")
    try:
        data = input("Enter Order to process:\n Input Schema:  BID, CCNumber, CID,SAName\n").strip().split(',')
        if len(data) != 4:
            raise ValueError("no of fields mismatch")
        bid = int(data[0].strip())
        ccnumber = data[1].strip()
        cid = int(data[2].strip())
        saname = data[3].strip()
        c.execute("SELECT * FROM `TRANSACTION` WHERE BID=? AND CCNumber=? AND CID=? AND SAName=?", (bid,ccnumber,cid,saname))
        if not c.fetchone():
            print("Error: Order not found!")
            return
        query = f"UPDATE `TRANSACTION` SET TTag=? WHERE BID=? AND CCNumber=? AND CID=? AND SAName=?"
        c.execute(query, ("Order Processed",bid,ccnumber,cid,saname) )
        conn.commit()
        print("Order Processed")
    except Exception as e:
        print(f"Error: {str(e)}")

def totalAmountPerCredit():
    query="""
    SELECT
        T.CCNumber,
        SUM(AI.PriceSold * AI.Quantity) AS TotalAmountCharged
    FROM
        `TRANSACTION` T
    JOIN
        APPEARS_IN AI ON T.BID = AI.BID
    GROUP BY
        T.CCNumber;
    """
    c.execute(query)
    rows = c.fetchall()

    # Get column names
    column_names = [description[0] for description in c.description]

    # Display data as a table
    print(tabulate(rows, headers=column_names, tablefmt="grid"))

def bestCustomers():
    query="""
    SELECT
        C.CID,
        C.FName,
        C.LName,
        SUM(AI.PriceSold * AI.Quantity) AS TotalMoneySpent
    FROM
        CUSTOMER C
    JOIN
        BASKET B ON C.CID = B.CID
    JOIN
        APPEARS_IN AI ON B.BID = AI.BID
    GROUP BY
        C.CID, C.FName, C.LName
    ORDER BY
        TotalMoneySpent DESC
    LIMIT 10;
    """
    c.execute(query)
    rows = c.fetchall()

    # Get column names
    column_names = [description[0] for description in c.description]

    # Display data as a table
    print(tabulate(rows, headers=column_names, tablefmt="grid"))

def frequentProducts():
    query="""
    SELECT
        P.PID,
        P.PName,
        SUM(AI.Quantity) AS TotalQuantitySold
    FROM
        PRODUCT P
    JOIN
        APPEARS_IN AI ON P.PID = AI.PID
    JOIN
        `TRANSACTION` T ON AI.BID = T.BID
    WHERE
        T.TDate BETWEEN date(?) AND date(?)
    GROUP BY
        P.PID, P.PName
    ORDER BY
        TotalQuantitySold DESC
    LIMIT 5;
    """
    date1=input("Please Enter the begining date in YYYY-MM-DD format\n").strip()
    date2=input("Please Enter the ending date in YYYY-MM-DD format\n").strip()
    c.execute(query,(date1,date2))
    rows = c.fetchall()

    # Get column names
    column_names = [description[0] for description in c.description]

    # Display data as a table
    print(tabulate(rows, headers=column_names, tablefmt="grid"))

def productsToDistinctCustomers():
    query="""
    SELECT
        P.PID,
        P.PName,
        COUNT(DISTINCT B.CID) AS NumberOfDistinctCustomers
    FROM
        PRODUCT P
    JOIN
        APPEARS_IN AI ON P.PID = AI.PID
    JOIN
        BASKET B ON AI.BID = B.BID
    JOIN
        `TRANSACTION` T ON B.BID = T.BID
    WHERE
        T.TDate BETWEEN date(?) AND date(?)
    GROUP BY
        P.PID, P.PName
    ORDER BY
        NumberOfDistinctCustomers DESC
    LIMIT 5;
    """
    date1=input("Please Enter the begining date in YYYY-MM-DD format\n").strip()
    date2=input("Please Enter the ending date in YYYY-MM-DD format\n").strip()
    c.execute(query,(date1,date2))
    rows = c.fetchall()

    # Get column names
    column_names = [description[0] for description in c.description]

    # Display data as a table
    print(tabulate(rows, headers=column_names, tablefmt="grid"))

def maxBasketTotalCC():
    query="""
    WITH BasketTotals AS (
        SELECT
            T.CCNumber,
            T.BID,
            SUM(AI.PriceSold * AI.Quantity) AS BasketTotalAmount
        FROM
            `TRANSACTION` T
        JOIN
            APPEARS_IN AI ON T.BID = AI.BID
        WHERE
            T.TDate BETWEEN date(?) AND date(?)
        GROUP BY
            T.CCNumber, T.BID
    )
    SELECT
        BT.CCNumber,
        MAX(BT.BasketTotalAmount) AS MaxBasketTotalAmount
    FROM
        BasketTotals BT
    GROUP BY
        BT.CCNumber;
    """
    date1=input("Please Enter the begining date in YYYY-MM-DD format\n").strip()
    date2=input("Please Enter the ending date in YYYY-MM-DD format\n").strip()
    c.execute(query,(date1,date2))
    rows = c.fetchall()

    # Get column names
    column_names = [description[0] for description in c.description]

    # Display data as a table
    print(tabulate(rows, headers=column_names, tablefmt="grid"))

def averageSPPerPT():
    query="""
    SELECT
        P.PType,
        AVG(AI.PriceSold) AS AverageSellingPrice
    FROM
        PRODUCT P
    JOIN
        APPEARS_IN AI ON P.PID = AI.PID
    JOIN
        `TRANSACTION` T ON AI.BID = T.BID
    WHERE
        T.TDate BETWEEN date(?) AND date(?)
        AND P.PType IN (SELECT DISTINCT P.PType FROM PRODUCT)
    GROUP BY
        P.PType;
    """
    date1=input("Please Enter the begining date in YYYY-MM-DD format\n").strip()
    date2=input("Please Enter the ending date in YYYY-MM-DD format\n").strip()
    c.execute(query,(date1,date2))
    rows = c.fetchall()

    # Get column names
    column_names = [description[0] for description in c.description]

    # Display data as a table
    print(tabulate(rows, headers=column_names, tablefmt="grid"))

def showTransactions():
    query="""
    SELECT
        T.BID AS TransactionBasketID,
        T.TDate AS TransactionDate,
        T.TTag AS TransactionTag,
        C.FName AS CustomerFirstName,
        C.LName AS CustomerLastName,
        C.EMail AS CustomerEmail,
        P.PName AS ProductName,
        P.PType AS ProductType,
        AI.Quantity AS QuantitySold,
        AI.PriceSold AS PricePerItem,
        (AI.Quantity * AI.PriceSold) AS ItemTotalAmount,
        T.CCNumber AS CreditCardNumberUsed
    FROM
        `TRANSACTION` T
    JOIN
        APPEARS_IN AI ON T.BID = AI.BID
    JOIN
        PRODUCT P ON AI.PID = P.PID
    JOIN
        BASKET BSK ON T.BID = BSK.BID
    JOIN
        CUSTOMER C ON BSK.CID = C.CID
    WHERE
        1=1
    """
    params=[]
    fname=input("Enter First Name to Filter By\n").strip()
    if fname:
        query+="""
        AND C.FName LIKE ?
        """
        params.append(f'%{fname}%')
    lname=input("Enter Last Name to Filter By\n").strip()
    if lname:
        query+="""
        AND C.LName LIKE ?
        """
        params.append(f'%{lname}%')
    pname=input("Enter Product Name to Filter By\n").strip()
    if pname:
        query+="""
        AND P.PName LIKE ?
        """
        params.append(f'%{pname}%')
    date1=input("Please Enter the begining date in YYYY-MM-DD format\n").strip()
    date2=input("Please Enter the ending date in YYYY-MM-DD format\n").strip()
    if date1 and date2:
        query+="""
        AND T.TDate BETWEEN date(?) AND date(?)
        """
        params.append(date1)
        params.append(date2)
    if params==[]:
        print("Filter Parameters are incorrect")
        return
    query+="""
    ORDER BY
        T.TDate DESC, T.BID;
    """
    c.execute(query,params)
    rows = c.fetchall()

    # Get column names
    column_names = [description[0] for description in c.description]

    # Display data as a table
    print(tabulate(rows, headers=column_names, tablefmt="grid"))

def showCustomers():
    query="""
    SELECT
        *
    FROM
        CUSTOMER;
    """
    c.execute(query)
    rows = c.fetchall()

    # Get column names
    column_names = [description[0] for description in c.description]

    # Display data as a table
    print(tabulate(rows, headers=column_names, tablefmt="grid"))

def showCreditCards():
    query="""
    SELECT
        *
    FROM
        CREDIT_CARD;
    """
    c.execute(query)
    rows = c.fetchall()

    # Get column names
    column_names = [description[0] for description in c.description]

    # Display data as a table
    print(tabulate(rows, headers=column_names, tablefmt="grid"))

def showShippingAddress():
    query="""
    SELECT
        *
    FROM
        SHIPPING_ADDRESS;
    """
    c.execute(query)
    rows = c.fetchall()

    # Get column names
    column_names = [description[0] for description in c.description]

    # Display data as a table
    print(tabulate(rows, headers=column_names, tablefmt="grid"))

def deleteAndLoadData():
    global conn
    global c
    conn.close()
    if os.path.exists(db_path):
        os.remove(db_path)
    print(f"File '{db_path}' deleted successfully.")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    with open("dmsd.txt", "r") as schema_file:
        schema_sql = schema_file.read()
    c.executescript(schema_sql)
    for stmt in insert_initial_rows_for_store:
        c.execute(stmt)

def showCreditLine():
    query="""
    SELECT
        S.CID,S.CreditLine,C.FName,C.LName
    FROM
        SILVER_AND_ABOVE S
    JOIN CUSTOMER C ON S.CID=C.CID;
    """
    c.execute(query)
    rows = c.fetchall()

    # Get column names
    column_names = [description[0] for description in c.description]

    # Display data as a table
    print(tabulate(rows, headers=column_names, tablefmt="grid"))

while(True):
    print("Use below options to manage the IT Store DB")
    print("0: To Save and Exit")
    print("1: Add Customer")
    print("2: Add Credit Card")
    print("3: Add Shipping Address")
    print("4: Modify Customer")
    print("5: Modify Credit Card")
    print("6: Modify Shipping Address")
    print("7: Create Basket")
    print("8: Add Item to basket")
    print("9: Process Order")
    print("10: Show Total amount charged per credit card")
    print("11: Show the 10 best customers")
    print("12: Show the 5 most frequently sold products")
    print("13: Show the products which are sold to the highest number of distinct customers")
    print("14: Shoe Maximum Basket Total amount per credit card")
    print("15: Show the average selling product price per product type")
    print("16: Show Transaction History")
    print("17: Show Customers")
    print("18: Show Credit Cards")
    print("19: Show Shipping Address")
    print("20: Delete DB and Load Data")
    print("21: Show Credit Line")
    cmd=input("Enter the option as required\n")
    if(cmd=='0'):
        break
    elif(cmd=='1'):
        addCustomer()
    elif(cmd=='2'):
        addCreditCard()
    elif(cmd=='3'):
        addShippingAddress()
    elif(cmd=='4'):
        modCustomer()
    elif(cmd=='5'):
        modCreditCard()
    elif(cmd=='6'):
        modShippingAddress()
    elif(cmd=='7'):
        createBasket()
    elif(cmd=='8'):
        addItemToBasket()
    elif(cmd=='9'):
        placeOrder()
    elif(cmd=='10'):
        totalAmountPerCredit()
    elif(cmd=='11'):
        bestCustomers()
    elif(cmd=='12'):
        frequentProducts()
    elif(cmd=='13'):
        productsToDistinctCustomers()
    elif(cmd=='14'):
        maxBasketTotalCC()
    elif(cmd=='15'):
        averageSPPerPT()
    elif(cmd=='16'):
        showTransactions()
    elif(cmd=='17'):
        showCustomers()
    elif(cmd=='18'):
        showCreditCards()
    elif(cmd=='19'):
        showShippingAddress()
    elif(cmd=='20'):
        deleteAndLoadData()
    elif(cmd=='21'):
        showCreditLine()
    else:
        print("Selected Option does not exist")
        
# Commit and close
conn.commit()
conn.close()

print("Thanks for shopping")
