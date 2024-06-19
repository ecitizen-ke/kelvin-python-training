from app import create_app

# Create the Flask application using create_app() function
app = create_app()

# Check if the script is executed directly (not imported as a module)
if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
