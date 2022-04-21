from typing import Optional

from beartype import beartype

from flet.constrained_control import ConstrainedControl
from flet.control import Control, OptionalNumber
from flet.ref import Ref


class IconButton(ConstrainedControl):
    def __init__(
        self,
        icon: str = None,
        ref: Ref = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        expand: int = None,
        opacity: OptionalNumber = None,
        visible: bool = None,
        disabled: bool = None,
        data: any = None,
        #
        # Specific
        #
        tooltip: str = None,
        icon_size: OptionalNumber = None,
        icon_color: str = None,
        content: Control = None,
        on_click=None,
    ):
        ConstrainedControl.__init__(
            self,
            ref=ref,
            width=width,
            height=height,
            expand=expand,
            opacity=opacity,
            visible=visible,
            disabled=disabled,
            data=data,
        )

        self.tooltip = tooltip
        self.icon = icon
        self.icon_size = icon_size
        self.icon_color = icon_color
        self.content = content
        self.on_click = on_click

    def _get_control_name(self):
        return "iconbutton"

    def _get_children(self):
        if self.__content == None:
            return []
        self.__content._set_attr_internal("n", "content")
        return [self.__content]

    # tooltip
    @property
    def tooltip(self):
        return self._get_attr("tooltip")

    @tooltip.setter
    def tooltip(self, value):
        self._set_attr("tooltip", value)

    # icon
    @property
    def icon(self):
        return self._get_attr("icon")

    @icon.setter
    def icon(self, value):
        self._set_attr("icon", value)

    # icon_size
    @property
    def icon_size(self):
        return self._get_attr("iconSize")

    @icon_size.setter
    def icon_size(self, value):
        self._set_attr("iconSize", value)

    # icon_color
    @property
    def icon_color(self):
        return self._get_attr("iconColor")

    @icon_color.setter
    def icon_color(self, value):
        self._set_attr("iconColor", value)

    # on_click
    @property
    def on_click(self):
        return self._get_event_handler("click")

    @on_click.setter
    def on_click(self, handler):
        self._add_event_handler("click", handler)

    # content
    @property
    def content(self):
        return self.__content

    @content.setter
    @beartype
    def content(self, value: Optional[Control]):
        self.__content = value
