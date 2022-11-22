import pandas as pd
import streamlit as st

st.title("🏈 NFL STAT TRACKER")
st.write("##### Stat tracker web scraper using pandas....[https://www.pro-football-reference.com]")
st.write("libraries used: - pandas, - streamlit")

years_arr = list(reversed(range(1966, 2023)))
stat_arr = ["passing", "rushing", "receiving", "scrimmage", "defense", "kicking", "returns", "scoring"]

st.sidebar.title("⚙ Options")
year_select = st.sidebar.selectbox("⚙ Year", years_arr)
stat_select = st.sidebar.selectbox("⚙ Stat", stat_arr)


def load_data(year, stat):
    try:
        url = f"https://www.pro-football-reference.com/years/{year}/{stat}.htm"
        html = pd.read_html(url, header=0)
        df = html[0]
        raw = df.fillna(0)
        playerstats = raw.drop(["Rk"], axis=1)
        return playerstats
    except KeyError:
        url = f"https://www.pro-football-reference.com/years/{year}/{stat}.htm"
        html = pd.read_html(url, header=1)
        df = html[0]
        raw = df.fillna(0)
        playerstats = raw.drop(["Rk"], axis=1)
        return playerstats


data = load_data(year_select, stat_select)

st.write(data)

teams_list = sorted(data.Tm.unique())
select_team = st.sidebar.multiselect("⚙ Team", teams_list, teams_list)

pos_list = sorted(data.Pos.unique())
select_pos = st.sidebar.multiselect("⚙ Position", pos_list, pos_list)

st.write("Filtered Data TEAM/POSITION")
filtered_data = data[(data.Tm.isin(select_team)) & (data.Pos.isin(select_pos))]
st.write(filtered_data)