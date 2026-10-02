from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Store received RFID data
rfid_data = []


# =========================
# DASHBOARD
# =========================
@app.route("/")
def dashboard():

    rows = ""

    for data in reversed(rfid_data):
        rows += f"""
        <tr>
            <td>{data['point']}</td>
            <td>{data['uid']}</td>
            <td>{data['time']}</td>
            <td><span class="detected">DETECTED</span></td>
        </tr>
        """

    if not rows:
        rows = """
        <tr>
            <td colspan="4">No RFID tags detected yet</td>
        </tr>
        """

    return f"""
    <!DOCTYPE html>
    <html>
    <head>

        <title>AgCane RFID Dashboard</title>

        <meta http-equiv="refresh" content="2">

        <style>

            body {{
                font-family: Arial, sans-serif;
                background: #f2f6f3;
                margin: 0;
                padding: 0;
            }}

            .header {{
                background: #1b5e20;
                color: white;
                padding: 25px;
                text-align: center;
            }}

            .header h1 {{
                margin: 0;
                font-size: 32px;
            }}

            .header p {{
                margin-top: 8px;
                font-size: 16px;
            }}

            .container {{
                width: 90%;
                max-width: 1100px;
                margin: 30px auto;
            }}

            .cards {{
                display: flex;
                gap: 20px;
                flex-wrap: wrap;
            }}

            .card {{
                background: white;
                padding: 20px;
                border-radius: 12px;
                flex: 1;
                min-width: 220px;
                box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            }}

            .card h3 {{
                margin-top: 0;
                color: #555;
            }}

            .value {{
                font-size: 28px;
                font-weight: bold;
                color: #1b5e20;
            }}

            .status {{
                color: #2e7d32;
            }}

            .table-box {{
                margin-top: 30px;
                background: white;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
            }}

            th {{
                background: #1b5e20;
                color: white;
                padding: 14px;
                text-align: center;
            }}

            td {{
                padding: 14px;
                text-align: center;
                border-bottom: 1px solid #ddd;
            }}

            .detected {{
                background: #c8e6c9;
                color: #1b5e20;
                padding: 6px 12px;
                border-radius: 20px;
                font-weight: bold;
            }}

            .footer {{
                text-align: center;
                margin-top: 30px;
                color: #777;
            }}

        </style>

    </head>

    <body>

        <div class="header">
            <h1>🚜 AgCane RFID Dashboard</h1>
            <p>Automated Stop and Data Capture System</p>
        </div>

        <div class="container">

            <div class="cards">

                <div class="card">
                    <h3>RFID Tags Detected</h3>
                    <div class="value">{len(rfid_data)}</div>
                </div>

                <div class="card">
                    <h3>Current Point</h3>
                    <div class="value">
                        {rfid_data[-1]['point'] if rfid_data else '--'}
                    </div>
                </div>

                <div class="card">
                    <h3>Latest RFID UID</h3>
                    <div class="value">
                        {rfid_data[-1]['uid'] if rfid_data else '--'}
                    </div>
                </div>

                <div class="card">
                    <h3>System Status</h3>
                    <div class="value status">ONLINE</div>
                </div>

            </div>


            <div class="table-box">

                <h2>📡 RFID Detection History</h2>

                <table>

                    <tr>
                        <th>Point</th>
                        <th>RFID UID</th>
                        <th>Date & Time</th>
                        <th>Status</th>
                    </tr>

                    {rows}

                </table>

            </div>

            <div class="footer">
                AgCane | Low-Cost & Rugged Automated Stop and Data Capture Module
            </div>

        </div>

    </body>
    </html>
    """


# =========================
# RECEIVE DATA FROM ESP8266
# =========================
@app.route("/data")
def receive_data():

    point = request.args.get("point")
    uid = request.args.get("uid")

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "point": point,
        "uid": uid,
        "time": current_time
    }

    rfid_data.append(data)

    print("\n==============================")
    print("       AgCane DATA RECEIVED")
    print("==============================")
    print("Point :", point)
    print("UID   :", uid)
    print("Time  :", current_time)
    print("==============================")

    return "Data received successfully"


# =========================
# RUN SERVER
# =========================
app.run(host="0.0.0.0", port=5000)
