from enum import IntEnum


class GraphTypes(IntEnum):
    LINE = 0,
    BAR = 1,
    HISTOGRAM = 2,
    PATH = 3,
    SCATTER = 4,
    PIE = 5,
    POLAR = 6,
    BUBBLE = 7,
    HEATMAP = 8,
    DENSITY = 9,
    VIOLIN = 10,
    CONNECTEDSCATTER = 11,
    CORRELOGRAM = 12,
    BOX = 13,
    SPIDER = 14,
    DOUGHNUT = 15

    def __str__(self):
        if self.value == GraphTypes.LINE:
            return 'Line'
        if self.value == GraphTypes.BAR:
            return 'Bar'
        if self.value == GraphTypes.HISTOGRAM:
            return 'Histogram'
        if self.value == GraphTypes.PATH:
            return 'Path'
        if self.value == GraphTypes.SCATTER:
            return 'Scatter'
        if self.value == GraphTypes.PIE:
            return 'Pie'
        if self.value == GraphTypes.POLAR:
            return 'Polar'
        if self.value == GraphTypes.BUBBLE:
            return 'Bubble'
        if self.value == GraphTypes.HEATMAP:
            return 'Heatmap'
        if self.value == GraphTypes.DENSITY:
            return 'Density'
        if self.value == GraphTypes.VIOLIN:
            return 'Violin'
        if self.value == GraphTypes.CONNECTEDSCATTER:
            return 'Connected Scatter'
        if self.value == GraphTypes.CORRELOGRAM:
            return 'Correlogram'
        if self.value == GraphTypes.BOX:
            return 'BoxPlot'
        if self.value == GraphTypes.SPIDER:
            return 'Spider'
        if self.value == GraphTypes.DOUGHNUT:
            return 'Doughnut'

    def __eq__(self, other):
        return self.value == other.value
