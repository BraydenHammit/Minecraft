def scoreAS(block,upgradeInv,multiplier,score):
    if (block == 'stone') and (not upgradeInv['penalty s']):
        score -= 1
    elif (block == 'netherrack') and (not upgradeInv['penalty n']):
        score -= 1
    elif (block == 'deepslate' and (not upgradeInv['penalty d'])):
        score -= 1.5
    elif (block == 'coal') or (block == 'nether gold') or (block == 'copper'):
        score += 1.75 * multiplier
    elif (block == 'redstone') or (block == 'lapis'):
        score += 2.5 * multiplier
    elif (block == 'iron') or (block == 'gold') or (block == 'quartz'):
        score += 3.25 * multiplier
    elif (block == 'diamond'):
        score += 5 * multiplier
    elif (block == 'amethyst') or (block == 'gilded blackstone'):
        score += 7.5 * multiplier
    elif (block == 'emerald') or (block == 'netherite'):
        score += 12.5 * multiplier

    return score