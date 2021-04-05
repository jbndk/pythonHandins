import pandas as pd
import mysql.connector as mysql

#url = 'C:\\Users\\Jonas\\Desktop\\Sem4\\Python\\docker_notebooks\\notebooks\\my_notebooks\\datafiles\\netflix.csv'
#df = pd.read_csv(url)

## connecting to the database using 'connect()' method
db = mysql.connect(
    # connect to the mysql server running in container with service name: db. CAUTION data here are not persisted past container lifespan
    host = "db", # would be localhost if not running in docker
    user = "root",
    passwd = "root",
    db = "db"
)
print(db)
