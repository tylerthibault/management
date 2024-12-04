from management_app import create_app

app = create_app()
app.LOGIN_TIMEOUT = 60

if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=5101)