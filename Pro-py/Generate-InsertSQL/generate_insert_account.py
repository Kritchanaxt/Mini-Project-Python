import pandas as pd

# Set custom column names to match the desired data
column_names = ['account_id', 'game_id', 'user_id', 'username', 'password', 'details', 'price', 'status', 'created_at']

# Load data from the file and set the column names
user_data = pd.read_csv('CSV/Account.csv', header=None, names=column_names)

# Function to generate SQL INSERT statements
def generate_insert_statements(table_name, data_frame):
    columns = ', '.join(data_frame.columns)  
    insert_values = []
    
    for _, row in data_frame.iterrows():
        values = []
        for value in row:
            if pd.isna(value):  
                values.append("NOW()")
            elif isinstance(value, str):  
                values.append(f"'{value.replace('\'', '\'\'')}'")  # Escape single quotes
            else:
                values.append(str(value)) 
        insert_values.append(f"({', '.join(values)})")
    
    # Create the INSERT statement by combining the values into a single statement
    insert_statement = f"INSERT INTO {table_name} ({columns}) VALUES \n" + ",\n".join(insert_values) + ";"
    
    return insert_statement

# Generate the SQL INSERT statement for the Accounts table
user_insert_sql = generate_insert_statements("Accounts", user_data)

# Print the SQL statement to the console
print(user_insert_sql)

# Save the SQL statement to a file
with open('insert_account.sql', 'w', encoding='utf-8') as user_file:
    user_file.write(user_insert_sql)

print("INSERT statements have been successfully generated and saved to .sql file.")
