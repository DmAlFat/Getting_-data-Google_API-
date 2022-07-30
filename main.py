import time
import sqlalchemy as sa
from connection_parameters import USER, PASSWORD, HOST, PORT, DATABASE
from transformer import gsheet_to_df


while True:
    getting_data = gsheet_to_df('Getting_data(Google_API)')
    connection_string = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (USER,PASSWORD,HOST,str(PORT),DATABASE)
    engine = sa.create_engine(connection_string)
    connection = engine.connect()
    getting_data.to_sql('Getting_data', con=engine, if_exists = 'replace', index= False)
    time.sleep(10)
