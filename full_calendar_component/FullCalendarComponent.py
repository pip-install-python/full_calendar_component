# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FullCalendarComponent(Component):
    """A FullCalendarComponent component.


Keyword arguments:

- id (string; optional)

- clickedEvent (dict; optional)

- dateClicked (string; optional)

- editable (boolean; default True)

- events (list of dicts; optional)

    `events` is a list of dicts with keys:

    - className (string; optional)

    - context (string; optional)

    - end (string; optional)

    - start (string; optional)

    - title (string; optional)

- initialDate (string; default '2021-12-01')

- selectable (boolean; default True)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'full_calendar_component'
    _type = 'FullCalendarComponent'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, initialDate=Component.UNDEFINED, selectable=Component.UNDEFINED, editable=Component.UNDEFINED, events=Component.UNDEFINED, clickedEvent=Component.UNDEFINED, dateClicked=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'clickedEvent', 'dateClicked', 'editable', 'events', 'initialDate', 'selectable']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'clickedEvent', 'dateClicked', 'editable', 'events', 'initialDate', 'selectable']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FullCalendarComponent, self).__init__(**args)
