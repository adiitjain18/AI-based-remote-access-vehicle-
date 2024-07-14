import boto3

# Initialize AWS DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='your-region')
table = dynamodb.Table('your-table-name')

# Function to send data to DynamoDB
def send_to_dynamodb(data):
    response = table.put_item(Item={
        'timestamp': str(time.time()),
        'ultrasonic_distance': data['ultrasonic_distance'],
        'adc_value': data['adc_value'],
        'image_url': 's3://your-bucket-name/path/to/image.jpg'
    })
    print("Data sent to DynamoDB:", response)

# Example usage
data_to_send = {
    'ultrasonic_distance': ultrasonic_distance,
    'adc_value': adc_value
}
send_to_dynamodb(data_to_send)
