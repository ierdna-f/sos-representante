import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from observability.log_helper import Log
from cache.cache_manager import CacheManager
from async_engine import run_parallel_extraction

class Application:
    def __init__(self, pdf_name):
        self.pdf_name = pdf_name
        self.pdf_path = os.path.join("data", pdf_name)
        self.cache_key = os.path.splitext(pdf_name)[0]

    def run(self):
        cached_data = CacheManager.get_cached_result(self.cache_key)
        
        if cached_data:
            return cached_data

        Log.info("Starting async processing...")
        output_path = os.path.join("data", f"{self.cache_key}.json")
        results = run_parallel_extraction(self.pdf_path, output_path)
        
        return results

if __name__ == "__main__":
    target_pdf = "estoque-inverno-2026.pdf"
    app = Application(target_pdf)
    app.run()