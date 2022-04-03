from django.db import models


class ColorOptions(models.TextChoices):
    DARK = "d"
    LIGHT = "l"


class ShapeOptions(models.TextChoices):
    ROUND = "r"
    SQUARE = "s"


class FillingOptions(models.TextChoices):
    FULL = "f"
    EMPTY = "e"


class HeightOptions(models.TextChoices):
    TALL = "t"
    SHORT = "s"


class Figure(models.Model):
    height = models.CharField(max_length=1, choices=HeightOptions.choices)
    colour = models.CharField(max_length=1, choices=ColorOptions.choices)
    filling = models.CharField(max_length=1, choices=FillingOptions.choices)
    shape = models.CharField(max_length=1, choices=ShapeOptions.choices)

    def __repr__(self):
        to_print: str = (
            f"[h:{self.height},f:{self.filling},s:{self.shape},c:{self.colour}]"
        )
        return to_print

    class Meta:
        unique_together = ["height", "colour", "filling", "shape"]
