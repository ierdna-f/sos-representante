import re

class ItemParser:
    REF_PATTERN = re.compile(r"Referência:\s*(\d+)", re.IGNORECASE)
    PRICE_PATTERN = re.compile(r"Preço:\s*R\$\s*(\d+[\.,]\d{2})", re.IGNORECASE)
    # Improved: Just find the word Total and the number, ignoring line endings
    STOCK_PATTERN = re.compile(r"Total\s+(\d+)", re.IGNORECASE)

    @classmethod
    def parse_block(cls, text, page_num):
        items = []
        blocks = re.split(r"(Referência:)", text)
        for i in range(1, len(blocks), 2):
            content = blocks[i+1]
            ref_match = cls.REF_PATTERN.search("Referência:" + content)
            price_match = cls.PRICE_PATTERN.search(content)
            
            if ref_match and price_match:
                # 1. Find all occurrences of "Total X" in this specific product block
                stock_matches = cls.STOCK_PATTERN.findall(content)
                
                # 2. The very last 'Total' in the block is the one we want (Grand Total)
                # This ignores the 'Total' in the header row (P M G Total)
                stock = 0
                if stock_matches:
                    stock = int(stock_matches[-1]) 
                
                items.append(
                    cls.build_item(
                        ref_match.group(1),
                        float(price_match.group(1).replace(',', '.')),
                        stock,
                        page_num
                    )
                )
        return items

    @staticmethod
    def build_item(ref, price, stock, page):
        return {
            "reference": ref,
            "original_price": price,
            "stock": stock,
            "page": page
        }