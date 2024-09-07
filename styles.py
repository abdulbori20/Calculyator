labelStyle = """
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #3498db;
                background-color: #ecf0f1;
                padding: 20px;
                border: 2px solid #2980b9;
                border-radius: 6px;
            }
        """

qlistwidget_style = """
            QListWidget {
                font-size: 20px;
                background-color: #ffffff;
                border: 1px solid #3498db;
                border-radius: 10px;
                padding: 10px;
            }

            QListWidget::item {
                padding: 10px;
                border-radius: 5px;
                background-color: #ecf0f1;
                color: #2c3e50;
            }

            QListWidget::item:selected {
                background-color: #3498db;
                color: #ffffff;
            }

            QListWidget::item:hover {
                background-color: #bdc3c7;
            }
        """