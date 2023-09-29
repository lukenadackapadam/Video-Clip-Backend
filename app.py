from flask import Flask, render_template, request, redirect, url_for, jsonify
import psycopg2
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import os
from tkinter import Tk, filedialog


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


@app.route('/', methods=['GET'])
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


@app.route('/subclip', methods=['POST'])
def subclip():
	# Create a Tkinter window to open the file dialog
	root = Tk()
	root.withdraw() # Hide the main window

# Ask the user to select the input video file
input_video = filedialog.askopenfilename(initialdir=os.path.expanduser("~") + "/Downloads/")

if not input_video:
    print("No video file selected. Exiting...")
else:
    # Set the start and end times for the subclip (in seconds)
    start_time = float(input("Enter the start time (in seconds): "))  # Start time of the subclip
    end_time = float(input("Enter the end time (in seconds): "))    # End time of the subclip

    # Get the user's "Downloads" folder path
    downloads_folder = os.path.expanduser("~") + "/Downloads/"

    # Output subclip file name
    output_subclip = downloads_folder + "output_subclip.mp4"

    # Load the input video using VideoFileClip
    video_clip = VideoFileClip(input_video)

    # Create the subclip with both video and audio
    subclip = video_clip.subclip(start_time, end_time)

    # Write the subclip to a file with audio included
    subclip.write_videofile(output_subclip, audio_codec='aac')

    print("Subclip with audio created successfully.")

if __name__ == '__main__':
	app.run(debug=True)
