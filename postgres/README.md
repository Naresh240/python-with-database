# python-with-postgres-database

# Pre-Requisites:
    Postgres Database Setup
    Install python3, pip
# Install Python3,pip
    yum install python3-pip python3-devel -y
# Postgres Database Setup
  [Postgres SetUP](https://github.com/Naresh240/postgres-database-setup/blob/main/README.md)
# Install required modules using below command
    pip3 install -r requirements.txt
# Run Application
    python3 application.py
# Open Port number 5000 with security group and check output with in WebUI
  http://18.205.106.9:5000/
  
  ![image](https://user-images.githubusercontent.com/58024415/104117351-ae2e0600-5346-11eb-8ecd-82b6748c351e.png)
  
  Provide details and Click on submit
  
  ![image](https://user-images.githubusercontent.com/58024415/104117370-d6b60000-5346-11eb-9f29-e4b0c165c7eb.png)

# Go to database and check whether data saved or not:
    su - postgres
    psql
    \c postgres
    select * from Userdetail;
  ![image](https://user-images.githubusercontent.com/58024415/104118537-e423b800-534f-11eb-9c2c-1746cd8f4b73.png)
