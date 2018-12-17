from app import create_app
app=create_app()
if __name__=='__main__':
    # host = app.config['HOST'], port = app.config['PORT'],
    app.run( debug=app.config['DEBUG'],threaded=False)