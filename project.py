#author- bhavya sharma


from flask import Flask, render_template, request
import speedtest
import ipaddress
import re
import socket
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speedtest')
def speed_test():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    return render_template('speedtest.html', download_speed=download_speed, upload_speed=upload_speed)

@app.route('/localip')
def local_ip():
    local_ip_address = socket.gethostbyname(socket.gethostname())
    subnet = get_subnet(local_ip_address)
    local_ips = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]]
    return render_template('localip.html', local_ips=local_ips, subnet=subnet)

def get_subnet(ip_address):
    # Get the subnet of the device
    network = ipaddress.IPv4Network(f"{ip_address}/24", strict=False)
    return network.network_address 

@app.route('/cpu')
def cpu_usage():
    return render_template('cpu.html')

@app.route('/get_cpu_usage')
def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    return {'cpu_percent': cpu_percent}

@app.route('/passwordstrength', methods=['GET', 'POST'])
def password_strength():
    if request.method == 'POST':
        password = request.form['password']
        strength = check_password_strength(password)
        return render_template('passwordstrength.html', password=password, strength=strength)
    return render_template('passwordstrength.html', password=None, strength=None)

def check_password_strength(password):
    # Custom rule: only allow "." as a special character
    special_char_count = len(re.findall(r'\.', password))
    
    length = len(password)
    if length < 8:
        return 'Weak'
    elif length < 12 and special_char_count == 0:
        return 'Moderate'
    elif length >= 12 and special_char_count > 0:
        return 'Strong'
    else:
        return 'Moderate'

if __name__ == '__main__':
    app.run(debug=True)


