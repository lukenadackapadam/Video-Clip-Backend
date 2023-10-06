from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
from moviepy.editor import VideoFileClip
import os

app = Flask(__name__)
CORS(app)

@app.route('/subclip', methods=['POST'])
def subclip():
	input_video = request.files.get('video')
	start_time = float(request.form.get('start_time', 0))
	end_time = float(request.form.get('end_time', 0))
	file_name = (request.form.get('file_name'))

	if not input_video:
		return jsonify({'error': 'No video file provided'}), 400
	
	try:

		# print(f"=====, {file_name}")
		# file_name = 'abc'
		# print(bool(file_name))
		# file_name = ""
		# print(bool(file_name))

			# Get the user's "Downloads" folder path
		downloads_folder = os.path.expanduser("~") + "/Downloads/"

			# Output subclip file name
		if not file_name:
			file_name = "outclip" 

		output_subclip = downloads_folder + file_name + ".mp4"

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
