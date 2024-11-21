import random

def daily_sales(available_items, inventory_records, current_day):
    '''
    This function is responsible for updating the sales for a given day.
    ---------------
    Function Input:
    ---------------
    available_items: (integer) Available Tshirts from the previous day.
    inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
    current_day: (integer) Day number which you want to add as the current day. 

    ----------------
    Function Output:
    ----------------
    available_items:(integer) This function returns this integer which updates the available items at the current day.

    The function will also update the inventory_records (For restocking) for a given current day. 
    '''
    
    if current_day % 7 == 0:
        return available_items
    sold_items = random.randint(0, min(200, available_items))
    available_items -= sold_items

    inventory_records[-1][1] = sold_items
    inventory_records[-1][3] = available_items

    return available_items