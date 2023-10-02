from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
from moviepy.editor import VideoFileClip
import os

app = Flask(__name__)
CORS(app)

# @app.route('/', methods=['GET'])
# def index():
# 	try:
# 	# Connect to the database
# 		conn = psycopg2.connect(database="video_clip_backend",
# 								user="luken",
# 								password="",
# 								host="localhost", port="5432")

# 	# create a cursor
# 		cur = conn.cursor()	

# 	# Select all products from the table
# 		cur.execute('''SELECT * FROM users''')

# 	# Fetch the data
# 		data = cur.fetchall()

# 	# close the cursor and connection
# 		cur.close()
# 		conn.close()

# 		result = []
# 		for row in data:
# 				result.append({
# 						'id': row[0],  # Assuming the first column is the ID
# 						'email': row[1],  # Replace 'name' with your column names
# 						'password': row[2],
# 			})

# 		return jsonify(result)

# 	except Exception as e:
# 		return jsonify({'error': str(e)})


@app.route('/subclip', methods=['POST'])
def subclip():
	input_video = request.files.get('video')
	start_time = float(request.form.get('start_time', 0))
	end_time = float(request.form.get('end_time', 0))

	if not input_video:
		return jsonify({'error': 'No video file provided'}), 400
	
	try:

			# Get the user's "Downloads" folder path
		downloads_folder = os.path.expanduser("~") + "/Downloads/"

			# Output subclip file name
		output_subclip = downloads_folder + "output_subclip.mp4"

			# Save the uploaded file to a temporary location
		input_video.save('temp_video.mp4')

			# Load the input video using VideoFileClip
		video_clip = VideoFileClip('temp_video.mp4')

			# Create the subclip with both video and audio
		subclip = video_clip.subclip(start_time, end_time)

			# Write the subclip to a file with audio included
		subclip.write_videofile(output_subclip, audio_codec='aac')

			# Clean up the temporary file
		os.remove('temp_video.mp4')

		return jsonify({"Message": "Subclip with audio created successfully."}), 200
	
	except Exception as e:
		return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
	app.run(debug=True)
