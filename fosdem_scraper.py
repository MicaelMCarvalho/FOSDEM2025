import requests
from bs4 import BeautifulSoup
from typing import Dict, List
import concurrent.futures
import time
from datetime import datetime
import os
import math

def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def parse_event_details(event_url: str) -> Dict:
    try:
        soup = get_soup(f"https://fosdem.org{event_url}")
        abstract = soup.find('div', class_='event-abstract')
        description = soup.find('div', class_='event-description')

        links_section = soup.find('h3', string='Links')
        links = []
        if links_section:
            links_list = links_section.find_next('ul')
            if links_list:
                links = [(li.a.text, li.a['href']) for li in links_list.find_all('li')]

        return {
            'url': event_url,
            'abstract': abstract.text.strip() if abstract else '',
            'description': description.text.strip() if description else '',
            'links': links
        }
    except Exception as e:
        print(f"Error parsing {event_url}: {e}")
        return {'url': event_url, 'abstract': '', 'description': '', 'links': []}

def scrape_fosdem_schedule() -> List[Dict]:
    base_url = "https://fosdem.org/2025/schedule/events/"
    soup = get_soup(base_url)

    events = []
    current_track = None

    for row in soup.find_all('tr'):
        track_header = row.find('td', colspan='8')
        if track_header:
            current_track = track_header.h4.text.strip() if track_header.h4 else None
            continue

        cells = row.find_all('td')
        if len(cells) == 8:  # Regular event row
            event_link = cells[0].find('a')
            if event_link:
                events.append({
                    'track': current_track,
                    'title': event_link.text.strip(),
                    'url': event_link['href'],
                    'speakers': [a.text.strip() for a in cells[1].find_all('a')],
                    'room': cells[2].text.strip(),
                    'day': cells[3].text.strip(),
                    'start': cells[4].text.strip(),
                    'end': cells[5].text.strip()
                })

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(parse_event_details, event['url']): idx
                        for idx, event in enumerate(events)}

        for future in concurrent.futures.as_completed(future_to_url):
            idx = future_to_url[future]
            details = future.result()
            events[idx].update(details)

    return events

def generate_markdown_chunk(events: List[Dict], chunk_number: int, total_chunks: int) -> str:
    current_date = datetime.now().strftime("%Y-%m-%d")

    md = f"# FOSDEM 2025 Schedule - Part {chunk_number + 1} of {total_chunks}\n\n"
    md += f"*Generated on {current_date}*\n\n"

    # Group events by track
    tracks = {}
    for event in events:
        track = event['track']
        if track not in tracks:
            tracks[track] = []
        tracks[track].append(event)

    if tracks:  # Only add table of contents if there are tracks
        md += "## Table of Contents\n\n"
        for track in tracks.keys():
            track_anchor = track.lower().replace(' ', '-').replace('(', '').replace(')', '')
            md += f"- [{track}](#{track_anchor})\n"
        md += "\n"

    for track, track_events in tracks.items():
        md += f"## {track}\n\n"

        for event in track_events:
            md += f"### {event['title']}\n\n"
            md += f"- **Speakers:** {', '.join(event['speakers'])}\n"
            md += f"- **Room:** {event['room']}\n"
            md += f"- **Day:** {event['day']}\n"
            md += f"- **Time:** {event['start']} - {event['end']}\n"
            md += f"- **Event Page:** [Link](https://fosdem.org{event['url']})\n\n"

            if event['abstract']:
                md += "#### Abstract\n\n"
                md += f"{event['abstract']}\n\n"

            if event['description']:
                md += "#### Description\n\n"
                md += f"{event['description']}\n\n"

            if event['links']:
                md += "#### Related Links\n\n"
                for link_text, link_url in event['links']:
                    md += f"- [{link_text}]({link_url})\n"
                md += "\n"

            md += "---\n\n"

    return md

def save_schedule_in_chunks(events: List[Dict], chunk_size: int = 100):
    # Create output directory if it doesn't exist
    output_dir = "fosdem_schedule"
    os.makedirs(output_dir, exist_ok=True)

    # Calculate number of chunks
    total_chunks = math.ceil(len(events) / chunk_size)

    # Save complete schedule
    complete_markdown = generate_markdown_chunk(events, 0, 1)
    complete_filename = os.path.join(output_dir, 'fosdem_2025_schedule_complete.md')
    with open(complete_filename, 'w', encoding='utf-8') as f:
        f.write(complete_markdown)
    print(f"Complete schedule saved to {complete_filename}")

    # Save chunked schedules
    for i in range(total_chunks):
        start_idx = i * chunk_size
        end_idx = min((i + 1) * chunk_size, len(events))
        chunk_events = events[start_idx:end_idx]

        chunk_markdown = generate_markdown_chunk(chunk_events, i, total_chunks)
        chunk_filename = os.path.join(output_dir, f'fosdem_2025_schedule_part_{i+1}.md')

        with open(chunk_filename, 'w', encoding='utf-8') as f:
            f.write(chunk_markdown)
        print(f"Part {i+1} saved to {chunk_filename}")

if __name__ == "__main__":
    print("Starting FOSDEM schedule scraping...")
    start_time = time.time()

    events = scrape_fosdem_schedule()
    save_schedule_in_chunks(events)

    print(f"\nScraped {len(events)} events in {time.time() - start_time:.2f} seconds")
    print(f"Files are saved in the 'fosdem_schedule' directory")
