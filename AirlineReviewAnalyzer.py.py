import requests
from bs4 import BeautifulSoup
import pandas as pd
import nltk
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer as Sia

# Download required NLTK data
nltk.download('vader_lexicon')

# Scrape airline names
def scrapper_names():
    url = 'https://www.airlinequality.com/review-pages/a-z-airline-reviews/'
    response = requests.get(url)
    airlines_names = []
    soup = BeautifulSoup(response.content, 'html.parser')
    for row in soup.find_all('ul', class_='items'):
        for i in row.find_all('li'):  # had to do this to get only airline names whilst igoring the reviews in the airlines home page 
            airlines_names.append(i.get_text().strip())
    return airlines_names

# Create a dataframe to store airline names
def airlines(airlines_names):
    df = pd.DataFrame(airlines_names, columns=['Airline'])
    return df

# Input airline name and validate
def input_airline(airline_list):
    actual_airline = input("Enter the name of the airline you want to search for: ").lower()
    if actual_airline in airline_list:
        print("Processing...")
        print(f"The {actual_airline} airline is in the list")
        return actual_airline
    else:
        print(f"The {actual_airline} airline is not in the list")
        return None

# Scrape reviews for the specified airline inputted by the user
def scrapper_reviews(actual_airline):
    if not actual_airline:
        return None
    url = f"https://www.airlinequality.com/airline-reviews/{actual_airline.replace(' ', '-')}"
    base_url = url
    pages = 5
    page_size = 100
    reviews = []

    for i in range(1, pages + 1):
        print(f"Scraping page {i}")
        url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"
        response = requests.get(url)
        content = response.content
        parsed_content = BeautifulSoup(content, 'html.parser')
        for para in parsed_content.find_all("div", {"class": "text_content"}):
            reviews.append(para.get_text().strip())
        print(f"   ---> {len(reviews)} total reviews")
    
    df = pd.DataFrame(reviews, columns=['Reviews'])
    # Handle splitting only if '|' exists in reviews 
    df['reviews'] = df['Reviews'].apply(lambda x: x.split('|')[1] if '|' in x else x)
    return df

# Perform sentiment analysis using VADER
def vader(df):
    if df is None or df.empty:
        print("No reviews to analyze.")
        return None
    sia = Sia()
    df["sentiments"] = ''
    df["Vader_Analysis"] = ''
    
    for i in range(len(df)):
        df.loc[i, "sentiments"] = sia.polarity_scores(df["reviews"][i])["compound"]
        if df["sentiments"][i] >= 0.05:
            df.loc[i, "Vader_Analysis"] = "Positive"
        elif df["sentiments"][i] <= -0.05:
            df.loc[i, "Vader_Analysis"] = "Negative"
        else:
            df.loc[i, "Vader_Analysis"] = "Neutral"
    return df

# Plot sentiment analysis results
def plotter(df):
    if df is None or df.empty:
        print("No data to plot.")
        return
    plt.figure(figsize=(10, 5))
    plt.title("Sentiment Analysis By Vader Analysis")
    plt.xlabel("Sentiments")
    plt.ylabel("Counts")
    df["Vader_Analysis"].value_counts().plot(kind="pie")
    plt.show()
    plt.savefig("Sentiment_Analysis_pie.png")
    df["Vader_Analysis"].value_counts().plot(kind="bar")
    plt.savefig("Sentiment_Analysis_bar.png")
    plt.show()


# Main function
def main():
    z = scrapper_names()
    str_1 = input("Enter the first 2 or more characters of the airline name: ").lower()
    airline = [i.lower() for i in z if i.lower().startswith(str_1)]
    
    if airline:
        print("Matching airlines:")
        for i in airline:
            print(i)
    else:
        print("No airlines found with those characters.")
        return
    
    actual_input = input_airline(airline)
    reviews = scrapper_reviews(actual_input)
    analyzed_reviews = vader(reviews)
    plotter(analyzed_reviews)
    print(analyzed_reviews)
    print("Done.")

if __name__ == "__main__":
    main()