from PyQt5 import QtWidgets, QtCore
from inventory_Dashboard import Ui_MainWindow as DashboardUI
from inventory_Customers_Page import Ui_MainWindow as CustomersUI
from inventory_Suppliers_Page import Ui_MainWindow as SuppliersUI
from inventory_Product_Page import Ui_MainWindow as ProductsUI
from inventory_Purchase_Product_Page import Ui_MainWindow as PurchaseProductsUI
from inventory_Outgoing_Page import Ui_MainWindow as OutgoingProductsUI
from inventory_System_Users_Page import Ui_MainWindow as SystemUsersUI
from inventory_Category_Page import Ui_MainWindow as CategoryUI
from add_category_form import Ui_MainWindow as AddCategoryUI
from add_product_form import Ui_MainWindow as AddProductUI
from add_suppliers_form import Ui_MainWindow as AddSupplierUI
from add_outgoing_form import Ui_MainWindow as AddOutgoingProductUI
from add_purchase_form import Ui_MainWindow as AddPurchaseProductUI
from add_customer_form import Ui_MainWindow as AddCustomerUI
from add_system_user_form import Ui_MainWindow as AddSystemUserUI
from database import Database


class InventoryRouter(QtWidgets.QMainWindow):
    def export_table_to_pdf(self):
        if hasattr(self.current_widget.ui, 'tableWidget'):
            tableWidget = self.current_widget.ui.tableWidget
            file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save PDF File", "", "PDF Files (*.pdf)")
            if not file_name:
                return
           
            from reportlab.lib.pagesizes import letter
            from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
            from reportlab.lib import colors
           
            data = []
            headers = [tableWidget.horizontalHeaderItem(i).text() for i in range(tableWidget.columnCount())]
            data.append(headers)
           
            for row in range(tableWidget.rowCount()):
                row_data = []
                for col in range(tableWidget.columnCount()):
                    item = tableWidget.item(row, col)
                    row_data.append(item.text() if item else "")
                data.append(row_data)
           
            pdf = SimpleDocTemplate(file_name, pagesize=letter)
            table = Table(data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            pdf.build([table])
            QtWidgets.QMessageBox.information(self, "Export Successful", "Table data exported successfully as PDF!")
    def export_table_to_excel(self):
        if hasattr(self.current_widget.ui, 'tableWidget'):
            tableWidget = self.current_widget.ui.tableWidget
            file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Excel File", "", "Excel Files (*.xlsx)")
            if not file_name:
                return
           
            import pandas as pd
            data = []
            headers = [tableWidget.horizontalHeaderItem(i).text() for i in range(tableWidget.columnCount())]
            for row in range(tableWidget.rowCount()):
                row_data = []
                for col in range(tableWidget.columnCount()):
                    item = tableWidget.item(row, col)
                    row_data.append(item.text() if item else "")
                data.append(row_data)
           
            df = pd.DataFrame(data, columns=headers)
            df.to_excel(file_name, index=False)
            QtWidgets.QMessageBox.information(self, "Export Successful", "Table data exported successfully as Excel!")
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Management System")
        self.setGeometry(100, 100, 950, 650)
       
        self.current_widget = None
        self.initUI()
   
    def initUI(self):
        self.load_dashboard()
   
    def load_dashboard(self):
        print("Switching to Dashboard")
        self.switch_page(DashboardUI)
   
    def load_customers(self):
        print("Switching to Customers")
        self.switch_page(CustomersUI)
   
    def load_suppliers(self):
        print("Switching to Suppliers - Button Clicked!")
        self.switch_page(SuppliersUI)
   
    def load_products(self):
        print("Switching to Products - Button Clicked!")
        self.switch_page(ProductsUI)
   
    def load_purchase_products(self):
        print("Switching to Purchase Products")
        self.switch_page(PurchaseProductsUI)
   
    def load_outgoing_products(self):
        print("Switching to Outgoing Products")
        self.switch_page(OutgoingProductsUI)
   
    def load_system_users(self):
        print("Switching to System Users")
        self.switch_page(SystemUsersUI)
   
    def load_category(self):
        print("Switching to Category")
        self.switch_page(CategoryUI)
   
    def switch_page(self, ui_class):
        if self.current_widget:
            self.current_widget.deleteLater()
        self.current_widget = PageWrapper(ui_class)
        self.setCentralWidget(self.current_widget)
       
        # Debug: Print available UI elements
        print("Loaded UI Elements:", dir(self.current_widget.ui))
       
        # Connect existing Actions column buttons if present
        if hasattr(self.current_widget.ui, 'tableWidget'):
            self.connect_actions_buttons(self.current_widget.ui.tableWidget)
       
        # Connect Add Category, Add Customer, Add Product, Add Supplier, Add Outgoing Product, Add Purchase Product & Add System User Buttons
        if hasattr(self.current_widget.ui, 'add_Category_Btn'):
            self.current_widget.ui.add_Category_Btn.clicked.connect(self.show_add_category_form)
        if hasattr(self.current_widget.ui, 'add_customer_Btn'):
            self.current_widget.ui.add_customer_Btn.clicked.connect(self.show_add_customer_form)
        if hasattr(self.current_widget.ui, 'add_product_Btn'):
            self.current_widget.ui.add_product_Btn.clicked.connect(self.show_add_product_form)
        if hasattr(self.current_widget.ui, 'add_supplier_Btn'):
            self.current_widget.ui.add_supplier_Btn.clicked.connect(self.show_add_supplier_form)
        if hasattr(self.current_widget.ui, 'add_Outgoing_Product_Btn'):
            self.current_widget.ui.add_Outgoing_Product_Btn.clicked.connect(self.show_add_outgoing_product_form)
        if hasattr(self.current_widget.ui, 'add_Purchase_Product_Btn'):
            self.current_widget.ui.add_Purchase_Product_Btn.clicked.connect(self.show_add_purchase_product_form)
        if hasattr(self.current_widget.ui, 'add_system_users_Btn'):
                self.current_widget.ui.add_system_users_Btn.clicked.connect(self.show_add_system_user_form)
        if hasattr(self.current_widget.ui, 'exportExcel_Btn'):
            self.current_widget.ui.exportExcel_Btn.clicked.connect(self.export_table_to_excel)
        if hasattr(self.current_widget.ui, 'exportPDF_Btn'):
            self.current_widget.ui.exportPDF_Btn.clicked.connect(self.export_table_to_pdf)
            self.current_widget.ui.exportExcel_Btn.clicked.connect(self.export_table_to_excel)
           
       
        # Access navbar items (QLabels) and install mouse event filter
        label_mapping = {
            'dashboard_btn': self.load_dashboard,
            'customer_btn': self.load_customers,
            'supplier_btn': self.load_suppliers,
            'product_btn': self.load_products,
            'purchase_product_btn': self.load_purchase_products,
            'outgoing_btn': self.load_outgoing_products,
            'system_users_btn': self.load_system_users,
            'category_btn': self.load_category
        }
       
        for label_name, function in label_mapping.items():
            label = getattr(self.current_widget.ui, label_name, None)
            if isinstance(label, QtWidgets.QLabel):
                print(f"{label_name} found. Making it clickable.")
                label.mousePressEvent = lambda event, func=function: (print(f"{label_name} clicked!"), func())[1]
            else:
                print(f"Warning: {label_name} is not a QLabel (found {type(label)})")
   
    def show_add_category_form(self):
        self.add_category_window = QtWidgets.QMainWindow()
        self.ui = AddCategoryUI()
        self.ui.setupUi(self.add_category_window)
        self.add_category_window.show()
   
    def show_add_customer_form(self):
        self.add_customer_window = QtWidgets.QMainWindow()
        self.ui = AddCustomerUI()
        self.ui.setupUi(self.add_customer_window)
        self.add_customer_window.show()
   
    def show_add_product_form(self):
        self.add_product_window = QtWidgets.QMainWindow()
        self.ui = AddProductUI()
        self.ui.setupUi(self.add_product_window)
        self.add_product_window.show()
   
    def show_add_supplier_form(self):
        self.add_supplier_window = QtWidgets.QMainWindow()
        self.ui = AddSupplierUI()
        self.ui.setupUi(self.add_supplier_window)
        self.add_supplier_window.show()
   
    def show_add_outgoing_product_form(self):
        self.add_outgoing_product_window = QtWidgets.QMainWindow()
        self.ui = AddOutgoingProductUI()
        self.ui.setupUi(self.add_outgoing_product_window)
        self.add_outgoing_product_window.show()
   
    def show_add_purchase_product_form(self):
        self.add_purchase_product_window = QtWidgets.QMainWindow()
        self.ui = AddPurchaseProductUI()
        self.ui.setupUi(self.add_purchase_product_window)
        self.add_purchase_product_window.show()
   
    def show_add_system_user_form(self):
        self.add_system_user_window = QtWidgets.QMainWindow()
        self.ui = AddSystemUserUI()
        self.ui.setupUi(self.add_system_user_window)
        self.add_system_user_window.show()
   
    def connect_actions_buttons(self, tableWidget):
        column_count = tableWidget.columnCount()
        tableWidget.setColumnCount(column_count + 1)
        tableWidget.setHorizontalHeaderItem(column_count, QtWidgets.QTableWidgetItem("Actions"))
       
        for row in range(tableWidget.rowCount()):
            delete_btn = QtWidgets.QPushButton("Delete")
            delete_btn.setStyleSheet("background-color: red; color: white; font-family: 'Nirmala UI'; font-size: 14px; border: none; padding: 2px;")
            delete_btn.clicked.connect(lambda _, r=row: self.delete_record(r))
            tableWidget.setCellWidget(row, column_count, delete_btn)
        from PyQt5.QtWidgets import QPushButton
       
        column_count = tableWidget.columnCount() - 1  # Assuming last column is 'Actions'
       
        for row in range(tableWidget.rowCount()):
            cell_widget = tableWidget.cellWidget(row, column_count)
            if cell_widget:
                edit_btn = cell_widget.findChild(QPushButton, "editBtn")
                delete_btn = cell_widget.findChild(QPushButton, "deleteBtn")
               
                if edit_btn:
                    edit_btn.setStyleSheet("background-color: blue; color: white; padding: 5px; font-family: 'Nirmala UI'; font-size: 9px; border: none;")
                    edit_btn.clicked.connect(lambda _, r=row: self.edit_record(r))
               
                if delete_btn:
                    delete_btn.setStyleSheet("background-color: red; color: white; padding: 5px; font-family: 'Nirmala UI'; font-size: 9px; border: none;")
                    delete_btn.clicked.connect(lambda _, r=row: self.delete_record(r))
   
    def edit_record(self, row):
        record_id = self.current_widget.ui.tableWidget.item(row, 0).text()
        print(f"Edit record ID: {record_id}")
        # Implement edit functionality here
   
    def delete_record(self, row):
        record_id = self.current_widget.ui.tableWidget.item(row, 0).text()
        confirmation = QtWidgets.QMessageBox.question(self, "Delete Record", f"Are you sure you want to delete ID {record_id}?",
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirmation == QtWidgets.QMessageBox.Yes:
            print(f"Deleting record ID: {record_id}")
            self.current_widget.ui.tableWidget.removeRow(row)
            
    def submit_data(self):
        name = self.name_input.text()
        contact = self.contact_input.text()
        email = self.email_input.text()
        address = self.address_input.text()  # Get input from address field
        
        if name and contact and email and address:  # Ensure fields are not empty
            success = db.insert_customer(name, contact, email, address)  # Call insert function
            
            if success:
                QMessageBox.information(self, "Success", "Customer added successfully!")
                self.load_data()  # Refresh table after adding new data
            else:
                QMessageBox.warning(self, "Error", "Failed to add customer.")
        else:
            QMessageBox.warning(self, "Warning", "Please fill all fields.")


           
class PageWrapper(QtWidgets.QMainWindow):
    def __init__(self, ui_class):
        super().__init__()
        self.ui = ui_class()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.centralwidget)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = InventoryRouter()
    window.show()
    sys.exit(app.exec_())