import psycopg2

name = "dem39isb1j7et9" 
user = "mesqnmchvpbzvs"
passwd ="1282b3280b841641ba302d6d1cd636b624269e7cd5519c01f539ff49b4252996" 


conn = psycopg2.connect("host=host address dbname=host dbname user= host db user")

cur = conn.cursor()

cur.execute("INSERT INTO AdmistrativeBudget VALUES (%s, %s, %s, %s, %s")

conn.commit()
conn.close()




