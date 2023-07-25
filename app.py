import streamlit as st
import cv2
from ultralytics import YOLO
import webbrowser


def play_webcam(conf, model):
    """
    Plays a webcam stream. Detects Objects in real-time using the YOLOv8 object detection model.

    Parameters:
        conf: Confidence of YOLOv8 model.
        model: An instance of the `YOLOv8` class containing the YOLOv8 model.

    Returns:
        None

    Raises:
        None
    """
    source_webcam = 0
    try:
        vid_cap = cv2.VideoCapture(source_webcam)
        st_frame = st.empty()
        while (vid_cap.isOpened()):
            success, image = vid_cap.read()
            if success:
                print(image)
                image = cv2.resize(image, (600, int(720 * (9 / 16))))
                # img = frame.to_ndarray(format="bgr24")
                res = model.predict(image, conf=conf)
                ## Tracking
                # res = model.track(image, conf=conf, persist=True, tracker="bytetrack.yaml")
                res_plotted = res[0].plot()
                st_frame.image(res_plotted,
                               caption='Detected Video',
                               channels="BGR",
                               use_column_width=True
                               )
            else:
                vid_cap.release()
                break
    except Exception as e:
        st.sidebar.error("Error loading video: " + str(e))

    # return image

st.title("Intramuros tourist Detection with YOLOv8 ⛪📱🚀")
st.write("This app uses YOLOv8 to perform real-time object detection on the webcam stream. It seamlessly detects famous tourist spots and buildings in Intramuros, providing users with information about the sites.")
locations = ['Casa Manila', 'Fort Santiago', 'King Charles IV Monument', 'Manila Cathedral', 'Palacio de Gobernador', 'San Agustin Church']
models = ['Yolov8n', 'YOLOv8s', 'YOLOv8m', 'YOLOv8l', 'YOLOv8x']

selected_confidence = st.sidebar.slider("Select Confidence Level", min_value=0.1, max_value=1.0, step=0.05, value=0.50)
selected_model = st.sidebar.selectbox("Select Model", models)
selected_location = st.sidebar.selectbox("Select Location", locations)



locations = {
    'Casa Manila': "https://en.wikipedia.org/wiki/Casa_Manila",
    'Fort Santiago': "https://en.wikipedia.org/wiki/Fort_Santiago",
    'King Charles IV Monument': "https://commons.wikimedia.org/wiki/File:King_Charles_IV_of_Spain_monument,_Intramuros,_2018_(01).jpg",
    'Manila Cathedral': "https://en.wikipedia.org/wiki/Manila_Cathedral",
    'Palacio del Gobernador': "https://en.wikipedia.org/wiki/Palacio_del_Gobernador",
    'San Agustin Church': "https://en.wikipedia.org/wiki/San_Agustin_Church_(Manila)"
}

locations_list = list(locations.keys())


# Creating the button to open the selected location's website
if st.sidebar.button("Check Information"):
    if selected_location in locations:
        website_url = locations[selected_location]
        webbrowser.open_new_tab(website_url)

model = YOLO('models/intramuros.pt')
play_webcam(0.15, model)
st.write(play_webcam(0.15, model))