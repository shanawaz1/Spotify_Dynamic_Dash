# Spotify Track Analytics Power BI Dashboard

## Overview

This project presents a visually engaging and interactive Power BI dashboard built on a Spotify track dataset. The dashboard enables users to explore track and artist performance, audio features, and streaming trends with dynamic filtering and rich visualizations. Album cover images are integrated using Spotify’s API and Python scripting for a complete, immersive analytics experience.

---

## Key Features

- **Dynamic Dropdown Filters:**  
  Slicer visuals allow users to filter by artist name, track name, and date, making the dashboard fully interactive and responsive.

- **Album Cover Integration:**  
  A Python script authenticates with the Spotify API using client credentials, fetches album cover URLs based on track names, and appends them to the dataset. The dashboard displays album covers using the HTML Content visual for a richer user experience.

- **Audio Feature Analysis:**  
  The dashboard includes cards showing key audio features for selected tracks/albums:
    - Acoustiness %
    - Danceability %
    - Liveness %
    - Valence %
    - Speechiness %
    - Energy % (visualized with Deneb)

- **Track Release Trends:**  
  A line chart visualizes the count of tracks released over time, helping users identify trends and peak periods in music releases.

- **Key Metrics and KPIs:**  
  Ten card (new) visuals display:
    - Artist(s) name
    - Total streams
    - Release date
    - First track name
    - Number of artists in album
    - Audio features (as above)

- **Performance Benchmarks:**  
  Additional cards show:
    - Top song vs. average song performance
    - Average streams per year

- **Artist Performance Comparison:**  
  A clustered column chart compares total streams for all songs by the selected artist, highlighting top-performing tracks.

---

## Data Preparation & Integration

- **Python Script:**  
  - Authenticates with Spotify API (requires client ID and secret).
  - Fetches album cover URLs for each track.
  - Merges cover URLs into the original CSV dataset.

- **Power BI Data Model:**  
  - Loads the enriched CSV file.
  - Establishes relationships and calculated columns/measures for all key metrics.

---

## Visuals Used

- Slicer (dropdown) for artist, track, and date
- HTML Content visual for album covers
- Deneb visual for energy percentage
- Line chart for track release timeline
- Card (new) visuals for KPIs and audio features
- Clustered column chart for artist track streams

---

## How to Use

1. **Clone or download this repository.**
2. **Set up your Spotify API credentials** and run the provided Python script to fetch album cover URLs and prepare your dataset.
3. **Open the Power BI `.pbix` file** in Power BI Desktop.
4. **Use the slicers** to filter by artist, track, or date. All visuals update dynamically.
5. **Explore the dashboard:**  
    - View album covers, audio features, and streaming KPIs.
    - Analyze trends and compare track performance.

---

## Screenshot

![Spotify Track Analytics Power BI Dashboard](image.jpg)

---

## Requirements

- Power BI Desktop (latest version recommended)
- Python 3.9, 3.10, or 3.11 (for running the Spotify API script)
- Spotify Developer Account (for API credentials)
- Required Python libraries: `spotipy`, `pandas`, `requests`

---

## License

This project is licensed under the MIT License.

---

*For questions, issues, or contributions, please open an issue or submit a pull request.*
