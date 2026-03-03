import pdfplumber
from layout.layout_manager import LayoutManager
from layout.item_parser import ItemParser

def run_extraction_for_page(pdf_path, page_num):
    results = []
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_num - 1]
        bboxes = LayoutManager.get_column_bboxes(page)
        
        for bbox in bboxes:
            text = page.within_bbox(bbox).extract_text()
            if text:
                results.extend(ItemParser.parse_block(text, page_num))
    return results