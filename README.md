# python-simple-flow-dashboard
This project visualizes a process flow in a simple dashboard using Python, Flask, and Konva. #python3 #Flask #Konva

The flow follows the following states:

- `Order-Book`
- `Check-Order`
- `Check-Inventory`
- `Process-Payment`
- `Deliver-Book`

- The application polls the server for flow state changes. It appends a message to a text area and highlights the flow state.
- To change the flow state,
```bash
curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' http://localhost:5000/setflowstate/Order-Book
```
Or use Postman to use the API.

This will send a POST request to http://localhost:5000/setflowstate/Order-Book with the JSON payload {"key":"value"}. The server should print this payload to the console and set the current flow state to 'Order-Book'.

## Prerequisites

- Python 3
- Flask
- Konva

## Installation

1. First, clone this repository to your local machine using `git clone <repo_url>`.
2. Navigate to the project directory.
3. It is recommended to set up a virtual environment before installing the project dependencies:
   
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
4. Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

## Usage

To run the server, activate the virtual environment if you haven't already, then execute:
```bash
python app.py
```
The dashboard can now be accessed at `http://localhost:5000`.

To change the current flow state, you can use an API testing tool like Postman to send a POST request to `http://localhost:5000/setflowstate/<flowstate>`, where `<flowstate>` is one of the flow states mentioned above.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
```

Make sure to replace `<repo_url>` with the actual URL of your repository. The license link at the bottom is for the MIT license, but you can replace it with the link to whatever license you're using for your project.

