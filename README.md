# Flask Location and IP Tracker

## Description
This Flask application is designed to log the GPS coordinates and IP details of visitors to your site. It utilizes ngrok to expose the local server to the internet, making it accessible remotely. The application captures the GPS location via the client-side JavaScript and the IP data directly from the server-side Flask app, storing both pieces of information in a single log file.

## Features
- IP logging: Captures and logs IP address, user agent, operating system, and other related data.
- GPS logging: Utilizes client-side JavaScript to fetch and log GPS coordinates.
- Data consolidation: Both IP and GPS data are consolidated into a single log entry per visit.

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Flask
- ngrok account (for tunneling your local server)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hotcard7/Locationtracker.git
   cd Locationtracker
2. **Install required Python packages**:
    ```bash
    pip install -r requirements.txt
3. **Install ngrok**:
     - Download ngrok from ngrok's download page.
     - Unzip the package and install it based on your operating system's requirements.
4. **Set up ngrok**:
    - Sign up for an account at ngrok's website if you haven't already.
    - Follow the instructions to get your auth token.
    - Connect your ngrok account by running:
        ```bash
        ./ngrok authtoken <your_auth_token>
    - This step ensures that your ngrok instance can connect up to 2 tunnels at the same time and avoids the sessions limitation issue.
### Running the Application
1. **Start the Flask app**:
    ```bash
    python app.py
    ```
    This script will automatically start ngrok in the background.

2.  **Access the application**:
    - Open the URL provided by ngrok in your web browser. It typically looks something like `http://<random-subdomain>.ngrok.io`.
    - Allow location access on the popup to enable GPS coordinate logging.
## Usage
Visit the exposed ngrok URL from any device to log the IP and GPS data. The data is appended to `output_log.txt` in the application's directory.
## Important Notes
- The application will request GPS coordinates from the client's device. Users need to grant permission for the most accurate results.
- IP address logged is the one seen by ngrok, which might be different from the visitor's actual public IP due to various network configurations (like NAT or proxy).
## Contributing
Feel free to fork the repository, make improvements, and submit pull requests. We appreciate contributions that improve the application or fix issues.
