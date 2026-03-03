import os
import json
from observability.log_helper import Log

class CacheManager:
    @staticmethod
    def get_cached_result(pdf_filename):
        base_name = os.path.splitext(pdf_filename)[0]
        cache_path = os.path.join("..", "input", f"{base_name}.json")
        return None

        if os.path.exists(cache_path):
            Log.info(f"Found file: {base_name} in cache, loading existing data")
            with open(cache_path, "r", encoding="utf-8") as f:
                return json.load(f)
        
        Log.info(f"Cache not found for: {base_name}")
        return None

    @staticmethod
    def save_to_cache(pdf_filename, data):
        """
        Saves the resulting data into the shared '../input' folder 
        using the PDF's base name.
        """
        if not os.path.exists(os.path.join("..", "input")):
            os.makedirs(os.path.join("..", "input"))
            
        base_name = os.path.splitext(pdf_filename)[0]
        cache_path = os.path.join("..", "input", f"{base_name}.json")
        
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        Log.info(f"Results saved to cache: {cache_path}")