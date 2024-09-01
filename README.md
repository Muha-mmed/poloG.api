# poloG.api

This is a Flask API that provides quotes by Polo G.

## Features

- Fetch random quotes by Polo G
- Access a collection of quotes with ease

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Muha-mmed/poloG.api.git
   cd poloG.api
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Flask app**:

   ```bash
   python app.py
   ```

2. **Access the API**:  
   Open your browser or API client (e.g., Postman) and navigate to `http://127.0.0.1:5000` to interact with the API.

## API Endpoints

- **GET** `/quote/rand_quote`: Retrieve a random Polo G quote.
- **GET** `/quote/<int:id>`: Get single quote by it's id
- **GET** `/quotes`: Retrieve all available quotes.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue if you have suggestions or improvements.

## License

This project is licensed under the MIT License.

