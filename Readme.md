 ### "Portfolio Friend APP"

"portfollio friend", allows the user to add assets to a portfolio and check risk metrics and correlations across the portfolio. Any ticker for any asset available in yahoo finance can be used in the app. You need that ticker to enter an asset into the app. Assets can include anything from shares,ETF’s to currencies(fiat and crypto) assuming the ticker is available in yahoo finance.

There is a logo file that is deliberately missing from the repo and that file is referenced in the main .py file. You just need to sub in your own logo file should you ever wish to work with this repo on heroku.

The .mov file in the repo contains a short movie clip of the app in action. You will need to download the file to view the movie.

July/2021



June /23: 

Repo needs to be updated to even run locally . Update Streamlit. Remove any refences to beta in .py file and also use @st.cache_data  which is relevant to most recent versuion of streamlit.  Since Salesforce took over Heroku I stopped hosting the App on that service so the Profile and .sh are not needed to run the app locally. 
