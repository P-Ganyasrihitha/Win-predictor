
    if st.button('Predict Probability'):
        runs_left = target - score
        balls_left = 120 - (overs*6)
        wickets = 10 - wickets
        crr = score/overs