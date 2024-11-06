import streamlit as st
from message_generator import generate_connection_request_message
from linkedin_scraper import linkedin_login,get_target_user_about_section,get_target_user_posts

def main():
    
    st.title("LinkedIn Connection Request Customizer")

    # Get the LinkedIn username and password from the user
    linkedin_username = st.text_input("Enter your LinkedIn username:")
    linkedin_password = st.text_input("Enter your LinkedIn password:", type="password")

    # Get the target profile URL from the user
    target_profile_url = st.text_input("Enter the target LinkedIn profile URL:")

    if st.button("Generate Connection Request"):
        try:
            # Log in to LinkedIn
            driver = linkedin_login(linkedin_username, linkedin_password)

            # Get the target user's posts
            target_name, target_about = get_target_user_about_section(driver, target_profile_url)

            target_user_posts = get_target_user_posts(driver, target_profile_url)

            st.success("Completed fetching User About section and Recent posts")
            # Close the browser
            driver.quit()
            
            # Generate the connection request message
            connection_message = generate_connection_request_message(target_name,target_about, target_user_posts)
            
            # Display the generated message in a text area with a copy icon
            st.subheader("Connection Request Message")
            st.code(connection_message, language='markdown',wrap_lines=True)

            # Display the target user's information
            st.subheader("User Details")
            st.markdown(f"Name: {target_name}")
            st.markdown("About :")
            st.code(target_about,language='markdown',wrap_lines=True)
            st.text("Recent Posts:")
            st.json(target_user_posts)

            

            # Display the generated message
            st.success("Connection request message generated:")

            
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()