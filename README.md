# Network Insight Dashboard

## Description
The Network Insight Dashboard is a Flask-based web application that provides a suite of tools to monitor and analyze key aspects of network performance and security. The dashboard is designed for network administrators and users who want to gain insights into their local network, test their internet speed, evaluate CPU usage, and assess password strength.

## Features

### 1. **Internet Speed Test**
- Measures both download and upload speeds in Mbps using the `speedtest` module.
- Provides a simple and user-friendly interface for initiating a speed test.

### 2. **Local IP Address and Subnet Information**
- Displays the local IP addresses of the host machine.
- Provides subnet details for network diagnostics.

### 3. **CPU Usage Monitor**
- Tracks the current CPU usage percentage in real-time using the `psutil` library.
- Displays CPU utilization for system performance analysis.

### 4. **Password Strength Checker**
- Allows users to input a password and receive a strength evaluation.
- Custom rules include:
  - Minimum password length of 8 characters.
  - Increased strength with the presence of a period (`.`) as a special character.
- Evaluates password strength as `Weak`, `Moderate`, or `Strong` based on length and character rules.

## Requirements
- Python 3.x
- Flask (`pip install flask`)
- Speedtest module (`pip install speedtest-cli`)
- Psutil module (`pip install psutil`)

## Installation
1. Clone this repository or download the source code.
2. Install the required libraries:
   ```bash
   pip install flask speedtest-cli psutil
   ```

## Running the Application
1. Navigate to the directory containing the source code.
2. Run the application:
   ```bash
   python project.py
   ```
3. Open a web browser and navigate to `http://127.0.0.1:5000` to access the dashboard.

## Code Structure
### Routes
- **`/`**: Renders the main index page.
- **`/speedtest`**: Runs and displays internet speed test results.
- **`/localip`**: Displays local IP addresses and subnet details.
- **`/cpu`**: Renders the CPU usage monitoring page.
- **`/get_cpu_usage`**: Provides CPU usage data as JSON for dynamic updates.
- **`/passwordstrength`**: Evaluates the strength of user-provided passwords.

### Utility Functions
- **`get_subnet(ip_address)`**: Extracts subnet information from a given IP address.
- **`check_password_strength(password)`**: Implements custom password strength rules and returns a strength label.

## Templates
The application uses Flask's Jinja2 templating engine to render HTML pages. Each feature has a corresponding template:
- `index.html`
- `speedtest.html`
- `localip.html`
- `cpu.html`
- `passwordstrength.html`

## Future Enhancements
- Adding graphical visualizations for CPU usage and network performance metrics.
- Extending password strength checks with more comprehensive rules.
- Adding support for IPv6 addresses and subnet information.
- Incorporating user authentication for enhanced security.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.


