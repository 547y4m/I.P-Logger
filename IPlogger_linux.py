from time import ctime
from pyfiglet import Figlet
from flask import Flask, render_template, request
from ip2geotools.databases.noncommercial import DbIpCity


 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    target_ip = request.access_route[0]
    ip_lookup = DbIpCity.get(target_ip, api_key="free")     
    with open("ip_addresses.log", "a") as f:
        f.write(f"\n\n\n\n\n{ctime()} : {request.access_route[0]}\n\n")
        f.write("=======IP DETAILS========== \n")
        f.write(f"City : {ip_lookup.city} \n")
        f.write(f"Region/State : {ip_lookup.region} \n")
        f.write(f"Country : {ip_lookup.country} \n")
        f.write(f"Latitude : {ip_lookup.latitude} \n")
        f.write(f"Longitude : {ip_lookup.longitude} \n")
        f.write(f"==========================")
        f.close()

    return render_template("index.html")
    