# FOSDEM Schedule Scraper

FOSDEM is the largest Open Source conference with more than 1000 events, due to that can be overwhelming to choose what to see. 
To solve it I built this simple python script to scrape the FOSDEM 2025 schedule and save it as a well-formatted Markdown file. This tool retrieves information about all talks, including titles, speakers, schedules, rooms, and detailed descriptions.
With this file, you can then upload it for example to notebooklm or another AI to ask it questions and easily find talks that you are interested in.

With this file you can then upload it to an AI tool, for example 

## Features

- Scrapes complete FOSDEM 2025 schedule
- Extracts talk details including abstracts and descriptions
- Organizes content by tracks
- Preserves all related links and resources
- Generates a clean, well-structured Markdown output
- Uses concurrent scraping for better performance

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/fosdem-schedule-scraper.git
cd fosdem-schedule-scraper
```

Install required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python fosdem_scraper.py
```

The script will:
1. Scrape the FOSDEM 2025 schedule
2. Process all events and their details
3. Generate a markdown file named `fosdem_2025_schedule.md`

## Output Format

The generated markdown file includes:

- Table of Contents with links to each track
- Events grouped by track
- For each talk:
  - Title
  - Speakers
  - Room
  - Day and time
  - Abstract
  - Description
  - Related links
  - Original event page link

## Requirements

- Python 3.7+
- requests
- beautifulsoup4
- typing

See `requirements.txt` for specific version requirements.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
