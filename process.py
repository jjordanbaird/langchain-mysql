from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI


# Now moving on to Langchain 
db = SQLDatabase.from_uri("mysql://root:password@localhost:3306/sample_db")

toolkit = SQLDatabaseToolkit(db=db)

agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True
)

sql = """
    Who are the most valuable customers in the Sales table? 
    Give me the top 5 along with their total sales."""

agent_executor.run(sql)
    # The wrong answer is returned:
        # The top 5 customers in the Sales table, in order of total sales, are customer 6 with 2014, customer 8 with 1706, customer 10 with 1581, customer 3 with 1164, and customer 2 with 1050.
    # This answer is not accounting for the quantity column in the Sales table
    # additional prompting is needed to get the correct answer

sql = """
    Who are the most valuable customers in the Sales table? 
    Give me the top 5 along with their total sales. Note that the total sales is the sum of the price * quantity."""

agent_executor.run(sql)
    # The correct answer is returned here
    # So you should definitely test out various expected queries before relying on a system like this in a production setting!
    # I assume that as these large language models improve, we'll see more and more accurate results with less prompting. 
"""
The top 5 customers in the Sales table, in order of total sales, are customer 10 with total sales of 12058, customer 8 with total sales of 11796, customer 3 with total sales of 9312, customer 2 with total sales of 5206, and customer 6 with total sales of 5121.
"""
