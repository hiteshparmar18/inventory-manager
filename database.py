import mysql.connector

class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "inventory_db"
        self.conn = None
        self.cursor = None

    def connect(self):
        """Establishes database connection and initializes the cursor."""
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
            print("✅ Database connected successfully!")
            return self.conn
        except mysql.connector.Error as e:
            print(f"❌ Database Connection Error: {e}")
            return None

    def insert_customer(self, name, phone, email, address):
        """Inserts customer data into the database."""
        if not self.conn or not self.cursor:
            print("⚠️ No database connection. Call connect() first.")
            return False

        try:
            query = "INSERT INTO customers (name, phone, email, address) VALUES (%s, %s, %s, %s)"
            values = (name, phone, email, address)
            self.cursor.execute(query, values)
            self.conn.commit()
            print("✅ Customer inserted successfully!")
            return True
        except mysql.connector.Error as e:
            print(f"❌ Error inserting customer: {e}")
            return False
  
    def insert_category(self, name):
        """Inserts category data into the database."""
        if not self.conn or not self.cursor:
            print("⚠️ No database connection. Call connect() first.")
            return False
        
        try:
            query = "INSERT INTO categories (name) VALUES (%s)"
            values = (name,)
            self.cursor.execute(query, values)
            self.conn.commit()
            print("✅ Category inserted successfully!")
            return True
        except mysql.connector.Error as e:
            print(f"❌ Error inserting category: {e}")
            return False 

    def insert_product(self, name, category_id, supplier_id, quantity, price):
        """Inserts product data into the database."""
        if not self.conn or not self.cursor:
            print("⚠️ No database connection. Call connect() first.")
            return False
        
        try:
            query = "INSERT INTO products (name, category_id, supplier_id, quantity, price) VALUES (%s, %s, %s, %s, %s)"
            values = (name, category_id, supplier_id, quantity, price)
            self.cursor.execute(query, values)
            self.conn.commit()
            print("✅ Product inserted successfully!")
            return True
        except mysql.connector.Error as e:
            print(f"❌ Error inserting product: {e}")
            return False
    
    def insert_outgoing_product(self, product_id, quantity, customer_id, outgoing_date):
        """Inserts outgoing product data into the database."""
        if not self.conn or not self.cursor:
            print("⚠️ No database connection. Call connect() first.")
            return False
        
        try:
            query = "INSERT INTO outgoing_stock (product_id, quantity, customer_id, outgoing_date) VALUES (%s, %s, %s, %s)"
            values = (product_id, quantity, customer_id, outgoing_date)
            self.cursor.execute(query, values)
            self.conn.commit()
            print("✅ Outgoing product inserted successfully!")
            return True
        except mysql.connector.Error as e:
            print(f"❌ Error inserting outgoing product: {e}")
            return False
    
    def insert_purchase_product(self, product_id, supplier_id, quantity, price, purchase_date):
        """Inserts purchased product data into the database."""
        if not self.conn or not self.cursor:
            print("⚠️ No database connection. Call connect() first.")
            return False
        
        try:
            query = "INSERT INTO purchases (product_id, supplier_id, quantity, price, purchase_date) VALUES (%s, %s, %s, %s, %s)"
            values = (product_id, supplier_id, quantity, price, purchase_date)
            self.cursor.execute(query, values)
            self.conn.commit()
            print("✅ Purchased product inserted successfully!")
            return True
        except mysql.connector.Error as e:
            print(f"❌ Error inserting purchased product: {e}")
            return False
    
    def insert_system_user(self, username, password_hash, email_id, role):
        """Inserts system user data into the database."""
        if not self.conn or not self.cursor:
            print("⚠️ No database connection. Call connect() first.")
            return False
        
        try:
            query = "INSERT INTO system_users (username, password_hash, email_id, role) VALUES (%s, %s, %s, %s)"
            values = (username, password_hash, email_id, role)
            self.cursor.execute(query, values)
            self.conn.commit()
            print("✅ System user inserted successfully!")
            return True
        except mysql.connector.Error as e:
            print(f"❌ Error inserting system user: {e}")
            return False
    
    def insert_supplier(self, name, phone, email, address):
        """Inserts supplier data into the database."""
        if not self.conn or not self.cursor:
            print("⚠️ No database connection. Call connect() first.")
            return False
        
        try:
            query = "INSERT INTO suppliers (name, phone, email, address) VALUES (%s, %s, %s, %s)"
            values = (name, phone, email, address)
            self.cursor.execute(query, values)
            self.conn.commit()
            print("✅ Supplier inserted successfully!")
            return True
        except mysql.connector.Error as e:
            print(f"❌ Error inserting supplier: {e}")
            return False

    def close(self):
        """Closes the database connection."""
        if self.conn:
            self.cursor.close()
            self.conn.close()
            print("✅ Database connection closed.")

# Example usage:
if __name__ == "__main__":
    db = Database()
    db.connect()
    db.insert_customer("chota don", "1234567890", "don@example.com", "123 Main St")
    db.insert_customer("chota don", "9627419632", "don@example.com", "123 Main India")
    db.insert_category("mobile")
    db.insert_product("Iphone 17 ", 1, 2, 10, 500000)
    db.insert_outgoing_product(1, 2, 1, "2025-04-04")
    db.insert_purchase_product(1, 2, 10, 45000, "2025-04-04")
    db.insert_system_user("chota don", "securepass", "don@example.com", "staff")
    db.insert_supplier("CAC SUPPLIER", "9876540210", "cacsupplier@example.com", "456 old Supplier St")
    db.close()