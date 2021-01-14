# python-with-mysql-database

# Pre-Requisites:
    Mysql Database Setup
    Install python, pip
# Mysql Database Setup
  [Mysql SetUp](https://github.com/Naresh240/Mysql-Database-Setup/blob/main/README.md)
# Install required modules using below command
    pip install -r requirements.txt
# Run Application
    python application.py
# Open Port number 5000 with security group and check output with in WebUI
  http://18.205.106.9:5000/
  
  ![image](https://user-images.githubusercontent.com/58024415/104117351-ae2e0600-5346-11eb-8ecd-82b6748c351e.png)
  
  Provide details and Click on submit
  
  ![image](https://user-images.githubusercontent.com/58024415/104117370-d6b60000-5346-11eb-9f29-e4b0c165c7eb.png)

# Go to database and check whether data saved or not:
    mysql -u naresh -p
    use mysql;
    select * from Userdetail;
  ![image](https://user-images.githubusercontent.com/58024415/104117397-05cc7180-5347-11eb-9fb0-fb94734a5cd5.png)
