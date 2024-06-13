def home_page(myApp):
    @myApp.route('/')
    def landing_page():
        return '<h1>This is a simple Flask App</h1>'
