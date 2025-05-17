import streamlit as st
from typing import List
# style mean colour backgroud
st.markdown("""
<style>
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #E0FFFF !important;
    }

    /* Main background */
    .stApp {
        background-color: #E0FFFF;
    }

    .recipe-card {
        background-color: #E0FFFF;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    .congratulations {
        background-color: #E0FFFF;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    .header {
        color: #E0FFFF;
        text-align: center;
    }

    .subheader {
        color: #E0FFFF;
        font-size: 24px;
    }

    .social-links {
        text-align: center;
        padding: 10px;
        background-color: #E0FFFF;
        border-radius: 5px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# City Class
class City:
    def __init__(self, name: str, category: str, overview: str, attractions: List[str],
                 local_foods: List[str], transport_info: str, best_time_to_visit: str,
                 summer_weather_avg: int, winter_weather_avg: int):
        self.name = name
        self.category = category
        self.overview = overview
        self.attractions = attractions
        self.local_foods = local_foods
        self.transport_info = transport_info
        self.best_time_to_visit = best_time_to_visit
        self.summer_weather_avg = summer_weather_avg
        self.winter_weather_avg = winter_weather_avg

    def display_details(self):
        st.header(self.name)
        st.subheader(self.category)
        st.write(self.overview)
        st.subheader("Popular Attractions")
        for attraction in self.attractions:
            st.markdown(f"- {attraction}")
        st.subheader("Local Foods")
        for food in self.local_foods:
            st.markdown(f"- {food}")
        st.subheader("Transport Information")
        st.write(self.transport_info)
        st.subheader("Best Time to Visit")
        st.write(self.best_time_to_visit)
        st.subheader("Typical Weather")
        st.write(f"🌞 Summer: {self.summer_weather_avg}°C | ❄️ Winter: {self.winter_weather_avg}°C")

    def get_budget_estimation(self, days: int, people: int, budget_type: str) -> str:
        rate = {"Economy": 5000, "Mid-range": 8000, "Luxury": 15000}
        cost = rate.get(budget_type, 0) * days * people
        return f"{budget_type} Budget for {days} days, {people} person(s): PKR {cost}"

    def display_budget(self, days: int, people: int):
        st.subheader("Budget Estimation")
        for level in ["Economy", "Mid-range", "Luxury"]:
            st.write(self.get_budget_estimation(days, people, level))

#  Trip Planner
class PakistanTripPlanner:
    def __init__(self):
        self.cities = self.load_cities()
        self.train_prices = {
            ("Lahore", "Karachi"): 3450,
           ("karachi","RAWALPINDI"): 5700,
            ("Rawalpindi", "Peshawar"): 750,
            ("Karachi", "Multan"): 3450,
            ("Lahore", "Multan"): 1700,
            ("Rawalpindi", "Lahore"): 600,
            ("Rawalpindi", "Multan"): 2550,
            ("Multan", "Peshawar"): 3150,
            ("Peshawar", "Faisalabad"): 2000,
            ("Bahawalpur", "Karachi"): 3050,
            ("Bahawalpur", "Multan"):400,
        }

    def load_cities(self):
        return {
            "Lahore": City("Lahore", "Big City", "Cultural capital of Pakistan.",
                           ["Badshahi Mosque", "Shalimar Bagh"], ["Nihari", "Halwa Puri"], 
                           "Metro, rickshaw, buses", "Oct-Apr", 35, 10),
            "Murree": City("Murree", "Mountain City", "Popular hill station.",
                           ["Mall Road", "Patriata"], ["Pakoras", "Karahi"], 
                           "Taxis, jeeps", "May-Jun, Sep-Oct", 25, -5),
            "Karachi": City("Karachi", "Sea City", "Largest port city.",
                           ["Clifton Beach", "Mazar-e-Quaid"], ["Biryani", "Haleem"], 
                           "Buses, rickshaw", "Oct-Mar", 32, 18),
            "Islamabad": City("Islamabad", "Big City", "Capital of Pakistan.",
                           ["Faisal Mosque", "Daman-e-Koh"], ["Chapli Kabab", "Sajji"], 
                           "Metro Bus, Careem, Uber", "Oct-Mar", 30, 5),
            "Multan": City("Multan", "Big City", "City of Saints and Shrines.",
                           ["Shrine of Bahauddin Zakariya", "Multan Fort"], ["Sohan Halwa", "BBQ"], 
                           "Rickshaws, buses", "Nov-Mar", 33, 12),
            "Peshawar": City("Peshawar", "Big City", "Historic city near Khyber Pass.",
                           ["Qissa Khwani Bazaar", "Bala Hissar Fort"], ["Chapli Kabab", "Peshawari Namak Mandi BBQ"], 
                           "Minibuses, taxis", "Oct-Mar", 32, 4),
            "Gwadar": City("Gwadar", "Sea City", "Emerging port city.",
                           ["Hammerhead", "Gwadar Port"], ["Grilled Fish", "Karahi"], 
                           "Buses, taxis", "Nov-Feb", 28, 18),
            "Skardu": City("Skardu", "Mountain City", "Gateway to mighty Karakorams.",
                           ["Shangrila Lake", "Deosai Plains"], ["Yak Meat", "Local Roti"], 
                           "Jeeps, flights", "May-Sep", 20, -10),
            "Hunza": City("Hunza", "Mountain City", "Famous valley in Gilgit-Baltistan.",
                           ["Altit Fort", "Attabad Lake"], ["Apricot Soup", "Chapshuro"], 
                           "Jeeps, private vans", "May-Oct", 22, -5)
        #    "Bahawalpur": City       "Noor Mahal", "Darbar Mahal",  "Sadiq Garh Palace.", "Gulzar Mahal", "Nishat Mahal",  "Dubai Palace"]
      
        }

    def get_city_list_by_category(self, category):
        return [c.name for c in self.cities.values() if category.lower() in c.category.lower()]

    def display_cities_by_category(self, category):
        st.title(f"{category} in Pakistan")
        cities = self.get_city_list_by_category(category)
        for name in cities:
            st.subheader(name)
            self.cities[name].display_details()

    def display_city_details(self, name: str):
        if name in self.cities:
            self.cities[name].display_details()
        else:
            st.error("City not found!")

    def get_user_input(self):
        city = st.selectbox("Choose your destination", list(self.cities.keys()))
        city = st.selectbox("Choose your from", list(self.cities.keys()))
        days = st.number_input("Days", 1, 30, 3)
        people = st.number_input("People", 1, 10, 2)
        return city, days, people

    def display_train_price(self, source, dest):
        st.subheader("🚆 Train Fare Estimation")
        price = self.train_prices.get((source, dest)) or self.train_prices.get((dest, source))
        if price:
            st.success(f"{source} ➝ {dest}: PKR {price}")
        else:
            st.warning("Fare not available.")

    def show_foods_page(self):
        st.title("🍽️ Pakistani Food Guide")
        city = st.selectbox("Select a City", list(self.cities.keys()))
        foods = self.cities[city].local_foods
        st.subheader(f"Famous Foods in {city}")
        for food in foods:
            st.markdown(f"- {food}")
# weather
    def show_weather_page(self):
        st.title("🌦️ Live Weather (Demo)")
        city = st.selectbox("Select City", list(self.cities.keys()))
        st.info(f"This would show live weather for {city} (plug in API for real data).")

    def run(self):
        page = st.sidebar.radio("Go to", [
            "Trip Planner", "Food Guide", "Train Tickets", "Live Weather",
            "Mountain Places", "Sea Places", "Big Cities", "Popular Places"
        ])
        # now start the app trip planner

        if page == "Trip Planner":
            st.title("🧳 PakTrip Planner")
            city, days, people = self.get_user_input()
            st.divider()
            self.display_city_details(city)
            self.cities[city].display_budget(days, people)
# food guide page
        elif page == "Food Guide":
            self.show_foods_page()
# train ticket page
        elif page == "Train Tickets":
            st.title("🚉 Train Fare Checker")
            source = st.selectbox("From", list(self.cities.keys()))
            dest = st.selectbox("To", list(self.cities.keys()))
            if source != dest:
                self.display_train_price(source, dest)
            else:
                st.warning("Choose two different cities.")

        elif page == "Live Weather":
            self.show_weather_page()

        elif page == "Mountain Places":
            self.display_cities_by_category("Mountain")

        elif page == "Sea Places":
            self.display_cities_by_category("Sea")

        elif page == "Big Cities":
            self.display_cities_by_category("Big")

        elif page == "Popular Places":
            st.title("🌟 Popular Places in Pakistan")
            for city in ["Lahore", "Karachi", "Islamabad", "Hunza", "Skardu"]:
                self.cities[city].display_details()

# side bar connect with me...........  :)

with st.sidebar:
    st.markdown("## Connect with the Creator")
    
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-LeezaSarwar-black?style=flat-square&logo=github)](https://github.com/LeezaSarwar)")
    
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Leeza%20Sarwar-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/leeza-sarwar-21ab61339)")
    
    st.markdown("[![X](https://img.shields.io/badge/X-@LeezaSarwar-black?style=flat-square&logo=x)](https://x.com/LeezaSarwar?t=M3pbn1Pf-gLv8wSu0G0vBw&s=09)")
    
    st.markdown("[![Email](https://img.shields.io/badge/Email-leezasarwar0@gmail.com-red?style=flat-square&logo=gmail)](mailto:leezasarwar0@gmail.com)")

    st.markdown("---")
    st.markdown("Created by: Leeza Sarwar")

#  Streamlit Run 
if __name__ == "__main__":
    planner = PakistanTripPlanner()
    planner.run()
