 # YouTube Data Analysis App

This Streamlit application integrates with a MySQL database to fetch and store YouTube channel and video data. Users can fetch data from the YouTube API (simulated in this example), store it in the database, and view the stored data through a user interface.

## Setup Instructions

1. Clone the repository:
git clone <repository_url>
cd <project_directory>

2. Install dependencies:
pip install -r requirements.txt


3. Configure MySQL database:
- Update `HOST`, `USER`, `PASSWORD`, and `DATABASE` constants in `app.py` and `db_utils.py` with your MySQL database details.

4. Run the Streamlit app:
streamlit run src/app.py


5. Interact with the app:
- Click on "Fetch and Store Data" to simulate fetching data from the YouTube API and storing it in the MySQL database.
- Click on "Display Data" to retrieve and display the stored data from the database.

6. Customize as needed:
- Modify SQL queries in `sql_queries.py` according to your data retrieval and storage needs.
- Extend functionalities in `app.py` based on project requirements.

## Project Structure

project_root/
│
├── data/
│ ├── db_utils.py
│ └── sql_queries.py
│
├── src/
│ └── app.py
│
├── requirements.txt
└── README.md

Replace placeholder values (`your_mysql_host`, `your_mysql_username`, `your_mysql_password`, `your_mysql_database`) with your actual MySQL database credentials.

This setup provides a complete example of how to integrate a MySQL database with a Streamlit application for storing and displaying YouTube channel and video data. Adjust the code as per your specific requirements, such as integrating with the actual YouTube Data API, handling real-time data, and implementing more complex SQL queries for data analysis and visualization.

