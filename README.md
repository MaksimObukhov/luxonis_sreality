# Luxonis Sreality Scraper
This repository contains a coding exercise for new developers joining the Python development team at [Luxonis](https://www.luxonis.com/).  
The web scraping project built with Scrapy to extract apartment listings from **Sreality.cz** and display them on a web page using a Flask web server. The scraping and web server components are containerized using Docker for easy deployment.

## Project Structure

The project is organized as follows:

- `luxonis/`: Contains the Scrapy project files
- `luxonis/luxonis_scraper/spiders/`: Contains the spider for scraping Sreality
- `luxonis/luxonis_scraper/pipelines.py`: Defines how scraped data is processed
- `server/`: Contains the Flask web server and HTML templates
- `server/http_server.py`: Flask web application
- `server/templates/website_page.html`: HTML template for displaying apartment listings
- `docker-compose.yml`: Defines the Docker services and their configurations
- `README.md`: This documentation

## Prerequisites

Before running the project, ensure you have the following dependencies installed:

- Docker
- Python (for Scrapy and Flask development)

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/luxonis-sreality-scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd luxonis-sreality-scraper
   ```

3. Build and run the Docker containers:

   ```bash
   docker-compose up
   ```

   This will set up the Scrapy spider, PostgreSQL database, and Flask web server.

4. Access the web interface:

   Open your web browser and visit [http://127.0.0.1:8080](http://127.0.0.1:8080) to view the scraped apartment listings.

## Customization

- **Scrapy Spider**: You can customize the Scrapy spider in `luxonis/luxonis_scraper/spiders/sreality_spider.py` to modify the data you want to scrape.

- **HTML Template**: To customize the appearance of the web page, modify the `website_page.html` template in the project root directory.

- **Database**: If needed, you can modify the PostgreSQL database settings in `docker-compose.yml`.
