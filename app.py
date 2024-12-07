from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# API endpoint to serve the crime data from data.json
@app.route('/api/data', methods=['GET'])
def get_crime_data():
    # Check if the data.json file exists
    if os.path.exists('data.json'):
        try:
            # Open and load the data from the file
            with open('data.json', 'r') as file:
                data = json.load(file)
            return jsonify(data)  # Return the data as JSON
        except Exception as e:
            # Handle errors in reading data
            return jsonify({'error': f"Error reading the data: {str(e)}"}), 500
    else:
        return jsonify({'error': "Data file not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
