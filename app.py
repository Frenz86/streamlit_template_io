import streamlit as st
import requests

url_API =st.text_input("inserisci url dell'api","https://fantasticiris.herokuapp.com/predict?")

def main():
    st.title("FANTASTICAPI - POST-GET Debugger")
    input1 = st.text_input("Please write the first feature",2.0)
    input2 = st.text_input("Please write the second feature",1.4)
    input3 = st.text_input("Please write the third feature",3.0)
    input4 = st.text_input("Please write the fourth feature",3.0)


    #VERY IMP!! IMPOSTARE GLI STESSI NOMI DELLE STRINGE INPUT IN FASTAPI
    data = { 
            "feature1": input1, # key must be the named the same as the api BASEMODEL
            "feature2": input2, # key must be the named the same as the api BASEMODEL
            "feature3": input3, # key must be the named the same as the api BASEMODEL
            "feature4": input4, # key must be the named the same as the api BASEMODEL
            }

    if st.button("Predict IRIS with method GET"):
        url = url_API
        data_keys = data.keys()
        data_values = data.values()
        url2 ="&".join("{0}={1}".format(x,y) for x,y in zip(data_keys,data_values))
        link = url+url2
        st.write('"{}"'.format(link))
        response = requests.get(link)
        prediction =response.json()
        prediction = prediction['prediction']
        st.success(f"The final prediction is: {prediction}")

    if st.button("Predict Iris with method POST"):
        url = url_API
        data_keys = data.keys()
        data_values = data.values()
        url2 ="&".join("{0}={1}".format(x,y) for x,y in zip(data_keys,data_values))
        link = url+url2
        st.write('"{}"'.format(link))
        response = requests.post(link)
        prediction =response.json()
        prediction = prediction['prediction']
        st.success(f"The final prediction is: {prediction}")

#by default it will main at 8501 port
if __name__ == '__main__':
    main()