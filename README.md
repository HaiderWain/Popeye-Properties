# Popeye-Properties: Smart Property Recommender

A dynamic web application built with **Django** that acts as an intelligent **property recommender system**. The objective of the application is to simplify the property search by suggesting the best property locations in Pakistan based on individual user interests and preferences.

## What Problem it solves?

The idea was to solve the real-world challenge of finding the perfect property. Instead of manually browsing through countless listings, Popeye-Properties uses user input to recommend locations that are relevant. 

## How Does it Solve the Problem?
**TOPSIS:** Specifically, the system uses the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** algorithm to quantitatively assess and rank properties based on user preferences, ensuring the most relevant suggestions are provided. TOPSIS came in the 1980s as a multi-criteria-based decision-making method. TOPSIS chooses the alternative of shortest the Euclidean distance from the ideal solution and greatest distance from the negative ideal solution. 

## Key Features

The current codebase structure implements the following:

* **User Management:** Handles user accounts, authentication, and personalization.
* **Property Recommendation Logic:** The core of the system (TOPSIS), responsible for processing user interests and generating location suggestions.
* **Blog/Content Section:** Potentially for articles, updates, or insights related to property and real estate.
* **Media Handling:** Manages images and other media assets for properties or blog content.

## Technologies Used

* **Django:** The powerful Python web framework forming the backbone of the application.
* **HTML:** For structuring the web pages and user interface.
* **Python:** The primary programming language for backend logic and system operations.
