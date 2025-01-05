import os
import urllib.request
from tkinter import Tk, Label, Entry, Button
from PIL import Image, ImageTk
from selenium import webdriver

# Global variables
html_content = ""
user_text = ""
img_path = "default1.png"


def next_id(user_id):
    """Calculate the next ID based on the current ID."""
    return f"N{int(user_id[1:]) + 1}"


def fetch_password(user_id):
    """Retrieve the password for the given user ID."""
    with open('password.txt', 'r') as file:
        content = file.read()
    start_pos = content.find(user_id) + 8
    end_pos = content.find(next_id(user_id)) - 1
    return content[start_pos:end_pos]


# Selenium WebDriver setup
driver_path = os.path.join(os.path.dirname(__file__), "chromedriver.exe")
driver = webdriver.Chrome(driver_path)


def scrape_user_data(user_id):
    """Scrape user data from the intranet."""
    global html_content

    # Log in to the intranet
    driver.get("http://intranet.rguktn.ac.in/SMS/")
    driver.find_element("name", "user1").send_keys(user_id)
    driver.find_element("name", "passwd1").send_keys(fetch_password(user_id))
    driver.find_element("name", "passwd1").submit()

    # Fetch profile data
    driver.get("http://intranet.rguktn.ac.in/SMS/profile.php")
    html = driver.page_source
    start_pos = html.find("profile-user-img img-responsive img-circle")
    end_pos = html.find("Semester Course Registration Completed")
    html_content = html[start_pos:end_pos]


def parse_html(html):
    """Extract details like name, class, gender, DOB, mobile, and address from HTML."""
    def extract_between(start_marker, end_marker, offset=0):
        start = html.find(start_marker) + offset
        end = html.find(end_marker, start)
        return html[start:end].strip()

    name = extract_between("value=\"275\"", "<span", 199)
    class_room = extract_between("Class Room:", "<span", 18)
    gender = extract_between("Gender", "<span class=\"html-tag\">", 188)
    dob = extract_between("Date of Birth", "<span class=\"html-tag\">", 195)
    mobile = extract_between("Mobile", "<span class=\"html-tag\">", 188)
    address = extract_between("value=\"335\"", "<span", 197)

    return name, class_room, gender, dob, mobile, address


def validate_user_id(user_id):
    """Validate the format of the user ID."""
    return len(user_id) >= 8 and user_id[1:].isdigit() and user_id[0].isalpha()


def fetch_user_details():
    """Handle button click and fetch user details."""
    global user_text, img_path

    user_id = user_id_entry.get()
    user_text = user_id

    if not validate_user_id(user_id):
        status_label.config(text="Error with User ID", fg="red")
        return

    scrape_user_data(user_id)
    details = parse_html(html_content)

    # Update UI labels
    name_label.config(text=details[0])
    class_label.config(text=details[1])
    gender_label.config(text=details[2])
    dob_label.config(text=details[3])
    mobile_label.config(text=details[4])
    address_label.config(text=details[5])

    # Fetch and display user image
    img_url = f"http://intranet.rguktn.ac.in/SMS/usrphotos/user/{user_id}.jpg"
    img_path = f"img/{user_id}.jpg"
    urllib.request.urlretrieve(img_url, img_path)
    display_image(img_path)


def display_image(img_file):
    """Display the user image."""
    image = Image.open(img_file).resize((300, 300))
    photo = ImageTk.PhotoImage(image)
    profile_pic_label.config(image=photo)
    profile_pic_label.image = photo


# Initialize GUI
app = Tk()
app.title("User Details")
app.geometry("670x680")
app.configure(background="white")

# GUI Components
profile_pic_label = Label(app)
profile_pic_label.pack(pady=30)

Label(app, text="User ID:", font="none 12 bold", bg="white").place(x=77, y=338)
user_id_entry = Entry(app, width=30)
user_id_entry.place(x=227, y=360)

submit_button = Button(app, text="Submit", command=fetch_user_details)
submit_button.place(x=447, y=355)

details_labels = [
    ("Name:", 388, "none"),
    ("Year:", 428, "none"),
    ("Gender:", 468, "none"),
    ("Date of Birth:", 508, "none"),
    ("Mobile:", 548, "none"),
    ("Address:", 588, "none"),
]

for text, y, initial_value in details_labels:
    Label(app, text=text, font="none 12 bold", bg="white").place(x=77, y=y)
    globals()[f"{text.split(':')[0].lower()}_label"] = Label(app, text=initial_value, bg="white", font="none 12 bold")
    globals()[f"{text.split(':')[0].lower()}_label"].place(x=230, y=y)

status_label = Label(app, text="Enter User ID", font="none 12 bold", bg="white", fg="red")
status_label.place(x=180, y=258)

# Start the GUI loop
app.mainloop()
