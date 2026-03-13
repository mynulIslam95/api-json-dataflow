from src.file_handler import read_json_file, write_json_file
from src.api_client import fetch_age_data, fetch_gender_data, fetch_country_data
from src.profile_service import create_processed_profile

user_data = read_json_file("config/user.json")

name = user_data["name"]

age_response = fetch_age_data(name)
gender_response = fetch_gender_data(name)
country_response = fetch_country_data(name)

print("Age status:", age_response.status_code)
print("Gender status:", gender_response.status_code)
print("Country status:", country_response.status_code)

print("Age raw response:", age_response.text)
print("Gender raw response:", gender_response.text)
print("Country raw response:", country_response.text)

age_data = age_response.json()
gender_data = gender_response.json()
country_data = country_response.json()

write_json_file("data/raw_age_response.json", age_data)
write_json_file("data/raw_gender_response.json", gender_data)
write_json_file("data/raw_country_response.json", country_data)

processed_profile = create_processed_profile(age_data, gender_data, country_data)

write_json_file("data/final_profile.json", processed_profile)

print("Final processed profile:", processed_profile)