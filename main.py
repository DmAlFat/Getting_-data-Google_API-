# Connect the necessary modules
import time
import sqlalchemy as sa
from connection_parameters import USER, PASSWORD, HOST, PORT, DATABASE
from transformer import gsheet_to_df


while True:  # use a loop with these parameters to continuously run the script
    getting_data = gsheet_to_df('Getting_data(Google_API)')  # apply a function to our google sheets table
    connection_string = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (USER,PASSWORD,HOST,str(PORT),DATABASE)  # establishing a connection to the database
    engine = sa.create_engine(connection_string)
    connection = engine.connect()
    getting_data.to_sql('Getting_data', con=engine, if_exists = 'replace', index= False)  # create a table in our database based on the received dataframe object
    time.sleep(10)  # set a timer for the next request execution to avoid exceeding the server access limit
