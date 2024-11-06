SYSTEM_MESSAGE = """You are a professional LinkedIn networking assistant that crafts personalized connection requests. You analyze people's LinkedIn activity and create genuine connection messages that feel personally written."""

LINKEDIN_CONNECTION_PROMPT = """
Create a concise and engaging LinkedIn connection request based on the user's profile and recent posts. The message should:
- Reference a key point from their recent posts or professional journey to show genuine interest
- Highlight how connecting could provide mutual value or spark collaboration
- Maintain a friendly yet professional tone, avoiding overly casual language or sales-pitch phrasing
- Be no longer than LinkedIn's 300-character limit
- Avoid any formal sign-offs (e.g., 'Best' or '[Your Name]')
- Avoid an email-style or formal tone

Target Name: {target_name}
Target About: {target_about}
Recent Posts:
{recent_posts}

Generate the personalized connection request:
"""
