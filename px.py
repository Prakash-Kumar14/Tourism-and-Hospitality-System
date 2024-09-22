import os
from azure.storage.queue import QueueServiceClient

# Replace these values with your actual Azure Storage account details
account_name = "skillclass"
account_key = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")  # Use environment variable
queue_name = "devv"

# Ensure account_key is set
if not account_key:
    raise ValueError("The environment variable AZURE_STORAGE_ACCOUNT_KEY is not set.")

# Create a connection string
connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"

# Initialize the QueueServiceClient
queue_service_client = QueueServiceClient.from_connection_string(conn_str=connection_string)

# Get a reference to the queue
queue_client = queue_service_client.get_queue_client(queue_name)

# Send a message to the queue
message_content = "Hello, Azure Queue!"
queue_client.send_message(message_content)

print(f"Message sent to the queue: {message_content}")

# Receive messages from the queue
messages = queue_client.receive_messages()

# Iterate over the messages
for received_message in messages:
    message_content_received = received_message.content
    message_id = received_message.id
    pop_receipt = received_message.pop_receipt

    print(f"Received message from the queue: {message_content_received}")

# Note: No deletion of messages is performed here

if not messages:
    print("No messages in the queue.")
