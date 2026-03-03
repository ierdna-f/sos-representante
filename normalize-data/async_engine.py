import json
import os
import time
import pdfplumber
from concurrent.futures import ProcessPoolExecutor
from process_page import run_extraction_for_page
from observability.log_helper import Log

def run_parallel_extraction(pdf_path, output_path):
    start_time = time.time()
    
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)

    Log.info(f"Async engine spinning up for {total_pages} pages...")
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(run_extraction_for_page, pdf_path, i) for i in range(1, total_pages + 1)]
        
        final_data = []
        for i, future in enumerate(futures, start=1):
            page_data = future.result()
            final_data.extend(page_data)
            if i % 3 == 0 or i % 5 == 0 or i == total_pages:
                Log.info(f"Progress: {i}/{total_pages} pages (Found {len(final_data)} items so far)")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(final_data, f, indent=4, ensure_ascii=False)
    
    duration = round(time.time() - start_time, 2)
    Log.info(f"Execution finished in {duration} seconds.")
    Log.info(f"Total computed items: {len(final_data)}")
    
    return final_data