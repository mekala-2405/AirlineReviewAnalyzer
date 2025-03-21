# AirlineReviewAnalyzer
#### Video Demo: https://www.youtube.com/watch?v=WaPITXyy7jk

#### Description: A lightweight Python tool designed to scrape airline reviews from the web, analyze their sentiment, and visualize the results. This project leverages web scraping, natural language processing (NLP), and data visualization to provide insights into airline customer experiences based on online reviews. This is an early version of the tool, and I plan to release updates with enhanced features and improved functionality as I continue to refine it.

Building this project was an exciting journey, marking my first significant endeavor in Python. Through this experience, I gained hands-on knowledge of libraries like `requests`, `BeautifulSoup`, `pandas`, `nltk`, and `matplotlib`, as well as skills in website interaction, data processing, and creative problem-solving. I’m eager to further develop my Python skills and create more impactful tools in the future.

One feature I was particularly excited to implement was the sentiment analysis using the VADER model. As someone interested in customer feedback, I wanted a way to quickly assess whether reviews for a given airline were positive, negative, or neutral, and then visualize these insights in an intuitive way—something not readily available in a simple, unified tool like this.

#### Current Features:
- Scrape a list of airline names from a review website.
- Allow users to input an airline name (with partial matching based on the first two characters).
- Validate the airline name and scrape up to 500 reviews (5 pages, 100 reviews per page).
- Perform sentiment analysis on the reviews using the VADER sentiment analyzer.
- Visualize sentiment results with a pie chart and bar graph.
- Display detailed review data, including sentiment scores and classifications.

#### Features to Be Implemented:
- Support for scraping reviews beyond the initial 5-page limit or 500 reviews based on user's interest.
- Enhanced input validation and error handling for edge cases.
- Options to filter reviews by date, rating, or other metadata.
- Export functionality to save results as CSV or other formats.
- A more polished user interface (possibly a GUI).
- Advanced sentiment analysis with custom scoring or additional NLP models.
- Comparative analysis across multiple airlines.

#### github/mekalaharsh-56
