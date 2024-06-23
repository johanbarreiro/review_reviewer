import streamlit as st
import pandas as pd
from rating_reviewer import classify_text as classify_review_text, convert_label_to_rating
from review_tool import adjust_review
from streamlit.web.cli import main

# Streamlit interface
st.title("Review Classification and Adjustment Tool")

# Tab setup
tab1, tab2 = st.tabs(["Review Classification", "Review Adjustment"])

with tab1:
    st.header("Review Classification")
    review_full = st.text_area("Full Review", key="full_review")

    if st.button("Classify Review"):
        # Classify the review text
        predicted_label = classify_review_text(review_full)
        predicted_rating = convert_label_to_rating(predicted_label)

        # Display the result
        st.write("Predicted Label:", predicted_label)
        st.write("Suggested rating for your review:", predicted_rating)

with tab2:
    st.header("Review Adjustment")
    review_basic = st.text_area("Basic Review", key="basic_review")

    # Button to adjust review based on classification rating
    if st.button("Adjust Review Based on Classification"):
        # First classify the review to get the suggested rating
        predicted_label = classify_review_text(review_basic)
        target_rating = convert_label_to_rating(predicted_label)

        # Adjust the review using the OpenAI API
        adjusted_review = adjust_review(review_basic, target_rating)

        # Display the adjusted review and the used target rating
        st.write("Target Rating (Based on Classification):", target_rating)
        st.write("Adjusted Review:", adjusted_review)

if __name__ == '__main__':
    main()
