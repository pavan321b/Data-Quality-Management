import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Generate random product reviews in different languages
def generate_review():
    languages = ['en_US', 'es_ES', 'de_DE']
    chosen_language = random.choice(languages)
    
    fake_localized = Faker(chosen_language)
    
    if chosen_language == 'en_US':
        return fake_localized.paragraph(nb_sentences=5), "English"
    elif chosen_language == 'es_ES':
        return fake_localized.paragraph(nb_sentences=5), "Spanish"
    elif chosen_language == 'de_DE':
        return fake_localized.paragraph(nb_sentences=5), "German"

# Generate synthetic data
data = []
for _ in range(10000):
    name = fake.name()
    product = random.choice(['Smartphone', 'Laptop', 'Headphones', 'Book', 'Camera', 'Watch', 'Shoes', 'Clothes', 'Backpack', 'Tablet'])
    review, review_language = generate_review()
    city = fake.city()
    state = fake.state()
    country = fake.country()
    phone_number = fake.phone_number()
    order_date = fake.date_this_decade()
    
    data.append([name, product, review, review_language, city, state, country, phone_number, order_date])

# Convert data to a DataFrame
df = pd.DataFrame(data, columns=['Customer\'s Full Name', 'Name of Product Purchased', 'Product Review', 'Product Review Language', 'City', 'State', 'Country', 'Phone Number', 'Order date'])

print(df.head())

# To save the data to a CSV file
# df.to_csv('synthetic_data.csv', index=False)
