import flask
from flask import request, jsonify
import heliport

app = flask.Flask(__name__)

app.config["DEBUG"] = True

h = heliport.Heliport(8)
heli = heliport.Helicopter("HeliBoy")


@app.route('/', methods=['GET'])
def home():
    return "<h1>Heliport 2: Electric Boogaloo</h1>"

# Return all the helicopter and port entries for the task
@app.route('/api/resources/all', methods=['Get'])
def api_all():
    return jsonify({'helicopter': id(heli),
                    'heliport': id(heliport)})

@app.route('/api/resources/helicopter/land', methods=['Put'])
def api_land():
    hret = heli.land(h)
    if hret == 0:
        return "Landed"
    elif hret == 1:
        return "Could not land at helipad as its full"
    else:
        return "Could not land as already landed"

@app.route('/api/resources/helicopter/takeoff', methods=['Put'])
def api_takeoff():
    hret = heli.take_off()
    if hret == 0:
        return "Taken Off"
    elif hret == 1:
        return "Could not takeoff from helipad your not there"
    else:
        return "Could not take off as flying"  


# @app.route('/api/resources/heliport/<int:task_id>', methods=['GET'])
# def get_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         abort (404)
#     else:

#     return jsonify ({'task': task[0]})


app.run()
