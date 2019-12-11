import MySQLdb 

print("Connecting to database using MySQLdb") 

db_connection = MySQLdb.connect(host='mysql683.loopia.se', db='swe3d_com', user='Test@s261825', passwd='bsgwPS6pyE4mcEqfkVW9JcvmndGF5QqeTqXDGWsquEJ6hFjZfdzqYWvL6pMULAVDYqmw9Hsu9yQgXKQHTpbrcUaEhveLAeu3C9nSBXtyav9g5uCZ2eRx37y2k5bqDVczjgpWdRKvpcG4CpgyspajkBv6pur6VL5N9vhu2D9gwSvDFJpBZcd6SLeKv76ncQtPdffyTbCFvtmAJtbpukur9PzAwuZ2ZZR24HPNXRnrWcxjZFypuSG9hyUnbcTZDC') 

print("Succesfully Connected to database using MySQLdb!") 

db_connection.close()