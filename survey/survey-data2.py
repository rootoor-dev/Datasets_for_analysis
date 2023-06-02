import pandas as pd

# Define the questionnaire items and response percentages
questionnaire = {'CS1': [0, 0, 50, 20, 20, 5, 5], 'CS2': [0, 0, 5, 20, 20, 55, 0], 'CS3': [0, 0, 0, 0, 10, 10, 80], 'CS4': [0, 0, 15, 5, 20, 20, 40], 'CS5': [0, 0, 0, 0, 20, 20, 60], 'CS6': [20, 20, 15, 5, 10, 10, 20], 'CS7': [0, 0, 0, 0, 10, 30, 60], 'CS8': [0, 0, 50, 30, 10, 5, 5], 'CS9': [0, 0, 0, 0, 20, 10, 70], 'CS10': [10, 20, 25, 5, 10, 10, 20], 'OE1': [20, 10, 5, 25, 20, 10, 10], 'OE2': [5, 5, 35, 25, 30, 0, 0], 'OE3': [0, 0, 0, 0, 10, 90, 0], 'OE4': [10, 0, 25, 40, 10, 15, 0], 'OE5': [0, 0, 0, 35, 10, 10, 45], 'OE6': [0, 0, 0, 0, 20, 60, 20], 'OE7': [10, 30, 10, 10, 15, 15, 10], 'OE8': [0, 0, 0, 0, 25, 0, 75], 'OE9': [0, 0, 0, 0, 20, 45, 35], 'OE10': [10, 20, 10, 30, 15, 35, 10], 'PA1': [100, 0, 0, 0, 0, 0, 0], 'PA2': [0, 0, 0, 5, 40, 55, 0], 'PA3': [0, 0, 10, 10, 25, 45, 10], 'PA4': [0, 0, 0, 5, 20, 20, 55], 'PA5': [0, 0, 0, 5, 25, 70, 0], 'PA6': [0, 0, 5, 0, 20, 50, 25], 'PA7': [0, 0, 0, 0, 0, 50, 50], 'PA8': [0, 30, 20, 5, 20, 20, 5], 'PA9': [0, 0, 0, 5, 20, 20, 55], 'PA10': [15, .

# Get the number of participants
N = 100  # Replace with the actual number of participants

# Create a DataFrame to store the responses
responses_df = pd.DataFrame(index=range(1, N + 1))

# Iterate over the questionnaire items
for item, percentages in questionnaire.items():
    # Generate the responses for the item based on the percentages
    responses = []
    for i, percentage in enumerate(percentages, start=1):
        response_count = int(percentage * N / 100)
        responses.extend([i] * response_count)

    # Add the responses to the DataFrame
    responses_df[item] = responses

# Save the DataFrame as Excel files
responses_df.to_excel('responses.xlsx', index=False)
responses_df.to_csv('responses.csv', index=False)
