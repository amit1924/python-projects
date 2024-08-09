import streamlit as st
from PIL import Image


# Set page config to change the title
st.set_page_config(page_title="Marriage Biodata", page_icon=":ring:")

# Custom CSS for larger fonts and colors
st.markdown(
    """
    <style>
    h1 {
        font-size: 3em; 
        color: #2E86C1; /* Title color */
    }
    h2 {
        font-size: 2.5em; 
        color: #2874A6; /* Section headers color */
    }
    h3 {
        font-size: 2em; 
        color: #1F618D; /* Sub-headers color */
    }
    p {
        font-size: 1.5em; 
        color: #34495E; /* Text color */
    }
    .answer {
        color: #28B463; /* Answers color */
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load your profile image
image = Image.open("profile.jpg")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ("Home", "Pictures"))

# App title
st.title("Marriage Biodata - Amit Kumar")

if options == "Home":
    # Display the profile image
    st.image(image, caption="Amit Kumar", use_column_width=True)

    # Personal Information
    st.header("Personal Information")
    st.write(
        f"**Full Name:** <span class='answer'>Amit Kumar</span>", unsafe_allow_html=True
    )
    st.write(
        f"**Date of Birth:** <span class='answer'>19th August 1991</span>",
        unsafe_allow_html=True,
    )
    st.write(
        f"**Height:** <span class='answer'>5 foot 7 inches</span>",
        unsafe_allow_html=True,
    )
    st.write(f"**Weight:** <span class='answer'>66 kg</span>", unsafe_allow_html=True)
    st.write(
        f"**Address:** <span class='answer'>Patna West Patel Nagar, Village - Dakhram (Darbhanga)</span>",
        unsafe_allow_html=True,
    )

    # Education and Profession
    st.header("Education and Profession")
    st.write(
        "**Matriculation and 10+2:** <span class='answer'>CBSE</span>",
        unsafe_allow_html=True,
    )
    st.write(
        "**Engineering:** <span class='answer'>Electrical Engineering</span>",
        unsafe_allow_html=True,
    )
    st.write(
        "**Profession:** <span class='answer'>Software Developer (Freelancer)</span>",
        unsafe_allow_html=True,
    )

    # Family Details
    st.header("Family Details")
    st.write(
        "**Father:** <span class='answer'>Retired Gazetted Officer from Patna Secretariat</span>",
        unsafe_allow_html=True,
    )
    st.write(
        "**Mother:** <span class='answer'>Housewife</span>", unsafe_allow_html=True
    )
    st.write(
        "**Younger Sister:** <span class='answer'>Government School Teacher</span>",
        unsafe_allow_html=True,
    )
    st.write(
        "**Elder Brother:** <span class='answer'>Works in Private Company</span>",
        unsafe_allow_html=True,
    )
    st.write(
        "**Sister-in-Law:** <span class='answer'>Probationary Officer in BOB</span>",
        unsafe_allow_html=True,
    )
    st.write(
        "**Grandfather:** <span class='answer'>Kailash Chandra Jha, Retired from All India Radio</span>",
        unsafe_allow_html=True,
    )

    # Community Information
    st.header("Community Information")
    st.write(
        "**Caste:** <span class='answer'>Hindu Brahmin</span>", unsafe_allow_html=True
    )
    st.write("**Gotra:** <span class='answer'>Shandilya</span>", unsafe_allow_html=True)

    # Partner Preferences
    st.header("Partner Preferences")
    preferred_age = st.slider("Preferred Age Range", 18, 40, (25, 30))
    preferred_height = st.text_input("Preferred Height Range", "5'2\" - 5'5\"")
    preferred_education = st.text_input("Preferred Education", "Graduate or above")
    preferred_occupation = st.text_input("Preferred Occupation", "Not Mandatory")

    # State variable to control summary visibility
    if "show_summary" not in st.session_state:
        st.session_state.show_summary = False

    # Submit Button
    if st.button("Generate Biodata"):
        st.session_state.show_summary = True

    if st.session_state.show_summary:
        st.subheader("Biodata Summary")
        st.write(
            f"**Full Name:** <span class='answer'>Amit Kumar</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Date of Birth:** <span class='answer'>19th August 1991</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Height:** <span class='answer'>5 foot 7 inches</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Weight:** <span class='answer'>66 kg</span>", unsafe_allow_html=True
        )
        st.write(
            f"**Address:** <span class='answer'>Patna West Patel Nagar, Village - Dakhram (Darbhanga)</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Profession:** <span class='answer'>Software Developer (Freelancer)</span>",
            unsafe_allow_html=True,
        )
        st.write(
            "**Father:** <span class='answer'>Retired Gazetted Officer from Patna Secretariat</span>",
            unsafe_allow_html=True,
        )
        st.write(
            "**Mother:** <span class='answer'>Housewife</span>", unsafe_allow_html=True
        )
        st.write(
            "**Younger Sister:** <span class='answer'>Rashmi, Government School Teacher</span>",
            unsafe_allow_html=True,
        )
        st.write(
            "**Elder Brother:** <span class='answer'>Works in Private Company</span>",
            unsafe_allow_html=True,
        )
        st.write(
            "**Sister-in-Law:** <span class='answer'>Probationary Officer in BOB</span>",
            unsafe_allow_html=True,
        )
        st.write(
            "**Grandfather:** <span class='answer'>Kailash Chandra Jha, Retired from All India Radio</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Caste:** <span class='answer'>Hindu Brahmin</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Gotra:** <span class='answer'>Shandilya</span>", unsafe_allow_html=True
        )
        st.write(
            f"**Preferred Age Range:** <span class='answer'>{preferred_age[0]} - {preferred_age[1]}</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Preferred Height Range:** <span class='answer'>{preferred_height}</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Preferred Education:** <span class='answer'>{preferred_education}</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"**Preferred Occupation:** <span class='answer'>{preferred_occupation}</span>",
            unsafe_allow_html=True,
        )

        # Button to hide summary
        if st.button("Hide Summary"):
            st.session_state.show_summary = False

    # Contact Form
    st.header("Contact Me")
    with st.form("contact_form"):
        st.write("For inquiries, you can reach out at: **9431629191**")
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send")

    if submit_button:
        st.success("Your message has been sent! Thank you for contacting me.")

elif options == "Pictures":
    st.header("Additional Pictures")

    # Load images for slideshow
    images = [
        Image.open("p-1.jpeg"),
        Image.open("p-2.jpg"),
        Image.open("p-8.jpg"),
    ]

    # State variable for current image index
    if "current_image_index" not in st.session_state:
        st.session_state.current_image_index = 0

    # Display the current image
    st.image(
        images[st.session_state.current_image_index],
        caption=f"Picture {st.session_state.current_image_index + 1}",
        use_column_width=True,
    )

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Previous"):
            if st.session_state.current_image_index > 0:
                st.session_state.current_image_index -= 1
    with col2:
        if st.button("Next"):
            if st.session_state.current_image_index < len(images) - 1:
                st.session_state.current_image_index += 1

# Run the app with `streamlit run marriage_biodata.py`
