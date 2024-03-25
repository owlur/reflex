"""Components for the DataList component of Radix Themes."""

from types import SimpleNamespace
from typing import Literal

from reflex.vars import Var

from ..base import LiteralAccentColor, RadixThemesComponent


class DataListRoot(RadixThemesComponent):
    """Root element for a DataList component."""

    tag = "DataList.Root"

    # The orientation of the data list item: "horizontal" | "vertical"
    orientation: Var[Literal["horizontal", "vertical"]]

    # The size of the data list item: "1" | "2" | "3"
    size: Var[Literal["1", "2", "3"]]

    # Trims the leading whitespace from the start or end of the text.
    trim: Var[Literal["normal", "start", "end", "both"]]


class DataListItem(RadixThemesComponent):
    """An item in the DataList component."""

    tag = "DataList.Item"

    align: Var[Literal["start", "center", "end", "baseline", "stretch"]]


class DataListLabel(RadixThemesComponent):
    """A label in the DataList component."""

    tag = "DataList.Label"

    width: Var[str]

    min_width: Var[str]

    max_width: Var[str]

    color: Var[LiteralAccentColor]


class DataListValue(RadixThemesComponent):
    """A value in the DataList component."""

    tag = "DataList.Value"


class DataList(SimpleNamespace):
    """DataList components namespace."""

    root = staticmethod(DataListRoot.create)
    item = staticmethod(DataListItem.create)
    label = staticmethod(DataListLabel.create)
    value = staticmethod(DataListValue.create)


data_list = DataList()
