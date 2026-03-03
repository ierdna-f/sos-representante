import os
import json
from observability.log_helper import Log

class CacheManager:
    @staticmethod
    def get_cached_result(filename):
        """
        Checks if a JSON result already exists for the given filename in the shared input folder.
        """
        # Directly pointing to the sibling input folder
        cache_path = os.path.join("..", "input", f"{filename}.json")
        
        if os.path.exists(cache_path):
            Log.info(f"Found file: {filename} in cache, loading existing data")
            with open(cache_path, "r", encoding="utf-8") as f:
                return json.load(f)
        
        Log.info(f"Cache not found for: {filename}")
        return None

    @staticmethod
    def save_to_cache(filename, data):
        """Saves the final result to the shared input folder."""
        # Ensure the input folder exists before saving
        if not os.path.exists(os.path.join("..", "input")):
            os.makedirs(os.path.join("..", "input"))
            
        cache_path = os.path.join("..", "input", f"{filename}.json")
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        Log.info(f"Successfully saved {filename} to ../input")