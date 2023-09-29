from flask import Flask, render_template, request, redirect, url_for, jsonify
import psycopg2

app = Flask(__name__)

# # Connect to the database
# conn = psycopg2.connect(database="flask_db", user="postgres",
# 						password="root", host="localhost", port="5432")

# # create a cursor
# cur = conn.cursor()

# # if you already have any table or not id doesnt matter this
# # will create a products table for you.
# cur.execute(
# 	'''CREATE TABLE IF NOT EXISTS products (id serial \
# 	PRIMARY KEY, name varchar(100), price float);''')

# # Insert some data into the table
# cur.execute(
# 	'''INSERT INTO products (name, price) VALUES \
# 	('Apple', 1.99), ('Orange', 0.99), ('Banana', 0.59);''')

# # commit the changes
# conn.commit()

# # close the cursor and connection
# cur.close()
# conn.close()


@app.route('/')
def index():
	try:
	# Connect to the database
		conn = psycopg2.connect(database="video_clip_backend",
								user="luken",
								password="",
								host="localhost", port="5432")

	# create a cursor
		cur = conn.cursor()	

	# Select all products from the table
		cur.execute('''SELECT * FROM users''')

	# Fetch the data
		data = cur.fetchall()

	# close the cursor and connection
		cur.close()
		conn.close()

		result = []
		for row in data:
				result.append({
						'id': row[0],  # Assuming the first column is the ID
						'email': row[1],  # Replace 'name' with your column names
						'password': row[2],
						# Add more fields as needed
			})

		return jsonify(result)

	except Exception as e:
		return jsonify({'error': str(e)})


# @app.route('/create', methods=['POST'])
# def create():
# 	conn = psycopg2.connect(database="flask_db",
# 							user="postgres",
# 							password="root",
# 							host="localhost", port="5432")

# 	cur = conn.cursor()

# 	# Get the data from the form
# 	name = request.form['name']
# 	price = request.form['price']

# 	# Insert the data into the table
# 	cur.execute(
# 		'''INSERT INTO products \
# 		(name, price) VALUES (%s, %s)''',
# 		(name, price))

# 	# commit the changes
# 	conn.commit()

# 	# close the cursor and connection
# 	cur.close()
# 	conn.close()

# 	return redirect(url_for('index'))


# @app.route('/update', methods=['POST'])
# def update():
# 	conn = psycopg2.connect(database="flask_db",
# 							user="postgres",
# 							password="root",
# 							host="localhost", port="5432")

# 	cur = conn.cursor()

# 	# Get the data from the form
# 	name = request.form['name']
# 	price = request.form['price']
# 	id = request.form['id']

# 	# Update the data in the table
# 	cur.execute(
# 		'''UPDATE products SET name=%s,\
# 		price=%s WHERE id=%s''', (name, price, id))

# 	# commit the changes
# 	conn.commit()
# 	return redirect(url_for('index'))


# @app.route('/delete', methods=['POST'])
# def delete():
# 	conn = psycopg2.connect
# 	(database="flask_db", user="postgres",
# 	password="root",
# 	host="localhost", port="5432")
# 	cur = conn.cursor()

# 	# Get the data from the form
# 	id = request.form['id']

# 	# Delete the data from the table
# 	cur.execute('''DELETE FROM products WHERE id=%s''', (id,))

# 	# commit the changes
# 	conn.commit()

# 	# close the cursor and connection
# 	cur.close()
# 	conn.close()

# 	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)
