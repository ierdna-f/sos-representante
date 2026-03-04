function build(rawItem, discountMultiplier) {
    const { reference, stock, original_price, page } = rawItem;
    // #TODO change this place, this should not calculate, just build
    const price = Number(original_price);
    const multiplier = Number(discountMultiplier);

    const finalPrice = price * (1 - multiplier);

    const centerStyle = {
        alignment: { horizontal: "center", vertical: "center" }
    };
    
    return {
        'Referência': { v: reference, t: 's', s: centerStyle },
        'Estoque': { v: stock, t: 'n', s: centerStyle },
        'Preço Original': { 
            v: original_price, 
            t: 'n', 
            z: '"R$ "#,##0.00',
            s: centerStyle 
        },
       [`Preço c/ Desconto ${discountMultiplier * 100}%`]: { 
            v: finalPrice, 
            t: 'n', 
            z: '"R$ "#,##0.00',
            s: centerStyle 
        },
        'Página': { 
            v: page,
            t: 'n',
            z: '0',
            s: centerStyle
        }
    };
}

module.exports = { build };