mkdir -p ~/.streamlit/

echo "[theme]
primaryColor = "#7792E3"
backgroundColor = "#073346"
secondaryBackgroundColor = "#2d3c52"
textColor = "#FFFFFF"
font = "sans serif"
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
