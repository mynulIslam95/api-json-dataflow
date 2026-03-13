# API JSON Dataflow

A clean and modular Python project that demonstrates how to build a simple data pipeline using JSON configuration, external APIs and structured JSON outputs.

The application reads a user name from a configuration file, queries multiple public APIs and combines the responses into a single processed user profile.

---

## Overview

This project demonstrates a simple end-to-end workflow commonly used in backend systems and data pipelines.

Input data is read from a JSON configuration file, external APIs are queried for predictions and the responses are processed and saved as structured JSON files.

The goal of the project is to practice API communication, JSON handling and clean Python project structure.

---

## Features

* Read input from a JSON configuration file
* Query multiple public APIs
* Convert API responses into Python dictionaries
* Process and combine API results
* Save raw responses for inspection
* Generate a final processed user profile

---

## APIs Used

| API         | Description                             |
| ----------- | --------------------------------------- |
| Agify       | Predicts age based on name              |
| Genderize   | Predicts gender based on name           |
| Nationalize | Predicts likely countries based on name |

---

## Project Structure

```id="3d4g8y"
api-json-dataflow/
│
├── README.md
├── main.py
│
├── config/
│   └── user.json
│
├── data/
│   ├── raw_age_response.json
│   ├── raw_gender_response.json
│   ├── raw_country_response.json
│   └── final_profile.json
│
└── src/
    ├── api_client.py
    ├── file_handler.py
    └── profile_service.py
```

---

## Workflow

```id="9q2t0d"
config/user.json
        ↓
Read input name
        ↓
Call APIs
(Agify / Genderize / Nationalize)
        ↓
Convert API responses to Python dictionaries
        ↓
Process and combine the results
        ↓
Save structured JSON output
```

---

## Example Input

`config/user.json`

```json id="6n7gfe"
{
  "name": "mynul"
}
```

---

## Example Output

`data/final_profile.json`

```json id="n1x3os"
{
  "name": "mynul",
  "predicted_age": 46,
  "predicted_gender": "male",
  "predicted_country": "BD"
}
```

---

## Installation

Clone the repository and install the required dependency.

```id="7bq5wh"
pip install requests
```

---

## Run the Application

```id="1q8y6s"
python main.py
```

The script will generate raw API responses and a final combined profile in the `data` directory.

---

## Learning Objectives

This project helps practice several core Python engineering concepts:

* JSON file reading and writing
* REST API requests using Python
* Data extraction from API responses
* Modular Python project structure
* Basic data processing pipeline design

## License

This project is intended for learning and experimentation.
