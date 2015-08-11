from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/jedi/<firstname>/<lastname>")
def jedi(firstname,lastname):
  	jedi_name = lastname[0:3]+firstname[0:2]
  	html = """
	  <html>
	    <body>
	        <h1>
	            Hello {}
	        </h1>
	    </body>
	  </html>  
	""" 
	return html.format(jedi_name.title())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)


# http://0.0.0.0:8888/jedi/maryam/hosseini
