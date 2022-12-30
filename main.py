from flask import Flask, json, render_template
from flask_cors import CORS
from google.cloud import datastore


counter = 0

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})



def get_client():
    return datastore.Client()

def create_thing(): 
    client = get_client()
    key = client.key('visit-id')
    #uploadcounter.update({'counter' : counter})
    return datastore.Entity(key)

def update_thing(thing):
    client = get_client()
    #print(client.put(thing))
    return client.put(thing)


def retrieve_things(counter):
    client = get_client()
    outputdata = client.key('visit-id', int(counter))
    #print(client.get(outputdata))
    return client.get(outputdata)
    
def get_things():
    result = []
    client = get_client()
    query = client.query(kind='visit-id')
    for entity in query.fetch():
        result.append(entity)
    return result

#def counter_update():
#    resultSorted = sorted(get_things(), key=lambda k:k['counter'] )
#    counterUpdate = resultSorted[-1].get("counter")
#    counter  = counterUpdate
#    #print(resultSorted)
#    return counter

@app.route('/')
def visit():
    global counter 
    counter += 1
    visitThing = create_thing()
    visitThing['counter'] = counter
    update_thing(visitThing)

    resultSorted = sorted(get_things(), key=lambda k:k['counter'] )
    counterUpdate = resultSorted[-1].get("counter")
    counter  = counterUpdate
    #print(counter)
    return str(counter)

    #return str(counter_update())
    
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
