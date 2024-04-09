
def formatar_numero(valor):
        if valor >= 1000000:
            return '{:.1f} MM'.format(valor / 1000000)
        elif valor >= 1000:
            return '{:.1f} Mil'.format(valor / 1000)
        else:
            return '{:,.0f}'.format(valor)
        
# função de formatação
def thousands_formatter(x, pos):
    if x >= 1_000_000:
        return '{:.0f}M'.format(x * 1e-6)
    elif x >= 1_000:
        return '{:.0f}K'.format(x * 1e-3)
    else:
        return '{:.0f}'.format(x)

