from constants import LINKEDIN_CONNECTION_PROMPT,SYSTEM_MESSAGE
from utils import call_openai_api

def format_posts_for_prompt(posts_array):
    formatted_posts = ""
    for i, post in enumerate(posts_array, 1):
        formatted_posts += f"Post {i}: {post.strip()}\n\n"
    return formatted_posts.strip()

def generate_connection_request_message(target_name, target_about, posts_array):
    formatted_posts = format_posts_for_prompt(posts_array)
    
    prompt = LINKEDIN_CONNECTION_PROMPT.format(
        target_name=target_name,
        target_about=target_about,
        recent_posts=formatted_posts
    )

    # Send to your AI model and get response
    generated_message = call_openai_api(user_prompt=prompt,system_prompt=SYSTEM_MESSAGE)
    return generated_message