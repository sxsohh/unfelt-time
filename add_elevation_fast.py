import pandas as pd
import asyncio
import aiohttp
import math
import time

INPUT_FILE = "data/processed/worldcities_time_dilation.csv"
OUTPUT_FILE = "data/processed/worldcities_time_dilation_with_elevation.csv"

BATCH_SIZE = 100  # OpenTopoData allows batches of 100 locations
API_URL = "https://api.opentopodata.org/v1/srtm90m"


def chunk_rows(df, batch_size):
    for i in range(0, len(df), batch_size):
        yield df.iloc[i:i + batch_size]


async def fetch_batch(session, batch):
    locations_str = "|".join(f"{row.lat},{row.lng}" for _, row in batch.iterrows())
    params = {"locations": locations_str}

    for attempt in range(3):  # retry logic
        try:
            async with session.get(API_URL, params=params) as response:
                data = await response.json()
                return data
        except Exception:
            await asyncio.sleep(0.5)

    return None


async def main():
    df = pd.read_csv(INPUT_FILE)
    df["elevation_meters"] = None

    batches = list(chunk_rows(df, BATCH_SIZE))
    total_batches = len(batches)

    print(f"Fetching elevation in {total_batches} batches...")

    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        for idx, batch in enumerate(batches):
            data = await fetch_batch(session, batch)

            if data and "results" in data:
                # Assign elevations back to the dataframe
                elevations = [r.get("elevation") for r in data["results"]]
                df.loc[batch.index, "elevation_meters"] = elevations

            if idx % 20 == 0:
                print(f"Processed {idx}/{total_batches} batches...")

    elapsed = time.time() - start_time
    print(f"Done in {elapsed:.2f} seconds.")

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    asyncio.run(main())
