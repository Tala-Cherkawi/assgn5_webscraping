# assgn5_webscraping
Methodology Overview:
Data Collection & Preprocessing
The dataset for eBay deals was cleaned using Pandas, with special attention given to ensuring all numerical fields were in the correct format and inconsistencies in the "shipping" column were addressed. Missing values in the "original_price" column were filled with values from the "price" column. Various transformations were applied to the "timestamp" column to enable time-based analysis.

Exploratory Data Analysis (EDA)
Several analyses were conducted to extract meaningful insights from the data. Time series analysis identified trends in deal activity by hour of the day. Price distributions were examined using histograms and boxplots, and a comparison of original versus discounted prices was visualized through scatter plots. Shipping information was analyzed by examining the distribution of various shipping methods, while text analysis was performed on product titles to count occurrences of popular keywords.

Visualization
Data visualizations, including bar charts, histograms, and scatter plots, were used to visualize key metrics. The analysis also included keyword frequency in titles, providing insights into product categories. The use of color palettes and customized visuals ensured the charts were not only informative but also aesthetically pleasing.

Key Findings from the EDA:
Time-Based Insights
There was a noticeable peak in deals during certain hours, indicating when sellers are most active. This hourly pattern could suggest optimal times for deal hunting.

Price & Discount Analysis
The distribution of prices showed that most deals were centered around a moderate price range, with a few high-ticket items skewing the data. The comparison between original price and discounted price revealed a significant number of items with large discounts.

Shipping Analysis
The analysis of shipping information highlighted a concentration of deals offering free shipping, which was the most common shipping method available. This was consistent across various product categories.

Textual Patterns in Product Titles
The keyword analysis revealed that products related to major brands like "Apple" and "Samsung" were highly frequent, with technology-related terms like "Laptop" and "iPhone" also prominent.

Challenges Faced:
Handling Missing and Inconsistent Data
A primary challenge involved cleaning up inconsistent shipping data and ensuring the "original_price" values were filled appropriately. Additionally, ensuring that time-based data was consistently formatted proved to be time-consuming.

Visualization Complexity
Due to the large size of the dataset, creating meaningful visualizations that were both clear and insightful required careful selection of appropriate plots and fine-tuning of chart parameters.

Potential Improvements:
Enhancing Data Cleanliness
Improvements could include further refinement of missing data handling, perhaps using predictive models for filling missing prices or shipping details, rather than relying solely on default values.

Advanced Analysis
Incorporating machine learning models for clustering or predictive analysis could provide deeper insights into trends and future pricing patterns based on historical data.

Better Data Storage Solutions
Transitioning from CSV to a relational database would improve efficiency for larger datasets and allow for more flexible querying, especially as the dataset grows over time.

Automation & Updating
Automating the data collection process and setting up a pipeline for regular updates would help maintain the relevance of the analysis over time, enabling a more dynamic understanding of eBay deals.
