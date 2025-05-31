# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FullCalendarComponent(Component):
    """A FullCalendarComponent component.


Keyword arguments:

- id (string; optional)

- businessHours (list of dicts; optional)

    `businessHours` is a list of dicts with keys:

    - daysOfWeek (list of numbers; optional)

    - endTime (string; optional)

    - startTime (string; optional)

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

- headerToolbar (dict; default {    start: 'title',    center: '',    end: 'today prev,next'})

- initialDate (string; default '2024-01-01')

- initialView (string; default 'dayGridMonth')

- multiMonthMaxColumns (number; default 2)

- navLinks (boolean; default True)

- nowIndicator (boolean; default True)

- resources (list of dicts; optional)

    `resources` is a list of dicts with keys:

    - id (string; optional)

    - title (string; optional)

- selectable (boolean; default True)

- timeClicked (string; optional)

- views (dict; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'full_calendar_component'
    _type = 'FullCalendarComponent'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, initialView=Component.UNDEFINED, headerToolbar=Component.UNDEFINED, initialDate=Component.UNDEFINED, selectable=Component.UNDEFINED, editable=Component.UNDEFINED, events=Component.UNDEFINED, views=Component.UNDEFINED, resources=Component.UNDEFINED, businessHours=Component.UNDEFINED, nowIndicator=Component.UNDEFINED, navLinks=Component.UNDEFINED, multiMonthMaxColumns=Component.UNDEFINED, clickedEvent=Component.UNDEFINED, dateClicked=Component.UNDEFINED, timeClicked=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'businessHours', 'clickedEvent', 'dateClicked', 'editable', 'events', 'headerToolbar', 'initialDate', 'initialView', 'multiMonthMaxColumns', 'navLinks', 'nowIndicator', 'resources', 'selectable', 'timeClicked', 'views']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'businessHours', 'clickedEvent', 'dateClicked', 'editable', 'events', 'headerToolbar', 'initialDate', 'initialView', 'multiMonthMaxColumns', 'navLinks', 'nowIndicator', 'resources', 'selectable', 'timeClicked', 'views']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FullCalendarComponent, self).__init__(**args)
