def create_processed_profile(age_data, gender_data, country_data):
    name = age_data.get("name")
    age = age_data.get("age")
    gender = gender_data.get("gender")

    country_list = country_data.get("country", [])

    top_country = "Unknown"

    if len(country_list) > 0:
        top_country = country_list[0].get("country_id", "Unknown")

    if age is None:
        age = "Unknown"

    if gender is None:
        gender = "Unknown"

    processed_profile = {
        "name": name,
        "predicted_age": age,
        "predicted_gender": gender,
        "predicted_country": top_country
    }

    return processed_profile