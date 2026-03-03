import re

class ItemParser:
    REF_PATTERN = re.compile(r"Referência:\s*(\d+)", re.IGNORECASE)
    PRICE_PATTERN = re.compile(r"Preço:.*?R\$\s*(\d+[\.,]\d{2})", re.IGNORECASE)
    TOTAL_ROW_PATTERN = re.compile(r"^\s*Total.*", re.IGNORECASE | re.MULTILINE)
    DIGITS_PATTERN = re.compile(r"\d+")

    @classmethod
    def parse_block(cls, text, page_num):
        items = []
        blocks = re.split(r"(Referência:)", text)
        for i in range(1, len(blocks), 2):
            content = blocks[i+1]
            ref_match = cls.REF_PATTERN.search("Referência:" + content)
            price_match = cls.PRICE_PATTERN.search(content)
            
            if ref_match and price_match:
                stock = 0
                total_row_match = cls.TOTAL_ROW_PATTERN.search(content)
                
                if total_row_match:
                    total_row_text = total_row_match.group(0)
                    all_nums = cls.DIGITS_PATTERN.findall(total_row_text)
                    if all_nums:
                        stock = int(all_nums[-1])
                
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