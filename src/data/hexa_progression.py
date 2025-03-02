"""
This module contains the HEXA Matrix level progression data.
"""

class HexaProgression:
    def __init__(self, level, 
                 # VI Skills
                 vi_sol_erda, vi_fragments, vi_erda_total, vi_frag_total,
                 # Mastery
                 mastery_sol_erda, mastery_fragments, mastery_erda_total, mastery_frag_total,
                 # Enhancement
                 enhance_sol_erda, enhance_fragments, enhance_erda_total, enhance_frag_total,
                 # Common
                 common_sol_erda, common_fragments, common_erda_total, common_frag_total):
        self.level = level
        # VI Skills
        self.vi_sol_erda = vi_sol_erda
        self.vi_fragments = vi_fragments
        self.vi_erda_total = vi_erda_total
        self.vi_frag_total = vi_frag_total
        # Mastery
        self.mastery_sol_erda = mastery_sol_erda
        self.mastery_fragments = mastery_fragments
        self.mastery_erda_total = mastery_erda_total
        self.mastery_frag_total = mastery_frag_total
        # Enhancement
        self.enhance_sol_erda = enhance_sol_erda
        self.enhance_fragments = enhance_fragments
        self.enhance_erda_total = enhance_erda_total
        self.enhance_frag_total = enhance_frag_total
        # Common
        self.common_sol_erda = common_sol_erda
        self.common_fragments = common_fragments
        self.common_erda_total = common_erda_total
        self.common_frag_total = common_frag_total

# Dictionary storing progression data for each level
HEXA_PROGRESSION = {
    0: HexaProgression(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    1: HexaProgression(1, 0, 0, 0, 0, 3, 50, 3, 50, 4, 75, 4, 75, 7, 125, 7, 125),
    2: HexaProgression(2, 1, 30, 1, 30, 1, 15, 4, 65, 1, 23, 5, 98, 2, 38, 9, 163),
    3: HexaProgression(3, 1, 35, 2, 65, 1, 18, 5, 83, 1, 27, 6, 125, 2, 44, 11, 207),
    4: HexaProgression(4, 1, 40, 3, 105, 1, 20, 6, 103, 1, 30, 7, 155, 2, 50, 13, 257),
    5: HexaProgression(5, 2, 45, 5, 150, 1, 23, 7, 126, 2, 34, 9, 189, 3, 57, 16, 314),
    6: HexaProgression(6, 2, 50, 7, 200, 1, 25, 8, 151, 2, 38, 11, 227, 3, 63, 19, 377),
    7: HexaProgression(7, 2, 55, 9, 255, 1, 28, 9, 179, 2, 42, 13, 269, 3, 69, 22, 446),
    8: HexaProgression(8, 3, 60, 12, 315, 2, 30, 11, 209, 3, 45, 16, 314, 5, 75, 27, 521),
    9: HexaProgression(9, 3, 65, 15, 380, 2, 33, 13, 242, 3, 49, 19, 363, 5, 82, 32, 603),
    10: HexaProgression(10, 10, 200, 25, 580, 5, 100, 18, 342, 8, 150, 27, 513, 14, 300, 46, 903),
    11: HexaProgression(11, 3, 80, 28, 660, 2, 40, 20, 382, 3, 60, 30, 573, 5, 110, 51, 1013),
    12: HexaProgression(12, 3, 90, 31, 750, 2, 45, 22, 427, 3, 68, 33, 641, 5, 124, 56, 1137),
    13: HexaProgression(13, 4, 100, 35, 850, 2, 50, 24, 477, 3, 75, 36, 716, 6, 138, 62, 1275),
    14: HexaProgression(14, 4, 110, 39, 960, 2, 55, 26, 532, 3, 83, 39, 799, 6, 152, 68, 1427),
    15: HexaProgression(15, 4, 120, 43, 1080, 2, 60, 28, 592, 3, 90, 42, 889, 6, 165, 74, 1592),
    16: HexaProgression(16, 4, 130, 47, 1210, 2, 65, 30, 657, 3, 98, 45, 987, 6, 179, 80, 1771),
    17: HexaProgression(17, 4, 140, 51, 1350, 2, 70, 32, 727, 3, 105, 48, 1092, 6, 193, 86, 1964),
    18: HexaProgression(18, 4, 150, 55, 1500, 2, 75, 34, 802, 3, 113, 51, 1205, 6, 207, 92, 2171),
    19: HexaProgression(19, 5, 160, 60, 1660, 2, 80, 36, 882, 4, 120, 55, 1325, 7, 220, 99, 2391),
    20: HexaProgression(20, 15, 350, 75, 2010, 8, 175, 44, 1057, 12, 263, 67, 1588, 17, 525, 116, 2916),
    21: HexaProgression(21, 5, 170, 80, 2180, 3, 85, 47, 1142, 4, 128, 71, 1716, 7, 234, 123, 3150),
    22: HexaProgression(22, 5, 180, 85, 2360, 3, 90, 50, 1232, 4, 135, 75, 1851, 7, 248, 130, 3398),
    23: HexaProgression(23, 5, 190, 90, 2550, 3, 95, 53, 1327, 4, 143, 79, 1994, 7, 262, 137, 3660),
    24: HexaProgression(24, 5, 200, 95, 2750, 3, 100, 56, 1427, 4, 150, 83, 2144, 7, 275, 144, 3935),
    25: HexaProgression(25, 5, 210, 100, 2960, 3, 105, 59, 1532, 4, 158, 87, 2302, 7, 289, 151, 4224),
    26: HexaProgression(26, 6, 220, 106, 3180, 3, 110, 62, 1642, 5, 165, 92, 2467, 9, 303, 160, 4527),
    27: HexaProgression(27, 6, 230, 112, 3410, 3, 115, 65, 1757, 5, 173, 97, 2640, 9, 317, 169, 4844),
    28: HexaProgression(28, 6, 240, 118, 3650, 3, 120, 68, 1877, 5, 180, 102, 2820, 9, 330, 178, 5174),
    29: HexaProgression(29, 7, 250, 125, 3900, 3, 125, 71, 2002, 6, 188, 108, 3008, 10, 344, 188, 5518),
    30: HexaProgression(30, 20, 500, 145, 4400, 10, 250, 81, 2252, 15, 375, 123, 3383, 20, 750, 208, 6268),
} 