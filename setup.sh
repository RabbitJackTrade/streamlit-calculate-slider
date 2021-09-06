mkdir -p ~/.streamlit/echo "\
[general]\n\
email = \"<youremail>\"\n\
" > ~/.streamlit/credentials.tomlecho "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
