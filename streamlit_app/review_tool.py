import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def adjust_review(basic_review, target_rating):
    messages = [
        {
            "role": "system",
            "content": (
                "Welcome to our review adjustment tool! Here’s how it works:\n"
                "Input a Basic Review: Start by writing a simple, honest review of your experience with the product or service.\n"
                "Adjust to Target Rating: Based on the rating you aim to achieve (1 to 5 stars), follow the guidelines below to modify your review accordingly.\n"
                "Review Adjustment Guidelines:\n"
                "1 Star: Highlight major issues and express strong dissatisfaction. Use phrases like 'extremely disappointed,' 'unacceptable quality,' and 'would not recommend.' Focus on negative aspects and explain why they significantly impacted your experience.\n"
                "2 Stars: Point out significant problems but mention any minor positives. Use phrases like 'disappointed,' 'needs improvement,' and 'not satisfied.' While you can acknowledge any good points, ensure the review leans heavily on the negatives.\n"
                "3 Stars: Provide a balanced review. Mention both positives and negatives equally. Use phrases like 'average experience,' 'had some issues,' and 'could be better.' Explain both the good and the bad aspects of your experience.\n"
                "4 Stars: Emphasize positive aspects but mention minor issues. Use phrases like 'very good,' 'pleased overall,' and 'a few minor problems.' Highlight what you liked while briefly touching on any small areas for improvement.\n"
                "5 Stars: Focus entirely on positive aspects and express high satisfaction. Use phrases like 'excellent,' 'highly recommend,' and 'exceeded expectations.' Highlight the best features and explain why the experience was outstanding.\n"
                "Example:\n"
                "Basic Review: 'I recently tried the new headphones and found them to be comfortable with decent sound quality, but the battery life was shorter than expected.'\n"
                "Target Rating: 5 Stars 'These new headphones are fantastic! They are incredibly comfortable and offer excellent sound quality. Even though the battery life could be longer, the overall experience is outstanding. Highly recommend!'\n"
                "Target Rating: 3 Stars 'The new headphones are pretty good. They are comfortable and the sound quality is decent, but the battery life is shorter than I expected. Overall, it's an average experience.'\n"
            )
        },
        {
            "role": "user",
            "content": basic_review
        },
        {
            "role": "user",
            "content": f"Target Rating (1 to 5 stars): {target_rating}"
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message["content"].strip()

# Example usage:
if __name__ == "__main__":
    basic_review = "I recently tried the new headphones and found them to be comfortable with decent sound quality, but the battery life was shorter than expected."
    target_rating = 5

    adjusted_review = adjust_review(basic_review, target_rating)
    print(adjusted_review)

