import streamlit as st

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🌐 Multi-Project Dashboard")
project = st.sidebar.radio(
    "Select a Project:",
    [
        "🖼️ Image App",
        "👥 People by Age Group",
        "📝 Register Form",
        "📸 Capture & Download Image"
    ]
)

# ---------------- IMAGE APP ----------------
if project == "🖼️ Image App":
    st.title("🖼️ Image App")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Flowers")
        with st.expander("Beautiful Flowers"):
            img_col1, img_col2 = st.columns(2)
            with img_col1:
                st.image(
                    "http://getwallpapers.com/wallpaper/full/5/f/b/967407-gorgerous-beautiful-flowers-wallpaper-1920x1080-ipad-pro.jpg",
                    width=150)
            with img_col2:
                st.image(
                    "https://tse4.mm.bing.net/th/id/OIP.ZFLxuj_j5RVmO658GvMsEwHaFi?pid=Api&P=0&h=180",
                    width=150)

    with col2:
        st.header("Animals")
        with st.expander("Cute Animals"):
            img_col1, img_col2 = st.columns(2)
            with img_col1:
                st.image("https://tse4.mm.bing.net/th/id/OIP.Jlh-TlckEek5sqlqHcalLQHaE8?pid=Api&P=0&h=180", width=150)
            with img_col2:
                st.image("https://tse4.mm.bing.net/th/id/OIP.3J2q-ML2eSU3xPhgV4ez0AHaE8?pid=Api&P=0&h=180", width=150)

    with col3:
        st.header("Space")
        with st.expander("Amazing Space Images"):
            img_col1, img_col2 = st.columns(2)
            with img_col1:
                st.image("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa", width=150)
            with img_col2:
                st.image("https://images.unsplash.com/photo-1462331940025-496dfbfc7564", width=150)

# ---------------- PEOPLE BY AGE GROUP PROJECT ----------------
elif project == "👥 People by Age Group":
    st.title("👥 People by Age Group")

    with st.sidebar:
        st.header("Person Ages")
        option = st.radio("Select Age Group:", ["1-25", "26-50", "51-75", "76-100"], index=0)

    users = [
        {"name": "Aarav", "age": 18, "gender": "Male", "age_group": "1-25"},
        {"name": "Priya", "age": 22, "gender": "Female", "age_group": "1-25"},
        {"name": "Rahul", "age": 24, "gender": "Male", "age_group": "1-25"},
        {"name": "Sneha", "age": 19, "gender": "Female", "age_group": "1-25"},
        {"name": "Kiran", "age": 25, "gender": "Male", "age_group": "1-25"},
        {"name": "Vikram", "age": 30, "gender": "Male", "age_group": "26-50"},
        {"name": "Meera", "age": 35, "gender": "Female", "age_group": "26-50"},
        {"name": "Raj", "age": 40, "gender": "Male", "age_group": "26-50"},
        {"name": "Pooja", "age": 45, "gender": "Female", "age_group": "26-50"},
        {"name": "Amit", "age": 50, "gender": "Male", "age_group": "26-50"},
        {"name": "Karthik", "age": 55, "gender": "Male", "age_group": "51-75"},
        {"name": "Anjali", "age": 60, "gender": "Female", "age_group": "51-75"},
        {"name": "Rajesh", "age": 65, "gender": "Male", "age_group": "51-75"},
        {"name": "Lakshmi", "age": 70, "gender": "Female", "age_group": "51-75"},
        {"name": "Sundar", "age": 75, "gender": "Male", "age_group": "51-75"},
        {"name": "Suresh", "age": 80, "gender": "Male", "age_group": "76-100"},
        {"name": "Kamala", "age": 85, "gender": "Female", "age_group": "76-100"},
        {"name": "Mohan", "age": 90, "gender": "Male", "age_group": "76-100"},
        {"name": "Leela", "age": 95, "gender": "Female", "age_group": "76-100"},
        {"name": "Raman", "age": 100, "gender": "Male", "age_group": "76-100"},
    ]

    st.text("Select an age group from the sidebar to view details below.")
    filtered_users = [u for u in users if u["age_group"] == option]
    st.subheader(f"Showing people in age group: {option}")
    st.table(filtered_users)

# ---------------- REGISTER FORM PROJECT ----------------
elif project == "📝 Register Form":
    st.title("📝 User Registration")

    if "users" not in st.session_state:
        st.session_state.users = []

    with st.form("Register Form", clear_on_submit=True):
        username = st.text_input("Enter username:")
        password = st.text_input("Enter password:", type="password")
        submitted = st.form_submit_button("Register")

    if submitted:
        if not username or not password:
            st.warning("⚠️ Please fill in both username and password.")
        elif any(u["Username"] == username for u in st.session_state.users):
            st.error("❌ Username already exists. Try another one.")
        else:
            st.session_state.users.append({"Username": username, "Password": password})
            st.success("✅ Registration successful!")

    if st.session_state.users:
        st.subheader("📋 Registered Users Table")
        st.table(st.session_state.users)

# ---------------- CAMERA CAPTURE PROJECT ----------------
elif project == "📸 Capture & Download Image":
    st.title("📸 Capture and Download Image")
    col1, col2 = st.columns(2)

    with col1:
        v = st.camera_input("Take a photo")

    with col2:
        if v is not None:
            with open("captured_image.png", "wb") as f:
                f.write(v.getbuffer())

            st.success("✅ Image saved successfully!")
            st.image(v, caption="Captured Image", use_column_width=True)

            with open("captured_image.png", "rb") as file:
                st.download_button(
                    label="📥 Download Image",
                    data=file,
                    file_name="captured_image.png",
                    mime="image/png"
                )
